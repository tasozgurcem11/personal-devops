import subprocess
import shlex
import os
from xattr import xattr
import mac_tag
import sys


def execute(cmd):
    try:
        cmd = shlex.split(cmd)
        byte_output = subprocess.check_output(cmd)
        output = byte_output.decode('UTF-8')
        return output
    except subprocess.CalledProcessError as cpe:
        return None
    except Exception as ex:
        print(ex)
        return None


def set_label(filename, color_name):
    # Enter your label names if you are using Mac OS
    colors = ['none', 'gray', 'green', 'purple', 'blue', 'yellow', 'red', 'orange', 'projects']
    key = u'com.apple.FinderInfo'
    attrs = xattr(filename)
    current = attrs.copy().get(key, chr(0)*32)
    changed = current[:9] + chr(colors.index(color_name)*2) + current[10:]
    attrs.set(key, changed)


def create_readme_file(project_name, project_path, project_description):
    current_path = os.getcwd()
    os.chdir(project_path)
    with open(os.path.join(project_path, project_name, 'README.md'), 'w') as f:
        f.write('# ' + project_description + '\n')
    os.chdir(current_path)


def create_project_directory(project_name, project_path):
    current_path = os.getcwd()
    os.chdir(project_path)
    os.mkdir(project_name)
    # set_label(os.path.join(project_path, project_name), 'orange')
    project_label_name = 'projects'
    mac_tag.add([project_label_name], [os.path.join(project_path, project_name)])
    os.chdir(current_path)


def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
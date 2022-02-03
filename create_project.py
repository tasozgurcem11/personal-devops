#!/usr/bin/env python3
from functions import create_project_directory, create_readme_file, query_yes_no
from git_commands import create_github_repository, add_gitignore_file, git_push, git_init
from credentials import *
import argparse
import os
import shutil


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to set dev-ops environment for public/private projects")
    parser.add_argument('-n', '--name', help='Name of the project', required=True)
    parser.add_argument('-d', '--description', help='Description of the project', required=True)
    parser.add_argument('-g', '--git', help='Add to github', action='store_true')
    parser.add_argument('-p', '--private', help='Create a private project', action='store_true')
    args = parser.parse_args()

    # Must do "brew install tag"

    if args.private:
        private = True
    else:
        private = False

    if args.git:
        git = True
    else:
        git = False

    project_name = args.name
    project_description = args.description

    if os.path.isdir(os.path.join(PROJECTS_PATH, project_name)):
        print(f'{project_name} already exists')
        if query_yes_no('Do you want to overwrite it?'):
            shutil.rmtree(os.path.join(PROJECTS_PATH, project_name))
        else:
            print('Stopping.')
            exit()

    create_project_directory(project_name, PROJECTS_PATH)
    create_readme_file(project_name, PROJECTS_PATH, project_description)
    add_gitignore_file(project_name, PROJECTS_PATH, INTERNAL_DEVOPS_PATH)

    if git:
        git_command = create_github_repository(GITHUB_API_TOKEN, args.name, args.description, private=args.private)
        git_init(os.path.join(PROJECTS_PATH, project_name), project_name, GITHUB_USERNAME)


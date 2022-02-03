import os
from git import Repo
from github import Github
import shutil

def create_github_repository(github_api_token, repo_name, repo_description, private=False):
    g = Github(login_or_token=github_api_token)
    user = g.get_user()
    repo = user.create_repo(repo_name,
                            allow_rebase_merge=True,
                            description=repo_description,
                            has_issues=True,
                            has_projects=False,
                            has_wiki=False,
                            auto_init=False,
                            private=private)


def add_gitignore_file(project_name, PROJECTS_PATH):
    current_gitignore_path = '.gitignore'
    gitignore_path_list = [PROJECTS_PATH, project_name, current_gitignore_path]
    shutil.copyfile(current_gitignore_path, os.path.join(*gitignore_path_list))


def git_push(PATH_OF_GIT_REPO):
    # empty_repo = Repo.init(PATH_OF_GIT_REPO)
    # origin = empty_repo.create_remote('origin', Repo.remotes.origin.url)
    # assert origin.exists()
    # assert origin == empty_repo.remotes.origin == empty_repo.remotes['origin']
    # origin.fetch()  # assure we actually have data. fetch() returns useful information
    # # Setup a local tracking branch of a remote branch
    # empty_repo.create_head('master', origin.refs.master)  # create local branch "master" from remote "master"
    # empty_repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
    # empty_repo.heads.master.checkout()  # checkout local "master" to working tree


    repo = Repo.init(PATH_OF_GIT_REPO)
    # repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(update=True)
    repo.index.commit('init commit')
    origin = repo.remote(name='origin').push()


def git_init(PATH_OF_GIT_REPO, github_repo_name, github_username):
    print(PATH_OF_GIT_REPO)
    os.chdir(PATH_OF_GIT_REPO)
    os.system("git init")
    os.system("git add . ")
    os.system('git commit -m "initial commit"')
    os.system('git branch -M main')
    os.system(f"git remote add origin git@github.com:{github_username}/{github_repo_name}.git")
    os.system("git push -u origin main")
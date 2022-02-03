## Devops for project creation shortcut

### Sample credentials.py file:

```
GITHUB_API_TOKEN = '1111111'

GITHUB_USERNAME = 'johndoe' 

PROJECTS_PATH = './projects' 
```

### Sample script:
` python create_project.py -n "name_of_the_project" -d "sample description for the project" -g`

Creates a new project in the projects folder. Creates git repo and pushes it to github. Also if in MacOS adds "Orange" finder label.
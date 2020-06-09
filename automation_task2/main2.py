import os
import json

os.system('virtualenv .venv')
os.system('source .venv/bin/activate')
os.system('pip install click')
os.system('pip install requests')

import requests
import click




url = "https://api.github.com/user/repos"
headers = {
    "Authorization": "token 6e160aaadeb88b4a519683a688aa000caad3537f"
}
payload = {
    "name" : "Python_project"
}
response = requests.post(url,headers = headers, data= json.dumps(payload))
print(response)

@click.command()
@click.option('-p', '--project', required=True, help='sdkjfds')
def create_project(project):
    os.mkdir(project)
    os.chdir(project)
    os.mkdir('css')
    os.mkdir('js')
    open('css/style.css', 'w').close()
    open('js/script.js', 'w').close()
    if click.confirm('git reponuz varmi? '):
        git_repo = click.prompt('repo unvani qeyd edin: ')
        os.system('git init')
        os.system(f'git remote add origin {git_repo}')
        os.system('git add .')
        os.system('git commit -m "project created"')
        os.system('git push origin master')


if __name__ == '__main__':
    create_project()

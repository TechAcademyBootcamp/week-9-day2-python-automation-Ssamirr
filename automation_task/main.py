import os
import requests
import click
import json



url = "https://api.github.com/user/repos"
headers = {
    "Authorization": "token 6e160aaadeb88b4a519683a688aa000caad3537f"
}
payload = {
    "name" : "Front_end_project"
}
response = requests.post(url,headers = headers, data= json.dumps(payload))
print(response)

@click.command()
@click.option('-p', '--project', required=True, help='sdkjfds')
@click.option('--path', help='sdkjfds')
def create_project(project, path):
    html = None
    with open('index.html', 'r') as f:
        html = f.read()
    if path:
        os.chdir(path)
    os.mkdir(project)
    os.chdir(project)
    os.mkdir('css')
    os.mkdir('js')
    open('css/style.css', 'w').close()
    open('js/script.js', 'w').close()
    with open('index.html', 'w') as f:
        f.write(html)

    if click.confirm('git reponuz varmi? '):
        git_repo = click.prompt('repo unvani qeyd edin: ')
        os.system('git init')
        os.system(f'git remote add origin {git_repo}')
        os.system('git add .')
        os.system('git commit -m "project created"')
        os.system('git push origin master')


if __name__ == '__main__':
    create_project()


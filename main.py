import gitlab
import subprocess
import os


ALIASES = {
    'sparkmeter': 'sm',
}

REPO_FOLDER = '/Devel'


def alias(path):
    # rename the org name to sm instead of sparkmeter to save space on the prompt
    for a in ALIASES.keys():

        # if the path doesnt start with an alias, perform no transformations on this path
        if not path.startswith(f'{a}/'):
            continue

        # replace the org name with the aliased name
        if path.startswith(f'{a}/'):
            path = path.replace(f'{a}/', f'{ALIASES[a]}/', 1)

        # replace any org name prefixes in repo names because we will already know which org we are in
        if f'/{a}' in path and not path.endswith(f'/{a}'):
            path = path.replace(f'/{a}', '/').replace('/-', '/').replace('/_', '/')
        return path


def download_starred():
    gl = gitlab.Gitlab.from_config()
    for project in gl.projects.list(owned=True, all=True):
        # determine the right path for this repo
        path = alias(project.path_with_namespace)
        path = os.path.join(REPO_FOLDER, path)
        git_url = project.http_url_to_repo
        #print(path)
        # clone the repo
        subprocess.call(['git', 'clone', git_url, path])


if __name__ = "__main__":
    download_starred()

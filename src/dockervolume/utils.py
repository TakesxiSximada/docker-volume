import os


def enclose_in_double_quote(word):
    return '"{}"'.format(word) if ' ' in word else word


def search_docker_compose_dir(directory=None):
    if directory is None:
        directory = os.getcwd()
    before = None
    while before != directory:
        if os.path.isfile(os.path.join(directory, 'docker-compose.yml')):
            return directory
        else:
            before = directory
            directory = os.path.dirname(directory)
    return None


class DummyChild(object):
    def wait(self):
        return 0

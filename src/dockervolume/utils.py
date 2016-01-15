import os
import glob


def enclose_in_double_quote(word):
    return '"{}"'.format(word) if ' ' in word else word


def search_file(pattern, directory=None):
    if directory is None:
        directory = os.getcwd()
    before = None
    while before != directory:
        search_pattern = os.path.join(directory, pattern)
        for path in glob.glob(search_pattern):
            if os.path.isfile(path):
                return path
        else:
            before = directory
            directory = os.path.dirname(directory)
    return None


def search_docker_voluem_yml(pattern='docker-volume.yml'):
    return search_file(pattern=pattern)


def search_docker_compose_yml(pattern='docker-compose.yml'):
    return search_file(pattern=pattern)


def search_docker_compose_dir(pattern='docker-compose.yml'):
    yml_path = search_file(pattern=pattern)
    return os.path.dirname(yml_path) if yml_path else None


class DummyChild(object):
    def wait(self):
        return 0

import os
import glob


def enclose_in_double_quote(word):
    """Enclose in duble quote

    >>> enclose_in_double_quote('para meter')
    '"para meter"'
    >>> enclose_in_double_quote('parameter')
    'parameter'
    """
    return '"{}"'.format(word) if ' ' in word else word


def search_file(pattern, directory=None):
    """Seach a file want to hit the pattern while it climbed

    """
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


def search_docker_compose_dir(pattern='docker-compose.yml'):
    yml_path = search_file(pattern=pattern)
    return os.path.dirname(yml_path) if yml_path else None


class DummyChild(object):
    def wait(self):
        return 0


DEFAULT_MACHINE_NAME = 'default'
DEFAULT_VOLUME_YML = 'docker-volume.yml'
DEFAULT_COMPOSE_YML = 'docker-compose.yml'


DEFAULT_CONF = DEFAULT_VOLUME_YML  # duprecated to DEFAULT_VOLUME_YML

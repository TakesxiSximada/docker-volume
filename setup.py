# -*- coding: utf-8 -*-
import os
import re
import sys
from setuptools import setup, find_packages


def here(name):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        name)


def read(name, mode='rt'):
    with open(here(name), mode) as fp:
        return fp.read()


def _get_version_str(file_path):
    version_file = read(file_path)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise ValueError("Unable to find version string.")


def find_version(path, pattern='.*\.py$'):
    regx = re.compile(pattern)
    for root, dirs, files in os.walk(path):  # 3.5... orz
        for filename in files:
            filepath = os.path.join(root, filename)
            if regx.match(filepath):
                try:
                    return _get_version_str(filepath)
                except ValueError:
                    pass  # next
    else:
        raise ValueError('Version file not found: {}'.format(path))


# comat libraries
version_require = []
if sys.version_info < (3, 4, 0):
    version_require.append('enum34')

if sys.version_info < (3, 3, 0):
    version_require.append('repoze.lru')

long_description = \
    read('README.rst') + '\n\n' + \
    read('CHANGES.rst') + '\n\n'

setup(
    name='docker-volume',
    version=find_version('src'),
    description='Management tool of VirtualBox Volume for Docker',
    long_description=long_description,
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python",
    ],
    author='TakesxiSximada',
    author_email='sximada@gmail.com',
    url='https://github.com/TakesxiSximada/docker-volume',
    download_url='https://github.com/TakesxiSximada/docker-volume/archive/master.zip',
    keywords='Docker, VirtualBox',
    packages=find_packages('src', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={'': 'src'},
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        'six',
        'mako',
        'jumon',
        'PyYAML',
        'lazr.delegates',
        'zope.interface',
        'zope.component',
    ] + version_require,
    tests_require=[
        'astroid',  # use by pylint
        'eventlet',  # use by detox
        'flake8',
        'vulture',
        'pylint',
        'nose',
        'mypy-lang',
        'tox',
        'detox',
        'selenium',
    ],
    extras_require={
        'docs': [
            'sphinx',
        ],
        'develop': [
            'wheel',
        ],
        'testing': [
            'astroid',  # use by pylint
            'eventlet',  # use by detox
            'flake8',
            'vulture',
            'pylint',
            'nose',
            'mypy-lang',
            'tox',
            'detox',
            'selenium',
        ],
    },
    entry_points="""\
      [console_scripts]
      docker-volume = dockervolume.commands:main
      """,
    )

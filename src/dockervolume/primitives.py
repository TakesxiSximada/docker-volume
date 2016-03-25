import logging
import subprocess

import six
from .utils import (
    enclose_in_double_quote,
    DummyChild,
    )

from .interfaces import ISetting
from .registries import get_registry
from .compat import makedirs

_logger = logging.getLogger()


def do_cmd(cmd, *args, **kwds):
    if not isinstance(cmd, six.string_types):
        cmd_for_print = ' '.join(map(enclose_in_double_quote, cmd))
    else:
        cmd_for_print = cmd
    _logger.info('EXECUTE: %s', cmd_for_print)

    registry = get_registry()
    setting = registry.queryUtility(ISetting)
    if not setting.dry_run:
        return subprocess.Popen(cmd, *args, **kwds)
    else:
        return DummyChild()


def do_docker_machine_ssh(env, *argv):
    if not isinstance(argv, six.string_types):
        argv = ' '.join(argv)
    cmd = 'docker-machine', 'ssh', env, argv
    return do_cmd(cmd)


def sharedfolderctl(env, mode, *argv):
    """VBoxManage sharedfolder add dev --name volumes --hostpath "$PWD/volumes" """
    cmd = ('VBoxManage', 'sharedfolder', mode, env, '--transient') + argv
    return do_cmd(cmd)


def add_volume(env, name, hostpath, **kwds):
    """VBoxManage sharedfolder add dev --name volumes --hostpath "$PWD/volumes" """
    return sharedfolderctl(
        env, 'add', '--name', name, '--hostpath', hostpath)


def remove_volume(env, name, **kwds):
    """VBoxManage sharedfolder remove dev --name volume """
    return sharedfolderctl(env, 'remove', '--name', name)


def mount_volume(
        env, name, vboxpath, uid=None, gid=None,
        dmode=None, fmode=None, **kwds):
    """Mount volume on the docker machine using docker-machine ssh

    docker-machine ssh dev "sudo mount -t vboxsf -o uid=0,gid=0 volumes $PWD/volume"
    """
    option_params = []
    if uid is not None:
        option_params.append('uid={}'.format(uid))
    if gid is not None:
        option_params.append('gid={}'.format(gid))
    if dmode is not None:
        option_params.append('dmode={}'.format(dmode))
    if fmode is not None:
        option_params.append('fmode={}'.format(fmode))

    option = '-o {}'.format(','.join(option_params)) if option_params else ''
    return do_docker_machine_ssh(
        env,
        'sudo mkdir -p {} && '.format(vboxpath),
        'sudo mount -t vboxsf {option} {name} {vboxpath}'.format(
            option=option, name=name, vboxpath=vboxpath),
        )


def unmount_volume(env, name, vboxpath, **kwds):
    """docker-machine ssh dev "sudo umount $vboxpath" """
    return do_docker_machine_ssh(
        env, 'sudo umount {}'.format(vboxpath))


def make_directory(env, name, directory, **kwds):
    directories = directory
    registry = get_registry()
    setting = registry.queryUtility(ISetting)
    if directories is not None:
        for dir_path in directories:
            _logger.info('CREATE DIRECTORY: %s', dir_path)
            if not setting.dry_run:
                makedirs(dir_path, exist_ok=True)
    return DummyChild()

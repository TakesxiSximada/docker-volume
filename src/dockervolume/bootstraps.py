import os.path
from .exc import (
    NoConfigurationError,
    )

from .utils import search_docker_compose_dir
from .settings import VolumeSettingParser
from .registries import get_registry
from .interfaces import (
    ISetting,
    IOperation,
    )
from .primitives import (
    add_volume,
    mount_volume,
    unmount_volume,
    remove_volume,
    make_directory,
    )
from .operations import VolumeOperation


def bootstrap(name, conf, compose_yml, dry_run):
    docker_compose_dir = search_docker_compose_dir(compose_yml)
    if docker_compose_dir is None:
        raise NoConfigurationError('Configuration file not found: {}'.format(conf))
    docker_compose_name = os.path.basename(docker_compose_dir)

    reg = get_registry()
    if not os.path.exists(conf):
        conf = os.path.join(docker_compose_dir, conf)
        if not os.path.exists(conf):
            raise NoConfigurationError('Configuration file not found: {}'.format(conf))
    setting_parser = VolumeSettingParser(name, conf, docker_compose_name)
    setting = setting_parser()
    if dry_run:
        setting.set_dry_run()

    reg.registerUtility(setting, ISetting)
    reg.registerUtility(VolumeOperation(make_directory), IOperation, 'directory')
    reg.registerUtility(VolumeOperation(add_volume), IOperation, 'add')
    reg.registerUtility(VolumeOperation(mount_volume), IOperation, 'mount')
    reg.registerUtility(VolumeOperation(unmount_volume), IOperation, 'unmount')
    reg.registerUtility(VolumeOperation(remove_volume), IOperation, 'remove')
    return reg

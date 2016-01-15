import sys
import argparse

from dockervolume.log import setup_logging
from dockervolume.core import VolumeCommand
from dockervolume.utils import search_docker_voluem_yml
from dockervolume.bootstraps import bootstrap


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help='add, mount, unmount, remove')
    parser.add_argument('name', help='docker machine name')
    parser.add_argument('--conf', default='docker-volume.yml')
    parser.add_argument('--dry-run', default=False, action='store_true')
    args = parser.parse_args(argv)

    name = args.name
    cmd = args.cmd
    conf = search_docker_voluem_yml(args.conf)
    dry_run = args.dry_run

    setup_logging()
    registry = bootstrap(name=name, conf=conf, dry_run=dry_run)
    execute = VolumeCommand(registry)
    execute(cmd)

if __name__ == '__main__':
    sys.exit(main())

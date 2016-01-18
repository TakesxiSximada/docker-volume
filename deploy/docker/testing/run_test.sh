#! /usr/bin/env sh
. /srv/docker-volume/env/bin/activate
cd /srv/docker-volume/repo && pip install -e .[testing] && detox

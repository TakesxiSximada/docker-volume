FROM dockervolume_develop:latest
MAINTAINER TakesxiSximada <sximada@gmail.com>

WORKDIR $SRV_ROOT/repo
CMD $SRV_ROOT/env/bin/pip install -e .[testing] && $SRV_ROOT/env/bin/detox

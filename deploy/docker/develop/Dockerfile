FROM dockervolume_app:latest
MAINTAINER TakesxiSximada <sximada@gmail.com>
RUN apt-get install -y python2.7 python2.7-dev
RUN apt-get install -y python3.3 python3.3-dev
RUN apt-get install -y python3.4 python3.4-dev
RUN apt-get install -y git emacs24 mercurial

WORKDIR $SRV_ROOT/repo
RUN $SRV_ROOT/env/bin/pip install -r $SRV_ROOT/src/requirements/develop.txt
RUN $SRV_ROOT/env/bin/pip install -r $SRV_ROOT/src/requirements/testing.txt
CMD tail -f /dev/null

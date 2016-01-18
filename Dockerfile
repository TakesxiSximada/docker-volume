FROM dockervolume_base:latest
MAINTAINER TakesxiSximada <sximada@gmail.com>
ENV SRV_ROOT /srv/docker-volume
ADD . $SRV_ROOT/src
WORKDIR $SRV_ROOT/src
RUN $SRV_ROOT/env/bin/pip install -r $SRV_ROOT/src/requirements.txt
RUN cp -R $SRV_ROOT/src/requirements $SRV_ROOT/var/
CMD ["$SRV_ROOT/env/bin/nosetests"]

FROM ubuntu:latest
MAINTAINER TakesxiSximada <sximada@gmail.com>
ENV PROJECT_NAME docker-volume

# IIJ mirror
RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/%g" /etc/apt/sources.list
RUN apt-get update -y

# for apt-add-repository
RUN apt-get install -y software-properties-common  # >= 14.04
# RUN apt-get install -y python-software-properties  # < 14.04

RUN apt-add-repository ppa:fkrull/deadsnakes
RUN apt-get update -y

RUN apt-get install -y git mercurial
RUN apt-get install -y python3.5 python3.5-dev python3-pip python-virtualenv  # use python3.5
RUN apt-get install -y curl

ENV SRV_ROOT /srv/$PROJECT_NAME
RUN mkdir -p $SRV_ROOT
RUN chmod 777 $SRV_ROOT
WORKDIR $SRV_ROOT
RUN mkdir -p config etc var log run lock

RUN curl https://bootstrap.pypa.io/get-pip.py -o var/get-pip.py

# RUN apt-get install -y python3-venv
RUN python3 -m venv env --without-pip
RUN env/bin/python var/get-pip.py
RUN if [ -f $SRV_ROOT/src/requirements.txt ]; then $SRV_ROOT/env/bin/pip install -r $SRV_ROOT/src/requirements.txt; fi
# RUN pip3 install virtualenv
# RUN virtualenv -p python3 env

VOLUME ["$SRV_ROOT/repo"]
CMD ["tail" , "-f" , "/dev/null"]

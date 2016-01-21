***************************************************************
docker-volume - Management tool of VirtualBox Volume for Docker
***************************************************************

It provide function of mounting local directories on the VirtualBox instance
with mount option. Using Docker Toolbox.

.. image:: https://circleci.com/gh/TakesxiSximada/docker-volume.svg?style=svg
   :target: https://circleci.com/gh/TakesxiSximada/docker-volume

Install
=======

Need Docker Toolbox.

.. code-block::

   $ pip install docker-volume


How to use it
=============

Configuration
-------------

$REPO_ROOT/docker-volume.yml

.. code-block::

   volumes:
     mysql:
       hostpath: ${here}/../volumes/mysql/
       vboxpath: /var/lib/mysql
       uid: 0
       gid: 0
       dmode: 777
     mongo:
       hostpath: ${here}/../volumes/mongo/
       vboxpath: /var/lib/mongo
       uid: 0
       gid: 0
       dmode: 777
     redis:
       hostpath: ${here}/../volumes/redis/
       vboxpath: /var/lib/redis
       uid: 0
       gid: 0
       dmode: 777

Add volume
----------

.. code-block::

   $ docker-volume add
   EXECUTE: VBoxManage sharedfolder add default --name docker-example_redis --hostpath /path/to/hostdir/volumes/redis
   EXECUTE: VBoxManage sharedfolder add default --name docker-example_mysql --hostpath /path/to/hostdir/volumes/mysql
   EXECUTE: VBoxManage sharedfolder add default --name docker-example_mongo --hostpath /path/to/hostdir/volumes/mongo

Mount volume
------------

Start docker machine.

.. code-block::

   $ docker-machine start default
   (dev) Starting VM...
   Machine "default" was started.
   Started machines may have new IP addresses. You may need to re-run the `docker-machine env` command.

mount volume.

.. code-block::

   $ docker-volume mount
   EXECUTE: docker-machine ssh default "sudo mkdir -p /var/lib/mysql &&  sudo mount -t vboxsf -o uid=0,gid=0,dmode=777 docker-example_mysql /var/lib/mysql"
   EXECUTE: docker-machine ssh default "sudo mkdir -p /var/lib/mongo &&  sudo mount -t vboxsf -o uid=0,gid=0,dmode=777 docker-example_mongo /var/lib/mongo"
   EXECUTE: docker-machine ssh default "sudo mkdir -p /var/lib/redis &&  sudo mount -t vboxsf -o uid=0,gid=0,dmode=777 docker-example_redis /var/lib/redis"

Make sure that it is mounted.

.. code-block::

   $ docker-machine ssh default "mount | grep /var/lib"
   /dev/sda1 on /mnt/sda1/var/lib/docker/aufs type ext4 (rw,relatime,data=ordered)
   none on /var/lib/mongo type vboxsf (rw,nodev,relatime)
   none on /var/lib/redis type vboxsf (rw,nodev,relatime)
   none on /var/lib/mysql type vboxsf (rw,nodev,relatime)


Unmount volume
--------------

Unmount volume.

.. code-block::

   $ docker-volume unmount
   EXECUTE: docker-machine ssh default "sudo umount /var/lib/redis"
   EXECUTE: docker-machine ssh default "sudo umount /var/lib/mysql"
   EXECUTE: docker-machine ssh default "sudo umount /var/lib/mongo"

Make sure that it is unmounted.

.. code-block::

   $ docker-machine ssh default "mount | grep /var/lib"
   /dev/sda1 on /mnt/sda1/var/lib/docker/aufs type ext4 (rw,relatime,data=ordered)


Remove volume
--------------

Stop docker machine.

.. code-block::

   $ docker-machine stop
   (dev) Stopping VM...
   Machine "default" was stopped.


Remove volume.

.. code-block::

   $ docker-volume remove
   EXECUTE: VBoxManage sharedfolder remove default --name docker-example_mongo
   EXECUTE: VBoxManage sharedfolder remove default --name docker-example_mysql
   EXECUTE: VBoxManage sharedfolder remove default --name docker-example_redis

Volume name
===========

Volume name is ${REPOSITORY_DIRECTORY_NAME}_${VOLUME_NAME}.

Other
=====

If you want to specify the machine name it?
-------------------------------------------

It specifies the `-m` or `--machine` option.

.. code-block::

   $ docker-volume add --dry-run --machine example
   EXECUTE: VBoxManage sharedfolder add example --transient --name docker-volume_repo --hostpath /path/to/hostdir/volumes/docker-volume
   EXECUTE: VBoxManage sharedfolder add example --transient --name docker-volume_spam --hostpath /path/to/hostdir/volumes/spam
   EXECUTE: VBoxManage sharedfolder add example --transient --name docker-volume_ham --hostpath /path/to/hostdir/volumes/ham

If you want to specify the single volume?
-----------------------------------------

It will specify a volume name if you want to operate a volume.

.. code-block::

   $ docker-volume add --dry-run spam
   EXECUTE: VBoxManage sharedfolder add default --transient --name docker-volume_spam --hostpath /path/to/hostdir/volumes/spam


and it will specify two volume name if you want to operate two volumes.

.. code-block::

   $ docker-volume add --dry-run spam ham
   EXECUTE: VBoxManage sharedfolder add default --transient --name docker-volume_spam --hostpath /path/to/hostdir/volumes/spam
   EXECUTE: VBoxManage sharedfolder add default --transient --name docker-volume_ham --hostpath /path/to/hostdir/volumes/ham

If you do not specify a volume name, all volumes are operation.

Development
===========

Source code repository: https://pypi.python.org/pypi/docker-volume

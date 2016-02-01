import os.path


class Volume(object):
    def __init__(self, hostpath, vboxpath, uid=None,
                 gid=None, dmode=None, fmode=None, directory=None):
        self.hostpath = os.path.abspath(hostpath)
        self.vboxpath = vboxpath

        self.uid = uid
        self.gid = gid
        self.dmode = dmode
        self.fmode = fmode
        self.directory = directory

    def to_dict(self):
        return {
            'hostpath': self.hostpath,
            'vboxpath': self.vboxpath,
            'uid': self.uid,
            'gid': self.gid,
            'dmode': self.dmode,
            'fmode': self.fmode,
            'directory': self.directory,
        }

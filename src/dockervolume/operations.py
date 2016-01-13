from zope.interface import implementer
from .interfaces import IOperation


class VolumeOperationMixin(object):
    @staticmethod
    def get_names(setting, *names):
        if not names:
            names = setting.keys()
        return names


@implementer(IOperation)
class VolumeOperation(VolumeOperationMixin):
    def __init__(self, func):
        self.func = func

    def __call__(self, setting, *names):
        names = self.get_names(setting, *names)
        for name in names:
            volume_name = setting.get_volume_name(name)
            child = self.func(setting.name, volume_name, **setting[name].to_dict())
            res = child.wait()
            if res != 0:
                return res
        return 0

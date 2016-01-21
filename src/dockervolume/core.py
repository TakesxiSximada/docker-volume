from .exc import NoOperationError
from .interfaces import (
    ISetting,
    IOperation,
    )


class VolumeCommand(object):
    def __init__(self, registry):
        self.registry = registry

    def __call__(self, cmd, *args, **kwds):
        func = self.registry.queryUtility(IOperation, cmd)
        if func is None:
            raise NoOperationError('`{}` is not supported command'.format(cmd))
        setting = self.registry.queryUtility(ISetting)
        return func(setting, *args, **kwds)

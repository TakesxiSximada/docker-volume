from zope.interface import Interface


class IOperation(Interface):
    def __call__(self, setting, *names):
        pass


class ISetting(Interface):
    pass

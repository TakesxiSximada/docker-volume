from zope.component import getGlobalSiteManager


def get_registry():
    return getGlobalSiteManager()

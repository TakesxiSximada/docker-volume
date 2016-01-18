# -*- coding: utf-8 -*-
import os
from os import makedirs as _makedirs
import sys
from sys import version_info
from six import (
    PY2,
    PY3,
    )


class VersionError(Exception):
    pass


def equal_version(major, minor):
    return version_info.major == major and version_info.minor == minor


def or_later_version(major, minor):
    return version_info >= (major, minor)


def before_version(major, minor):
    return version_info < (major, minor)


PY23 = equal_version(2, 3)  # noqa
PY24 = equal_version(2, 4)
PY25 = equal_version(2, 5)
PY26 = equal_version(2, 6)
PY27 = equal_version(2, 7)
PY30 = equal_version(3, 0)
PY31 = equal_version(3, 1)
PY32 = equal_version(3, 2)
PY33 = equal_version(3, 3)
PY34 = equal_version(3, 4)
PY35 = equal_version(3, 5)
PY36 = equal_version(3, 6)


PY23_BEFORE = before_version(2, 3)
PY24_BEFORE = before_version(2, 4)
PY25_BEFORE = before_version(2, 5)
PY26_BEFORE = before_version(2, 6)
PY27_BEFORE = before_version(2, 7)
PY30_BEFORE = before_version(3, 0)
PY31_BEFORE = before_version(3, 1)
PY32_BEFORE = before_version(3, 2)
PY33_BEFORE = before_version(3, 3)
PY34_BEFORE = before_version(3, 4)
PY35_BEFORE = before_version(3, 5)
PY36_BEFORE = before_version(3, 6)


PY23_OR_LATER = or_later_version(2, 3)
PY24_OR_LATER = or_later_version(2, 4)
PY25_OR_LATER = or_later_version(2, 5)
PY26_OR_LATER = or_later_version(2, 6)
PY27_OR_LATER = or_later_version(2, 7)
PY30_OR_LATER = or_later_version(3, 0)
PY31_OR_LATER = or_later_version(3, 1)
PY32_OR_LATER = or_later_version(3, 2)
PY33_OR_LATER = or_later_version(3, 3)
PY34_OR_LATER = or_later_version(3, 4)
PY35_OR_LATER = or_later_version(3, 5)
PY36_OR_LATER = or_later_version(3, 6)


def get_implementation():
    if PY33_BEFORE:
        version_str = sys.version.lower()
        if 'pypy' in version_str:
            return 'pypy'
        elif 'jython' in version_str:
            return 'jython'
        elif 'iron' in version_str:
            return 'iron'
        else:
            return 'unknown'
    else:
        return sys.implementation


def get_platform():
    if PY33_BEFORE and sys.platform.startswith('linux'):
        return 'linux'  # see: http://docs.python.org/3.3/library/sys.html#sys.platform
    else:
        return sys.platform


platform = get_platform()
implementation = get_implementation()


# https://github.com/requests/requests-docs-bg/blob/master/requests/compat.py
if PY2:
    from urllib import quote, unquote, quote_plus, unquote_plus, urlencode
    from urlparse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
    from urllib2 import parse_http_list
    import cookielib
    from Cookie import Morsel
    from StringIO import StringIO
elif PY3:
    from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag  # noqa
    from urllib.request import parse_http_list  # noqa
    from http import cookiejar as cookielib  # noqa
    from http.cookies import Morsel  # noqa
    from io import StringIO  # noqa
    from collections import OrderedDict  # noqa
else:
    VersionError('Unknown version')


if PY33_OR_LATER:
    from functools import lru_cache
else:
    from repoze.lru import lru_cache  # noqa


def makedirs_for_py2k(path, *args, **kwds):
    if kwds.get('exist_ok', None):
        del kwds['exist_ok']
        if not os.path.isdir(path):
            return _makedirs(path, *args, **kwds)
    else:
        return _makedirs(path, *args, **kwds)

makedirs = _makedirs if PY3 else makedirs_for_py2k

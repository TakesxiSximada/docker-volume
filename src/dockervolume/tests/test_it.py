# -*- coding: utf-8 -*-
from unittest import TestCase


class DummyTest(TestCase):
    def _get_target(self):
        from .. import dummy_for_unittest as fn
        return fn

    def _call_fut(self, *args, **kwds):
        fn = self._get_target()
        return fn(*args, **kwds)

    def test_it(self):
        res = self._call_fut()
        self.assertEqual('hello world', res)

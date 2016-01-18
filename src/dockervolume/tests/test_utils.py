from unittest import TestCase


class FileSearchTest(TestCase):
    def test_it(self):
        import os
        import shutil
        import tempfile
        from ..utils import (
            makedirs,
            search_file,
            )

        path = tempfile.mkdtemp()
        try:
            work_dir = os.path.join(path, 'a/b/c/d')
            makedirs(work_dir, exist_ok=True)
            target_file = os.path.abspath(os.path.join(path, 'TARGETFILE'))
            with open(target_file, 'w+b') as fp:
                fp.write('dummy'.encode())
            ans = os.path.abspath(search_file('TARGETFILE', work_dir))
            self.assertEqual(target_file, ans)
        finally:
            shutil.rmtree(path)

    def test_nothing(self):
        import os
        import shutil
        import tempfile
        from ..utils import (
            makedirs,
            search_file,
            )
        path = tempfile.mkdtemp()
        try:
            work_dir = os.path.join(path, 'a/b/c/d')
            makedirs(work_dir, exist_ok=True)
            ans = search_file('TARGETFILE', work_dir)
            self.assertIsNone(None, ans)
        finally:
            shutil.rmtree(path)

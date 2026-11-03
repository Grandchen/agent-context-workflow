"""Exercise public-package failure detection on temporary synthetic copies."""
from pathlib import Path
import os
import shutil
import tempfile
import unittest

from check_package import check


class PackageChecks(unittest.TestCase):
    def setUp(self):
        scratch_base = os.environ.get('ACW_TEST_TMP')
        self.scratch = tempfile.TemporaryDirectory(dir=scratch_base)
        allowed = Path(scratch_base or tempfile.gettempdir()).resolve()
        if not Path(self.scratch.name).resolve().is_relative_to(allowed):
            raise RuntimeError('Unexpected test scratch location')
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name) / 'package'
        original = Path(__file__).resolve().parents[1]
        shutil.copytree(original, self.root,
                        symlinks=True,
                        ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))

    def test_current_package(self):
        self.assertEqual(check(self.root)[0], [])

    def test_missing_reference(self):
        path = self.root / 'skills/context-workflow/references/navigation.md'
        path.unlink()
        self.assertTrue(any('missing/escaping relative link' in item for item in check(self.root)[0]))

    def test_existing_file_outside_package_is_rejected(self):
        (self.root.parent / 'outside.md').write_text('synthetic', encoding='utf-8')
        with (self.root / 'README.md').open('a', encoding='utf-8') as stream:
            stream.write('\n[escape](../outside.md)\n')
        self.assertTrue(any('missing/escaping relative link' in item for item in check(self.root)[0]))

    def test_machine_path_is_reported_without_echoing_content(self):
        path_text = 'C:' + '/' + 'Users' + '/synthetic/private.md'
        (self.root / 'leak.md').write_text(path_text, encoding='utf-8')
        problems = check(self.root)[0]
        self.assertTrue(any('machine-local absolute path' in item for item in problems))
        self.assertFalse(any(path_text in item for item in problems))

    def test_other_local_path_forms(self):
        examples = ['d:' + r'\private\record.md', r'\\server\share\record.md',
                    r'\\?\UNC\server\share\private.md', r'\\.\pipe\synthetic',
                    '/home/synthetic/record.md', '/Users/synthetic/record.md', '/etc/synthetic.conf',
                    'file:///synthetic/record.md']
        for value in examples:
            with self.subTest(value=value):
                (self.root / 'leak.md').write_text(value, encoding='utf-8')
                self.assertTrue(any('machine-local absolute path' in item for item in check(self.root)[0]))
                self.assertFalse(any(value in item for item in check(self.root)[0]))


if __name__ == '__main__':
    unittest.main()

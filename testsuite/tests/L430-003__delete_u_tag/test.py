from support import *
import re

class TestRun(TestCase):
    def test_delete_unannotated_tag(self):
        """Try deleting an unnanotated tag.
        """
        cd ('%s/repo' % TEST_DIR)

        p = Run('git push origin :some-tag'.split())
        self.assertEqual(p.status, 0, ex_run_image(p))
        self.assertTrue(re.match('.*-\s+\[deleted\]\s+some-tag',
                                 p.out, re.DOTALL),
                        ex_run_image(p))

if __name__ == '__main__':
    runtests()
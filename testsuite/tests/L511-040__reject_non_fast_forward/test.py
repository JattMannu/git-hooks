from support import *

class TestRun(TestCase):
    def test_push_commit_on_master(self):
        """Try non-fast-forward push on master.
        """
        cd ('%s/repo' % TEST_DIR)

        p = Run('git push -f origin master'.split())

        self.assertTrue(p.status != 0, p.image)

        expected_out = (
            r".*Non-fast-forward updates are not allowed on this branch;" +
            r".*error: hook declined to update refs/heads/master" +
            r".*\[remote rejected\]\s+master\s+->\s+master\s+" +
                r"\(hook declined\)")

        self.assertTrue(re.match(expected_out, p.cmd_out, re.DOTALL),
                        p.image)

if __name__ == '__main__':
    runtests()

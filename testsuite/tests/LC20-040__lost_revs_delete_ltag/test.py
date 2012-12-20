from support import *

class TestRun(TestCase):
    def test_delete_tag(self):
        """Delete a lightweight tag causing multiple commits to be lost.
        """
        cd ('%s/repo' % TEST_DIR)

        p = Run('git push origin :retired/gdb-7.2'.split())
        expected_out = """\
remote: DEBUG: Content-Type: text/plain; charset="us-ascii"
remote: MIME-Version: 1.0
remote: Content-Transfer-Encoding: 7bit
remote: From: Test Suite <testsuite@adacore.com>
remote: To: git-hooks-ci@example.com
remote: Bcc: file-ci@gnat.com
remote: Subject: [repo] Deleted tag retired/gdb-7.2
remote: X-ACT-checkin: repo
remote: X-Git-Refname: refs/tags/retired/gdb-7.2
remote: X-Git-Oldrev: dd6165c96db712d3e918fb5c61088b171b5e7cab
remote: X-Git-Newrev: 0000000000000000000000000000000000000000
remote:
remote: The lightweight tag 'retired/gdb-7.2' was deleted.
remote: It previously pointed to:
remote:
remote:  dd6165c... Modify file `d' alone.
remote:
remote: !!! WARNING: THE FOLLOWING COMMITS ARE NO LONGER ACCESSIBLE (LOST):
remote: -------------------------------------------------------------------
remote:
remote:   4f0f08f... Minor modifications.
remote:   4a325b3... 1 modified file, 1 new file.
remote:   cc8d2c2... Modify `c', delete `b'.
remote:   dd6165c... Modify file `d' alone.
To ../bare/repo.git
 - [deleted]         retired/gdb-7.2
"""
        self.assertTrue(p.status == 0, p.image)
        self.assertEqual(expected_out, p.cmd_out, p.image)

if __name__ == '__main__':
    runtests()
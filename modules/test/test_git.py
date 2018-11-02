import unittest
from mock import MagicMock
from modules import git
from web import catch_timeout

class TestGit(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    @catch_timeout
    def test_issue_missingArgument(self):
        self.input.group = lambda x: [None, 'someorg/somerepo somehandle'][x]
        git.post_issue(self.phenny, self.input)
        self.phenny.say.assert_called_once_with(
            "Please try again. Usage: .issue <org>/<repo> handle> <password> <issue title>")

    @catch_timeout
    def test_issue_noArgument(self):
        self.input.group = lambda x: [None, ''][x]
        git.post_issue(self.phenny, self.input)
        self.phenny.say.assert_called_once_with(
            "Usage: .issue <org>/<repo> handle> <password> <issue title>")

    @catch_timeout
    def test_issue_invalidPassword(self):
        self.input.group = lambda x: [None, 'luo-yuyuan/phenny luo-yuyuan wrongpassword Issue Title'][x]
        git.post_issue(self.phenny, self.input)
        self.phenny.say.assert_called_once_with(
            "Please try again. Usage: .issue <org>/<repo> <handle> <password> <issue title>")
        
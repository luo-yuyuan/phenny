import unittest
from mock import MagicMock
from modules import choose
from web import catch_timeout


class TestChoose(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_valid(self):
        self.input.group = lambda x: ['.choose', 'canada usa'][x]
        choose.choose(self.phenny, self.input)
        out = self.phenny.reply.call_args[0][0]
        m = (out == 'canada' or out == 'usa')
        self.assertTrue(m)

    def test_valid2(self):
        self.input.group = lambda x: ['.choose', 'chocolate vanilla'][x]
        choose.choose(self.phenny, self.input)
        out = self.phenny.reply.call_args[0][0]
        m = (out == 'chocolate' or out == 'vanilla')
        self.assertTrue(m)
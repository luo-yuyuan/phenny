import unittest
from mock import MagicMock
from modules import choose
from web import catch_timeout


class TestChoose(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    @catch_timeout
    def test_valid(self):
        self.input.group = lambda x: ['', '.choose canada usa'][x]
        choose.choose(self.phenny, self.input)
        out = self.phenny.reply.call_args[0][0]
        self.assertTrue(out == 'canada' or out == 'usa')

    @catch_timeout
    def test_valid2(self):
        self.input.group = lambda x: ['', '.choose chocolate vanilla'][x]
        choose.choose(self.phenny, self.input)
        out = self.phenny.reply.call_args[0][0]
        self.assertFalse(out != 'chocolate' and out != 'vanilla')
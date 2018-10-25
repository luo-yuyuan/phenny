import unittest
from mock import MagicMock
from modules import chillmeter
from web import catch_timeout


class TestChillmeter(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    @catch_timeout
    def test_chill(self):
        chillmeter.chill(self.phenny, self.input)
        self.assertTrue(self.phenny.say.called)





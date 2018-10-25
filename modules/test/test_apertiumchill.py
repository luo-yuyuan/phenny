import unittest
from mock import MagicMock
from modules import apertiumchill
from web import catch_timeout


class TestApertiumchill(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    @catch_timeout
    def test_chill(self):
        apertiumchill.chill(self.phenny, self.input)
        self.assertTrue(self.phenny.say.called)
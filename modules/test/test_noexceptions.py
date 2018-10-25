import unittest
from mock import MagicMock
from modules import noexceptions
from web import catch_timeout


class TestChoose(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()
        self.input.nick = 'Testuser'
        self.input.group = lambda x: ['', 'test'][x]

    @catch_timeout
    def test_noexceptions(self):
        noexceptions.noexceptions(self.phenny, self.input)
        self.phenny.say.assert_called_once_with('NO EXCEPTIONS, Testuser!')

    @catch_timeout
    def test_harglebarglep(self):
        noexceptions.harglebargleP(self.phenny, self.input)
        self.phenny.say.assert_called_once_with('HARGLE BARGLE, test!')

    @catch_timeout
    def test_bargle(self):
        self.input = 'hargle'
        noexceptions.bargle(self.phenny, self.input)
        self.phenny.say.assert_called_once_with('bargle!')

    @catch_timeout
    def test_hargle(self):
        self.input = 'bargle'
        noexceptions.hargle(self.phenny, self.input)
        self.phenny.say.assert_called_once_with('HARGLE BARGLE!')

    @catch_timeout
    def test_udmurt(self):
        self.input = 'udmurt'
        noexceptions.udmurt(self.phenny, self.input)
        self.phenny.say.assert_called_once_with('\o/ \o/ \o/ U D M U R T \o/ \o/ \o/')

    @catch_timeout
    def test_particles(self):
        noexceptions.particles(self.phenny, self.input)
        self.phenny.say.assert_called_once_with('Testuser: this is my particles face :(((((')

    @catch_timeout
    def test_nightnight(self):
        message = ['nn, Testuser!', 'night, Testuser!', 'жашкы жат, Testuser!', 'later, Testuser!', 'sweet dreams, Testuser!', 'o/, Testuser!']
        noexceptions.nightnight(self.phenny, self.input)
        out = self.phenny.say.call_args[0][0]
        self.assertTrue(out in message)

    @catch_timeout
    def test_uderp(self):
        message = ['\o/ UD \o/, Testuser!', '（。々°） #u_dep, Testuser!', 'ᕕ(ᐛ)ᕗ #u_dep, Testuser!', 'universal derpendencies!, Testuser!', 'treegrams ftw!, Testuser!']
        noexceptions.uderp(self.phenny, self.input)
        out = self.phenny.say.call_args[0][0]
        self.assertTrue(out in message)
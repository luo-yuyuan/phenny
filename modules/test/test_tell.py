"""
Tests for phenny's tell.py
"""

import unittest
import datetime
from mock import MagicMock
from modules import tell

class TestTell(unittest.TestCase):

    def setUp(self):
        self.phenny = MagicMock()
        self.phenny.nick = 'phenny'
        self.phenny.config.host = 'irc.freenode.net'

        self.input = MagicMock()

        tell.setup(self.phenny)

    def create_alias(self, alias):
        self.input.group = lambda x: ['', 'add', alias][x]
        tell.alias(self.phenny, self.input)
        tell.aliasPairMerge(self.phenny, self.input.nick, alias)

    def create_reminder(self, teller):
        timenow = datetime.datetime.utcnow().strftime('%d %b %Y %H:%MZ')
        self.phenny.reminders[teller] = [(teller, 'do', timenow, 'something')]

    def test_messageAlert(self):
        self.input.sender = '#testsworth'
        self.input.nick = 'Testsworth'

        aliases = ['tester', 'testing', 'testmaster']
        self.phenny.reminders = {}

        for alias in aliases:
            self.create_alias(alias)
            self.create_reminder(alias)

        tell.messageAlert(self.phenny, self.input)

        text = ': You have messages. Say something, and I\'ll read them out.'
        self.phenny.say.assert_called_once_with(self.input.nick + text)

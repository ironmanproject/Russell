#!usr/bin/env python3

import unittest
from process_commands import *

keywords = []
phrase = ''
string = 'Hello World!'

class TestProcessCommands(unittest.TestCase):

  def test_keywords(self):
    self.assertEqual(find_keywords(string), 'Hello World')

if __name__ == '__main__':
  unittest.main()

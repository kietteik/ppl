import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.test("a11bdc","a11bdc,<EOF>",102))
      
    def test_float(self):
        """test real"""
        self.assertTrue(TestLexer.test("1.0 1e-12 1.0e-12 0.000000001","1.0,1e-12,1.0e-12,0.000000001,<EOF>",101))

    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.test(' \'Minh\'\'t\' ',"Minh,t,<EOF>",103))

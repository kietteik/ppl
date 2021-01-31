import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            "abDc123a", "abDc123a,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_real_1(self):
        self.assertTrue(TestLexer.checkLexeme("1e+3", "1e+3,<EOF>", 108))

    def test_real_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.e+3", "Error Token 1,<EOF>", 109))

    def test_real_3(self):
        self.assertTrue(TestLexer.checkLexeme("1.1e+3", "1.1e+3,<EOF>", 110))

    def test_real_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            ".11e+3", "Error Token .,<EOF>", 111))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'abcdef'", "'abcdef',<EOF>", 112))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'ab''cdef'", "'ab''cdef',<EOF>", 113))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'ab'''cdef'", "'ab''',cdef,Error Token '", 114))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'aAGHJb''''cde#$&^&*(^(^(()f'", "'aAGHJb''''cde#$&^&*(^(^(()f',<EOF>", 115))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "dsds''a'", "dsds,'',a,Error Token '", 116))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'dsds''a", "'dsds',Error Token '", 117))

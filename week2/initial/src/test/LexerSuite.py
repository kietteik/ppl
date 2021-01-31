import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    # def test_real(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         '1e12', "1e12,<EOF>", 100))

    def test_real1(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1.e12', "Error Token 1", 101))

    def test_real2(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1..e12', "Error Token 1", 102))

    def test_real3(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1e-12', "1e-12,<EOF>", 103))

    def test_real4(self):
        self.assertTrue(TestLexer.checkLexeme(
            '0.0000001', "0.0000001,<EOF>", 104))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'abcdef'", "'abcdef',<EOF>", 112))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'ab''cdef'", "'ab''cdef',<EOF>", 113))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'ab'''cdef'", "'ab''',cdef,Error Token '", 114))

    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a12345", "a12345,<EOF>", 121))

    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "b78123", "b78123,<EOF>", 122))

    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "123", "Error Token 1", 123))

    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "223bs", "Error Token 2", 124))

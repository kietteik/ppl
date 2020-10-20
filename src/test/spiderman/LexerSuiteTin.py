import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_id_1(self):
        self.assertTrue(TestLexer.checkLexeme("t", "t,<EOF>", 101))

    def test_id_2(self):
        self.assertTrue(TestLexer.checkLexeme("test", "test,<EOF>", 102))

    def test_id_3(self):
        self.assertTrue(TestLexer.checkLexeme("te5t", "te5t,<EOF>", 103))

    def test_id_4(self):
        self.assertTrue(TestLexer.checkLexeme("tE5t", "tE5t,<EOF>", 104))

    def test_id_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "test____", "test____,<EOF>", 105))

    def test_id_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "t1e2s__3t5", "t1e2s__3t5,<EOF>", 106))

    def test_id_7(self):
        self.assertTrue(TestLexer.checkLexeme("Test", "Error Token T", 107))

    def test_id_8(self):
        self.assertTrue(TestLexer.checkLexeme("T_e_5_t", "Error Token T", 108))

    def test_id_9(self):
        self.assertTrue(TestLexer.checkLexeme("11st", "11,st,<EOF>", 109))

    def test_id_10(self):
        self.assertTrue(TestLexer.checkLexeme("11St", "11,Error Token S", 110))

    def test_id_11(self):
        self.assertTrue(TestLexer.checkLexeme("_", "Error Token _", 111))

    def test_id_12(self):
        self.assertTrue(TestLexer.checkLexeme("._st", ".,Error Token _", 112))

    def test_id_13(self):
        self.assertTrue(TestLexer.checkLexeme("*T123", "*,Error Token T", 113))

    def test_id_14(self):
        self.assertTrue(TestLexer.checkLexeme("+t____", "+,t____,<EOF>", 114))

    def test_id_15(self):
        self.assertTrue(TestLexer.checkLexeme("t_eS+", "t_eS,+,<EOF>", 115))

    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("1", "1,<EOF>", 116))

    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 117))

    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("0x123", "0x123,<EOF>", 118))

    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("0X123", "0X123,<EOF>", 119))

    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>", 120))

    def test_integer_6(self):
        self.assertTrue(TestLexer.checkLexeme("0O123", "0O123,<EOF>", 121))

    def test_integer_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0xA123EF", "0xA123EF,<EOF>", 122))

    def test_integer_8(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 123))

    def test_integer_9(self):
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>", 124))

    def test_integer_10(self):
        self.assertTrue(TestLexer.checkLexeme("0x0123", "0,x0123,<EOF>", 125))

    def test_integer_11(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0x123EFG", "0x123EF,Error Token G", 126))

    def test_integer_12(self):
        self.assertTrue(TestLexer.checkLexeme("0o0123", "0,o0123,<EOF>", 127))

    def test_integer_13(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o12345678", "0o1234567,8,<EOF>", 128))

    def test_integer_14(self):
        self.assertTrue(TestLexer.checkLexeme("0x", "0,x,<EOF>", 129))

    def test_integer_15(self):
        self.assertTrue(TestLexer.checkLexeme("0o", "0,o,<EOF>", 130))

    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("12.3e+1", "12.3e+1,<EOF>", 131))

    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.34e-1", "12.34e-1,<EOF>", 132))

    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("12.34e1", "12.34e1,<EOF>", 133))

    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("12.e+1", "12.e+1,<EOF>", 134))

    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-1", "12.e-1,<EOF>", 135))

    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("12.e1", "12.e1,<EOF>", 136))

    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("12.34", "12.34,<EOF>", 137))

    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("12.", "12.,<EOF>", 138))

    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("12e+34", "12e+34,<EOF>", 139))

    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("0e34", "0e34,<EOF>", 140))

    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme(".34", ".,34,<EOF>", 141))

    def test_float_12(self):
        self.assertTrue(TestLexer.checkLexeme(".3e+44", ".,3e+44,<EOF>", 142))

    def test_float_13(self):
        self.assertTrue(TestLexer.checkLexeme(".3e45", ".,3e45,<EOF>", 143))

    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme("e+12", "e,+,12,<EOF>", 144))

    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12e.34", "12,e,.,34,<EOF>", 145))

    def test_float_16(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.2e.34", "1.2,e,.,34,<EOF>", 146))

    def test_float_17(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.2.e+34", "1.2,.,e,+,34,<EOF>", 147))

    def test_float_18(self):
        self.assertTrue(TestLexer.checkLexeme("12e34.", "12e34,.,<EOF>", 148))

    def test_float_19(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12..e+34", "12.,.,e,+,34,<EOF>", 149))

    def test_float_20(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12..34e+5", "12.,.,34e+5,<EOF>", 150))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme('"abc"', 'abc,<EOF>', 151))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abc\'"def"', 'abc\'"def,<EOF>', 152))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme('""', ',<EOF>', 153))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme('"abc\b"', 'abc,<EOF>', 154))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme('"abc\f"', 'abc,<EOF>', 155))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme('"abc\t"', 'abc	,<EOF>', 156))

    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme('"abc\r"', 'abc\n,<EOF>', 157))

    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abc\b\f\t\r\'""', 'abc	\n\'",<EOF>', 158))

    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\bcdef"', 'a\\bcdef,<EOF>', 159))

    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\bcdef"', 'a\\bcdef,<EOF>', 160))

    def test_string_11(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\fcdef"', 'a\\fcdef,<EOF>', 161))

    def test_string_12(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\rcdef"', 'a\\rcdef,<EOF>', 162))

    def test_string_13(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\ncdef"', 'a\\ncdef,<EOF>', 163))

    def test_string_14(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\tcdef"', 'a\\tcdef,<EOF>', 164))

    def test_string_15(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\\'cdef"', 'a\\\'cdef,<EOF>', 165))

    def test_string_16(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\\\cdef"', 'a\\\\cdef,<EOF>', 166))

    def test_string_17(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"a\\b\\f\\r\\n\\t\\\'\\\\cdef"', 'a\\b\\f\\r\\n\\t\\\'\\\\cdef,<EOF>', 167))

    def test_string_18(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"\\c"', 'Illegal Escape In String: \c', 168))

    def test_string_19(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"\\"', 'Illegal Escape In String: \\"', 169))

    def test_string_20(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abd\'def"', 'Illegal Escape In String: abd\'d', 170))

    def test_string_21(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abcdef', 'Unclosed String: abcdef', 171))

    def test_string_22(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abc\ndef"', 'Unclosed String: abc', 172))

    def test_string_23(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"\nabcdef"', 'Unclosed String: ', 173))

    def test_string_24(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abcdef\n"', 'Unclosed String: abcdef', 174))

    def test_string_25(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abc"def', 'abc,def,<EOF>', 175))

    def test_string_26(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abc""def', 'abc,Unclosed String: def', 176))

    def test_string_27(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abcdef\\b', 'Unclosed String: abcdef\\b', 177))

    def test_string_28(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"abcdef\\b', 'Unclosed String: abcdef\\b', 178))

    def test_string_29(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"He asked me: \'"Where is John?\'""', 'He asked me: \'"Where is John?\'",<EOF>', 179))

    def test_string_30(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"He asked" me: \'"Where is John?\'""', 'He asked,me,:,Error Token \'', 180))

    def test_array_1(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3}", "{1,2,3},<EOF>", 181))

    def test_array_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,3},{2,1},{1,2}}", "{{1,3},{2,1},{1,2}},<EOF>", 182))

    def test_array_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{{1}},{{2}},{3}}", "{{{1}},{{2}},{3}},<EOF>", 183))

    def test_array_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,2},{{2}},{3}}", "{{1,2},{{2}},{3}},<EOF>", 184))

    def test_array_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,{2}}}", "{,{,1,,,{2},},},<EOF>", 185))

    def test_array_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,2,1},{1,2},{1}}", "{{1,2,1},{1,2},{1}},<EOF>", 186))

    def test_array_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{ {1.2, 2.3, 1.4},{  1.5 , 2.6},{ 1.7}}", "{ {1.2, 2.3, 1.4},{  1.5 , 2.6},{ 1.7}},<EOF>", 187))

    def test_array_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{ 1  , 2 ,    3 }", "{ 1  , 2 ,    3 },<EOF>", 188))

    def test_array_9(self):
        self.assertTrue(TestLexer.checkLexeme(
            '{{True,False},{{True}},{False}}', '{{True,False},{{True}},{False}},<EOF>', 189))

    def test_array_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            '{{12.e5,12.e5},{{12.e5}},{12.e5}}', '{{12.e5,12.e5},{{12.e5}},{12.e5}},<EOF>', 190))

    def test_cmt_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            '** This is a comment.**', '<EOF>', 191))

    def test_cmt_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            '** This is first comment.**** This is second comment.**', '<EOF>', 192))

    def test_cmt_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            '** This is a comment.', 'Unterminated Comment', 193))

    def test_cmt_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            '** This is a * comment.', 'Unterminated Comment', 194))

    def test_cmt_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            '** This is a comment.*', 'Unterminated Comment', 195))

    def test_cmt_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            '** This is a ** comment.**', 'comment,.,Unterminated Comment', 196))

    def test_cmt_7(self):
        self.assertTrue(TestLexer.checkLexeme('*****', '*,<EOF>', 197))

    def test_cmt_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            'This is a ** comment.**', 'Error Token T', 198))

    def test_bool_1(self):
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 198))

    def test_bool_2(self):
        self.assertTrue(TestLexer.checkLexeme("False", "False,<EOF>", 199))

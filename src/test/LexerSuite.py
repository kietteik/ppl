import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("aBBc", "aBBc,<EOF>", 102))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("bEAs12d", "bEAs12d,<EOF>", 103))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a__CS__", "a__CS__,<EOF>", 104))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "__a_b1_CS", "Error Token _", 105))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "A_b1_CS", "Error Token A", 106))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "23abc_a", "23,abc_a,<EOF>", 107))

    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "e-123Bb", "e,-,123,Error Token B", 108))

    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("bCD__12", "bCD__12,<EOF>", 109))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("______", "Error Token _", 110))

    def test_int_1(self):
        self.assertTrue(TestLexer.checkLexeme("0x12F3", "0x12F3,<EOF>", 111))

    def test_int_2(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC", "0XABC,<EOF>", 112))

    def test_int_3(self):
        self.assertTrue(TestLexer.checkLexeme("0X0", "0,Error Token X", 113))

    def test_int_4(self):
        self.assertTrue(TestLexer.checkLexeme("0XA00A", "0XA00A,<EOF>", 114))

    def test_int_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o0", "0,o0,<EOF>", 115))

    def test_int_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "230", "230,<EOF>", 116))

    def test_int_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0O4619", "0O461,9,<EOF>", 117))

    def test_int_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0O4617", "0O4617,<EOF>", 118))

    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("10e-10", "10e-10,<EOF>", 119))

    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0.e-2", "0.e-2,<EOF>", 120))

    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0.12e-10", "0.12e-10,<EOF>", 121))

    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("12.e", "12.,e,<EOF>", 122))

    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.1e-10", "12.1e-10,<EOF>", 123))

    def test_bool_1(self):
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 124))

    def test_bool_2(self):
        self.assertTrue(TestLexer.checkLexeme("False", "False,<EOF>", 125))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"abc\\n \\t \\r def\"", "abc\\n \\t \\r def,<EOF>", 126))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"He asked me: \'"Where is John?\'"', 'Unclosed String: He asked me: \'"Where is John?\'"', 127))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"This is a string containing tab \t\"", "This is a string containing tab \t,<EOF>", 128))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"This is a test string with \'" ** see ** wahphapp"', "This is a test string with '\" ** see ** wahphapp,<EOF>", 129))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"This is a test string with \\\'abc""', 'This is a test string with \\\'abc,Unclosed String: ', 130))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            '"This is a test string with \'abc""', "Illegal Escape In String: This is a test string with 'a", 131))

    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"This is a string containing tab \\t\"", "This is a string containing tab \\t,<EOF>", 132))

    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"This is a string containing escapeSeq\\b \\r \\\\ \\t\"", "This is a string containing escapeSeq\\b \\r \\\\ \\t,<EOF>", 133))

    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"abcd '\"", "Unclosed String: abcd '\"", 134))

    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"'\"''", "Illegal Escape In String: '\"''", 135))

    def test_array_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{1,1,3}", '{1,1,3},<EOF>', 139))

    def test_array_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{{1,0x26F7},{2,1},{1,2}}""", "{{1,0x26F7},{2,1},{1,2}},<EOF>", 140))

    def test_array_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{{1}},{{2}},{3}}", "{{{1}},{{2}},{3}},<EOF>", 141))

    def test_array_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,2},{{2}},{3}}", "{{1,2},{{2}},{3}},<EOF>", 142))

    def test_array_5(self):
        # chua bao loi
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,{2}}}", "{,{,1,,,{2},},},<EOF>", 143))

    def test_array_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1,2,1},{1,2},{1}}", "{{1,2,1},{1,2},{1}},<EOF>", 144))

    def test_array_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{1.2, 2.3,  1.4},{1.5,2.6},{1.7}}", "{{1.2, 2.3,  1.4},{1.5,2.6},{1.7}},<EOF>", 145))

    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "** put anything inside the comment section **", "<EOF>", 146))

    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**odd**** test second comment **", "<EOF>", 147))

    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**even**** test second comment **", "<EOF>", 148))

    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**odd**abd** test second comment **123", "abd,123,<EOF>", 149))

    def test_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**even**{1,2,3}** test second comment **", "{1,2,3},<EOF>", 150))

    def test_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**even**{1,2,3}* test second comment **", "{1,2,3},*,test,second,comment,Unterminated Comment", 151))

    def test_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**even***Var{1,2,3}** test second comment **", "*,Var,{1,2,3},<EOF>", 152))

    def test_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**even**{1,2,3}* thisId****", "{1,2,3},*,thisId,<EOF>", 153))

    def test_comment_9(self):
        self.assertTrue(TestLexer.checkLexeme(
            "**even**{1,2,3}*****texting *asd****", "{1,2,3},*,texting,*,asd,<EOF>", 154))

    def test_comment_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a********  *** **** *acd*", "a,Unterminated Comment", 155))

    def test_comment_11(self):
        self.assertTrue(TestLexer.checkLexeme(
            "*** * **** **", "<EOF>", 156))

    def test_statement_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: a=2", "Var,:,a,=,2,<EOF>", 157))

    def test_statement_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "var=0x123abc;", "var,=,0x123,abc,;,<EOF>", 158))

    def test_statement_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Function: name Do EndFor. V=", "Function,:,name,Do,EndFor,.,Error Token V", 159))

    def test_statement_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "If a==True Then", "If,a,==,True,Then,<EOF>", 160))

    def test_statement_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "While identifiers Do EndWhile.", "While,identifiers,Do,EndWhile,.,<EOF>", 161))

    def test_operators_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "!True", "!,True,<EOF>", 162))

    def test_operators_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "+.*./.-.", "+.,*.,Error Token /", 163))

    def test_operators_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "+-*%%..==", "+,-,*,%,%,.,.,==,<EOF>", 164))

    def test_operators_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a||b\\c\\.d", "a,||,b,\,c,\.,d,<EOF>", 165))

    def test_operators_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a==d+.3*-4", "a,==,d,+.,3,*,-,4,<EOF>", 166))

    def test_operators_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a&&b||c", "a,&&,b,||,c,<EOF>", 167))

    def test_unclose_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"abcd", "Unclosed String: abcd", 168))

    def test_unclose_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"abcd\"\"123", "abcd,Unclosed String: 123", 169))

    def test_unclose_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"\"abcd\"", ",abcd,Unclosed String: ", 170))

    def test_unclose_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"abcd\"123\"ac\"s\"", "abcd,123,ac,s,Unclosed String: ", 171))

    def test_unclose_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"\"\"abcd\"123\"ac\"s\"unclosed", ",abcd,123,ac,s,Unclosed String: unclosed", 172))

    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"this string has illegal \\\"", "Illegal Escape In String: this string has illegal \\\"", 173))

    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"this string has illegal \\q\'\"", "Illegal Escape In String: this string has illegal \q", 174))

    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"this string has illegal \'b \"", "Illegal Escape In String: this string has illegal 'b", 175))

    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"this string has illegal \\123 \"", "Illegal Escape In String: this string has illegal \\1", 176))

    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\" \fwe \asd\\b\\t \"", " we sd\\b\\t ,<EOF>", 177))

    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"\'s\"", "Illegal Escape In String: 's", 178))

    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\" '\'\" \"", "Illegal Escape In String:  ''", 179))

    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"this string has illegal \\i\'\"", "Illegal Escape In String: this string has illegal \i", 180))

    def test_separators_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "[]():.", "[,],(,),:,.,<EOF>", 181))

    def test_separators_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            ",;{}=", ",,;,{,},=,<EOF>", 182))

    def test_separators_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "[a]b(c)a:.", "[,a,],b,(,c,),a,:,.,<EOF>", 183))

    def test_separators_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a,c;v{s}d=", "a,,,c,;,v,{,s,},d,=,<EOF>", 184))

    def test_separators_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "[{(]})}", "[,{,(,],},),},<EOF>", 185))

    def test_keywork_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "BodyBreakContinueDoElseElseIfEndBody", "Body,Break,Continue,Do,Else,ElseIf,EndBody,<EOF>", 186))

    def test_keywork_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "EndIfEndForEndWhileForFunctionIf", "EndIf,EndFor,EndWhile,For,Function,If,<EOF>", 187))

    def test_keywork_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ParameterReturnThenVar", "Parameter,Return,Then,Var,<EOF>", 188))

    def test_keywork_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "WhileTrueFalse", "While,True,False,<EOF>", 189))

    def test_keywork_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "EndDo", "EndDo,<EOF>", 190))

    def test_relation_op_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "==!=<><=", "==,!=,<,>,<=,<EOF>", 191))

    def test_relation_op_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            ">==/=<.>.<=.>=.", ">=,=/=,<.,>.,<=.,>=.,<EOF>", 192))

    def test_relation_op_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a==b>=c<=b", "a,==,b,>=,c,<=,b,<EOF>", 193))

    def test_relation_op_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a=/===ab<.>.b", "a,=/=,==,ab,<.,>.,b,<EOF>", 194))

    def test_relation_op_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            ">=b.>.a<.b", ">=,b,.,>.,a,<.,b,<EOF>", 195))

    def test_token_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var:abc=123;", "Var,:,abc,=,123,;,<EOF>", 196))

    def test_token_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Function: main Body:Var:a=1;EndBody.", "Function,:,main,Body,:,Var,:,a,=,1,;,EndBody,.,<EOF>", 197))

    def test_token_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "For(a=1,a<10,1)Doabc=2;EndFor.", "For,(,a,=,1,,,a,<,10,,,1,),Do,abc,=,2,;,EndFor,.,<EOF>", 198))

    def test_token_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "While a==1 Doprint(123);EndWhile.", "While,a,==,1,Do,print,(,123,),;,EndWhile,.,<EOF>", 199))

    def test_token_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a[12][2]={123,123,123}", "a,[,12,],[,2,],=,{123,123,123},<EOF>", 200))


# SAMPLE

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 901))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 902))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 903))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 904))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 905))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 906))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 907))

    def test_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            '\"abc def\t\"  ', 'abc def	,<EOF>', 908))

    def test_normal_string_unclose(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            ' \"abc def  ', "Unclosed String: abc def  ", 909))

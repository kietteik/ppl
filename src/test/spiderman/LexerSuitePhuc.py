import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("abcd","abcd,<EOF>",101))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("a1cd","a1cd,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("a1Ad","a1Ad,<EOF>",103))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",104))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("a_a","a_a,<EOF>",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("a_a123","a_a123,<EOF>",106))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("a_","a_,<EOF>",107))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("a____","a____,<EOF>",108))
    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("a1a1a1a1__AAA","a1a1a1a1__AAA,<EOF>",109))
    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("A_a_1_A","Error Token A",110))
    def test_identifier_11(self):
        self.assertTrue(TestLexer.checkLexeme("Abcd","Error Token A",111))
    def test_identifier_12(self):
        self.assertTrue(TestLexer.checkLexeme("11cd","11,cd,<EOF>",112))
    def test_identifier_13(self):
        self.assertTrue(TestLexer.checkLexeme("11Ad","11,Error Token A",113))
    def test_identifier_14(self):
        self.assertTrue(TestLexer.checkLexeme("_","Error Token _",114))
    def test_identifier_15(self):
        self.assertTrue(TestLexer.checkLexeme("._aA",".,Error Token _",115))
    def test_identifier_16(self):
        self.assertTrue(TestLexer.checkLexeme("*A123","*,Error Token A",116))
    def test_identifier_17(self):
        self.assertTrue(TestLexer.checkLexeme("-Aa_","-,Error Token A",117))
    def test_identifier_18(self):
        self.assertTrue(TestLexer.checkLexeme("+a____","+,a____,<EOF>",118))
    def test_identifier_19(self):
        self.assertTrue(TestLexer.checkLexeme("a+","a,+,<EOF>",119))
    def test_identifier_20(self):
        self.assertTrue(TestLexer.checkLexeme("a_aA.","a_aA,.,<EOF>",120))
    def test_array_1(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3}","{1,2,3},<EOF>",121))
    def test_array_2(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,3},{2,1},{1,2}}","{{1,3},{2,1},{1,2}},<EOF>",122))
    def test_array_3(self):
        self.assertTrue(TestLexer.checkLexeme("{{{1}},{{2}},{3}}","{{{1}},{{2}},{3}},<EOF>",123))
    def test_array_4(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,2},{{2}},{3}}","{{1,2},{{2}},{3}},<EOF>",124))
    def test_array_5(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,{2}}}","{,{,1,,,{2},},},<EOF>",125))
    def test_array_6(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,2,1},{1,2},{1}}","{{1,2,1},{1,2},{1}},<EOF>",126))
    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme('"This is a string containing tab \\t" ','This is a string containing tab \\t,<EOF>',127))
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme('"This is a string containing newline \n" ','Unclosed String: This is a string containing newline ',128))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme('"He asked me: \'"Where is John?\'""','He asked me: \'"Where is John?\'",<EOF>',129))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme('"He asked" me: \'"Where is John?\'""','He asked,me,:,Error Token \'',130))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme('""',',<EOF>',131))
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme('12.0e3','12.0e3,<EOF>',132))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme('12e3','12e3,<EOF>',133))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme('12.e5','12.e5,<EOF>',134))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme('12.0e+3','12.0e+3,<EOF>',135))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme('12000.','12000.,<EOF>',136))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme('120000e-1','120000e-1,<EOF>',137))
    def test_aray_boolean_1(self):
        self.assertTrue(TestLexer.checkLexeme('{{True,False},{{True}},{False}}','{{True,False},{{True}},{False}},<EOF>',138))
    def test_aray_boolean_2(self):
        self.assertTrue(TestLexer.checkLexeme('{{12.e5,12.e5},{{12.e5}},{12.e5}}','{{12.e5,12.e5},{{12.e5}},{12.e5}},<EOF>',139))
    def test_hex_1(self):
        self.assertTrue(TestLexer.checkLexeme("0x0","0,x0,<EOF>",140))
    def test_hex_2(self):
        self.assertTrue(TestLexer.checkLexeme("0XFFA012","0XFFA012,<EOF>",141))
    def test_oct_1(self):
        self.assertTrue(TestLexer.checkLexeme("0o0","0,o0,<EOF>",142))
    def test_oct_2(self):
        self.assertTrue(TestLexer.checkLexeme("0o12347896","0o12347,896,<EOF>",143))
    def test_bool_1(self):
        self.assertTrue(TestLexer.checkLexeme("True","True,<EOF>",144))
    def test_bool_2(self):
        self.assertTrue(TestLexer.checkLexeme("False","False,<EOF>",145))
    def test_array_7(self):
        self.assertTrue(TestLexer.checkLexeme("{ {1.2, 2.3, 1.4},{  1.5 , 2.6},{ 1.7}}","{ {1.2, 2.3, 1.4},{  1.5 , 2.6},{ 1.7}},<EOF>",146))
    def test_array_8(self):
        self.assertTrue(TestLexer.checkLexeme("{ 1  , 2 ,    3 }","{ 1  , 2 ,    3 },<EOF>",147))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme('"\'abc"','Illegal Escape In String: \'a',148))
    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello anh em\\minh la sinh vien khoa may tinh"','Illegal Escape In String: Hello anh em\\m',149))
    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme('"Em la:\n sanh vien!"','Unclosed String: Em la:',150))
    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme('** This is the comment.**** This is the comment.**','<EOF>',151))
    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is the comment.
* This is the second comment
* This is the third comment**""",'<EOF>',152))
    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is the comment.
* This is the second comment
* This is the third comment** 
** Ahis is unclosed comment *""",'Unterminated Comment',153))
    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme('"\\abc"','Illegal Escape In String: \\a',154))
    def test_ILLEGAL_ESCAPE_1(self):
        self.assertTrue(TestLexer.checkLexeme('"\\r"','\\r,<EOF>',155))
    def test_ILLEGAL_ESCAPE_2(self):
        self.assertTrue(TestLexer.checkLexeme('"\\r\\b\\t\\n\\f\\\'\\\\"','\\r\\b\\t\\n\\f\\\'\\\\,<EOF>',156))
    def test_ILLEGAL_ESCAPE_3(self):
        self.assertTrue(TestLexer.checkLexeme('"\\\'"','\\\',<EOF>',157))
    def test_ILLEGAL_ESCAPE_4(self):
        self.assertTrue(TestLexer.checkLexeme('"\'""','\'",<EOF>',158))
    def test_separate_token_1(self):
        self.assertTrue(TestLexer.checkLexeme("Function: Do While!.","Function,:,Do,While,!,.,<EOF>",159))
    def test_separate_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("abc = 123xyz \ defz","abc,=,123,xyz,\,defz,<EOF>",160))
    def test_separate_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("foo(a + b - c * d[9])","foo,(,a,+,b,-,c,*,d,[,9,],),<EOF>",161))
    def test_separate_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("+. -. *. \ =/= <. >. <=. >=.","+.,-.,*.,\,=/=,<.,>.,<=.,>=.,<EOF>",162))
    def test_separate_token_5(self):
        self.assertTrue(TestLexer.checkLexeme("+ - * \ % == != < > <= >=","+,-,*,\,%,==,!=,<,>,<=,>=,<EOF>",163))
    def test_separate_token_6(self):
        self.assertTrue(TestLexer.checkLexeme("! && ||","!,&&,||,<EOF>",164))
    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\r123""","""Unclosed String: abc\n123""",165))
    def test_ILLEGAL_ESCAPE_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\123""","""Illegal Escape In String: abc\\1""",166))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("-40.0","-,40.0,<EOF>",167))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("-zyx123","-,zyx123,<EOF>",168))
    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("-12358.69abc","-,12358.69,abc,<EOF>",169))
    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("-1.2,3.","-,1.2,,,3.,<EOF>",170))
    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme("-1.e-29","-,1.e-29,<EOF>",171))
    def test_float_12(self):
        self.assertTrue(TestLexer.checkLexeme("-1.e-2359","-,1.e-2359,<EOF>",172))
    def test_separate_token_7(self):
        self.assertTrue(TestLexer.checkLexeme("a__var__123 = 456","a__var__123,=,456,<EOF>",173))
    def test_separate_token_8(self):
        self.assertTrue(TestLexer.checkLexeme("Var x (123, string);","Var,x,(,123,,,string,),;,<EOF>",174))
    def test_separate_token_9(self):
        self.assertTrue(TestLexer.checkLexeme("Var: b[2][3]={{1,2,3},{4,5,6}};","Var,:,b,[,2,],[,3,],=,{{1,2,3},{4,5,6}},;,<EOF>",175))
    def test_separate_token_10(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: x;
Function: fact
    Parameter: n
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * fact (n - 1);
        EndIf.
    EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody.""","Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>",176))
    def test_separate_token_11(self):
        self.assertTrue(TestLexer.checkLexeme("a[3 + foo(2)] = a[b [2][3]] + 4;","a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>",177))
    def test_separate_token_12(self):
        self.assertTrue(TestLexer.checkLexeme("v = (4. \. 3.) *. 3.14 *. r *. r *. r;","v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>",178))
    def test_separate_token_13(self):
        self.assertTrue(TestLexer.checkLexeme("Return n * fact (n - 1);","Return,n,*,fact,(,n,-,1,),;,<EOF>",179))
    def test_separate_token_14(self):
        self.assertTrue(TestLexer.checkLexeme("True != False;","True,!=,False,;,<EOF>",180))
    def test_separate_token_cmt_15(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a block comment ** 123abc","123,abc,<EOF>",181))
    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is the comment.
* This is the second comment
* This is the third comment** 
** This is unclosed comment **
abc = 123xyz \ defz;""",'abc,=,123,xyz,\,defz,;,<EOF>',182))
    def test_interger_1(self):
        self.assertTrue(TestLexer.checkLexeme("123456 0 ","123456,0,<EOF>",183))
    def test_hex_3(self):
        self.assertTrue(TestLexer.checkLexeme("0xABC 0XABC","0xABC,0XABC,<EOF>",184))
    def test_oct_3(self):
        self.assertTrue(TestLexer.checkLexeme("0o123 0O123","0o123,0O123,<EOF>",185))
    def test_oct_4(self):
        self.assertTrue(TestLexer.checkLexeme("0o123A 0O123C","0o123,Error Token A",186))
    def test_hex_4(self):
        self.assertTrue(TestLexer.checkLexeme("0x123XY15","0x123,Error Token X",187))
    def test_interger_2(self):
        self.assertTrue(TestLexer.checkLexeme("12345600","12345600,<EOF>",188))
    def test_hex_5(self):
        self.assertTrue(TestLexer.checkLexeme("0xABCDEF","0xABCDEF,<EOF>",189))
    def test_array_9(self):
        self.assertTrue(TestLexer.checkLexeme("{{{1}},{{2},{3}}","{,{{1}},,,{{2},{3}},<EOF>",190))
    def test_array_10(self):
        self.assertTrue(TestLexer.checkLexeme("{ {1   , 2 },{ { { {4 } } }     },{ 3     }    }","{ {1   , 2 },{ { { {4 } } }     },{ 3     }    },<EOF>",191))
    def test_float_13(self):
        self.assertTrue(TestLexer.checkLexeme("0.12e5","0.12e5,<EOF>",192))
    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme("12e3458","12e3458,<EOF>",193))
    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme("1233.e-3","1233.e-3,<EOF>",194))
    def test_float_16(self):
        self.assertTrue(TestLexer.checkLexeme(".477",".,477,<EOF>",195))
    def test_float_17(self):
        self.assertTrue(TestLexer.checkLexeme("599.","599.,<EOF>",196))
    def test_float_18(self):
        self.assertTrue(TestLexer.checkLexeme("9E-88","9E-88,<EOF>",197))
    def test_float_19(self):
        self.assertTrue(TestLexer.checkLexeme(".776E-6",".,776E-6,<EOF>",198))
    def test_float_20(self):
        self.assertTrue(TestLexer.checkLexeme("11.0","11.0,<EOF>",199))
    def test_float_21(self):
        self.assertTrue(TestLexer.checkLexeme("0.","0.,<EOF>",200))
    def test_autogen_153(self):
        """Comment - ***"""
        self.assertTrue(TestLexer.checkLexeme("**a* **","<EOF>",201))
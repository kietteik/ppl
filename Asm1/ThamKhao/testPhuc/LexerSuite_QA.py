import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
        #  success identifier 101 - 110
    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("a___","a___,<EOF>",101))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("a1111","a1111,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("a1AAAA","a1AAAA,<EOF>",103))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",104))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("a_A_1_","a_A_1_,<EOF>",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("aaaa","aaaa,<EOF>",106))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("aA_Aa","aA_Aa,<EOF>",107))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("a____a","a____a,<EOF>",108))
    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("a1a1a1__AAA_a","a1a1a1__AAA_a,<EOF>",109))
    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("anhHuynh_1+","anhHuynh_1,+,<EOF>",110))
        # error identifier 111 - 120
    def test_identifier_11(self):
        self.assertTrue(TestLexer.checkLexeme("AnhHuynh","Error Token A",111))
    def test_identifier_12(self):
        self.assertTrue(TestLexer.checkLexeme("1AnhHuynh","1,Error Token A",112))
    def test_identifier_13(self):
        self.assertTrue(TestLexer.checkLexeme("11_AnhHuynh","11,Error Token _",113))
    def test_identifier_14(self):
        self.assertTrue(TestLexer.checkLexeme("____","Error Token _",114))
    def test_identifier_15(self):
        self.assertTrue(TestLexer.checkLexeme("._aAnhHuynh",".,Error Token _",115))
    def test_identifier_16(self):
        self.assertTrue(TestLexer.checkLexeme("*AnhHuynh123","*,Error Token A",116))
    def test_identifier_17(self):
        self.assertTrue(TestLexer.checkLexeme("-AnhHuynh_a_","-,Error Token A",117))
    def test_identifier_18(self):
        self.assertTrue(TestLexer.checkLexeme("+=anhhuynh____","+,=,anhhuynh____,<EOF>",118))
    def test_identifier_19(self):
        self.assertTrue(TestLexer.checkLexeme("a++","a,+,+,<EOF>",119))
    def test_identifier_20(self):
        self.assertTrue(TestLexer.checkLexeme("a_anhhuynh____.+","a_anhhuynh____,.,+,<EOF>",120))


    # test interger from 121 - 130
        # success interger
    def test_interger_1(self):
        self.assertTrue(TestLexer.checkLexeme("123456789","123456789,<EOF>",121))
    def test_interger_2(self):
        self.assertTrue(TestLexer.checkLexeme("0x123456789","0x123456789,<EOF>",122))
    def test_interger_3(self):
        self.assertTrue(TestLexer.checkLexeme("0XFFF","0XFFF,<EOF>",123))
    def test_interger_4(self):
        self.assertTrue(TestLexer.checkLexeme("0o1234567","0o1234567,<EOF>",124))
    def test_interger_5(self):
        self.assertTrue(TestLexer.checkLexeme("1000","1000,<EOF>",125))

        # error interger
    def test_interger_6(self):
        self.assertTrue(TestLexer.checkLexeme("0x0","0,x0,<EOF>",126))
    def test_interger_7(self):
        self.assertTrue(TestLexer.checkLexeme("0XFYA012","0XF,Error Token Y",127))
    def test_interger_8(self):
        self.assertTrue(TestLexer.checkLexeme("0o0123456","0,o0123456,<EOF>",128))
    def test_interger_9(self):
        self.assertTrue(TestLexer.checkLexeme("0o1234789","0o12347,89,<EOF>",129))
    def test_interger_10(self):
        self.assertTrue(TestLexer.checkLexeme("123o12347890","123,o12347890,<EOF>",130))

    # test float from
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme('30.1e5','30.1e5,<EOF>',131))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme('30.1E5','30.1E5,<EOF>',132))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme('30e5','30e5,<EOF>',133))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme('30E5','30E5,<EOF>',134))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme('30.e5','30.e5,<EOF>',135))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme('30.E5','30.E5,<EOF>',136))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme('30.5e+3','30.5e+3,<EOF>',137))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme('30.5E-3','30.5E-3,<EOF>',138))
    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme('30.','30.,<EOF>',139))
    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme('30e-0','30e-0,<EOF>',140))
    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme("30E0","30E0,<EOF>",141))
    def test_float_12(self):
        self.assertTrue(TestLexer.checkLexeme("-30e3458","-,30e3458,<EOF>",142))
    def test_float_13(self):
        self.assertTrue(TestLexer.checkLexeme("-3033.e-3","-,3033.e-3,<EOF>",143))
    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme(".30",".,30,<EOF>",144))
    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme("-30.","-,30.,<EOF>",145))
    def test_float_16(self):
        self.assertTrue(TestLexer.checkLexeme("30f-88","30,f,-,88,<EOF>",146))
    def test_float_17(self):
        self.assertTrue(TestLexer.checkLexeme("30.30e","30.30,e,<EOF>",147))
    def test_float_18(self):
        self.assertTrue(TestLexer.checkLexeme("30.30-e","30.30,-,e,<EOF>",148))
    def test_float_19(self):
        self.assertTrue(TestLexer.checkLexeme("0.0e","0.0,e,<EOF>",149))
    def test_float_20(self):
        self.assertTrue(TestLexer.checkLexeme("0.0e-1","0.0e-1,<EOF>",150))

    # test string
    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme('"String contain tab \t"','String contain tab 	,<EOF>',151))
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme('"String contain newline\n" ','Unclosed String: String contain newline\n',152))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme('"String contain quote \'"In quote string\'"" ','String contain quote \'"In quote string\'",<EOF>',153))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme('"String contain back_slash \\\\" ','String contain back_slash \\\\,<EOF>',154))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme('""',',<EOF>',155))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme('"\'String contain Illegal Escape"','Illegal Escape In String: \'S',156))
    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello BKU \\m"','Illegal Escape In String: Hello BKU \\m',157))
    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello BKU','Unclosed String: Hello BKU',158))
    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme('"String with special characters #$%!^&"','String with special characters #$%!^&,<EOF>',159))
    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme('"Multi-quote String: \'" in-quote-1 \'" \'" in-quote-2 \'"  "','Multi-quote String: \'" in-quote-1 \'" \'" in-quote-2 \'"  ,<EOF>',160))

    # test boolean
    def test_boolean_1(self):
        self.assertTrue(TestLexer.checkLexeme('TrueFalse','True,False,<EOF>',161))
    def test_boolean_2(self):
        self.assertTrue(TestLexer.checkLexeme('FalseTrue','False,True,<EOF>',162))

    # test array
        # success array
    def test_array_1(self):
        self.assertTrue(TestLexer.checkLexeme("{988,56,59,69}","{988,56,59,69},<EOF>",163))
    def test_array_2(self):
        self.assertTrue(TestLexer.checkLexeme("{{9,88},{46,59},{69,2}}","{{9,88},{46,59},{69,2}},<EOF>",164))
    def test_array_3(self):
        self.assertTrue(TestLexer.checkLexeme("{{{988}},{{988465969}},{988,56,59,69}}","{{{988}},{{988465969}},{988,56,59,69}},<EOF>",116523))
    def test_array_4(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,2},{{2}},{3}}","{{1,2},{{2}},{3}},<EOF>",166))
    def test_array_5(self):
        self.assertTrue(TestLexer.checkLexeme('{{True,False},{{True}},{False}}','{{True,False},{{True}},{False}},<EOF>',167))
    def test_array_6(self):
        self.assertTrue(TestLexer.checkLexeme('{{12.e5,12.e5},{{12.e5}},{12.e5}}','{{12.e5,12.e5},{{12.e5}},{12.e5}},<EOF>',168))
        # error array
    def test_array_7(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,{2}}}","{,{,1,,,{2},},},<EOF>",169))
    def test_array_8(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,2,1},{1,2},{1}}","{{1,2,1},{1,2},{1}},<EOF>",170))
    def test_array_9(self):
        self.assertTrue(TestLexer.checkLexeme("{ {1.2, 2.3, 1.4},{  1.5 , 2.6},{ 1.7}}","{ {1.2, 2.3, 1.4},{  1.5 , 2.6},{ 1.7}},<EOF>",171))
    def test_array_10(self):
        self.assertTrue(TestLexer.checkLexeme("{ 1  , 2 ,    3 }","{ 1  , 2 ,    3 },<EOF>",172))

    # test comment
    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme('** This is the one line comment.**','<EOF>',173))
    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme('**\nThis is the multiline comment 1.\nThis is the multiline comment 2\nThis is the multiline comment 3\n**','<EOF>',174))
    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme('**\n*This is the multiline comment 1.\n*This is the multiline comment 2\n*This is the multiline comment 3\n**','<EOF>',175))
    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme('**This is the 1st comment.****This is the 2nd comment****This is the 3rd comment**','<EOF>',176))
    def test_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme('****','<EOF>',177))
    def test_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme('**"String"**','<EOF>',178))
    def test_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme('**\n*\n*\n*\n**','<EOF>',179))
    def test_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme('*****','*,<EOF>',180))
    def test_comment_9(self):
        self.assertTrue(TestLexer.checkLexeme('**This is the comment*','Unterminated Comment',181))
    def test_comment_10(self):
        self.assertTrue(TestLexer.checkLexeme('**This is the comment* *','Unterminated Comment',182))

    # test illegal escape
    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme('"\\r"','\\r,<EOF>',183))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme('"\\r\\b\\t\\n\\f\\\'\\\\"','\\r\\b\\t\\n\\f\\\'\\\\,<EOF>',184))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme('"\\\'"','\\\',<EOF>',185))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme('"\'""','\'",<EOF>',186))


    def test_token_1(self):
        self.assertTrue(TestLexer.checkLexeme("Function: For EndFor While EndWhile!.","Function,:,For,EndFor,While,EndWhile,!,.,<EOF>",187))
    def test_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("anhhuynh = 123anh \ huynh;","anhhuynh,=,123,anh,\,huynh,;,<EOF>",188))
    def test_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("anh(a+b+c,a++,a[2])","anh,(,a,+,b,+,c,,,a,+,+,,,a,[,2,],),<EOF>",189))
    def test_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("+.-.*.\=/=<.>.<=.>=.","+.,-.,*.,\,=/=,<.,>.,<=.,>=.,<EOF>",190))
    def test_token_5(self):
        self.assertTrue(TestLexer.checkLexeme("+-*\%==!=<><=>=","+,-,*,\,%,==,!=,<,>,<=,>=,<EOF>",191))
    def test_token_6(self):
        self.assertTrue(TestLexer.checkLexeme("!&&||","!,&&,||,<EOF>",192))
    def test_token_7(self):
        self.assertTrue(TestLexer.checkLexeme("Var anh = 988, huynh = 5969","Var,anh,=,988,,,huynh,=,5969,<EOF>",193))
    def test_token_8(self):
        self.assertTrue(TestLexer.checkLexeme("string interger float boolean","string,interger,float,boolean,<EOF>",194))
    def test_token_9(self):
        self.assertTrue(TestLexer.checkLexeme("return {1,2,3,4} + {a,b,c,d}","return,{1,2,3,4},+,{,a,,,b,,,c,,,d,},<EOF>",195))
    def test_token_10(self):
        input = """Var: a,b,c;
                    Function: boo
                        Parameter: x,y,z;
                        Body:
                            While (True)
                                Return 1;
                            EndWhile.
                        EndBody.
                    Function: foo
                        Body:
                            For 
                            fact (x);
                        EndBody."""
        expect = "Var,:,a,,,b,,,c,;,Function,:,boo,Parameter,:,x,,,y,,,z,;,Body,:,While,(,True,),Return,1,;,EndWhile,.,EndBody,.,Function,:,foo,Body,:,For,fact,(,x,),;,EndBody,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,196))
    def test_separate_token_11(self):
        self.assertTrue(TestLexer.checkLexeme("a[3+5] = a[3][foo(x,y,z)]","a,[,3,+,5,],=,a,[,3,],[,foo,(,x,,,y,,,z,),],<EOF>",197))
    def test_separate_token_12(self):
        self.assertTrue(TestLexer.checkLexeme("x = y * z - a +. (y - 1)*a","x,=,y,*,z,-,a,+.,(,y,-,1,),*,a,<EOF>",198))
    def test_separate_token_13(self):
        self.assertTrue(TestLexer.checkLexeme("If (a == b) return n * foo (n - 1) EndIf;","If,(,a,==,b,),return,n,*,foo,(,n,-,1,),EndIf,;,<EOF>",199))
    def test_separate_token_14(self):
        self.assertTrue(TestLexer.checkLexeme("Do Continue; While (True) EndDo;","Do,Continue,;,While,(,True,),EndDo,;,<EOF>",200))
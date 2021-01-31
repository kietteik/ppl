import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # test ID
    def test_ID_101(self):
        self.assertTrue(TestLexer.checkLexeme("a b c 4","a,b,c,4,<EOF>",101))
    def test_ID_102(self):
        self.assertTrue(TestLexer.checkLexeme("AbCd","AbCd,<EOF>",102))
    def test_ID_103(self):
        self.assertTrue(TestLexer.checkLexeme("_A_B","_A_B,<EOF>",103))
    def test_ID_104(self):
        self.assertTrue(TestLexer.checkLexeme("abc123","abc123,<EOF>",104))
    def test_ID_105(self):
        self.assertTrue(TestLexer.checkLexeme("123abc","123,abc,<EOF>",105))
    def test_ID_106(self):
        self.assertTrue(TestLexer.checkLexeme("123\n123","123,123,<EOF>",106))
    def test_ID_107(self):
        self.assertTrue(TestLexer.checkLexeme("abc123?","abc123,Error Token ?",107))
    def test_ID_108(self):
        self.assertTrue(TestLexer.checkLexeme("abc/n123","abc,/,n123,<EOF>",108))
    def test_ID_109(self):
        self.assertTrue(TestLexer.checkLexeme("abc\n123","abc,123,<EOF>",109))
    def test_ID_110(self):
        self.assertTrue(TestLexer.checkLexeme("abc\t123","abc,123,<EOF>",110))
    def test_ID_111(self):
        self.assertTrue(TestLexer.checkLexeme("abc_\n_123","abc_,_123,<EOF>",111))
    def test_ID_112(self):
        self.assertTrue(TestLexer.checkLexeme("_\na","_,a,<EOF>",112))
    def test_ID_113(self):
        self.assertTrue(TestLexer.checkLexeme("abc$123","abc,Error Token $",113))    
    def test_ID_114(self):
        self.assertTrue(TestLexer.checkLexeme("123$$abc$$123","123,Error Token $",114)) 
    def test_ID_115(self):
        self.assertTrue(TestLexer.checkLexeme("&abc123","Error Token &",115))  
    #test float point
    def test_floatpoint_116(self):
        self.assertTrue(TestLexer.checkLexeme("12e34","12e34,<EOF>",116))
    def test_floatpoint_117(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-3","12.e-3,<EOF>",117))
    def test_floatpoint_118(self):
        self.assertTrue(TestLexer.checkLexeme(".4",".4,<EOF>",118))
    def test_floatpoint_119(self):
        self.assertTrue(TestLexer.checkLexeme("5.","5.,<EOF>",119))
    def test_floatpoint_120(self):
        self.assertTrue(TestLexer.checkLexeme("9E-8","9E-8,<EOF>",120))
    def test_floatpoint_121(self):
        self.assertTrue(TestLexer.checkLexeme(".7E-6",".7E-6,<EOF>",121))
    def test_floatpoint_122(self):
        self.assertTrue(TestLexer.checkLexeme("1.0","1.0,<EOF>",122))
    def test_floatpoint_123(self):
        self.assertTrue(TestLexer.checkLexeme("0.1","0.1,<EOF>",123))
    def test_floatpoint_124(self):
        self.assertTrue(TestLexer.checkLexeme("-0.1","-,0.1,<EOF>",124))
    def test_floatpoint_125(self):
        self.assertTrue(TestLexer.checkLexeme("-4.0","-,4.0,<EOF>",125))
    def test_floatpoint_126(self):
        self.assertTrue(TestLexer.checkLexeme("-abc123","-,abc123,<EOF>",126))
    def test_floatpoint_127(self):
        self.assertTrue(TestLexer.checkLexeme("-123.4abc","-,123.4,abc,<EOF>",127))
    def test_floatpoint_128(self):
        self.assertTrue(TestLexer.checkLexeme("-1.2,3.,.4,5e6","-,1.2,,,3.,,,.4,,,5e6,<EOF>",128))
    def test_floatpoint_129(self):
        self.assertTrue(TestLexer.checkLexeme("-1.e-2","-,1.e-2,<EOF>",129))
    def test_floatpoint_130(self):
        self.assertTrue(TestLexer.checkLexeme("-1.e-2.0","-,1.e-2,.0,<EOF>",130))
    #test block comment
    def test_block_comment_131(self):
        self.assertTrue(TestLexer.checkLexeme("/* A block comment */","<EOF>",131))    
    def test_block_comment_132(self):
        self.assertTrue(TestLexer.checkLexeme("/* This is a block comment */ 123abc","123,abc,<EOF>",132))    
    def test_block_comment_133(self):
        self.assertTrue(TestLexer.checkLexeme("/* Not a block comment.","/,*,Not,a,block,comment,Error Token .",133))    
    def test_block_comment_134(self):
        self.assertTrue(TestLexer.checkLexeme("/* abc // 123 */","<EOF>",134))    
    def test_block_comment_135(self):
        self.assertTrue(TestLexer.checkLexeme("/* abc \n 123 */","<EOF>",135))
    def test_block_comment_136(self):
        self.assertTrue(TestLexer.checkLexeme("/* abc \b \t \r 123 */","<EOF>",136))
    #test line comment 
    def test_line_comment_137(self):
        self.assertTrue(TestLexer.checkLexeme("// A line comment.","<EOF>",137))    
    def test_line_comment_138(self):
        self.assertTrue(TestLexer.checkLexeme("// abc123!@#$%^&*","<EOF>",138))    
    def test_line_comment_139(self):
        self.assertTrue(TestLexer.checkLexeme("// A line \t comment. \n 123abc","123,abc,<EOF>",139))   
    #test keyword
    def test_keyword_140(self):
        self.assertTrue(TestLexer.checkLexeme("falsebreak","falsebreak,<EOF>",140))   
    def test_keyword_141(self):
        self.assertTrue(TestLexer.checkLexeme("true int float","true,int,float,<EOF>",141))
    #test separators
    def test_separators_142(self):
        self.assertTrue(TestLexer.checkLexeme("abc {123 456} cdf","abc,{,123,456,},cdf,<EOF>",142))  
    def test_separators_143(self):
        self.assertTrue(TestLexer.checkLexeme("array[2] = {2, 4}","array,[,2,],=,{,2,,,4,},<EOF>",143))  
    def test_separators_144(self):
        self.assertTrue(TestLexer.checkLexeme("for(i = 0;;i++)","for,(,i,=,0,;,;,i,+,+,),<EOF>",144))  
    def test_separators_145(self):
        self.assertTrue(TestLexer.checkLexeme("void b(a)","void,b,(,a,),<EOF>",145))  
    def test_separators_146(self):
        self.assertTrue(TestLexer.checkLexeme("// abcdef..","<EOF>",146))  
    def test_separators_147(self):
        self.assertTrue(TestLexer.checkLexeme("abc123 123abc ()","abc123,123,abc,(,),<EOF>",147))  
    def test_separators_148(self):
        self.assertTrue(TestLexer.checkLexeme("a[1] = b[2]","a,[,1,],=,b,[,2,],<EOF>",148))  
    #test operator
    def test_operator_149(self):
        self.assertTrue(TestLexer.checkLexeme("3 > 4","3,>,4,<EOF>",149))  
    def test_operator_150(self):
        self.assertTrue(TestLexer.checkLexeme("a = 2 + 3","a,=,2,+,3,<EOF>",150))  
    def test_operator_151(self):
        self.assertTrue(TestLexer.checkLexeme("x = 1.0 - 0.2e3","x,=,1.0,-,0.2e3,<EOF>",151))  
    def test_operator_152(self):
        self.assertTrue(TestLexer.checkLexeme("a = 7 / 2","a,=,7,/,2,<EOF>",152))  
    def test_operator_153(self):
        self.assertTrue(TestLexer.checkLexeme("x != 5","x,!=,5,<EOF>",153))  
    def test_operator_154(self):
        self.assertTrue(TestLexer.checkLexeme("a < 3 < b","a,<,3,<,b,<EOF>",154))          
    def test_operator_155(self):
        self.assertTrue(TestLexer.checkLexeme("a || b && c","a,||,b,&&,c,<EOF>",155))  
    def test_operator_156(self):
        self.assertTrue(TestLexer.checkLexeme("a = b = 3","a,=,b,=,3,<EOF>",156)) 
    #test variable declaration
    def test_variabledecl_157(self):
        self.assertTrue(TestLexer.checkLexeme("floa9t x, a[5];","floa9t,x,,,a,[,5,],;,<EOF>",157))
    def test_variabledecl_158(self):
        self.assertTrue(TestLexer.checkLexeme("int a, b, c[1], d, e[2];","int,a,,,b,,,c,[,1,],,,d,,,e,[,2,],;,<EOF>",158))
    def test_variabledecl_159(self):
        self.assertTrue(TestLexer.checkLexeme("int str='A string!'","int,str,=,Error Token '",159))
    def test_variabledecl_160(self):
        self.assertTrue(TestLexer.checkLexeme("""_="this is a string" ""","_,=,this is a string,<EOF>",160))
    def test_variabledecl_161(self):
        self.assertTrue(TestLexer.checkLexeme("__var__123 = 456","__var__123,=,456,<EOF>",161))
    def test_variabledecl_162(self):
        self.assertTrue(TestLexer.checkLexeme("float x {{123, string}} {};","float,x,{,{,123,,,string,},},{,},;,<EOF>",162))
    #test illegal escape in string
    def test_IllegalEscapeString_163(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\i123 ""","""Illegal Escape In String: abc\\i""",163))
    def test_IllegalEscapeString_164(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc "xyz\\m123" ""","abc,Illegal Escape In String: xyz\\m""",164))     
    def test_IllegalEscapeString_165(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc \\b\"","abc \\b,<EOF>",165))    
    def test_IllegalEscapeString_166(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc\\n\"","abc\\n,<EOF>",166))  
    def test_IllegalEscapeString_167(self):
        self.assertTrue(TestLexer.checkLexeme(".a","Error Token .",167))
    #test unclosed string
    def test_UnclosedString_168(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\r123""","""Unclosed String: abc""",168)) 
    def test_UnclosedString_169(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\123""","""Illegal Escape In String: abc\\1""",169))
    #test string
    def test_String_170(self):
        self.assertTrue(TestLexer.checkLexeme("""abc/d\\\\1234""","abc,/,d,Error Token \\",170))
    def test_String_171(self):
        self.assertTrue(TestLexer.checkLexeme("abc = 123xyz / defz","abc,=,123,xyz,/,defz,<EOF>",171))  
    def test_String_172(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is \\t\\r a string!" ""","This is \\t\\r a string!,<EOF>",172))  
    def test_String_173(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a \\n\\b string!" ""","This is a \\n\\b string!,<EOF>",173))  
    def test_String_174(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "456a\\\\789" ""","""123,456a\\\\789,<EOF>""",174))  
    def test_String_175(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\n123" ""","Unclosed String: abc",175))
    #test the other
    def test_other_176(self):
        self.assertTrue(TestLexer.checkLexeme("x = y ^ 7","x,=,y,Error Token ^",176))
    def test_other_177(self):
        self.assertTrue(TestLexer.checkLexeme("/*This is not a comment","/,*,This,is,not,a,comment,<EOF>",177))
    def test_other_178(self):
        self.assertTrue(TestLexer.checkLexeme("===","==,=,<EOF>",178))
    def test_other_179(self):
        self.assertTrue(TestLexer.checkLexeme(""" &&& ""","&&,Error Token &",179))
    def test_other_180(self):
        self.assertTrue(TestLexer.checkLexeme("""a <= b = c""","a,<=,b,=,c,<EOF>",180))
    def test_other_181(self):
        self.assertTrue(TestLexer.checkLexeme("***","*,*,*,<EOF>",181))
    def test_other_182(self):
        self.assertTrue(TestLexer.checkLexeme(""" "2 - 2 =""0" ""","2 - 2 =,0,<EOF>",182))
    def test_other_183(self):
        self.assertTrue(TestLexer.checkLexeme("=!==","=,!=,=,<EOF>",183))
    def test_other_184(self):
        self.assertTrue(TestLexer.checkLexeme(""" string str = "abc ""","string,str,=,Unclosed String: abc ",184))
    def test_other_185(self):
        self.assertTrue(TestLexer.checkLexeme(""" str = //"str"; ""","str,=,<EOF>",185))
    def test_other_186(self):
        self.assertTrue(TestLexer.checkLexeme("int-void-float-break","int,-,void,-,float,-,break,<EOF>",186))
    def test_other_187(self):
        self.assertTrue(TestLexer.checkLexeme("abc 123 x @","abc,123,x,Error Token @",187))
    def test_other_188(self):
        self.assertTrue(TestLexer.checkLexeme("/*This is \"a comment.\" */","<EOF>",188))
    def test_other_189(self):
        self.assertTrue(TestLexer.checkLexeme("//This is still a \"comment.\" 123 \n abc","abc,<EOF>",189))
    def test_other_190(self):
        self.assertTrue(TestLexer.checkLexeme("/* abc /* 123 // $z&*/","<EOF>",190))
    def test_other_191(self):
        self.assertTrue(TestLexer.checkLexeme("// x = 1 + 2 % 3\n","<EOF>",191))
    def test_other_192(self):
        self.assertTrue(TestLexer.checkLexeme("var x^","var,x,Error Token ^",192))
    def test_other_193(self):
        self.assertTrue(TestLexer.checkLexeme("-123","-,123,<EOF>",193))
    def test_other_194(self):
        self.assertTrue(TestLexer.checkLexeme("1-2","1,-,2,<EOF>",194))
    def test_other_195(self):
        self.assertTrue(TestLexer.checkLexeme("+1-2","+,1,-,2,<EOF>",195))
    def test_other_196(self):
    	self.assertTrue(TestLexer.checkLexeme("12-34+*5","12,-,34,+,*,5,<EOF>",196))
    def test_other_197(self):
        self.assertTrue(TestLexer.checkLexeme(""" "A Unclose String""","Unclosed String: A Unclose String",197))
    def test_other_198(self):
        self.assertTrue(TestLexer.checkLexeme("_--^abc","_,-,-,Error Token ^",198))
    def test_other_199(self):
        self.assertTrue(TestLexer.checkLexeme("abc123\t_de","abc123,_de,<EOF>",199))
    def test_other_200(self):
        self.assertTrue(TestLexer.checkLexeme("1.2.3e4E5","1.2,.3e4,E5,<EOF>",200))
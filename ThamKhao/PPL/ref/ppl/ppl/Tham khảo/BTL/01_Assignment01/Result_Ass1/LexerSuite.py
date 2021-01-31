import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("MinhTham","MinhTham,<EOF>",101))
        self.assertTrue(TestLexer.test("Minh Tham","Minh,Tham,<EOF>",102))
        self.assertTrue(TestLexer.test("MinhTham@","MinhTham,Error Token @",103))
        self.assertTrue(TestLexer.test("1613166Minh","1613166,Minh,<EOF>",104))
        self.assertTrue(TestLexer.test("1Minh","1,Minh,<EOF>",105))
        self.assertTrue(TestLexer.test("_Minh123","_Minh123,<EOF>",106))
        self.assertTrue(TestLexer.test("1613166Tham1613166","1613166,Tham1613166,<EOF>",107))
        self.assertTrue(TestLexer.test("Tham16_1_31_66","Tham16_1_31_66,<EOF>",108))
        self.assertTrue(TestLexer.test("0T","0,T,<EOF>",109))
        self.assertTrue(TestLexer.test("_","_,<EOF>",110))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123_123","123,_123,<EOF>",111))
        self.assertTrue(TestLexer.test("0128312412","0128312412,<EOF>",112))
        self.assertTrue(TestLexer.test("01283 12412","01283,12412,<EOF>",113))
        self.assertTrue(TestLexer.test("1237123","1237123,<EOF>",114))

    def test_real(self):
        """test real"""
        self.assertTrue(TestLexer.test("Tham 10.e2","Tham,10.e2,<EOF>",115))
        self.assertTrue(TestLexer.test("Tham 10.","Tham,10.,<EOF>",116))
        self.assertTrue(TestLexer.test("Tham .10","Tham,.10,<EOF>",117))
        self.assertTrue(TestLexer.test("1010.","1010.,<EOF>",118))
        self.assertTrue(TestLexer.test("Tham 10E10","Tham,10E10,<EOF>",119))
        self.assertTrue(TestLexer.test("Tham 10E-2","Tham,10E-2,<EOF>",120))
        self.assertTrue(TestLexer.test("Tham 10.10E-10","Tham,10.10E-10,<EOF>",121))
        self.assertTrue(TestLexer.test("Tham 10.10e-10","Tham,10.10e-10,<EOF>",122))
        self.assertTrue(TestLexer.test("Tham 10.e10","Tham,10.e10,<EOF>",123))
        self.assertTrue(TestLexer.test("Tham .10E-10","Tham,.10E-10,<EOF>",124))
        self.assertTrue(TestLexer.test("Tham .10e10","Tham,.10e10,<EOF>",125))

    def test_boolean(self):
        """test boolean"""
        self.assertTrue(TestLexer.test("TRue","TRue,<EOF>",126))
        self.assertTrue(TestLexer.test("false","false,<EOF>",127))
        self.assertTrue(TestLexer.test("True","True,<EOF>",128))
        self.assertTrue(TestLexer.test("faLSE","faLSE,<EOF>",129))
        self.assertTrue(TestLexer.test("tRue faLSE","tRue,faLSE,<EOF>",130))

    def test_whitespace(self):
        """test whitespace"""
        self.assertTrue(TestLexer.test(" \n\t", "<EOF>", 131))
        self.assertTrue(TestLexer.test("\t", "<EOF>", 132))
        self.assertTrue(TestLexer.test("\n", "<EOF>", 133))
        self.assertTrue(TestLexer.test(" \t \n \r", "<EOF>", 134))
        self.assertTrue(TestLexer.test("Minh\nTham \t\r", "Minh,Tham,<EOF>", 135))

    def test_keywords(self):
        """test whitespace"""
        self.assertTrue(TestLexer.test("WitH", "WitH,<EOF>", 136))
        self.assertTrue(TestLexer.test("BreAK", "BreAK,<EOF>", 137))
        self.assertTrue(TestLexer.test("ConTinue", "ConTinue,<EOF>", 138))
        self.assertTrue(TestLexer.test("FoR", "FoR,<EOF>", 139))
        self.assertTrue(TestLexer.test("TO", "TO,<EOF>", 140))
        self.assertTrue(TestLexer.test("DowTO", "DowTO,<EOF>", 141))
        self.assertTrue(TestLexer.test("Do", "Do,<EOF>", 142))
        self.assertTrue(TestLexer.test("If", "If,<EOF>", 143))
        self.assertTrue(TestLexer.test("THEN", "THEN,<EOF>", 144))
        self.assertTrue(TestLexer.test("ElsE", "ElsE,<EOF>", 145))
        self.assertTrue(TestLexer.test("ReTURN", "ReTURN,<EOF>", 146))
        self.assertTrue(TestLexer.test("WHIle", "WHIle,<EOF>", 147))
        self.assertTrue(TestLexer.test("BegiN END FUnction ProceduRE", "BegiN,END,FUnction,ProceduRE,<EOF>", 148))
        self.assertTrue(TestLexer.test("Of REal Integer STRING", "Of,REal,Integer,STRING,<EOF>", 149))
        self.assertTrue(TestLexer.test("VaR True FALSe ArrAY", "VaR,True,FALSe,ArrAY,<EOF>", 150))

    def test_comments(self):
        """test comment"""
        self.assertTrue(TestLexer.test("//c","<EOF>",151))
        self.assertTrue(TestLexer.test("{\n\n\naaaaaaa}","<EOF>",152))
        self.assertTrue(TestLexer.test("//c{","<EOF>",153))
        self.assertTrue(TestLexer.test("//c{aa\nTham","Tham,<EOF>",154))
        self.assertTrue(TestLexer.test("(* This is a block comment \n*)", "<EOF>", 155))
        self.assertTrue(TestLexer.test("////This is a*{ } line comment", "<EOF>", 156))
        self.assertTrue(TestLexer.test("{ This is a * block comment \n}", "<EOF>", 157))
        self.assertTrue(TestLexer.test("(**)", "<EOF>", 158))
        self.assertTrue(TestLexer.test("{ This is a block } comment ", "comment,<EOF>", 159))
        self.assertTrue(TestLexer.test("(* This is a block *)id", "id,<EOF>", 160))
        self.assertTrue(TestLexer.test("Minh //This is ", "Minh,<EOF>", 161))
    def test_operators(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("not anD ant", "not,anD,ant,<EOF>", 162))
        self.assertTrue(TestLexer.test("oR diV MOD", "oR,diV,MOD,<EOF>", 163))
        self.assertTrue(TestLexer.test("+-*/= <> < > <= >= :=", "+,-,*,/,=,<>,<,>,<=,>=,:=,<EOF>", 164))
    def test_seperators(self):
        self.assertTrue(TestLexer.test("[]:();..,..():[]", "[,],:,(,),;,..,,,..,(,),:,[,],<EOF>", 165))
        self.assertTrue(TestLexer.test("(Minh Tham)", "(,Minh,Tham,),<EOF>", 166))
    def test_error_char(self):
        """test error char"""
        self.assertTrue(TestLexer.test("Minh $", "Minh,Error Token $", 167))
        self.assertTrue(TestLexer.test("1234_Minh@", "1234,_Minh,Error Token @", 168))
        self.assertTrue(TestLexer.test("!@@@", "Error Token !", 169))

    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.test("\"Toi la Minh Tham\"","Toi la Minh Tham,<EOF>",170))
        self.assertTrue(TestLexer.test("\"Toi\\t la Minh Tham\"","Toi\\t la Minh Tham,<EOF>",171))
        self.assertTrue(TestLexer.test("\"Toi \\n la \\f Minh Tham\"","Toi \\n la \\f Minh Tham,<EOF>",172))
        self.assertTrue(TestLexer.test("\"Toi la Minh \\\Tham\"","Toi la Minh \\\Tham,<EOF>",173))
        self.assertTrue(TestLexer.test("\"Toi \\rla \\\' Minh \\\Tham\"","Toi \\rla \\\' Minh \\\Tham,<EOF>",174))
        self.assertTrue(TestLexer.test("\"Toi \\\" la Minh \\\Tham\"","Toi \\\" la Minh \\\Tham,<EOF>",175))

    def test_unclose_string(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test('"this is unclose string', "Unclosed String: this is unclose string",176))
        self.assertTrue(TestLexer.test('Minh Tham "',"Minh,Tham,Unclosed String: ",177))
        #self.assertTrue(TestLexer.test('"Minh\nTham"', "Unclosed String: Minh",178))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test('"Minh\\k Tham "', "Illegal Escape In String: Minh\k",178))
        self.assertTrue(TestLexer.test('"\\kMinh\\k Tham "', "Illegal Escape In String: \k",179))
        self.assertTrue(TestLexer.test('"Minh Tham \m"', "Illegal Escape In String: Minh Tham \m",180))

    def test_complex_181(self):
        input = "[n, m] = map(int, minh_t().[123]"
        expect = "[,n,,,m,],=,map,(,int,,,minh_t,(,),Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_complex_182(self):
        input = "Minhx := 1+2+5+7+ex[2]"
        expect = "Minhx,:=,1,+,2,+,5,+,7,+,ex,[,2,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_complex_183(self):
        input = "defion chdiff(a, b):\n  if a[i][j] != b[i][j]:\n s += ans"
        expect = "defion,chdiff,(,a,,,b,),:,if,a,[,i,],[,j,],Error Token !"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_complex_184(self):
        input = "For i=1 to do and a:= 13.t5"
        expect = "For,i,=,1,to,do,and,a,:=,13.,t5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_complex_185(self):
        input = "[n,nt, minh_t().[123]"
        expect = "[,n,,,nt,,,minh_t,(,),Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_complex_186(self):
        input = "_minh toi \\[n, m] = map(int, minh_t().[123]"
        expect = "_minh,toi,Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_complex_187(self):
        input = "n = input()\nl = list(map"
        expect = "n,=,input,(,),l,=,list,(,map,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_complex_188(self):
        input = "x:= x + 1.2e1"
        expect = "x,:=,x,+,1.2e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_complex_189(self):
        input = " minh_t()12.e[123]"
        expect = "minh_t,(,),12.,e,[,123,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_complex_190(self):
        input = "123.ee{[123] \\ } minh"
        expect = "123.,ee,minh,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_complex_191(self):
        input = "0\nt = [\"RU\", \"UR\"]\nwhile (i < len(s)):\n "
        expect = "0,t,=,[,RU,,,UR,],while,(,i,<,len,(,s,),),:,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_complex_192(self):
        input = "if len(k) == 1:\n        return 1\n    if len(k) % 2 == 1:\n   return 1 + f(k[0:len(k)-1])"
        expect = "if,len,(,k,),=,=,1,:,return,1,if,len,(,k,),Error Token %"
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_complex_193(self):
        input = "[n, m] = nput().strip().split()))\ns = [abs(l[i+1] - l[i])"
        expect = "[,n,,,m,],=,nput,(,),Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_complex_194(self):
        input = "nput().strip().split()))\ns = [abs(l[i+1] - l[i]) = map(int, minh_t().[123]"
        expect = "nput,(,),Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_complex_195(self):
        input = "for i in range(len(a)):\n        for j in range(len(a[0]))"
        expect = "for,i,in,range,(,len,(,a,),),:,for,j,in,range,(,len,(,a,[,0,],),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_complex_196(self):
        input = "int n,m;\n    cin >> n >> m;\n    int arr[n + 1];\n "
        expect = "int,n,,,m,;,cin,>,>,n,>,>,m,;,int,arr,[,n,+,1,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_complex_197(self):
        input = "pair<int, int> b)\n{\n    if (a.first < b.first)\n"
        expect = "pair,<,int,,,int,>,b,),Error Token {"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_complex_198(self):
        input = "int n, m, q;\n    cin >> n >> m >> q;\n    string s1, s2;\n"
        expect = "int,n,,,m,,,q,;,cin,>,>,n,>,>,m,>,>,q,;,string,s1,,,s2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test_complex_199(self):
        input = " for (long long i = 0; i < n; i ++)\n        cin >> a1[i];\n"
        expect = "for,(,long,long,i,=,0,;,i,<,n,;,i,+,+,),cin,>,>,a1,[,i,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_complex_200(self):
        input = "if (a.first == b.first && a.second < b.second)\n"
        expect = "if,(,a,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 200))
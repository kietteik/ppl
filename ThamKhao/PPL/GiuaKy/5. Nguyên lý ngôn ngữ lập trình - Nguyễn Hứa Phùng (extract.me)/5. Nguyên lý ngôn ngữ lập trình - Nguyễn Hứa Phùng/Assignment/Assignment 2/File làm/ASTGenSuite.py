import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # Test Variable Declaration
    def test_vardecl_301(self):
        input = """
        int a;
        """
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_vardecl_302(self):
        input = """
        boolean b;
        """
        expect = str(Program([VarDecl("b",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))    
    
    def test_vardecl_303(self):
        input = """
        float c;
        """
        expect = str(Program([VarDecl("c",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))    
   
    def test_vardecl_304(self):
        input = """
        int a,b,c;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_vardecl_305(self):
        input = """
        boolean arr[2];
        """
        expect = str(Program([VarDecl("arr",ArrayType(2,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))    

    def test_vardecl_306(self):
        input = """
        int x,z;
        float a;
        """
        expect = str(Program([VarDecl("x",IntType()),VarDecl("z",IntType()),VarDecl("a",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))  

    def test_vardecl_307(self):
        input = """
        int a,b;
        float c;
        boolean arr[2];
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",FloatType()),VarDecl("arr",ArrayType(2,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_vardecl_308(self):
        input = """
        int a123;
        """
        expect = str(Program([VarDecl("a123",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_vardecl_309(self):
        input = """
        int a123[4], b567[8];
        """
        expect = str(Program([VarDecl("a123",ArrayType(4,IntType())),VarDecl("b567",ArrayType(8,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_vardecl_310(self):
        input = """
        float a[4], b, c[2];
        """
        expect = str(Program([VarDecl("a",ArrayType(4,FloatType())),VarDecl("b",FloatType()),VarDecl("c",ArrayType(2,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))


    # Test Function Declaration
    def test_funcdecl_311(self):
        input = """
        int main() {}
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcdecl_312(self):
        input = """
        float foo() 
        {
            foo2(0);
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([CallExpr(Id("foo2"),[IntLiteral(0)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_funcdecl_313(self):
        input = """
        void a() {}
        int b() {}
        """
        expect = str(Program([FuncDecl(Id("a"),[],VoidType(),Block([])),FuncDecl(Id("b"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_funcdecl_314(self):
        input = """
        void a() {
            int x;
        }
        int b() {}
        """
        expect = str(Program([FuncDecl(Id("a"),[],VoidType(),Block([VarDecl("x",IntType())])),FuncDecl(Id("b"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_funcdecl_315(self):
        input = """
        void a() {
            int x;
        }
        int b() {}
        float c;
        """
        expect = str(Program([FuncDecl(Id("a"),[],VoidType(),Block([VarDecl("x",IntType())])),FuncDecl(Id("b"),[],IntType(),Block([])),VarDecl("c",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_funcdecl_316(self):
        input = """
        void a() {
            int x;
            y();
        }
        int b() {}
        float c;
        """
        expect = str(Program([FuncDecl(Id("a"),[],VoidType(),Block([VarDecl("x",IntType()),CallExpr(Id("y"),[])])),FuncDecl(Id("b"),[],IntType(),Block([])),VarDecl("c",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_funcdecl_317(self):
        input = """
        void a() {
            int x;
            y(0);
        }
        int b() {}
        float c;
        """
        expect = str(Program([FuncDecl(Id("a"),[],VoidType(),Block([VarDecl("x",IntType()),CallExpr(Id("y"),[IntLiteral(0)])])),FuncDecl(Id("b"),[],IntType(),Block([])),VarDecl("c",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_funcdecl_318(self):
        input = """
        void a(int x){}
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("x",IntType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_funcdecl_319(self):
        input = """
        void a(int x, boolean y){}
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("x",IntType()),VarDecl("y",BoolType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_funcdecl_320(self):
        input = """
        float a(int x, boolean y)
        {
            float c;
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("x",IntType()),VarDecl("y",BoolType())],FloatType(),Block([VarDecl("c",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_funcdecl_321(self):
        input = """
        float a(int x, boolean y)
        {
            float c;
            y(0);
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("x",IntType()),VarDecl("y",BoolType())],FloatType(),Block([VarDecl("c",FloatType()),CallExpr(Id("y"),[IntLiteral(0)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_funcdecl_322(self):
        input = """
        float a(int x, boolean y)
        {
            float c;
            d(0);
        }
        int b() {}        
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("x",IntType()),VarDecl("y",BoolType())],FloatType(),Block([VarDecl("c",FloatType()),CallExpr(Id("d"),[IntLiteral(0)])])),FuncDecl(Id("b"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_funcdecl_323(self):
        input = """
        float a(int x, boolean y)
        {
            float c;
            d(0);
        }
        int b() {
            float m;
            n(1);
        }        
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("x",IntType()),VarDecl("y",BoolType())],FloatType(),Block([VarDecl("c",FloatType()),CallExpr(Id("d"),[IntLiteral(0)])])),FuncDecl(Id("b"),[],IntType(),Block([VarDecl("m",FloatType()),CallExpr(Id("n"),[IntLiteral(1)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_funcdecl_324(self):
        input = """
        int[] a(float b, boolean c[]){}
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_funcdecl_325(self):
        input = """
        int[] a(float b, boolean c[])
        {
            float d;  
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([VarDecl("d",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_funcdecl_326(self):
        input = """
        int[] a(float b, boolean c[])
        {
            float d;
            boolean e[2];
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([VarDecl("d",FloatType()),VarDecl("e",ArrayType(2,BoolType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_funcdecl_327(self):
        input = """
        int[] a(float b, boolean c[])
        {
            int a123[4], b567[8];  
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([VarDecl("a123",ArrayType(4,IntType())),VarDecl("b567",ArrayType(8,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_funcdecl_328(self):
        input = """
        int[] a(float b, boolean c[])
        {
            int a123[4], b567[8];
            foo("Ass2");
        }
        """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([VarDecl("a123",ArrayType(4,IntType())),VarDecl("b567",ArrayType(8,IntType())),CallExpr(Id("foo"),[StringLiteral("Ass2")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_funcdecl_329(self):
        input = """
            int foo2(){
                foo(foo());
            }
        """
        expect = str(Program([FuncDecl(Id("foo2"),[],IntType(),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_funcdecl_330(self):
        input = """
            int foo2(){
                foo(foo("Ass2"));
            }
        """
        expect = str(Program([FuncDecl(Id("foo2"),[],IntType(),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[StringLiteral("Ass2")])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))


    # Test Expression
    def test_exp_331(self):
        input = """
        int foo() 
        {
            x = 1;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_exp_332(self):
        input = """
        int foo() 
        {
            x = 1;
            y = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("=",Id("y"),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_exp_333(self):
        input = """
        int foo() 
        {
            x = 1;
            y = 2;
            z = x + y;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("=",Id("y"),IntLiteral(2)),BinaryOp("=",Id("z"),BinaryOp("+",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_exp_334(self):
        input = """
        int foo() 
        {
            x = 1;
            y = 2;
            z = x / y + z;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("=",Id("y"),IntLiteral(2)),BinaryOp("=",Id("z"),BinaryOp("+",BinaryOp("/",Id("x"),Id("y")),Id("z")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_exp_335(self):
        input = """
        int foo() 
        {
            x = "abc";
            y = "cde";
            z = x + y;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),StringLiteral("abc")),BinaryOp("=",Id("y"),StringLiteral("cde")),BinaryOp("=",Id("z"),BinaryOp("+",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_exp_336(self):
        input = """
        int foo() 
        {
            x = "abc";
            y = "cde";
            z = x != y;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),StringLiteral("abc")),BinaryOp("=",Id("y"),StringLiteral("cde")),BinaryOp("=",Id("z"),BinaryOp("!=",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_exp_337(self):
        input = """
        int foo() 
        {
            x = "abc";
            y = "cde";
            z = x * (y + "mnl");
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),StringLiteral("abc")),BinaryOp("=",Id("y"),StringLiteral("cde")),BinaryOp("=",Id("z"),BinaryOp("*",Id("x"),BinaryOp("+",Id("y"),StringLiteral("mnl"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_exp_338(self):
        input = """
        int foo() 
        {
            x = "abc";
            y = "cde";
            t = z = x * (y + "mnl");
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),StringLiteral("abc")),BinaryOp("=",Id("y"),StringLiteral("cde")),BinaryOp("=",Id("t"),BinaryOp("=",Id("z"),BinaryOp("*",Id("x"),BinaryOp("+",Id("y"),StringLiteral("mnl")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_exp_339(self):
        input = """
        int foo() 
        {
            x = 1 != 2 || true != false;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),BinaryOp("||",BinaryOp("!=",IntLiteral(1),IntLiteral(2)),BinaryOp("!=",BooleanLiteral("true"),BooleanLiteral("false"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_exp_340(self):
        input = """
        int foo() 
        {
            x = 1 > 2 && true || false;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",Id("x"),BinaryOp("||",BinaryOp("&&",BinaryOp(">",IntLiteral(1),IntLiteral(2)),BooleanLiteral("true")),BooleanLiteral("false")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))


    # Test Index in Array
    def test_indexArr_341(self):
        input = """
        int main()
        {
            a [ 1 ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_indexArr_342(self):
        input = """
        int main()
        {
            a [ 1 + 1 ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1))),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_indexArr_343(self):
        input = """
        int main()
        {
            a [ 1 + 1 ] = b [ 3 ] ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1))),ArrayCell(Id("b"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_indexArr_344(self):
        input = """
        int main()
        {
            a [ 1 + a[1] ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),IntLiteral(1)))),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_indexArr_345(self):
        input = """
        int main()
        {
            a [ 1 + a[1 + a[1]] ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),IntLiteral(1)))))),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_indexArr_346(self):
        input = """
        int main()
        {
            a [ 1 + a[1] ] = foo();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),IntLiteral(1)))),CallExpr(Id("foo"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_indexArr_347(self):
        input = """
        int main()
        {
            a [ foo() ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),CallExpr(Id("foo"),[])),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_indexArr_348(self):
        input = """
        int main()
        {
            a [ foo(a[1]) ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(1))])),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_indexArr_349(self):
        input = """
        int main()
        {
            a [ (1 + a[1]) % 2 ] = 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("%",BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),IntLiteral(1))),IntLiteral(2))),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_indexArr_350(self):
        input = """
        int main()
        {
            a [ 1 + a[1] ] = b [ a[2] ] + 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),ArrayCell(Id("a"),IntLiteral(1)))),BinaryOp("+",ArrayCell(Id("b"),ArrayCell(Id("a"),IntLiteral(2))),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))


    # Test Statement
    def test_Statement_351(self):
        input = """
        int main()
        {
                if (JohnSnow) Said = "You know nothingg..";
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("JohnSnow"),BinaryOp("=",Id("Said"),StringLiteral("You know nothingg..")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_Statement_352(self):
        input = """
        int main()
        {
                if (GAM == "Bang B") ScoreCKTG2019 = "1-5";
                else
                    ScoreCKTG2019 = "0-6";
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("GAM"),StringLiteral("Bang B")),BinaryOp("=",Id("ScoreCKTG2019"),StringLiteral("1-5")),BinaryOp("=",Id("ScoreCKTG2019"),StringLiteral("0-6")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_Statement_353(self):
        input = """
        int main()
        {
                if ((Zeros != "NOOB") && (Levi != "Farm")) GAM = "Qua vong bang.";
                    else GAM = "5 chu he.";
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp("!=",Id("Zeros"),StringLiteral("NOOB")),BinaryOp("!=",Id("Levi"),StringLiteral("Farm"))),BinaryOp("=",Id("GAM"),StringLiteral("Qua vong bang.")),BinaryOp("=",Id("GAM"),StringLiteral("5 chu he.")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))   

    def test_Statement_354(self):
        input = """
        int main()
        {
            if (a == 1) b = 2;
            if (b == 2) a = 1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2))),If(BinaryOp("==",Id("b"),IntLiteral(2)),BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_Statement_355(self):
        input = """
        int main()
        {
            if (a == 1) foo();
                else foo(b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_Statement_356(self):
        input = """
        int main(){
                if(true) {}
                else if(false) a = 1;
                else b = 2;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral("true"),Block([]),If(BooleanLiteral("false"),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_Statement_357(self):
        input = """
        int main()
        {
            do {}
            while(true);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([])],BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_Statement_358(self):
        input = """
        int main()
        {
            do { a = 1; }
            while(false);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",Id("a"),IntLiteral(1))])],BooleanLiteral("false"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_Statement_359(self):
        input = """
        int main()
        {
            do 
            { 
                a[1] = b[2];
                b[1] = a[2]; 
            }
            while(a[3] == b[3]);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),IntLiteral(2))),BinaryOp("=",ArrayCell(Id("b"),IntLiteral(1)),ArrayCell(Id("a"),IntLiteral(2)))])],BinaryOp("==",ArrayCell(Id("a"),IntLiteral(3)),ArrayCell(Id("b"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_Statement_360(self):
        input = """
        int main()
        {
            do 
            {
                do {} while (c == d);
            }
            while (a == b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Dowhile([Block([])],BinaryOp("==",Id("c"),Id("d")))])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_Statement_361(self):
        input = """
        int main()
        {
            do
            {
                if (c == d) a = 1;
                else b = 1;
            }
            while (a == b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("==",Id("c"),Id("d")),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(1)))])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_Statement_362(self):
        input = """
        int main()
        {
            do
            {
                if (c == d || a > b) a = 1;
                else b = 1;
            }
            while (a != b && c != d);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("||",BinaryOp("==",Id("c"),Id("d")),BinaryOp(">",Id("a"),Id("b"))),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(1)))])],BinaryOp("&&",BinaryOp("!=",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_Statement_363(self):
        input = """
        int main()
        {
            do
            {
                if (c == d) {}
                else {}
            }
            while (a == b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("==",Id("c"),Id("d")),Block([]),Block([]))])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_Statement_364(self):
        input = """
        int main()
        {
            do
            { 
            	{} {} 
            }
            while (a == b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Block([]),Block([])])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_Statement_365(self):
        input = """
        int main()
        {
            do
            {
                {{{}}}
            }
            while (a == b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Block([Block([Block([])])])])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_Statement_366(self):
        input = """
        int main()
        {
            do
            {
                if (c == d) do {} while (true);
                else b = 1;
            }
            while (a == b);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("==",Id("c"),Id("d")),Dowhile([Block([])],BooleanLiteral("true")),BinaryOp("=",Id("b"),IntLiteral(1)))])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_Statement_367(self):
        input = """
        int main()
        {
            do
            {
                if (c == d) a = 1;
                else b = 1;
            }
            while (1+1);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([If(BinaryOp("==",Id("c"),Id("d")),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(1)))])],BinaryOp("+",IntLiteral(1),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_Statement_368(self):
        input = """
        int main()
        {
            do
            {
                foo();
            }
            while (foo());
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([CallExpr(Id("foo"),[])])],CallExpr(Id("foo"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_Statement_369(self):
        input = """
        int main() 
        {
            for (i = 0; i < 5; i = i + 1) a = a + i;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),Id("i"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_Statement_370(self):
        input = """
        int main() 
        {
            for (i = 0; i < 5; i = i + 1) { }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_Statement_371(self):
        input = """
        int main() 
        {
            for (i = 0; i < 5; i = i + 1) foo("loop");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),CallExpr(Id("foo"),[StringLiteral("loop")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_Statement_372(self):
        input = """
        int main() 
        {
            for (i = 0; i < 5; i = i + 1)
                for (j = 0; j < 5; j = j + 1) {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),IntLiteral(5)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_Statement_373(self):
        input = """
        int main() 
        {
            for (i = 0; i < 5; i = i + 1)
            { 
                break;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_Statement_374(self):
        input = """
        int main() 
        {
            for (10; i < 5; i = i + 1)
            { 
                continue;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_Statement_375(self):
        input = """
        int main() 
        {
            for (10; i < 5; 20)
            { 
                return;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([Return()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_Statement_376(self):
        input = """
        int main()
        {
            do 
            {
                for (10; i < 5; 20)
                { 
                    return;
                }
            }
            while(false);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([Return()]))])],BooleanLiteral("false"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_Statement_377(self):
        input = """
        int main()
        {
            do 
            {
                for (10; i < 5; 20)
                { 
                    if (JohnSnow) Said = "You know nothingg..";
                }
            }
            while(false);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([If(Id("JohnSnow"),BinaryOp("=",Id("Said"),StringLiteral("You know nothingg..")))]))])],BooleanLiteral("false"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_Statement_378(self):
        input = """
        int main()
        {
            do 
            {
                for (10; i < 5; 20)
                { 
                    if (JohnSnow) Said = "You know nothingg..";
                    a [ foo() ] = 2;
                }
            }
            while(false);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([If(Id("JohnSnow"),BinaryOp("=",Id("Said"),StringLiteral("You know nothingg.."))),BinaryOp("=",ArrayCell(Id("a"),CallExpr(Id("foo"),[])),IntLiteral(2))]))])],BooleanLiteral("false"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_Statement_379(self):
        input = """
        int main() 
        {
            for (10; i < 5; 20)
            { 
                return;
                break;
                continue;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([Return(), Break(), Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_Statement_379(self):
        input = """
        int main() 
        {
        	break;
        	continue;
        	return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break(),Continue(),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_Statement_380(self):
        input = """
        int main() 
        {
            for (10; i < 5; 20)
            { 
                foo(foo("Ass2"));
                return;   
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([CallExpr(Id("foo"),[CallExpr(Id("foo"),[StringLiteral("Ass2")])]),Return()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
                

    # Test Other
    def test_other_381(self):
        input = """
        int main()
        {
            a [ foo() + foo2() ] = foo3();
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),BinaryOp("+",CallExpr(Id("foo"),[]),CallExpr(Id("foo2"),[]))),CallExpr(Id("foo3"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_other_382(self):
        input = """
        int main()
        {
            foo(a = 1e-2, "abc");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[BinaryOp("=",Id("a"),FloatLiteral(0.01)),StringLiteral("abc")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_other_383(self):
        input = """
        int main()
        {
            a[1] =  !b[2] && c[3] ;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),BinaryOp("&&",UnaryOp("!",ArrayCell(Id("b"),IntLiteral(2))),ArrayCell(Id("c"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_other_384(self):
        input = """
        int main () 
        {
             return 1;   
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_other_385(self):
        input = """
        int main () 
        {
             return a + b - c;   
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_other_386(self):
        input = """
        int main()
        {
            foo()[1];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_other_387(self):
        input = """
        int main()
        {
            foo("string")[1];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("foo"),[StringLiteral("string")]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_other_388(self):
        input = """
        int main()
        {
            foo(foo())[1];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[])]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_other_389(self):
        input = """
        int main()
        {
            foo(foo("1")[1])[1];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("foo"),[ArrayCell(CallExpr(Id("foo"),[StringLiteral("1")]),IntLiteral(1))]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_other_390(self):
        input = """int main(){
            (((a)));
        }"""
        expect=str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("a")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
  
    def test_other_391(self):
        input = """
        int main()
        {
            foo(a + b % 2)[1];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("foo"),[BinaryOp("+",Id("a"),BinaryOp("%",Id("b"),IntLiteral(2)))]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_other_392(self):
        input = """
        int main()
        {
            {} {{}} {} {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([]),Block([Block([])]),Block([]),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_other_393(self):
        input = """
        int main()
        {
            foo();
            // A Line Comment.
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_other_394(self):
        input = """
        int main()
        {
            foo();
            /*
            A Block Comment.
            */
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_other_395(self):
        input = """
        int main()
        {
            __foo(__abc,cde__)[2] = "Het y tuong roii..";
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("__foo"),[Id("__abc"),Id("cde__")]),IntLiteral(2)),StringLiteral("Het y tuong roii.."))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_other_396(self):
        input = """
        int main()
        {
            status[0] = foo("100 testcases met qua..");
            status[0 + 1 / 2 + 1 / 2] = "Them cho testcase nay no dai ra 1 ty.";
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(Id("status"),IntLiteral(0)),CallExpr(Id("foo"),[StringLiteral("100 testcases met qua..")])),BinaryOp("=",ArrayCell(Id("status"),BinaryOp("+",BinaryOp("+",IntLiteral(0),BinaryOp("/",IntLiteral(1),IntLiteral(2))),BinaryOp("/",IntLiteral(1),IntLiteral(2)))),StringLiteral("Them cho testcase nay no dai ra 1 ty."))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_other_397(self):
        input = """
        int main()
        {
            do 
            {
                printf("Cuu toi voi ._.");
            }
            while(Gan_het_chua);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Cuu toi voi ._.")])])],Id("Gan_het_chua"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_other_398(self):
        input = """
        int main()
        {
            if (this_testcase == 399)
                status = "Yay~yay Con 1 testcase nua >.<";
            else
                status = "2 testcases nua lan :'<"; // this_testcase = 398;

        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("this_testcase"),IntLiteral(399)),BinaryOp("=",Id("status"),StringLiteral("Yay~yay Con 1 testcase nua >.<")),BinaryOp("=",Id("status"),StringLiteral("2 testcases nua lan :'<")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_other_399(self):
        input = """
        int main()
        {
            for (10; i < 5; 20)
            { 
                printf("Con 1 testcase cuoi. Quay lenn O.o");
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(5)),IntLiteral(20),Block([CallExpr(Id("printf"),[StringLiteral("Con 1 testcase cuoi. Quay lenn O.o")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_other_400(self):
        input = """
        int main()
        {
            status = "Phewww. Im done. Let's decide what i should do now .__.";
            if (isLate() == true) go_to_bed("during 10 hours");
            else go_to_bed("during 12 hours"); 
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("status"),StringLiteral("Phewww. Im done. Let's decide what i should do now .__.")),If(BinaryOp("==",CallExpr(Id("isLate"),[]),BooleanLiteral("true")),CallExpr(Id("go_to_bed"),[StringLiteral("during 10 hours")]),CallExpr(Id("go_to_bed"),[StringLiteral("during 12 hours")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
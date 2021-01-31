import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_declare_0(self):
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_declare_1(self):
        input = """Var:x, a;"""
        expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_declare_2(self):
        input = """Var:x = 1, a;"""
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(1)),
            VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_declare_3(self):
        input = """Var:x = True, a;"""
        expect = str(Program([VarDecl(Id("x"),[],BooleanLiteral(True)),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_declare_4(self):
        input = """Var:x[10][50] = {2}, a = 10, c = 100.5;
        Var: me, you;
        Var: he[1][2][3][4][5] = {1};
        Var: she = False;
        """
        expect = Program([VarDecl(Id("x"),[10,50],ArrayLiteral([IntLiteral(2)])),VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("c"),[],FloatLiteral(100.5)), VarDecl(Id("me"),[],[]), VarDecl(Id("you"),[],[]), VarDecl(Id("he"),[1,2,3,4,5],ArrayLiteral([IntLiteral(1)])), VarDecl(Id("she"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_declare_5(self):
        input = """Var: x[10][50] = {{1},{2},{3},{4}};
        Var: a = 10, c = 100.5;
        Var: me;
        """
        expect = Program([VarDecl(Id('x'),[10,50],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)]),ArrayLiteral([IntLiteral(3)]),ArrayLiteral([IntLiteral(4)])])),VarDecl(Id('a'),[],IntLiteral(10)),VarDecl(Id('c'),[],FloatLiteral(100.5)),VarDecl(Id('me'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_funcDeclar_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = {1,2,3,4};
        Var: ngao, du = 3, thienha[5][9][1][2];
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[5,9,3],None),VarDecl(Id('b'),[7],None)],([VarDecl(Id('m'),[10,8],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),VarDecl(Id('ngao'),[],None),VarDecl(Id('du'),[],IntLiteral(3)),VarDecl(Id('thienha'),[5,9,1,2],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_ifStmtInFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        Else
            Var: a; 
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[If([(BinaryOp('==',Id('x'),Id('y')),[],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))])],([VarDecl(Id('a'),[],None)],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_ifStmtInFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then y = y + 1;
        ElseIf x < y Then y = y - x;
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[If([(BinaryOp('==',Id('x'),Id('y')),[],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]),(BinaryOp('>',Id('x'),Id('y')),[],[Assign(Id('y'),BinaryOp('+',Id('y'),IntLiteral(1)))]),(BinaryOp('<',Id('x'),Id('y')),[],[Assign(Id('y'),BinaryOp('-',Id('y'),Id('x')))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_ifStmtInFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1;
        ElseIf x < y Then Var: b = 2;
        Else
            If y > 10 Then y = y \ 2;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[If([(BinaryOp('==',Id('x'),Id('y')),[],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]),(BinaryOp('>',Id('x'),Id('y')),[VarDecl(Id('a'),[],IntLiteral(1))],[]),(BinaryOp('<',Id('x'),Id('y')),[VarDecl(Id('b'),[],IntLiteral(2))],[])],([],[If([(BinaryOp('>',Id('y'),IntLiteral(10)),[],[Assign(Id('y'),BinaryOp('\\',Id('y'),IntLiteral(2)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_ifStmtInFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1; x = a * 10.5;
        ElseIf x < y Then Var: b = 2; y = b + foo();
        Else
            If y > 10 Then y = y \ 2; Return 1;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[If([(BinaryOp('==',Id('x'),Id('y')),[],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]),(BinaryOp('>',Id('x'),Id('y')),[VarDecl(Id('a'),[],IntLiteral(1))],[Assign(Id('x'),BinaryOp('*',Id('a'),FloatLiteral(10.5)))]),(BinaryOp('<',Id('x'),Id('y')),[VarDecl(Id('b'),[],IntLiteral(2))],[Assign(Id('y'),BinaryOp('+',Id('b'),CallExpr(Id('foo'),[])))])],([],[If([(BinaryOp('>',Id('y'),IntLiteral(10)),[],[Assign(Id('y'),BinaryOp('\\',Id('y'),IntLiteral(2))),Return(IntLiteral(1))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_funcDeclar_2(self):
        input = """Function: main
        Body:
        (a + foo())[1] = 1;
        a[1] = a[1] * s;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[])),[IntLiteral(1)]),IntLiteral(1)),Assign(ArrayCell(Id('a'),[IntLiteral(1)]),BinaryOp('*',ArrayCell(Id('a'),[IntLiteral(1)]),Id('s')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcDeclar_3(self):
        input = """Function: main
        Body:
        (a + foo())[1] = {{1,2,3}, {1,2,3}, {1,2,3}};
        a[1] = a[1 + foo((a + foo())[1])] * s;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[])),[IntLiteral(1)]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),Assign(ArrayCell(Id('a'),[IntLiteral(1)]),BinaryOp('*',ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[])),[IntLiteral(1)])]))]),Id('s')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_forFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, 2) Do
        writeln(i);
        EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_forFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i + 2) Do
        x = x + 10.0;
        EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(2)),([],[Assign(Id('x'),BinaryOp('+',Id('x'),FloatLiteral(10.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_forFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        Var: qq, dd, ee;
        For (i = 0, i < 10, i + 2) Do
            Var: y = True;
            x = foo(i);
            x[i] = foo[x+i];
            For (j = 5, j >= 0, j -1) Do
            Break;
            Return 1;
            EndFor.
        EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([VarDecl(Id('qq'),[],None),VarDecl(Id('dd'),[],None),VarDecl(Id('ee'),[],None)],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(2)),([VarDecl(Id('y'),[],BooleanLiteral('true'))],[Assign(Id('x'),CallExpr(Id('foo'),[Id('i')])),Assign(ArrayCell(Id('x'),[Id('i')]),ArrayCell(Id('foo'),[BinaryOp('+',Id('x'),Id('i'))])),For(Id('j'),IntLiteral(5),BinaryOp('>=',Id('j'),IntLiteral(0)),BinaryOp('-',Id('j'),IntLiteral(1)),([],[Break(),Return(IntLiteral(1))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_whileFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While x == True Do 
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[While(BinaryOp('==',Id('x'),BooleanLiteral('true')),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_whileFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While x == True Do 
                While y == 1 Do
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[While(BinaryOp('==',Id('x'),BooleanLiteral('true')),([],[While(BinaryOp('==',Id('y'),IntLiteral(1)),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_whileFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While x == True Do 
                While y == 1 Do
                    dd = nn;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[While(BinaryOp('==',Id('x'),BooleanLiteral('true')),([],[While(BinaryOp('==',Id('y'),IntLiteral(1)),([],[Assign(Id('dd'),Id('nn'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_whileFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                x = x + 1;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[While(BinaryOp('<',Id('x'),FloatLiteral(10.5)),([],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),While(BinaryOp('==',Id('y'),IntLiteral(1)),([],[Assign(Id('dd'),Id('nn')),Assign(ArrayCell(Id('y'),[Id('i')]),ArrayCell(Id('x'),[BinaryOp('+',Id('y'),Id('i'))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_whileFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                x = x + 1;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[While(BinaryOp('<',Id('x'),FloatLiteral(10.5)),([],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),While(BinaryOp('==',Id('y'),IntLiteral(1)),([],[Assign(Id('dd'),Id('nn')),Assign(ArrayCell(Id('y'),[Id('i')]),ArrayCell(Id('x'),[BinaryOp('+',Id('y'),Id('i'))])),Assign(ArrayCell(Id('a'),[IntLiteral(221)]),FloatLiteral(10.9))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_DoWhileFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do While 1
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[Dowhile(([],[]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_DoWhileFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do
                Do 
                    Var: a = 10, c = 100.5;
                While (x <= 1) || (x != 10)
                EndDo.
            While (x <= 1) || (x != 10)
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[Dowhile(([],[Dowhile(([VarDecl(Id('a'),[],IntLiteral(10)),VarDecl(Id('c'),[],FloatLiteral(100.5))],[]),BinaryOp('||',BinaryOp('<=',Id('x'),IntLiteral(1)),BinaryOp('!=',Id('x'),IntLiteral(10))))]),BinaryOp('||',BinaryOp('<=',Id('x'),IntLiteral(1)),BinaryOp('!=',Id('x'),IntLiteral(10))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    
    def test_DoWhileFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123], b, c
        Body:
            Do 
                Var: a = 10, c = 100.5;
                x = a[x + 1][foo(a + 1) + 3];
            While (x <= 1) || (x != 10)
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([VarDecl(Id('a'),[],IntLiteral(10)),VarDecl(Id('c'),[],FloatLiteral(100.5))],[Assign(Id('x'),ArrayCell(Id('a'),[BinaryOp('+',Id('x'),IntLiteral(1)),BinaryOp('+',CallExpr(Id('foo'),[BinaryOp('+',Id('a'),IntLiteral(1))]),IntLiteral(3))]))]),BinaryOp('||',BinaryOp('<=',Id('x'),IntLiteral(1)),BinaryOp('!=',Id('x'),IntLiteral(10))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_all_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            y = x-(!(!True));
            Return;
        EndBody.
        Function: count
        Parameter: i
        Body:
            y = x-(!(!True));
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[VarDecl(Id('a'),[83],None)],([],[Assign(Id('y'),BinaryOp('-',Id('x'),UnaryOp('!',UnaryOp('!',BooleanLiteral('true'))))),Return(None)])),FuncDecl(Id('count'),[VarDecl(Id('i'),[],None)],([],[Assign(Id('y'),BinaryOp('-',Id('x'),UnaryOp('!',UnaryOp('!',BooleanLiteral('true'))))),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_ifStmtInFunc_5(self):
        input = """
        Var: i[123][1][2]={1,2,3,4,5};
        Function: main
        Parameter: a, b
        Body:
        Var: r = 10., v;
        If 5 + 2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        Else
            Var:a;
            a = x +3;
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('i'),[123,1,2],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))])],([VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_ifStmtInFunc_6(self):
        input = """
        Var: i[123][1][2]={1,2,3,4,5};
        Function: main
        Parameter: a, b
        Body:
        Var: r = 10., v;
        If 5 + 2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('i'),[123,1,2],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_ifStmtInFunc_7(self):
        input = """
            Var: i;
            Function: main
            Parameter: a, b
            Body:
            Var: r = 10., v;
            If 5 + 2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            ElseIf 5+2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            ElseIf 5+2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            Else
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            EndIf.
            EndBody.
            """
        expect = Program([VarDecl(Id('i'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))])],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_all_2(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('printLn'),[Id('x')]),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_all_3(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
            Break;
            Return;
            foo();
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('printLn'),[Id('x')]),Continue(),Break(),Return(None),CallStmt(Id('foo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_declare_6(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = Program([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_declare_7(self):
        input = """Var: a = 0;
        Function: main
        Body:
            a[3 + foo(2)] = a[b [2][3]] + 4;
        EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_declare_8(self):
        input = """Var: a = 0;
        Function: main
        Body:
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_declare_9(self):
        input = """Var: a = 0;
        Function: main
        Body:
            foo(a[1][2] + 2, x + 1);
        EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_declare_10(self):
        input = """Var: a = 0;
        Function: main
        Body:
            x = foo(a[1][2] + 2, x + 1);
        EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[Assign(Id('x'),CallExpr(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_whileFunc_6(self):
        input = """Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_all_4(self):
        input = """Var: a = 0;
Function: main
Body:
    For (i = 0, i < 10, 2) Do
        writeln(i);
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_all_5(self):
        input = """Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];"""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_all_6(self):
        input = """Var: x;
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
    EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_all_7(self):
        input = """Var: a[5] = {1,4,3,2,0};
Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = Program([VarDecl(Id('a'),[5],ArrayLiteral([IntLiteral(1),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(0)])),VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_all_8(self):
        input = """Var: x;
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
    EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_all_9(self):
        input = """Var: a = 0;
Function: main
Body:
    foo(a[1][2] + 2, x + 1);
    foo (2 + x, 4. \. y);
    goo ();
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\\.',FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_all_10(self):
        input = """Var: a = 0;
Function: main
Body:
    foo(a[1][2] + 2, x + 1);
    foo (2 + x, 4. \. y);
    goo ();
    If bool_of_string ("True") Then
        a = int_of_string (read ());
        b = float_of_int (a) +. 2.0;
        foo(a[1][2] + 2, x + 1);
        foo (2 + x, 4. \. y);
        goo ();
    EndIf.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\\.',FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[]),If([(CallExpr(Id('bool_of_string'),[StringLiteral("""True""")]),[],[Assign(Id('a'),CallExpr(Id('int_of_string'),[CallExpr(Id('read'),[])])),Assign(Id('b'),BinaryOp('+.',CallExpr(Id('float_of_int'),[Id('a')]),FloatLiteral(2.0))),CallStmt(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\\.',FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_all_11(self):
        input = """Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(5))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_all_12(self):
        input = """Var: a = 1, b[2][3] = {5}, c[2] = {{1,3},{1,5,7}};
Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(1)),VarDecl(Id('b'),[2,3],ArrayLiteral([IntLiteral(5)])),VarDecl(Id('c'),[2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(3)]),ArrayLiteral([IntLiteral(1),IntLiteral(5),IntLiteral(7)])])),FuncDecl(Id('test'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(5))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_all_13(self):
        input = """Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return a[4][5 + b[2][3]];
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(5))])],([],[Return(ArrayCell(Id('a'),[IntLiteral(4),BinaryOp('+',IntLiteral(5),ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_all_14(self):
        input = """Var: a = "Xin chao moi nguoi!";
Var: b = 5, c = False;"""
        expect = Program([VarDecl(Id('a'),[],StringLiteral("""Xin chao moi nguoi!""")),VarDecl(Id('b'),[],IntLiteral(5)),VarDecl(Id('c'),[],BooleanLiteral('false'))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_all_15(self):
        input = """Function: test
Body:
    If n > 10 Then
        Return n;
    ElseIf n > 8 Then
        Return n + 1;
    ElseIf n > 6 Then
        Return n + 2;
    ElseIf n > 4 Then
        Return n + 3;
    ElseIf n > 2 Then
        Return n + 4;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(Id('n'))]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(1)))]),(BinaryOp('>',Id('n'),IntLiteral(6)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(2)))]),(BinaryOp('>',Id('n'),IntLiteral(4)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(3)))]),(BinaryOp('>',Id('n'),IntLiteral(2)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(4)))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_all_16(self):
        input = """Function: test
Body:
    If n > 10 Then
        Return n;
    ElseIf n > 8 Then
        Return n + 1;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(Id('n'))]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(1)))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_all_17(self):
        input = """Function: test
Body:
    If n > 10 Then
        Return n;
    ElseIf n > 8 Then
        Return n + 1;
    ElseIf n > 6 Then
        Return n + 2;
    ElseIf n > 4 Then
        Return n + 3;
    ElseIf n > 2 Then
        Return n + 4;
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[Return(Id('n'))]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(1)))]),(BinaryOp('>',Id('n'),IntLiteral(6)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(2)))]),(BinaryOp('>',Id('n'),IntLiteral(4)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(3)))]),(BinaryOp('>',Id('n'),IntLiteral(2)),[],[Return(BinaryOp('+',Id('n'),IntLiteral(4)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_all_18(self):
        input = """Var: x;
Function: fact
Parameter: n

Body:
    Var: i, x = 0;
    For (i = 1, i < 3, -. 5) Do
        x = i +7;
        If n > 100 Then
            Break;
        EndIf.
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],None),VarDecl(Id('x'),[],IntLiteral(0))],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(3)),UnaryOp('-.',IntLiteral(5)),([],[Assign(Id('x'),BinaryOp('+',Id('i'),IntLiteral(7))),If([(BinaryOp('>',Id('n'),IntLiteral(100)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    def test_all_19(self):
        input = """Var: x[0O56]  = {{1,2},{2}};"""
        expect = Program([VarDecl(Id('x'),[46],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    def test_all_20(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, -. 2) Do
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-.',IntLiteral(2)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_all_21(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10,  2) Do
        Return 1;
        Break;
        Continue;
        foo(float_of_int (a) + 2);
        goo(a+1);
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[Return(IntLiteral(1)),Break(),Continue(),CallStmt(Id('foo'),[BinaryOp('+',CallExpr(Id('float_of_int'),[Id('a')]),IntLiteral(2))]),CallStmt(Id('goo'),[BinaryOp('+',Id('a'),IntLiteral(1))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    def test_all_22(self):
        input = """Var: a = 5;
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[5],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    def test_all_23(self):
        input = """Var: a = 5;
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    Var: b[5];
    Var: c, d = 6, e;
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[5],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('b'),[5],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None)],[Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    
    def test_all_24(self):
        input = """Function: main
Body:
    While True Do print("Hello World!"); EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BooleanLiteral('true'),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    def test_all_25(self):
        input = """Function: main
Body:
    While True Do EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[While(BooleanLiteral('true'),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    def test_all_26(self):
        input = """Var: a = "a string";
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = Program([VarDecl(Id('a'),[],StringLiteral("""a string""")),VarDecl(Id('b'),[5],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    def test_all_27(self):
        input = """Var: a = "a string";
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    x = y + (z -q) *. 10 +. 100.;
    x = n >=. z;
EndBody."""
        expect = Program([VarDecl(Id('a'),[],StringLiteral("""a string""")),VarDecl(Id('b'),[5],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('+.',BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10))),FloatLiteral(100.0))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    def test_all_28(self):
        input = """Var: a = "a string";
** Day la comment
* Day cung la comment
* Comment luon **
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = Program([VarDecl(Id('a'),[],StringLiteral("""a string""")),FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    def test_all_29(self):
        input = """Var: a = "a string";
** Day la comment
* Day cung la comment
* Comment luon 
* Day cung la comment nhung chua dong lai**
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = Program([VarDecl(Id('a'),[],StringLiteral("""a string""")),FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    def test_all_30(self):
        input = """**This is program
* Here is declare
* Here for function**"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))
    def test_all_31(self):
        input = """ """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    def test_all_32(self):
        input = """Var: x, y = 2., z = 3.5;
Function: you
Parameter: x , y[5]
Body:
Var: a, b, c = "string";
Var: a = False;
If (z == True) Then
    Return 1;
EndIf.
While (True)  Do    
    foo();
    goo(a);
    Break;                      
EndWhile.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],FloatLiteral(2.0)),VarDecl(Id('z'),[],FloatLiteral(3.5)),FuncDecl(Id('you'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[5],None)],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],StringLiteral("""string""")),VarDecl(Id('a'),[],BooleanLiteral('false'))],[If([(BinaryOp('==',Id('z'),BooleanLiteral('true')),[],[Return(IntLiteral(1))])],([],[])),While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[]),CallStmt(Id('goo'),[Id('a')]),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    def test_all_33(self):
        input = """Var: x, y = 1, z = 3.5;
Var: t;
Var: sp, yz;
Function: you
Parameter: q , d[5]
Body:
Var: a = "string", b;
Var: c = False;
foo(a + c);
If (z == True) Then
    x = d[y *. z +. t -. c \ 10];
    Return 1;
ElseIf x != 4.e5 Then
    x = (a + b) * y - z + (sp *. yz);
Else
    Continue;
EndIf.
While (True)  Do    
    foo();
    goo(a);
    Break;                      
EndWhile.
For (i = 0, i < 10, -2) Do
    x = i;
EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],IntLiteral(1)),VarDecl(Id('z'),[],FloatLiteral(3.5)),VarDecl(Id('t'),[],None),VarDecl(Id('sp'),[],None),VarDecl(Id('yz'),[],None),FuncDecl(Id('you'),[VarDecl(Id('q'),[],None),VarDecl(Id('d'),[5],None)],([VarDecl(Id('a'),[],StringLiteral("""string""")),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],BooleanLiteral('false'))],[CallStmt(Id('foo'),[BinaryOp('+',Id('a'),Id('c'))]),If([(BinaryOp('==',Id('z'),BooleanLiteral('true')),[],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Return(IntLiteral(1))]),(BinaryOp('!=',Id('x'),FloatLiteral(400000.0)),[],[Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),Id('b')),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz'))))])],([],[Continue()])),While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[]),CallStmt(Id('goo'),[Id('a')]),Break()])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-',IntLiteral(2)),([],[Assign(Id('x'),Id('i'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    def test_all_34(self):
        input = """Var: a;
Function: main
Parameter: q , d[5]
Body:                                       
    x = foo(0XAB) + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = Program([VarDecl(Id('a'),[],None),FuncDecl(Id('main'),[VarDecl(Id('q'),[],None),VarDecl(Id('d'),[5],None)],([],[Assign(Id('x'),BinaryOp('+',CallExpr(Id('foo'),[IntLiteral(171)]),CallExpr(Id('goo'),[IntLiteral(10)]))),Assign(Id('y'),CallExpr(Id('foo'),[BinaryOp('+',Id('x'),CallExpr(Id('goo'),[BooleanLiteral('true')]))])),CallStmt(Id('print'),[BinaryOp('+',Id('x'),Id('y'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    def test_all_35(self):
        input = """Var: a;
Function: main
Parameter: q , d[5]
Body:                                       
    x = foo("ahihi") + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = Program([VarDecl(Id('a'),[],None),FuncDecl(Id('main'),[VarDecl(Id('q'),[],None),VarDecl(Id('d'),[5],None)],([],[Assign(Id('x'),BinaryOp('+',CallExpr(Id('foo'),[StringLiteral("""ahihi""")]),CallExpr(Id('goo'),[IntLiteral(10)]))),Assign(Id('y'),CallExpr(Id('foo'),[BinaryOp('+',Id('x'),CallExpr(Id('goo'),[BooleanLiteral('true')]))])),CallStmt(Id('print'),[BinaryOp('+',Id('x'),Id('y'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    def test_all_36(self):
        input = """Var: uh;
Function: main
Parameter: q , d[5]
Body:                                       
    x = foo("ahihi") + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = Program([VarDecl(Id('uh'),[],None),FuncDecl(Id('main'),[VarDecl(Id('q'),[],None),VarDecl(Id('d'),[5],None)],([],[Assign(Id('x'),BinaryOp('+',CallExpr(Id('foo'),[StringLiteral("""ahihi""")]),CallExpr(Id('goo'),[IntLiteral(10)]))),Assign(Id('y'),CallExpr(Id('foo'),[BinaryOp('+',Id('x'),CallExpr(Id('goo'),[BooleanLiteral('true')]))])),CallStmt(Id('print'),[BinaryOp('+',Id('x'),Id('y'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    def test_all_37(self):
        input = """Var: a;
Function: main
Parameter: q , d[5]
    Body: 
    Var: x, y = 1, z = 3.5;
    If((a > b) && (c < d)) Then
        Break;
    EndIf.                                          
    x = foo("ahihi") + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = Program([VarDecl(Id('a'),[],None),FuncDecl(Id('main'),[VarDecl(Id('q'),[],None),VarDecl(Id('d'),[5],None)],([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],IntLiteral(1)),VarDecl(Id('z'),[],FloatLiteral(3.5))],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[Break()])],([],[])),Assign(Id('x'),BinaryOp('+',CallExpr(Id('foo'),[StringLiteral("""ahihi""")]),CallExpr(Id('goo'),[IntLiteral(10)]))),Assign(Id('y'),CallExpr(Id('foo'),[BinaryOp('+',Id('x'),CallExpr(Id('goo'),[BooleanLiteral('true')]))])),CallStmt(Id('print'),[BinaryOp('+',Id('x'),Id('y'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
    def test_all_38(self):
        input = """Var: x;
Function: fact
Parameter: n, y
Body:
    While n[1] == a[2] Do
        **Check**
        Break;
    EndWhile.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None),VarDecl(Id('y'),[],None)],([],[While(BinaryOp('==',ArrayCell(Id('n'),[IntLiteral(1)]),ArrayCell(Id('a'),[IntLiteral(2)])),([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    def test_all_39(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a  >= 5) Do 
        a = a + 1;
    EndWhile.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[While(BinaryOp('>=',Id('a'),IntLiteral(5)),([],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    def test_all_40(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        a = a + - 1;
    EndWhile.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[Assign(Id('a'),BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_all_41(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        Do
            Do
                print("Hello World!");
            While a > b
            EndDo.
            print("Hello World!");
        While a > b
        EndDo.
        print("Hello World!");
    While a > b
    EndDo.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    def test_all_42(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        print("Hello World!");
        While (a <= - 5) Do 
            print("Hello World!");
            While (a <= - 5) Do 
                print("Hello World!");
                While (a <= - 5) Do 
                    print("Hello World!");
                EndWhile.
            EndWhile.
        EndWhile.
    EndWhile.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))
    def test_all_43(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        print("Hello World!");
        While (a <= - 5) Do
            Do
                Do
                    Do
                        print("Hello World!");
                    While a > b
                    EndDo.
                    print("Hello World!");
                While a > b
                EndDo.
                print("Hello World!");
            While a > b
            EndDo.
            print("Hello World!");
            While (a <= - 5) Do 
                print("Hello World!");
                While (a <= - 5) Do 
                    Do
                        Do
                            Do
                                print("Hello World!");
                            While a > b
                            EndDo.
                            print("Hello World!");
                        While a > b
                        EndDo.
                        print("Hello World!");
                    While a > b
                    EndDo.
                    print("Hello World!");
                EndWhile.
            EndWhile.
        EndWhile.
    EndWhile.
EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral(0)),FuncDecl(Id('main'),[],([],[While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),While(BinaryOp('<=',Id('a'),UnaryOp('-',IntLiteral(5))),([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_all_44(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        print("Hello World!");
        For (i = 0, i < 10, -2) Do
            For (i = 0, i < 10, 2) Do
                print("Hello World!");
                For (i = 0, i < 10, 2) Do
                    For (i = 0, i < 10, 2) Do
                        print("Hello World!");
                    EndFor.
                    print("Hello World!");
                EndFor.
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-',IntLiteral(2)),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_all_45(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!");
            EndIf. 
            For (i = 0, i < 10, 2) Do         
                For (i = 0, i < 10,-. 2) Do
                    For (i = 0, i < 10, 2) Do  
                        If((a > b) && (c < d)) Then
                            If((a > b) && (c < d)) Then
                                print("Hello World!");
                            EndIf. 
                            print("Hello World!");
                        EndIf.     
                    EndFor.
                    print("Hello World!");
                EndFor.
                If((a > b) && (c < d)) Then
                    print("Hello World!");
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-.',IntLiteral(2)),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])),If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_all_46(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                Break;
            EndIf. 
            For (i = 0, i < 10, -2) Do         
                If((a == b) && (c < d)) Then
                    Break;
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[Break()])],([],[])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-',IntLiteral(2)),([],[If([(BinaryOp('&&',BinaryOp('==',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[Break()])],([],[]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    def test_all_47(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n > 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    EndIf.
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    ElseIf n > 8 Then
        print("Hello World!");
    ElseIf n > 2 Then
        print("Hello World!");
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(2)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_all_48(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
        expect = Program([FuncDecl(Id('test'),[],([],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('!=',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_all_49(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r'))),Assign(Id('x'),CallExpr(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))])),Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z'))),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),Id('b')),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz')))),Assign(Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))),UnaryOp('-',IntLiteral(5))),UnaryOp('-',IntLiteral(5))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_all_50(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 != r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id('v'),BinaryOp('!=',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),BinaryOp('*.',BinaryOp('*.',Id('r'),Id('r')),Id('r')))),Assign(Id('x'),CallExpr(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))])),Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z'))),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),Id('b')),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz')))),Assign(Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))),UnaryOp('-',IntLiteral(5))),UnaryOp('-',IntLiteral(5))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_all_51(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + - b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r'))),Assign(Id('x'),CallExpr(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))])),Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z'))),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),UnaryOp('-',Id('b'))),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz')))),Assign(Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))),UnaryOp('-',IntLiteral(5))),UnaryOp('-',IntLiteral(5))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))
    def test_all_52(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo()));
                    EndFor.
                Else
                    Do
                        Continue;
                    While (a \. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])])]))])],([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\\.',Id('a'),FloatLiteral(10.0)),FloatLiteral(10.5)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    def test_all_53(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),IntLiteral(1193046)),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral(5)])])])]))])],([],[Dowhile(([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\\.',Id('a'),FloatLiteral(10.0)),FloatLiteral(0.0105)))]),BinaryOp('=/=',BinaryOp('\\.',Id('a'),FloatLiteral(10.0)),FloatLiteral(0.0105)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_all_54(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 + foo(2)]][3]] + 4;
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))])]))])]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_all_55(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!");
            EndIf. 
            For (i = 0, i < 10, - 2) Do         
                If((a != b) >= (c < d)) Then
                    print("Hello World!");
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-',IntLiteral(2)),([],[If([(BinaryOp('>=',BinaryOp('!=',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_all_56(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z - q - 1 - 4 + 6) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c % 10];
    x = (a + - b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r'))),Assign(Id('x'),CallExpr(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))])),Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('+',BinaryOp('-',BinaryOp('-',BinaryOp('-',Id('z'),Id('q')),IntLiteral(1)),IntLiteral(4)),IntLiteral(6)),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z'))),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('%',Id('c'),IntLiteral(10)))])),Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),UnaryOp('-',Id('b'))),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz')))),Assign(Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))),UnaryOp('-',IntLiteral(5))),UnaryOp('-',IntLiteral(5))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    def test_all_57(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 + foo(2)]][3]] + 4;
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))])]))])]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_all_58(self):
        input = """Function: fact
Parameter: n
Body:
Var: x;
    x = d[y *. z +. t -. c \ 10];
    b[2][3][3 + foo(a[3 + foo(a[3 + foo(2)])])] = {{2,3,4},{4,5,6}};
    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 * foo(2)]][3]] + 4;
EndBody."""
        expect = Program([FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('x'),[],None)],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3),BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))])]))])]))]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))])]))])]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[ArrayCell(Id('a'),[BinaryOp('*',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_all_59(self):
        input = """
Var: i[123][1][2]={{1}, {2}};
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
If (5 + 2 == 3) Then 
Else
    Var:a;
    a = x +3;
    Return;
EndIf.
Return;
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])])),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        If
                        ([
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [],
                            []
                            )
                        ],
                            (
                                [VarDecl(Id('a'), [], None)],
                                [
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Return(None)
                                ]
                            )
                        ),
                        Return(None)
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_all_60(self):
        input = """
Var: i[123][1][2]={{1}, {2}};
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
a[3 + foo(2)] = -.(a[b[2][3]] =/= 4);
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])])),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        Assign(
                                ArrayCell(
                                    Id('a'),
                                    [BinaryOp(
                                        '+',
                                        IntLiteral(3), 
                                        CallExpr(Id('foo'), [IntLiteral(2)])
                                    )]
                                ), 
                                UnaryOp('-.',
                                    BinaryOp(
                                        '=/=',
                                            ArrayCell(
                                                Id('a'),
                                                [
                                                    ArrayCell(
                                                        Id('b'),
                                                        [
                                                            IntLiteral(2),
                                                            IntLiteral(3)
                                                        ]
                                                    ), 
                                                ]
                                        ), 
                                        IntLiteral(4)
                                    )
                                )
                          )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_all_61(self):
        input = """
Var: i[123][1][2]={{1}, {2}};
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
For (i = 0, i < 10, i + 10.23) Do
    Var:a;
    If 5 + 2 == 3 Then 
        For (i = 0, i < 10, i + 10.23) Do
        Var:a;
        If 5 + 2 == 3 Then 
        EndIf.
        a = x +3;
        EndFor.
    EndIf.
    a = x +3;
EndFor.
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])])),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<',Id('i'), IntLiteral(10)),
                            BinaryOp('+',Id('i'),FloatLiteral(10.23)),
                            (
                                [VarDecl(Id('a'), [], None)],
                                [
                                    If
                                    ([
                                        (
                                        BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                                        [],
                                        [
                                            For(
                                                Id('i'),
                                                IntLiteral(0),
                                                BinaryOp('<',Id('i'), IntLiteral(10)),
                                                BinaryOp('+',Id('i'),FloatLiteral(10.23)),
                                                (
                                                    [VarDecl(Id('a'), [], None)],
                                                    [
                                                        If
                                                        ([
                                                            (
                                                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                                                            [

                                                            ],
                                                            []
                                                            )
                                                        ],
                                                            ([],[])
                                                        ),
                                                        Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))
                                                    ]
                                                )
                                            )
                                        ]
                                        )
                                    ],
                                        ([],[])
                                    ),
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))
                                ]
                            )
                        )

                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_all_62(self):
        input = """Var: x, y = 1, z = 3.5;
Var: t;
Var: sp, yz;
Function: you
Parameter: q , d[5]
Body:
Var: a = "string", b;
Var: c = False;
foo(a + c);
If (z == True) Then
    x = d[y *. z +. t -. c \ 10];
    Return 1;
ElseIf x != 4.e5 Then
    x = (a + b) * y - z + (sp *. yz);
Else
    Continue;
EndIf.
While (True)  Do    
    foo();
    goo(a);
    Break;                      
EndWhile.
For (i = 0, i < 10, -2) Do
    x = i;
EndFor.
EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],IntLiteral(1)),VarDecl(Id('z'),[],FloatLiteral(3.5)),VarDecl(Id('t'),[],None),VarDecl(Id('sp'),[],None),VarDecl(Id('yz'),[],None),FuncDecl(Id('you'),[VarDecl(Id('q'),[],None),VarDecl(Id('d'),[5],None)],([VarDecl(Id('a'),[],StringLiteral("""string""")),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],BooleanLiteral('false'))],[CallStmt(Id('foo'),[BinaryOp('+',Id('a'),Id('c'))]),If([(BinaryOp('==',Id('z'),BooleanLiteral('true')),[],[Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Return(IntLiteral(1))]),(BinaryOp('!=',Id('x'),FloatLiteral(400000.0)),[],[Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),Id('b')),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz'))))])],([],[Continue()])),While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[]),CallStmt(Id('goo'),[Id('a')]),Break()])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-',IntLiteral(2)),([],[Assign(Id('x'),Id('i'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_all_63(self):
        input = """
        Var: i[123][1][2]={{2,3,4},{4,5,6}};
        Function: main
        Parameter: a, b
        Body:
        Var: r = 10., v;
        If 5 + 2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        Else
            Var:a;
            a = x +3;
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('i'),[123,1,2],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))])],([VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_all_64(self):
        input = """
        Var: i[123][1][2]={{2,3,4},{4,5,6}};
        Function: main
        Parameter: a, b
        Body:
        Var: r = 10., v;
        If 5 + 2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('i'),[123,1,2],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_all_65(self):
        input = """
            Var: i[123][1][2]={{2,3,4},{4,5,6}};
            Function: main
            Parameter: a, b
            Body:
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
            Var: r = 10., v;
            If 5 + 2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            ElseIf 5+2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            ElseIf 5+2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            Else
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            EndIf.
            EndBody.
            """
        expect = Program([VarDecl(Id('i'),[123,1,2],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[10],None),VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]),(BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))])],([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_all_66(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
            x = 10;
            printLn(x);
            Continue;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(5)),FuncDecl(Id('main'),[],([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[10],None)],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('printLn'),[Id('x')]),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_all_67(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
Function: test
** Day la comment
* Day cung la comment
* Comment luon 
* Day cung la comment nhung chua dong lai**
Body:
    Var: b[2][3] = {{2,3,4},{4,5,6}};
    Var: c, d = 6, e, f;
    Var: m, n[10];
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                        x = d[y *. z +. t -. c \ 10];
                        b[2][3] = {{2,3,4},{4,5,6}};
                        a[3 + foo(2)] = a[b [2][3]] + 4;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        x = foo(a[1][2] + 2, x + 1);
                        x = y + (z -q) *. 10;
                        x = n >=. z;
                        x = d[y *. z +. t -. c \ 10];
                        x = (a + - b) * y - z + (sp *. yz);
                        a = a + - 1 + - 5 - -5;
                        print("Hello World!");
                    ElseIf n >=. 8-.a Then
                        ** Day la comment
                        * Day cung la comment
                        * Comment luon 
                        * Day cung la comment nhung chua dong lai**
                        For (i = 0, i < 10, 2) Do
                            For (i = 0, i < 10, 2) Do
                                If((a > b) && (c < d)) Then
                                    Break;
                                EndIf. 
                                For (i = 0, i < 10, -2) Do         
                                    If((a == b) && (c < d)) Then
                                        Break;
                                    EndIf. 
                                EndFor.
                                print("Hello World!");
                            EndFor.
                        EndFor.
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                ** Day la comment**
                print("Hello World!");
            EndIf.
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                foo(a[1][2] + 2, x + 1);
                foo (2 + x, 4. \. y);
                goo ();
                If bool_of_string ("True") Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                    Do
                        Do
                            Do
                                print("Hello World!");
                            While a > b
                            EndDo.
                            print("Hello World!");
                        While a > b
                        EndDo.
                        print("Hello World!");
                    While a > b
                    EndDo.
                    foo(a[1][2] + 2, x + 1);
                    foo (2 + x, 4. \. y);
                    goo ();
                EndIf.
            EndWhile.
            ** *Day la comment**
            print("Hello World!");
        EndIf.
        For (i = 0, i < 10,  2) Do
            Return 1;
            Break;
            Continue;
            foo(float_of_int (a) + 2);
            goo(a+1);
        EndFor.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
        expect = Program([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[10],None),FuncDecl(Id('test'),[],([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[10],None)],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('!=',Id('n'),IntLiteral(10)),[],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>',Id('n'),IntLiteral(8)),[],[If([(BinaryOp('>',Id('n'),IntLiteral(10)),[],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))])),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r'))),Assign(Id('x'),CallExpr(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))])),Assign(Id('x'),BinaryOp('+',Id('y'),BinaryOp('*.',BinaryOp('-',Id('z'),Id('q')),IntLiteral(10)))),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z'))),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral(10)))])),Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),UnaryOp('-',Id('b'))),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz')))),Assign(Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))),UnaryOp('-',IntLiteral(5))),UnaryOp('-',IntLiteral(5)))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),(BinaryOp('>=.',Id('n'),BinaryOp('-.',IntLiteral(8),Id('a'))),[],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[If([(BinaryOp('&&',BinaryOp('>',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[Break()])],([],[])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),UnaryOp('-',IntLiteral(2)),([],[If([(BinaryOp('&&',BinaryOp('==',Id('a'),Id('b')),BinaryOp('<',Id('c'),Id('d'))),[],[Break()])],([],[]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")]),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),CallStmt(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\\.',FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[]),If([(CallExpr(Id('bool_of_string'),[StringLiteral("""True""")]),[],[Assign(Id('a'),CallExpr(Id('int_of_string'),[CallExpr(Id('read'),[])])),Assign(Id('b'),BinaryOp('+.',CallExpr(Id('float_of_int'),[Id('a')]),FloatLiteral(2.0))),Dowhile(([],[Dowhile(([],[Dowhile(([],[CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])]),BinaryOp('>',Id('a'),Id('b'))),CallStmt(Id('foo'),[BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp('+',Id('x'),IntLiteral(1))]),CallStmt(Id('foo'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\\.',FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[])])],([],[]))])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[Return(IntLiteral(1)),Break(),Continue(),CallStmt(Id('foo'),[BinaryOp('+',CallExpr(Id('float_of_int'),[Id('a')]),IntLiteral(2))]),CallStmt(Id('goo'),[BinaryOp('+',Id('a'),IntLiteral(1))])])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[])),CallStmt(Id('print'),[StringLiteral("""Hello World!""")])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))


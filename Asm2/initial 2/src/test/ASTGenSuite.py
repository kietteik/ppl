import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_vardec(self):
        """Simple program: int main() {} """
        input = """Var: a[0o123];"""
        expect = Program([VarDecl(Id("a"), [0o123], [])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_vardec_1(self):
        input = """Var:x, a;"""
        expect = str(
            Program([VarDecl(Id("x"), [], None), VarDecl(Id("a"), [], None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_vardec_2(self):
        input = """Var:x = 1, a;"""
        expect = str(
            Program([VarDecl(Id("x"), [], IntLiteral(1)), VarDecl(Id("a"), [], None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_vardec_3(self):
        input = """Var:x = True, a;"""
        expect = str(Program(
            [VarDecl(Id("x"), [], BooleanLiteral(True)), VarDecl(Id("a"), [], None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_vardec_4(self):
        input = """Var:x[10]= {1,2,3},a;"""
        expect = str(Program(
            [VarDecl(Id("x"), [10], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])), VarDecl(Id("a"), [], None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_vardec_5(self):
        input = """Var: m=12, n[10];"""
        expect = Program(
            [VarDecl(Id('m'), [], IntLiteral('12')), VarDecl(Id('n'), [10], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_vardec_6(self):
        input = """Var: n[10]={1,2,3}, a,b,c,d;"""
        expect = Program([VarDecl(Id('n'), [10], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(
            Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_vardec_7(self):
        input = """Var: n[10]={1,2,3}, a2[3],b123[123],c,d;"""
        expect = Program([VarDecl(Id('n'), [10], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(
            Id('a2'), [3], None), VarDecl(Id('b123'), [123], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_vardec_8(self):
        input = """Var: n[10][2]={{ 1},{2},{3}}, a,b,c,d;"""
        expect = Program([VarDecl(Id('n'), [10, 2], ArrayLiteral([ArrayLiteral([IntLiteral('1')]), ArrayLiteral([IntLiteral('2')]), ArrayLiteral(
            [IntLiteral('3')])])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_vardec_9(self):
        input = """Var: a[1],b[1],c[1],d[1];"""
        expect = Program([VarDecl(Id('a'), [1], None), VarDecl(
            Id('b'), [1], None), VarDecl(Id('c'), [1], None), VarDecl(Id('d'), [1], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_vardec_10(self):
        input = """Var: n[10][1][2][3]={1,2,3}, a,b,c,d;"""
        expect = Program([VarDecl(Id('n'), [10, 1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(
            Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_vardec_11(self):
        input = """Var: a[1],b[1],c[1],d[1];
        Var: a[1],b[1],c[1],d[1];"""
        expect = Program([VarDecl(Id('a'), [1], None), VarDecl(Id('b'), [1], None), VarDecl(Id('c'), [1], None), VarDecl(Id('d'), [
                         1], None), VarDecl(Id('a'), [1], None), VarDecl(Id('b'), [1], None), VarDecl(Id('c'), [1], None), VarDecl(Id('d'), [1], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_vardec_12(self):
        input = """Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;"""
        expect = Program([VarDecl(Id('qwe'), [1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [
        ], None), VarDecl(Id('qwe'), [1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_vardec_13(self):
        input = """Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;"""
        expect = Program([VarDecl(Id('qwe'), [1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(
            Id('qwe'), [1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None), VarDecl(Id('a'), [], IntLiteral('1'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_vardec_14(self):
        input = """Var:a=1;Var:a=1;Var:a=1;Var:a=1;Var:a=1;"""
        expect = Program([VarDecl(Id('a'), [], IntLiteral('1')), VarDecl(Id('a'), [], IntLiteral('1')), VarDecl(
            Id('a'), [], IntLiteral('1')), VarDecl(Id('a'), [], IntLiteral('1')), VarDecl(Id('a'), [], IntLiteral('1'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_vardec_15(self):
        input = """Var: n[10][1][2][3]={{123,2,3,4},{2},{3}};"""
        expect = Program([VarDecl(Id('n'), [10, 1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral('123'), IntLiteral(
            '2'), IntLiteral('3'), IntLiteral('4')]), ArrayLiteral([IntLiteral('2')]), ArrayLiteral([IntLiteral('3')]) ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    # FUNCTION TEST
    def test_funcdec_1(self):
        input = """Function: main
        Body:
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_funcdec_2(self):
        input = """Function: main
        Body:Var:a=1;
        EndBody."""
        expect = Program(
            [FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [], IntLiteral('1'))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_funcdec_3(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2], ArrayLiteral([IntLiteral('12'), IntLiteral(
            '3'), IntLiteral('4')])), VarDecl(Id('b'), [], IntLiteral('2')), VarDecl(Id('c'), [], BooleanLiteral('true'))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_funcdec_4(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2], ArrayLiteral([IntLiteral('12'), IntLiteral('3'), IntLiteral('4')])), VarDecl(
            Id('b'), [], IntLiteral('2')), VarDecl(Id('c'), [], BooleanLiteral('true')), VarDecl(Id('c'), [], IntLiteral('4'))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_funcdec_5(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        a=b+1;b=a==b;r=a+b+c-e-.d;
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2], ArrayLiteral([IntLiteral('12'), IntLiteral('3'), IntLiteral('4')])), VarDecl(Id('b'), [], IntLiteral('2')), VarDecl(Id('c'), [], BooleanLiteral('true')), VarDecl(Id('c'), [], IntLiteral(
            '4'))], [Assign(Id('a'), BinaryOp('+', Id('b'), IntLiteral('1'))), Assign(Id('b'), BinaryOp('==', Id('a'), Id('b'))), Assign(Id('r'), BinaryOp('-.', BinaryOp('-', BinaryOp('+', BinaryOp('+', Id('a'), Id('b')), Id('c')), Id('e')), Id('d')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_funcdec_6(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        a=b+1;b=a==b;r=a+b+c-e-.d;
        foo(foo((a+b+.12e10))+foo());
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2], ArrayLiteral([IntLiteral('12'), IntLiteral('3'), IntLiteral('4')])), VarDecl(Id('b'), [], IntLiteral('2')), VarDecl(Id('c'), [], BooleanLiteral('true')), VarDecl(Id('c'), [], IntLiteral('4'))], [Assign(Id('a'), BinaryOp('+', Id('b'), IntLiteral('1'))), Assign(
            Id('b'), BinaryOp('==', Id('a'), Id('b'))), Assign(Id('r'), BinaryOp('-.', BinaryOp('-', BinaryOp('+', BinaryOp('+', Id('a'), Id('b')), Id('c')), Id('e')), Id('d'))), CallStmt(Id('foo'), [BinaryOp('+', CallExpr(Id('foo'), [BinaryOp('+.', BinaryOp('+', Id('a'), Id('b')), FloatLiteral(12e10))]), CallExpr(Id('foo'), []))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_funcdec_7(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        EndBody.Function: foo
        Body:a=b+1;b=a==b;r=a+b+c-e-.d;
        foo((a+b+.12e10));EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('a'), [2], ArrayLiteral([IntLiteral('12'), IntLiteral('3'), IntLiteral('4')])), VarDecl(Id('b'), [], IntLiteral('2')), VarDecl(Id('c'), [], BooleanLiteral('true')), VarDecl(Id('c'), [], IntLiteral('4'))], [])), FuncDecl(Id('foo'), [], ([], [Assign(
            Id('a'), BinaryOp('+', Id('b'), IntLiteral('1'))), Assign(Id('b'), BinaryOp('==', Id('a'), Id('b'))), Assign(Id('r'), BinaryOp('-.', BinaryOp('-', BinaryOp('+', BinaryOp('+', Id('a'), Id('b')), Id('c')), Id('e')), Id('d'))), CallStmt(Id('foo'), [BinaryOp('+.', BinaryOp('+', Id('a'), Id('b')), FloatLiteral(12e10))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_funcdec_8(self):
        input = """Function: main
        Body:
        EndBody.
        Function: foo
        Body:
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([], [])),
                          FuncDecl(Id('foo'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_funcdec_9(self):
        input = """Function: main
        Body:
        EndBody.Function: main
        Body:
        EndBody.Function: main
        Body:
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([], [])), FuncDecl(
            Id('main'), [], ([], [])), FuncDecl(Id('main'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_funcdec_10(self):
        input = """
        Var: a = 5;Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;Var: m, n[10];
        Function: main
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = Program([VarDecl(Id('a'), [], IntLiteral('5')), VarDecl(Id('b'), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral('2'), IntLiteral('3'), IntLiteral('4')]), ArrayLiteral([IntLiteral('4'), IntLiteral('5'), IntLiteral('6')])])), VarDecl(
            Id('c'), [], None), VarDecl(Id('d'), [], IntLiteral('6')), VarDecl(Id('e'), [], None), VarDecl(Id('f'), [], None), VarDecl(Id('m'), [], None), VarDecl(Id('n'), [10], None), FuncDecl(Id('main'), [], ([], [])), FuncDecl(Id('main'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    # STATEMENT

    def test_param_1(self):
        input = """Function: abctest
        Parameter: n,a[2],b[5][6],m
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+.1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('abctest'), [VarDecl(Id('n'), [], None), VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [5, 6], None), VarDecl(Id('m'), [], None)], ([], [If([(BinaryOp('>', Id('n'), IntLiteral(
            '10')), [], [Return(IntLiteral('5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp('+.', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_elseif_1(self):
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            ElseIf n < 10 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)], ([], [If([(BinaryOp('>', Id('n'), IntLiteral('10')), [], [Return(IntLiteral('5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp(
            '+', Id('a'), IntLiteral('1'))), Return(Id('a'))]), (BinaryOp('<', Id('n'), IntLiteral('10')), [], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_elseif_2(self):
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [VarDecl(Id('n'), [], None)], ([], [If([(BinaryOp('>', Id('n'), IntLiteral('10')), [], [Return(IntLiteral('5'))]), (BinaryOp(
            '>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_param_0(self):
        input = """Function: abctest
        Parameter: n,a[2],b[5][6],m
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+.1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('abctest'), [VarDecl(Id('n'), [], None), VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [5, 6], None), VarDecl(Id('m'), [], None)], ([], [If([(BinaryOp('>', Id('n'), IntLiteral(
            '10')), [], [Return(IntLiteral('5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp('+.', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_ifelse_1(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            Var:b,c,d;
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('abctest'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [5, 6], None)], ([VarDecl(Id('b'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)], [If([(BinaryOp(
            '>', Id('n'), IntLiteral('10')), [], [Return(IntLiteral('5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_ifelse_2(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('abctest'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [5, 6], None)], ([VarDecl(Id('b'), [], None)], [If([(BinaryOp('>', Id('n'), IntLiteral('10')), [], [Return(
            IntLiteral('5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_ifelse_3(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            Var:c=2;
            If n > 10 Then
                Return 5;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('abctest'),[VarDecl(Id('a'),[2],None),VarDecl(Id('b'),[5,6],None)],([VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],IntLiteral('2'))],[If([(BinaryOp('>',Id('n'),IntLiteral('10')),[],[Return(IntLiteral('5'))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_param_2(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('abctest'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [5, 6], None)], ([], [If([(BinaryOp('>', Id('n'), IntLiteral('10')), [], [Return(IntLiteral(
            '5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_for_1(self):
        input = """Function: main
        Parameter: x
        Body:   For (a=5,a<10,aa+1) Do abc(a); EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [For(Id('a'), IntLiteral('5'), BinaryOp(
            '<', Id('a'), IntLiteral('10')), BinaryOp('+', Id('aa'), IntLiteral('1')), ([], [CallStmt(Id('abc'), [Id('a')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_for_2(self):
        input = """Function: main
        Parameter: x
        Body:
            For (a=5,a<10,a+.1) Do
                abc(a);
                For (a=2,a==0,a*1) Do
                    If ab==cd Then
                    a=a+1;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[For(Id('a'),IntLiteral('5'),BinaryOp('<',Id('a'),IntLiteral('10')),BinaryOp('+.',Id('a'),IntLiteral('1')),([],[CallStmt(Id('abc'),[Id('a')]),For(Id('a'),IntLiteral('2'),BinaryOp('==',Id('a'),IntLiteral('0')),BinaryOp('*',Id('a'),IntLiteral('1')),([],[If([(BinaryOp('==',Id('ab'),Id('cd')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_for_3(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
            writeln(i);
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [For(Id('i'), IntLiteral('0'), BinaryOp(
            '<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_for_4(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [
                         CallStmt(Id('writeln'), [Id('i')]), For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_for_5(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
                While (True) Do
                For (i = 0, i < 10, 2) Do
                Var:a=1;
                writeln(i);
                a=b;
                EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [While(BooleanLiteral('true'), ([], [
                         For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([VarDecl(Id('a'), [], IntLiteral('1'))], [CallStmt(Id('writeln'), [Id('i')]), Assign(Id('a'), Id('b'))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_for_6(self):
        input = """Function: main
        Body:
            Var:var=2;
            For (i = 0, i < 10, 2) Do
                While (True) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                    writeln(i);
                    EndFor.
                a=b;
                EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('var'), [], IntLiteral('2'))], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [While(BooleanLiteral('true'), ([], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')]), For(
            Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')]), For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')])])), CallStmt(Id('writeln'), [Id('i')])])), Assign(Id('a'), Id('b'))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_for_7(self):
        input = """Function: main
        Body:
            Var:var=2;
            For (i = 0, i < 10, 2) Do
                While (True) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                    writeln(i);
                    EndFor.
                a=b;
                EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('var'), [], IntLiteral('2'))], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [While(BooleanLiteral('true'), ([], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')]), For(
            Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')]), For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('writeln'), [Id('i')])])), CallStmt(Id('writeln'), [Id('i')])])), Assign(Id('a'), Id('b'))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_while_1(self):
        input = """Function: main
        Parameter: x
        Body:   While (True) Do
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BooleanLiteral('true'),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_while_2(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(c<=d)) Do
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('<=',Id('c'),Id('d'))),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_while_3(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_while_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_while_5(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),CallStmt(Id('writeln'),[Id('i')])])),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_while_6(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('writeln'),[Id('i')])])),CallStmt(Id('writeln'),[Id('i')])])),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_while_7(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                foo(a==1);
                EndWhile.
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('foo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('writeln'),[Id('i')])])),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_while_8(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                foo(a==1);
                EndWhile.
                writeln(i);
                EndWhile.
                EndFor.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('foo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('writeln'),[Id('i')])]))])),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_while_9(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                foo(a==1);
                EndWhile.
                writeln(i);
                EndWhile.
                EndFor.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('foo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('writeln'),[Id('i')])]))])),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_while_10(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                    While ((b>=a)==(b!=c)+d*a*b) Do
                    writeln(i);
                        While ((b>=a)==(b!=c)+d*a) Do
                        writeln(i);
                        foo(a==1);
                        EndWhile.
                    writeln(i);
                    EndWhile.
                EndFor.
                        While ((b>=a)==(b!=c)+d*a) Do
                        writeln(i);
                        foo(a==1);
                        EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')))),([],[CallStmt(Id('writeln'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('foo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('writeln'),[Id('i')])]))])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('foo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_dowhile_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_dowhile_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_dowhile_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3')))),CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_dowhile_4(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                While (True)
                EndDo.
                Do
                    writeln(i);
                    While (a==12+3)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BooleanLiteral('true')),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_dowhile_5(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Do
                    writeln(i);
                While (a==12+3)
                EndDo.
                Do
                    writeln(i);
                While (a==12+3)
                EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3')))),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_dowhile_6(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                            writeln(i);
                        Do
                        While (a==12+3)
                        EndDo.
                        While (a==12+3)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_dowhile_7(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                        While (True) Do
                        EndWhile.
                        Do
                        While (a==12+3)
                        EndDo.
                        While (a==12+3)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),While(BooleanLiteral('true'),([],[])),Dowhile(([],[]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_dowhile_8(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                        While (True) Do
                            Do
                            writeln(i);
                            While(True)
                            EndDo.
                        EndWhile.
                        Do
                        While (a==2+1)
                        EndDo.
                        While (a==2+1)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),While(BooleanLiteral('true'),([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BooleanLiteral('true'))])),Dowhile(([],[]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('2'),IntLiteral('1'))))]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('2'),IntLiteral('1'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_dowhile_9(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                        While (True) Do
                            writeln(i);
                        EndWhile.
                    While(True)
                    EndDo.
                    Do
                        writeln(i);
                    While (a==2+1)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),While(BooleanLiteral('true'),([],[CallStmt(Id('writeln'),[Id('i')])]))]),BooleanLiteral('true')),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('2'),IntLiteral('1'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_dowhile_10(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                            writeln(i);
                        Do
                        While ((a==b)==(c==d))
                        EndDo.
                        While ((a==b)==(d==d))
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),CallStmt(Id('writeln'),[Id('i')]),Dowhile(([],[]),BinaryOp('==',BinaryOp('==',Id('a'),Id('b')),BinaryOp('==',Id('c'),Id('d'))))]),BinaryOp('==',BinaryOp('==',Id('a'),Id('b')),BinaryOp('==',Id('d'),Id('d'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_break_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_break_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_break_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    Break;
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                Break;
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Dowhile(([],[Break(),CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3')))),CallStmt(Id('writeln'),[Id('i')]),Break()]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_break_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                If (a==2) Then
                Break;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Break()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_break_5(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Break;
                EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Break()])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_continue_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Continue;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Continue()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_continue_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Continue;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),Continue()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_continue_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    Continue;
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                Continue;
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Dowhile(([],[Continue(),CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3')))),CallStmt(Id('writeln'),[Id('i')]),Continue()]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_continue_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                If (a==2) Then
                Continue;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Continue()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_continue_5(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Continue;
                EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Continue()])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_return_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Return True;
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Return(BooleanLiteral('true')),Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_return_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Return True;
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),Return(BooleanLiteral('true')),Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_return_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    Return True;
                    Break;
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                Return True;
                Break;
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Dowhile(([],[Return(BooleanLiteral('true')),Break(),CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3')))),CallStmt(Id('writeln'),[Id('i')]),Return(BooleanLiteral('true')),Break()]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_return_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                If (a==2) Then
                Return True;
                Break;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(BooleanLiteral('true')),Break()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_return_5(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Return True;
                Break;
                EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(BooleanLiteral('true')),Break()])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_return_6(self):
        input = """Function: main
        Parameter: x
        Body:
                Return a+b+c==2;
                Do
                Continue;
                If (a==2) Then
                Return;
                Break;
                EndIf.
                While (True)
                EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Return(BinaryOp('==',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral('2'))),Dowhile(([],[Continue(),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(None),Break()])],([],[]))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_return_7(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                    writeln(i);
                    If (a==2) Then
                        Continue;
                    Else
                        Return a+b+c==2;
                        Break;
                    EndIf.
                While (True)
                EndDo.
                Return a+b+c==2;
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Continue()])],([],[Return(BinaryOp('==',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral('2'))),Break()]))]),BooleanLiteral('true')),Return(BinaryOp('==',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral('2')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_return_8(self):
        input = """Function: main
        Parameter: x
        Body:   Return;
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_return_9(self):
        input = """Function: main
        Parameter: x
        Body:   Return1+1;
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Return(BinaryOp('+',IntLiteral('1'),IntLiteral('1')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_return_10(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
                writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Continue;
                EndIf.
                EndFor.
                EndFor.
                Return1+1;
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Continue()])],([],[]))]))])),Return(BinaryOp('+',IntLiteral('1'),IntLiteral('1')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_comment_in_program_1(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"**"""
        expect = Program([VarDecl(Id('he'),[],StringLiteral('hello')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_comment_in_program_2(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"** Var: a[1] = {"bk","c","d"};"""
        expect = Program([VarDecl(Id('he'),[],StringLiteral('hello')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),VarDecl(Id('a'),[1],ArrayLiteral([StringLiteral('bk'),StringLiteral('c'),StringLiteral('d')]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_comment_in_program_3(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Declare variable**
        Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('he'),[],StringLiteral('hello')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))])),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_comment_in_program_4(self):
        input = """******Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment**"""
        expect = Program([VarDecl(Id('he'),[],StringLiteral('hello')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_comment_in_program_5(self):
        input = """******Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment****followed by a comment**"""
        expect = Program([VarDecl(Id('he'),[],StringLiteral('hello')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_funccall_0(self):
        input = """Function: main
        Parameter: x
        Body:   fooo((a+1));
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[BinaryOp('+',Id('a'),IntLiteral('1'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_funccall_1(self):
        input = """Function: main
        Parameter: x
        Body:   fooo((a+1));
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[BinaryOp('+',Id('a'),IntLiteral('1'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_funccall_2(self):
        input = """Function: main
        Parameter: x
        Body:   fooo((a+1)+True+abcd);
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[BinaryOp('+',BinaryOp('+',BinaryOp('+',Id('a'),IntLiteral('1')),BooleanLiteral('true')),Id('abcd'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_funccall_3(self):
        input = """Function: main
        Parameter: x
        Body:   fooo("this is a string param","and second string");
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[StringLiteral('this is a string param'),StringLiteral('and second string')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_funccall_4(self):
        input = """Function: main
        Parameter: x
        Body:   fooo("this is a string param",funct("string",12));
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[StringLiteral('this is a string param'),CallExpr(Id('funct'),[StringLiteral('string'),IntLiteral('12')])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_funccall_5(self):
        input = """Function: main
        Parameter: x
        Body:   fooo(fucn1(func2(func3("string",{1,2,3},{{23},{1,3,4}}))),"and second string");
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[CallExpr(Id('fucn1'),[CallExpr(Id('func2'),[CallExpr(Id('func3'),[StringLiteral('string'),ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')]),ArrayLiteral([ArrayLiteral([IntLiteral('23')]),ArrayLiteral([IntLiteral('1'),IntLiteral('3'),IntLiteral('4')])])])])]),StringLiteral('and second string')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_funccall_6(self):
        input = """Function: main
        Parameter: x
        Body:   fooo();
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('fooo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_assignment_1(self):
        input = """Function: main
        Parameter: x
        Body:   a=12;a[2][3][4]={1,2,34};
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('a'),IntLiteral('12')),Assign(ArrayCell(Id('a'),[IntLiteral('2'),IntLiteral('3'),IntLiteral('4')]),ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('34')]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_assignment_2(self):
        input = """Function: main
        Parameter: x
        Body:   a=12;a[2][3][4]=2;
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('a'),IntLiteral('12')),Assign(ArrayCell(Id('a'),[IntLiteral('2'),IntLiteral('3'),IntLiteral('4')]),IntLiteral('2'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_assignment_3(self):
        input = """Function: main
        Parameter: x
        Body:   a="string string";
                b=foo();
                c[1]=foo(foo());
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('a'),StringLiteral('string string')),Assign(Id('b'),CallExpr(Id('foo'),[])),Assign(ArrayCell(Id('c'),[IntLiteral('1')]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_ast_1(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable**
        Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                If (a==2) Then
                Return True;
                Break;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody.
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('he'),[],StringLiteral("""hello""")),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('a'),[],IntLiteral('1')),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true')),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(BooleanLiteral('true')),Break()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_ast_2(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable**
        Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                    writeln(i);
                    If (a==2) Then
                        Return True;
                        If n > 10 Then
                            Return 5;
                        ElseIf n >5 Then a=a+1; Return a;
                        ElseIf n < 10 Then a=a+1; Return a;
                        ElseIf n < 100 Then a=a+1; Return b;
                        Else
                            Return False;
                        EndIf.
                        Break;
                    EndIf.
                    While ((b>=a)==(b!=c)+d*a*b*c) Do
                        writeln(i);
                        If n > 10 Then
                            Return 5;
                        ElseIf n >5 Then a=a+1; Return a;
                        ElseIf n < 10 Then a=a+1; Return a;
                        Else
                            Return False;
                        EndIf.
                    EndWhile.
                EndWhile.
        EndBody.
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('he'),[],StringLiteral("""hello""")),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('a'),[],IntLiteral('1')),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true')),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(BooleanLiteral('true')),If([(BinaryOp('>',Id('n'),IntLiteral('10')),[],[Return(IntLiteral('5'))]),(BinaryOp('>',Id('n'),IntLiteral('5')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1'))),Return(Id('a'))]),(BinaryOp('<',Id('n'),IntLiteral('10')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1'))),Return(Id('a'))]),(BinaryOp('<',Id('n'),IntLiteral('100')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1'))),Return(Id('b'))])],([],[Return(BooleanLiteral('false'))])),Break()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('>',Id('n'),IntLiteral('10')),[],[Return(IntLiteral('5'))]),(BinaryOp('>',Id('n'),IntLiteral('5')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1'))),Return(Id('a'))]),(BinaryOp('<',Id('n'),IntLiteral('10')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1'))),Return(Id('a'))])],([],[Return(BooleanLiteral('false'))]))]))]))])),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_ast_3(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable******
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Function: main
        Parameter: x
        Body:   a="string string \\n \\t *commetn****unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        EndBody.
        Function: main2
        Parameter: x,a[2],b[2][3]
        **comment**
        Body:   a="string string'"'" ***unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        **comment**
        EndBody.
        **comment**
        """
        expect = Program([VarDecl(Id('he'),[],StringLiteral("""hello""")),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('a'),[],IntLiteral('1')),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('a'),StringLiteral("""string string \\n \\t *commetn****unclosing comment""")),Assign(Id('b'),CallExpr(Id('foo'),[])),Assign(ArrayCell(Id('c'),[IntLiteral('1')]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[])]))])),FuncDecl(Id('main2'),[VarDecl(Id('x'),[],None),VarDecl(Id('a'),[2],None),VarDecl(Id('b'),[2,3],None)],([],[Assign(Id('a'),StringLiteral("""string string'"'" ***unclosing comment""")),Assign(Id('b'),CallExpr(Id('foo'),[])),Assign(ArrayCell(Id('c'),[IntLiteral('1')]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_ast_4(self):
        input = """
        Var: he = "hello\\t\\n\\b\\t\\\\abce***string{}{}{2,3,4,}}'"string in string'"";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable******
        Function: main
        **Declare variable******
        Parameter: x
        Body:   a="string string";
                x=n >=.z;
                x=d[y *.z +. t -.c\ 10];
                x=(a + -b) * y -z+ (sp *. yz);
                a=a + -1 + - 5--5;
        **Declare variable******
                b=foo();
                c[1]=foo(foo());
        EndBody.
        **Declare variable******
        Function: main2
        Parameter: x,a[2],b[2][3]
        **comment**
        Body:   a="string string'"'" ***unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        **comment**
        EndBody.
        **comment**"""
        expect = Program([VarDecl(Id('he'),[],StringLiteral("hello\\t\\n\\b\\t\\\\abce***string{}{}{2,3,4,}}\'\"string in string\'\"")),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),VarDecl(Id('qwe'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('a'),[],IntLiteral('1')),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('a'),StringLiteral("string string")),Assign(Id('x'),BinaryOp('>=.',Id('n'),Id('z'))),Assign(Id('x'),ArrayCell(Id('d'),[BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('y'),Id('z')),Id('t')),BinaryOp('\\',Id('c'),IntLiteral('10')))])),Assign(Id('x'),BinaryOp('+',BinaryOp('-',BinaryOp('*',BinaryOp('+',Id('a'),UnaryOp('-',Id('b'))),Id('y')),Id('z')),BinaryOp('*.',Id('sp'),Id('yz')))),Assign(Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral('1'))),UnaryOp('-',IntLiteral('5'))),UnaryOp('-',IntLiteral('5')))),Assign(Id('b'),CallExpr(Id('foo'),[])),Assign(ArrayCell(Id('c'),[IntLiteral('1')]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[])]))])),FuncDecl(Id('main2'),[VarDecl(Id('x'),[],None),VarDecl(Id('a'),[2],None),VarDecl(Id('b'),[2,3],None)],([],[Assign(Id('a'),StringLiteral("""string string'"'" ***unclosing comment""")),Assign(Id('b'),CallExpr(Id('foo'),[])),Assign(ArrayCell(Id('c'),[IntLiteral('1')]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_ast_5(self):
        input = """Function: main
        Body:
            Var:var=2;
            For (i = 0, i < 10, 2) Do
                While (True) Do
                    For (i = 0, i < 10, 2) Do
                        writeln(i);
                        For (i = 0, i < 10, 2) Do
                            writeln(i);
                            For (i = 0, i < 10, 2) Do
                            writeln(i);
                            EndFor.
                            writeln(i);
                        EndFor.
                        a=b;
                    EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = Program(
            [FuncDecl(
                Id("main"),
                [],
                ([VarDecl(Id("var"), [], IntLiteral(2))],
                 [
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        IntLiteral(2),
                        ([], [
                            While(
                                BooleanLiteral("True"),
                                ([], [
                                    For(
                                        Id("i"),
                                        IntLiteral(0),
                                        BinaryOp("<", Id("i"), IntLiteral(10)),
                                        IntLiteral(2),
                                        ([], [
                                            CallStmt(Id("writeln"), [Id("i")]),
                                            For(
                                                Id("i"),
                                                IntLiteral(0),
                                                BinaryOp("<", Id("i"),
                                                         IntLiteral(10)),
                                                IntLiteral(2),
                                                ([], [
                                                    CallStmt(
                                                        Id("writeln"), [Id("i")]),
                                                    For(
                                                        Id("i"),
                                                        IntLiteral(0),
                                                        BinaryOp(
                                                            "<", Id("i"), IntLiteral(10)),
                                                        IntLiteral(2),
                                                        ([], [
                                                            CallStmt(
                                                                Id("writeln"), [Id("i")])
                                                        ])
                                                    ),
                                                    CallStmt(
                                                        Id("writeln"), [Id("i")]),
                                                ])
                                            ),
                                            Assign(Id("a"), Id("b"))
                                        ])
                                    )
                                ])
                            )
                        ])
                    )
                ])
            )]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

    
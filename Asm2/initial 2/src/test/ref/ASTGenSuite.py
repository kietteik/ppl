import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_var_dec_1(self):
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_var_dec_2(self):
        input = """Var:x=2;"""
        expect = Program([VarDecl(Id("x"), [], IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_var_dec_3(self):
        input = """Var:x=5;"""
        expect = Program([VarDecl(Id("x"), [], IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_var_dec_4(self):
        input = """Var:x=False;"""
        expect = Program([VarDecl(Id("x"), [], BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_var_dec_5(self):
        input = """Var:x[2][3]={{2,3},{3,4}};"""
        expect = Program([VarDecl(Id("x"), [2, 3], ArrayLiteral([ArrayLiteral(
            [IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_var_dec_6(self):
        input = """Var:x[1][2]={{True,False},{2.0,4.1}};"""
        expect = Program([VarDecl(Id("x"), [1, 2], ArrayLiteral([ArrayLiteral([BooleanLiteral(
            True), BooleanLiteral(False)]), ArrayLiteral([FloatLiteral(2.0), FloatLiteral(4.1)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_var_dec_7(self):
        input = """
        Var:x[2]={2,3};
        Var: a,b,c=4;
        """
        expect = Program([VarDecl(Id("x"), [2], ArrayLiteral([IntLiteral(2), IntLiteral(3)])), VarDecl(
            Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], IntLiteral(4))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_var_dec_8(self):
        input = """
        Var: c, d = 6, e, f = "abcdef";
        """
        expect = Program([VarDecl(Id('c'), [], []), VarDecl(Id('d'), [], IntLiteral(
            6)), VarDecl(Id('e'), [], []), VarDecl(Id('f'), [], StringLiteral('abcdef'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_var_dec_9(self):
        input = """
        Var:x[1][2]={{"hotinbk"},{False,True}};
        Var: a,b,c=4;
        """
        expect = Program([VarDecl(Id('x'), [1, 2], ArrayLiteral([ArrayLiteral([StringLiteral('hotinbk')]), ArrayLiteral([
            BooleanLiteral(False), BooleanLiteral(True)])])), VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], []), VarDecl(Id('c'), [], IntLiteral(4))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_var_dec_10(self):
        input = """
        Var: a, b=1;
        Var: c[1]={2}, d;
        Var: e;
        """
        expect = Program([VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], IntLiteral(1)), VarDecl(
            Id('c'), [1], ArrayLiteral([IntLiteral(2)])), VarDecl(Id('d'), [], []), VarDecl(Id('e'), [], [])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_func_dec_1(self):
        input = """
        Function: foo
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_func_dec_2(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id('foo'), [VarDecl(Id('a'), [5], []), VarDecl(Id('b'), [], [])], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_func_dec_3(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            a = b;
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], [])], ([], [Assign(Id('a'), Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_func_dec_4(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], [])], ([], [Assign(
            Id('b'), ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)])), Assign(Id('a'), Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_func_dec_5(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        Function: main
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], [])], ([], [Assign(Id('b'), ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)])), Assign(Id('a'), Id('b'))])), FuncDecl(
            Id('main'), [VarDecl(Id('c'), [], []), VarDecl(Id('d'), [], [])], ([], [Assign(ArrayCell(Id('c'), [IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(2)])), Assign(Id('d'), FloatLiteral(20.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_func_dec_6(self):
        input = """
        Var: a = 1.2e-3;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        Function: goo
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = Program([VarDecl(Id('a'), [], FloatLiteral(0.0012)), VarDecl(Id('b'), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], [])], ([], [Assign(
            Id('b'), ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)])), Assign(Id('a'), Id('b'))])), FuncDecl(Id('goo'), [VarDecl(Id('c'), [], []), VarDecl(Id('d'), [], [])], ([], [Assign(ArrayCell(Id('c'), [IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(2)])), Assign(Id('d'), FloatLiteral(20.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_func_dec_7(self):
        input = """
        Var: a = 1.2e-3;
        Function: foo
        Parameter: a, b
        Body:
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            b = a[2][1];
            a = b;
        EndBody.
        Function: goo
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = Program([
            VarDecl(Id('a'), [], FloatLiteral(0.0012)),
            FuncDecl(
                Id('foo'),
                [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], [])],
                (
                    [
                        VarDecl(Id('b'), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(
                            3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))
                    ],
                    [
                        Assign(Id('b'), ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)])), Assign(
                            Id('a'), Id('b'))
                    ]
                )
            ),
            FuncDecl(
                Id('goo'),
                [VarDecl(Id('c'), [], []), VarDecl(Id('d'), [], [])],
                (
                    [],
                    [
                        Assign(ArrayCell(Id('c'), [IntLiteral(2)]), ArrayLiteral(
                            [IntLiteral(3), IntLiteral(2)])),
                        Assign(Id('d'), FloatLiteral(20.0))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_expression_1(self):
        input = """
        Function: foo
        Body:
            a = a > b;
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [Assign(Id('a'), BinaryOp('>', Id('a'), Id('b')))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_expression_2(self):
        input = """
        Function: foo
        Body:
            a = a && b > c;
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp('>', BinaryOp(
                                '&&', Id('a'), Id('b')), Id('c'))
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_expression_3(self):
        input = """
        Function: foo
        Body:
            a = a && b > c + d;
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '>',
                                BinaryOp('&&', Id('a'), Id('b')),
                                BinaryOp('+', Id('c'), Id('d'))
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_expression_4(self):
        input = """
        Function: foo
        Body:
            a = a && b > c + d*e;
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '>',
                                BinaryOp('&&', Id('a'), Id('b')),
                                BinaryOp(
                                    '+',
                                    Id('c'),
                                    BinaryOp('*', Id('d'), Id('e'))
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_expression_5(self):
        input = """
        Function: foo
        Body:
            a = !-a && b > c + d*e;
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            BinaryOp(
                                '>',
                                BinaryOp(
                                    '&&',
                                    UnaryOp('!', UnaryOp('-', Id('a'))),
                                    Id('b')
                                ),
                                BinaryOp(
                                    '+',
                                    Id('c'),
                                    BinaryOp('*', Id('d'), Id('e'))
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_expression_6(self):
        input = """
        Function: foo
        Body:
            a = foo(a[1][2]);
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            CallExpr(
                                Id('foo'),
                                [
                                    ArrayCell(
                                        Id('a'),
                                        [IntLiteral(1), IntLiteral(2)]
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_expression_7(self):
        input = """
        Function: foo
        Body:
            a = foo(a[1][2]*3.2e-3 + {{2},{2}} +goo());
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Assign(
                            Id('a'),
                            CallExpr(
                                Id('foo'),
                                [
                                    BinaryOp(
                                        '+',
                                        BinaryOp(
                                            '+',
                                            BinaryOp(
                                                '*',
                                                ArrayCell(
                                                    Id('a'),
                                                    [IntLiteral(
                                                        1), IntLiteral(2)]
                                                ),
                                                FloatLiteral(0.0032)
                                            ),
                                            ArrayLiteral(
                                                [ArrayLiteral([IntLiteral(2)]), ArrayLiteral(
                                                    [IntLiteral(2)])]
                                            )
                                        ),
                                        CallExpr(Id('goo'), [])
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_expression_8(self):
        input = """
        Function: foo
        Body:
            a = (a*2.e3 > 4 + 5)\\.b*.d -. f;
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'), [], ([], [Assign(Id('a'), BinaryOp('-.', BinaryOp('*.', BinaryOp('\.', BinaryOp(
            '>', BinaryOp('*', Id('a'), FloatLiteral(2000.0)), BinaryOp('+', IntLiteral(4), IntLiteral(5))), Id('b')), Id('d')), Id('f')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_if_1(self):
        input = """
        Function: foo
        Body:
            If a < b Then
                While True Do
                    foo(a,b);
                EndWhile.
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        If(
                            [
                                (
                                    BinaryOp('<', Id('a'), Id('b')),
                                    [],
                                    [
                                        While(
                                            BooleanLiteral(True), ([], [CallStmt(
                                                Id('foo'), [Id('a'), Id('b')])])
                                        )
                                    ]
                                )
                            ],
                            []
                        ),

                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_if_2(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                While True Do
                    foo(a,b);
                EndWhile.
            Else
                Return a;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        If(
                            [(
                                BinaryOp('&&', Id('a'), Id('b')),
                                [],
                                [
                                    While(
                                        BooleanLiteral(True), ([], [CallStmt(
                                            Id('foo'), [Id('a'), Id('b')])])
                                    )
                                ]
                            )],
                            ([], [Return(Id('a'))])
                        ),
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_if_3(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                While True Do
                    foo(a,b);
                EndWhile.
            ElseIf a != b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
            Else
                Return a;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        If(
                            [
                                (BinaryOp('&&', Id('a'), Id('b')), [], [
                                 While(BooleanLiteral(True), ([], [CallStmt(Id('foo'), [Id('a'), Id('b')])]))]),
                                (BinaryOp('!=', Id('a'), Id('b')), [], [For(Id('i'), IntLiteral(1), BinaryOp('<', Id(
                                    'i'), IntLiteral(10)), IntLiteral(2), ([], [CallStmt(Id('foo'), [Id('b'), Id('a')])]))])
                            ],
                            ([], [Return(Id('a'))])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_if_4(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                a=b;
            ElseIf a != b Then
                c=d;
            ElseIf a == b Then
                e=f;
            Else
                g=h;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        If(
                            [(BinaryOp('&&', Id('a'), Id('b')), [], [
                                Assign(Id('a'), Id('b'))]),
                             (BinaryOp('!=', Id('a'), Id('b')),
                              [], [Assign(Id('c'), Id('d'))]),
                             (BinaryOp('==', Id('a'), Id('b')),
                              [], [Assign(Id('e'), Id('f'))]),
                             ],
                            ([], [Assign(Id('g'), Id('h'))])
                        ),
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_if_5(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                If a == (b + 1) Then
                    foo(b,a);
                ElseIf a == b Then
                    a = b > c;
                Else
                    Return a;
                EndIf.
            ElseIf a != b Then
                e=f;
            ElseIf a == b Then
                g=h;
            Else
                Return g;
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        If(
                            [
                                (BinaryOp('&&', Id('a'), Id('b')), [], [If([(BinaryOp('==', Id('a'), BinaryOp('+', Id('b'), IntLiteral(1))), [], [CallStmt(Id('foo'), [
                                 Id('b'), Id('a')])]), (BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), BinaryOp('>', Id('b'), Id('c')))])], ([], [Return(Id('a'))])), ]),
                                (BinaryOp('!=', Id('a'), Id('b')),
                                    [], [Assign(Id('e'), Id('f'))]),
                                (BinaryOp('==', Id('a'), Id('b')),
                                 [], [Assign(Id('g'), Id('h'))])
                            ],
                            ([], [Return(Id('g'))])
                        ),



                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_if_6(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                If a == (b + 1) Then
                    foo(b,a);
                ElseIf a == b Then
                    a=b;
                Else
                    Return a;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        If(
                            [
                                (
                                    BinaryOp('&&', Id('a'), Id('b')),
                                    [],
                                    [
                                        If(
                                            [
                                                (BinaryOp('==', Id('a'), BinaryOp('+', Id('b'), IntLiteral(1))), [], [CallStmt(Id('foo'), [Id('b'), Id(
                                                    'a')])]),
                                                (BinaryOp('==', Id('a'), Id('b')), [], [Assign(Id('a'), Id('b'))])],
                                            ([], [Return(Id('a'))])
                                        )
                                    ]
                                )
                            ],
                            []
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_for_1(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<', Id('i'), IntLiteral(10)),
                            IntLiteral(2),
                            ([], [CallStmt(Id('writeln'), [Id('i')])])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_for_2(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                For (j = 0, j < 10, 1) Do
                    writeln(i);
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<', Id('i'),
                                     IntLiteral(10)),
                            IntLiteral(1),
                            ([],
                             [
                                For(
                                    Id('j'),
                                    IntLiteral(0),
                                    BinaryOp('<', Id('j'),
                                             IntLiteral(10)),
                                    IntLiteral(1),
                                    ([], [CallStmt(Id('writeln'), [Id('i')])]))
                            ])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_for_3(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                For (j = 0, j < 10, 1) Do
                    writeln(i);
                    If a && b Then
                        While True Do
                            foo(a,b);
                        EndWhile.
                    Else
                        Return a;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<', Id('i'), IntLiteral(10)),
                            IntLiteral(1),
                            ([],
                             [
                                For(
                                    Id('j'),
                                    IntLiteral(0),
                                    BinaryOp('<', Id('j'), IntLiteral(10)),
                                    IntLiteral(1),
                                    ([],
                                     [
                                        CallStmt(Id('writeln'), [Id('i')]),
                                        If(
                                            [
                                                (
                                                    BinaryOp(
                                                        '&&', Id('a'), Id('b')),
                                                    [],
                                                    [
                                                        While(BooleanLiteral(True), ([], [
                                                              CallStmt(Id('foo'), [Id('a'), Id('b')])]))
                                                    ]
                                                )
                                            ],
                                            ([], [Return(Id('a'))]
                                             )
                                        )
                                    ])
                                )
                            ])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_for_4(self):
        input = """
        Function: foo
        Body:
            For (i = 0, a*.b\\.c+.d-.e=/=f , goo(g,h)) Do
                For (j = 0, j < 10, 1) Do
                    writeln(i);
                    If a && b Then
                        While True Do
                            foo(a,b);
                        EndWhile.
                    Else
                        Return a;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('=/=', BinaryOp('-.', BinaryOp('+.', BinaryOp('\.', BinaryOp(
                                '*.', Id('a'), Id('b')), Id('c')), Id('d')), Id('e')), Id('f')),
                            CallExpr(Id('goo'), [Id('g'), Id('h')]),
                            ([],
                             [
                                For(
                                    Id('j'),
                                    IntLiteral(0),
                                    BinaryOp('<', Id('j'), IntLiteral(10)),
                                    IntLiteral(1),
                                    ([],
                                     [
                                        CallStmt(Id('writeln'), [Id('i')]),
                                        If(
                                            [
                                                (
                                                    BinaryOp(
                                                        '&&', Id('a'), Id('b')),
                                                    [],
                                                    [
                                                        While(BooleanLiteral(True), ([], [
                                                              CallStmt(Id('foo'), [Id('a'), Id('b')])]))
                                                    ]
                                                )
                                            ],
                                            ([], [Return(Id('a'))]
                                             )
                                        )
                                    ])
                                )
                            ])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_for_5(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                foo(a,b);
                fun2(d,e);
                fun3(f,g);
            EndFor.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<', Id('i'), IntLiteral(10)),
                            IntLiteral(1),
                            ([],
                             [
                                CallStmt(Id('foo'), [Id('a'), Id('b')]),
                                CallStmt(Id('fun2'), [Id('d'), Id('e')]),
                                CallStmt(Id('fun3'), [Id('f'), Id('g')])
                            ])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_for_6(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do

            EndFor.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<', Id('i'), IntLiteral(10)),
                            IntLiteral(1),
                            ([], [])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_while_1(self):
        input = """
        Function: foo
        Body:
            While True Do
                doThis();
            EndWhile.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        While(
                            BooleanLiteral(True),
                            ([],
                             [CallStmt(Id('doThis'), [])])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_while_2(self):
        input = """
        Function: foo
        Body:
            While True Do
                doThis();
                doThat();
                While (a+b|| g) Do
                    doOtherThings();
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        While(
                            BooleanLiteral(True),
                            ([],
                             [
                                CallStmt(Id('doThis'), []),
                                CallStmt(Id('doThat'), []),
                                While(
                                    BinaryOp('||', BinaryOp(
                                        '+', Id('a'), Id('b')), Id('g')),
                                    ([],
                                     [CallStmt(Id('doOtherThings'), [])])
                                )
                            ])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_while_3(self):
        input = """
        Function: foo
        Body:
            While True Do
            
            EndWhile.
        EndBody."""
        expect = Program(
            [FuncDecl(Id('foo'), [], ([], [While(BooleanLiteral(True), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_do_while_1(self):
        input = """
        Function: foo
        Body:
            Do
                doOtherThings();
            While a > b
            EndDo.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Dowhile(
                            ([], [CallStmt(Id('doOtherThings'), [])]),
                            BinaryOp('>', Id('a'), Id('b'))
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_do_while_2(self):
        input = """
        Function: foo
        Body:
            Do
                doOtherThings();
                Do
                    doThat();
                While c > d
                EndDo.
            While a > b
            EndDo.
        EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [],
                (
                    [],
                    [
                        Dowhile(
                            ([],
                             [
                                CallStmt(Id('doOtherThings'), []),
                                Dowhile(
                                    ([], [CallStmt(Id('doThat'), [])]), BinaryOp('>', Id('c'), Id('d')))
                            ]),
                            BinaryOp('>', Id('a'), Id('b'))
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_do_while_3(self):
        input = """
        Function: foo
        Body:
            Do
                
            While e > f
            EndDo.
            Do
                doOtherThings();
                Do
                    doThat();
                While c > d
                EndDo.
            While a > b
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('foo'), [], ([], [Dowhile(([], []), BinaryOp('>', Id('e'), Id('f'))), Dowhile(([], [CallStmt(
            Id('doOtherThings'), []), Dowhile(([], [CallStmt(Id('doThat'), [])]), BinaryOp('>', Id('c'), Id('d')))]), BinaryOp('>', Id('a'), Id('b')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_full_1(self):
        input = """Function: foo
                Parameter: a,b,c
                Body:
                    If a < b Then
                        While True Do
                            foo(a,b);
                        EndWhile.
                    ElseIf a == b Then
                        For (i = 1, i < 10, 1) Do
                            foo(b,a);
                        EndFor.
                    Else
                        Return a;
                    EndIf.
                EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [VarDecl(Id('a'), [], []), VarDecl(
                    Id('b'), [], []), VarDecl(Id('c'), [], [])],
                (
                    [],
                    [
                        If([(BinaryOp('<', Id('a'), Id('b')), [], [While(BooleanLiteral(True), ([], [CallStmt(Id('foo'), [Id('a'), Id('b')])]))]), (BinaryOp('==', Id('a'), Id('b')), [], [
                           For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [CallStmt(Id('foo'), [Id('b'), Id('a')])]))])], ([], [Return(Id('a'))]))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_full_2(self):
        input = """Function: foo
                    Parameter: a,b,c
                    Body:
                        If a < b Then
                            While True Do
                                foo(a,b);
                            EndWhile.
                        ElseIf a == b Then
                            For (i = 1, i < 10, 1) Do
                                foo(b,a);
                            EndFor.
                        Else
                            Return a;
                        EndIf.
                    EndBody."""
        expect = Program([
            FuncDecl(
                Id('foo'),
                [VarDecl(Id('a'), [], []), VarDecl(
                    Id('b'), [], []), VarDecl(Id('c'), [], [])],
                (
                    [],
                    [
                        If([(BinaryOp('<', Id('a'), Id('b')), [], [While(BooleanLiteral(True), ([], [CallStmt(Id('foo'), [Id('a'), Id('b')])]))]), (BinaryOp('==', Id('a'), Id('b')), [], [
                           For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [CallStmt(Id('foo'), [Id('b'), Id('a')])]))])], ([], [Return(Id('a'))]))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_full_3(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do
                        foo(boo(10));
                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], []), VarDecl(Id('c'), [], [])], ([], [If([(BinaryOp('<', Id('a'), Id('b')), [], [While(BooleanLiteral(True), ([], [CallStmt(Id('foo'), [Id('a'), Id('b')])]))]), (BinaryOp('==', Id('a'), Id('b')), [], [For(
            Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [CallStmt(Id('foo'), [Id('b'), Id('a')])]))])], ([], [Dowhile(([], [CallStmt(Id('foo'), [CallExpr(Id('boo'), [IntLiteral(10)])])]), BinaryOp('<=.', Id('a'), FloatLiteral(10.0)))])), ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_full_4(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do

                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], []), VarDecl(Id('c'), [], [])], ([], [If([(BinaryOp('<', Id('a'), Id('b')), [], [While(BooleanLiteral(True), ([], []))]), (BinaryOp('==', Id('a'), Id('b')), [], [
                         For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [CallStmt(Id('foo'), [Id('b'), Id('a')])]))])], ([], [Dowhile(([], []), BinaryOp('<=.', Id('a'), FloatLiteral(10.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_full_5(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    Var: a=1;
                    While True Do
                        
                    EndWhile.
                ElseIf a == b Then
                    Var: b=2;
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Var: x=2;
                    Var: y[2]={1,2}, z;
                    Do

                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], []), VarDecl(Id('c'), [], [])], ([], [If([(BinaryOp('<', Id('a'), Id('b')), [VarDecl(Id('a'), [], IntLiteral(1))], [While(BooleanLiteral(True), ([], []))]), (BinaryOp('==', Id('a'), Id('b')), [VarDecl(Id('b'), [], IntLiteral(2))], [For(
            Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [CallStmt(Id('foo'), [Id('b'), Id('a')])]))])], ([VarDecl(Id('x'), [], IntLiteral(2)), VarDecl(Id('y'), [2], ArrayLiteral([IntLiteral(1), IntLiteral(2)])), VarDecl(Id('z'), [], [])], [Dowhile(([], []), BinaryOp('<=.', Id('a'), FloatLiteral(10.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_full_6(self):
        input = """Function: foo
                Parameter: a,b,c
                Body:
                    a = b;
                    b = a;
                    a = 1 + b;
                    If a < b Then
                        While True Do
                            foo(foo(foo()));
                        EndWhile.
                    ElseIf a == b Then
                        For (i = 1, i < 10, 1) Do
                            While True Do
                                foo(foo(foo()));
                            EndWhile.
                        EndFor.
                    Else
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5)
                        EndDo.
                    EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], []), VarDecl(Id('c'), [], [])], ([], [Assign(Id('a'), Id('b')), Assign(Id('b'), Id('a')), Assign(Id('a'), BinaryOp('+', IntLiteral(1), Id('b'))), If([(BinaryOp('<', Id('a'), Id('b')), [], [While(BooleanLiteral(True), ([], [CallStmt(Id('foo'), [CallExpr(Id('foo'), [CallExpr(Id('foo'), [])])])]))]),
                                                                                                                                                                                                                                                    (BinaryOp('==', Id('a'), Id('b')), [], [For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [While(BooleanLiteral(True), ([], [CallStmt(Id('foo'), [CallExpr(Id('foo'), [CallExpr(Id('foo'), [])])])]))]))])], ([], [Dowhile(([], [Continue()]), BinaryOp('=/=', BinaryOp('\.', Id('a'), FloatLiteral(10.0)), FloatLiteral(10.5)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_comment_1(self):
        input = """
        ** This is a block comment **
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = Program([VarDecl(Id('b'), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(
            6)])])), FuncDecl(Id('foo'), [VarDecl(Id('a'), [], []), VarDecl(Id('b'), [], [])], ([], [Assign(Id('b'), ArrayCell(Id('a'), [IntLiteral(2), IntLiteral(1)])), Assign(Id('a'), Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    # def test_funcdec_1(self):
    #     input = """Function: foo
    #     Body:
    #         a = 1;
    #     EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('foo'), [], ([], [
    #                      Assign(Id('a'), IntLiteral(1))]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    # def test_funcdec_2(self):
    #     input = """Function: foo
    #     Body:
    #         Var: b=2;
    #         a = 1;
    #     EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('foo'), [], ([VarDecl(Id('b'), [], IntLiteral(2))], [
    #                      Assign(Id('a'), IntLiteral(1))]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    # def test_funcdec_3(self):
    #     input = """
    #     Var: x;
    #     Function: foo
    #     Parameter: a,b
    #     Body:
    #         Var: y;
    #         If a && b Then
    #             While True Do
    #                 foo(a,b);
    #             EndWhile.
    #         Else
    #             Return a+b;
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = Program([FuncDecl(Id('foo'), [], ([VarDecl(Id('b'), [], IntLiteral(2))], [
    #                      Assign(Id('a'), IntLiteral(1))]))])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 309))

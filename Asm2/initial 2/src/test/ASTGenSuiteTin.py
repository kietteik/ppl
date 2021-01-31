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
                            ([],[])
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
                            ([],[])
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
                doSth(i);
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
                            ([], [CallStmt(Id('doSth'), [Id('i')])])
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
                    doSth(i);
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
                                    ([], [CallStmt(Id('doSth'), [Id('i')])]))
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
                    doSth(i);
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
                                        CallStmt(Id('doSth'), [Id('i')]),
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
                    doSth(i);
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
                                        CallStmt(Id('doSth'), [Id('i')]),
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

    def test_full_7(self):
        input = """Var:x[10][50] = {2}, a = 10, c = 100.5;
        Var: me, you;
        Var: he[1][2][3][4][5] = {1};
        Var: she = False;
        """
        expect = Program([VarDecl(Id("x"),[10,50],ArrayLiteral([IntLiteral(2)])),VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("c"),[],FloatLiteral(100.5)), VarDecl(Id("me"),[],[]), VarDecl(Id("you"),[],[]), VarDecl(Id("he"),[1,2,3,4,5],ArrayLiteral([IntLiteral(1)])), VarDecl(Id("she"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_full_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = {1,2,3,4};
        Var: ngao, du = 3, thienha[5][9][1][2];
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[5,9,3]),VarDecl(Id(b),[7])],([VarDecl(Id(m),[10,8],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(ngao)),VarDecl(Id(du),IntLiteral(3)),VarDecl(Id(thienha),[5,9,1,2])][]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_full_9(self):
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
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])Else([VarDecl(Id(a))],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_full_10(self):
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
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(1)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(-,Id(y),Id(x)))])Else([],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_full_11(self):
        input = """Function: main
        Body:
        (a + foo())[1] = 1;
        a[1] = a[1] * s;
        EndBody.
        """
        expect = """Program([FuncDecl(Id(main)[],([][Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),IntLiteral(1)),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[IntLiteral(1)]),Id(s)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_full_12(self):
        input = """Function: main
        Body:
        (a + foo())[1] = {{1,2,3}, {1,2,3}, {1,2,3}};
        a[1] = a[1 + foo((a + foo())[1])] * s;
        EndBody.
        """
        expect = """Program([FuncDecl(Id(main)[],([][Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)])]))]),Id(s)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_full_13(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do While 1
            EndDo.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][Dowhile([],[],IntLiteral(1))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_full_14(self):
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
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83]),VarDecl(Id(b)),VarDecl(Id(c))],([][Dowhile([VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5))],[Assign(Id(x),ArrayCell(Id(a),[BinaryOp(+,Id(x),IntLiteral(1)),BinaryOp(+,CallExpr(Id(foo),[BinaryOp(+,Id(a),IntLiteral(1))]),IntLiteral(3))]))],BinaryOp(||,BinaryOp(<=,Id(x),IntLiteral(1)),BinaryOp(!=,Id(x),IntLiteral(10))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_full_15(self):
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
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][Assign(Id(y),BinaryOp(-,Id(x),UnaryOp(!,UnaryOp(!,BooleanLiteral(true))))),Return()])),FuncDecl(Id(count)[VarDecl(Id(i))],([][Assign(Id(y),BinaryOp(-,Id(x),UnaryOp(!,UnaryOp(!,BooleanLiteral(true))))),Return()]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_full_16(self):
        input = """
        Var: a[123][1][2]={1,2,3,4,5};
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
        expect = """Program([VarDecl(Id(a),[123,1,2],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5))),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][If(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])Else([],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_full_17(self):
        input = """Var: a = 5;
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
        expect = """Program([VarDecl(Id(a),IntLiteral(5)),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallStmt(Id(printLn),[Id(x)]),Continue(),Break(),Return(),CallStmt(Id(foo),[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_full_18(self):
        input = """Var: x = 0;
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
        expect = """Program([VarDecl(Id(x),IntLiteral(0)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))]),CallStmt(Id(foo),[BinaryOp(+,IntLiteral(2),Id(x)),BinaryOp(\.,FloatLiteral(4.0),Id(y))]),CallStmt(Id(goo),[]),If(CallExpr(Id(bool_of_string),[StringLiteral(True)]),[],[Assign(Id(a),CallExpr(Id(int_of_string),[CallExpr(Id(read),[])])),Assign(Id(b),BinaryOp(+.,CallExpr(Id(float_of_int),[Id(a)]),FloatLiteral(2.0))),CallStmt(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))]),CallStmt(Id(foo),[BinaryOp(+,IntLiteral(2),Id(x)),BinaryOp(\.,FloatLiteral(4.0),Id(y))]),CallStmt(Id(goo),[])])Else([],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_full_19(self):
        input = """Var: x = 1, y[2][3] = {5}, z[2] = {{1,3},{1,5,7}};
                Function: foo
                Parameter: n
                Body:
                    If n > 10 Then
                        Return 5;
                    Else
                        Return False;
                    EndIf.
                EndBody."""
        expect = """Program([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(y),[2,3],ArrayLiteral(IntLiteral(5))),VarDecl(Id(z),[2],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(5),IntLiteral(7)))),FuncDecl(Id(foo)[VarDecl(Id(n))],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(IntLiteral(5))])Else([],[Return(BooleanLiteral(false))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_full_20(self):
        input = """Function: goo
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
        expect = """Program([FuncDecl(Id(goo)[],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(Id(n))])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[Return(BinaryOp(+,Id(n),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(6)),[],[Return(BinaryOp(+,Id(n),IntLiteral(2)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(4)),[],[Return(BinaryOp(+,Id(n),IntLiteral(3)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(2)),[],[Return(BinaryOp(+,Id(n),IntLiteral(4)))])Else([],[Return(BooleanLiteral(false))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_full_21(self):
        input = """Var: a;
                Function: foo
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
        expect = """Program([VarDecl(Id(a)),FuncDecl(Id(foo)[VarDecl(Id(n))],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[Return(IntLiteral(1)),Break(),Continue(),CallStmt(Id(foo),[BinaryOp(+,CallExpr(Id(float_of_int),[Id(a)]),IntLiteral(2))]),CallStmt(Id(goo),[BinaryOp(+,Id(a),IntLiteral(1))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_full_22(self):
        input = """Var: a = "a string";
                ** This is a comment
                * also a comment
                * Comment  
                * Another comment line**
                Function: foo
                Body:
                    x = y + (z -q) *. 10;
                    x = n >=. z;
                EndBody."""
        expect = """Program([VarDecl(Id(a),StringLiteral(a string)),FuncDecl(Id(foo)[],([][Assign(Id(x),BinaryOp(+,Id(y),BinaryOp(*.,BinaryOp(-,Id(z),Id(q)),IntLiteral(10)))),Assign(Id(x),BinaryOp(>=.,Id(n),Id(z)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_full_23(self):
        input = """Var: a, b = 2., c = 3.5;
                Function: foo
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
        expect = """Program([VarDecl(Id(a)),VarDecl(Id(b),FloatLiteral(2.0)),VarDecl(Id(c),FloatLiteral(3.5)),FuncDecl(Id(foo)[VarDecl(Id(x)),VarDecl(Id(y),[5])],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),StringLiteral(string)),VarDecl(Id(a),BooleanLiteral(false))][If(BinaryOp(==,Id(z),BooleanLiteral(true)),[],[Return(IntLiteral(1))])Else([],[]),While(BooleanLiteral(true),[],[CallStmt(Id(foo),[]),CallStmt(Id(goo),[Id(a)]),Break()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_full_24(self):
        input = """Var: a, b = 1, c = 3.5;
                Var: t;
                Var: d, e;
                Function: foo
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
        expect = """Program([VarDecl(Id(a)),VarDecl(Id(b),IntLiteral(1)),VarDecl(Id(c),FloatLiteral(3.5)),VarDecl(Id(t)),VarDecl(Id(d)),VarDecl(Id(e)),FuncDecl(Id(foo)[VarDecl(Id(q)),VarDecl(Id(d),[5])],([VarDecl(Id(a),StringLiteral(string)),VarDecl(Id(b)),VarDecl(Id(c),BooleanLiteral(false))][CallStmt(Id(foo),[BinaryOp(+,Id(a),Id(c))]),If(BinaryOp(==,Id(z),BooleanLiteral(true)),[],[Assign(Id(x),ArrayCell(Id(d),[BinaryOp(-.,BinaryOp(+.,BinaryOp(*.,Id(y),Id(z)),Id(t)),BinaryOp(\,Id(c),IntLiteral(10)))])),Return(IntLiteral(1))])ElseIf(BinaryOp(!=,Id(x),FloatLiteral(400000.0)),[],[Assign(Id(x),BinaryOp(+,BinaryOp(-,BinaryOp(*,BinaryOp(+,Id(a),Id(b)),Id(y)),Id(z)),BinaryOp(*.,Id(sp),Id(yz))))])Else([],[Continue()]),While(BooleanLiteral(true),[],[CallStmt(Id(foo),[]),CallStmt(Id(goo),[Id(a)]),Break()]),For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),UnaryOp(-,IntLiteral(2)),[],[Assign(Id(x),Id(i))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_full_25(self):
        input = """Var: a = 0;
                Function: main
                Body:
                    Do
                        Do
                            Do
                                print("Programming!");
                            While a > b
                            EndDo.
                            print("Programming!");
                        While a > b
                        EndDo.
                        print("Programming!");
                    While a > b
                    EndDo.
                EndBody."""
        expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][Dowhile([],[Dowhile([],[Dowhile([],[CallStmt(Id(print),[StringLiteral(Programming!)])],BinaryOp(>,Id(a),Id(b))),CallStmt(Id(print),[StringLiteral(Programming!)])],BinaryOp(>,Id(a),Id(b))),CallStmt(Id(print),[StringLiteral(Programming!)])],BinaryOp(>,Id(a),Id(b)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_full_26(self):
        input = """Var: a = 0;
                Function: main
                Body:
                    While (a <= - 5) Do 
                        print("Programming!");
                        While (a <= - 5) Do 
                            print("Programming!");
                            While (a <= - 5) Do 
                                print("Programming!");
                                While (a <= - 5) Do 
                                    print("Programming!");
                                EndWhile.
                            EndWhile.
                        EndWhile.
                    EndWhile.
                EndBody."""
        expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][While(BinaryOp(<=,Id(a),UnaryOp(-,IntLiteral(5))),[],[CallStmt(Id(print),[StringLiteral(Programming!)]),While(BinaryOp(<=,Id(a),UnaryOp(-,IntLiteral(5))),[],[CallStmt(Id(print),[StringLiteral(Programming!)]),While(BinaryOp(<=,Id(a),UnaryOp(-,IntLiteral(5))),[],[CallStmt(Id(print),[StringLiteral(Programming!)]),While(BinaryOp(<=,Id(a),UnaryOp(-,IntLiteral(5))),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])])])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_full_27(self):
        input = """Var: x;
                Function: foo
                Parameter: n
                Body:
                    For (i = 0, i < 10, 2) Do
                        print("Programming!");
                        For (i = 0, i < 10, -2) Do
                            For (i = 0, i < 10, 2) Do
                                print("Programming!");
                                For (i = 0, i < 10, 2) Do
                                    For (i = 0, i < 10, 2) Do
                                        print("Programming!");
                                    EndFor.
                                    print("Programming!");
                                EndFor.
                            EndFor.
                            print("Programming!");
                        EndFor.
                    EndFor.
                EndBody."""
        expect = """Program([VarDecl(Id(x)),FuncDecl(Id(foo)[VarDecl(Id(n))],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallStmt(Id(print),[StringLiteral(Programming!)]),For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),UnaryOp(-,IntLiteral(2)),[],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallStmt(Id(print),[StringLiteral(Programming!)]),For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallStmt(Id(print),[StringLiteral(Programming!)])]),CallStmt(Id(print),[StringLiteral(Programming!)])])]),CallStmt(Id(print),[StringLiteral(Programming!)])])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_full_28(self):
        input = """Function: foo
                Body:
                    If n > 10 Then
                        If n > 10 Then
                            print("Programming!");
                        ElseIf n > 8 Then
                            If n > 10 Then
                                print("Programming!");
                            ElseIf n > 8 Then
                                If n > 10 Then
                                    print("Programming!");
                                ElseIf n > 8 Then
                                    If n > 10 Then
                                        print("Programming!");
                                    ElseIf n > 8 Then
                                        print("Programming!");
                                    EndIf.
                                    print("Programming!");
                                EndIf.
                                print("Programming!");
                            EndIf.
                            print("Programming!");
                        EndIf.
                        print("Programming!");
                    ElseIf n > 8 Then
                        print("Programming!");
                    ElseIf n > 2 Then
                        print("Programming!");
                    Else
                        print("Programming!");
                    EndIf.
                EndBody."""
        expect = """Program([FuncDecl(Id(foo)[],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[If(BinaryOp(>,Id(n),IntLiteral(10)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[If(BinaryOp(>,Id(n),IntLiteral(10)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[If(BinaryOp(>,Id(n),IntLiteral(10)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[If(BinaryOp(>,Id(n),IntLiteral(10)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])Else([],[]),CallStmt(Id(print),[StringLiteral(Programming!)])])Else([],[]),CallStmt(Id(print),[StringLiteral(Programming!)])])Else([],[]),CallStmt(Id(print),[StringLiteral(Programming!)])])Else([],[]),CallStmt(Id(print),[StringLiteral(Programming!)])])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])ElseIf(BinaryOp(>,Id(n),IntLiteral(2)),[],[CallStmt(Id(print),[StringLiteral(Programming!)])])Else([],[CallStmt(Id(print),[StringLiteral(Programming!)])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_full_29(self):
        input = """Var: a;
                Function: foo
                Parameter: b
                Body:
                    c = d[y *. z +. t -. c \ 10];
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
        expect = """Program([VarDecl(Id(a)),FuncDecl(Id(foo)[VarDecl(Id(b))],([][Assign(Id(c),ArrayCell(Id(d),[BinaryOp(-.,BinaryOp(+.,BinaryOp(*.,Id(y),Id(z)),Id(t)),BinaryOp(\,Id(c),IntLiteral(10)))])),Assign(ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),Assign(Id(v),BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(\.,FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id(r)),Id(r)),Id(r))),Assign(Id(x),CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))])),Assign(Id(x),BinaryOp(+,Id(y),BinaryOp(*.,BinaryOp(-,Id(z),Id(q)),IntLiteral(10)))),Assign(Id(x),BinaryOp(>=.,Id(n),Id(z))),Assign(Id(x),ArrayCell(Id(d),[BinaryOp(-.,BinaryOp(+.,BinaryOp(*.,Id(y),Id(z)),Id(t)),BinaryOp(\,Id(c),IntLiteral(10)))])),Assign(Id(x),BinaryOp(+,BinaryOp(-,BinaryOp(*,BinaryOp(+,Id(a),Id(b)),Id(y)),Id(z)),BinaryOp(*.,Id(sp),Id(yz)))),Assign(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),UnaryOp(-,IntLiteral(1))),UnaryOp(-,IntLiteral(5))),UnaryOp(-,IntLiteral(5))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_full_30(self):
        input = """Var: a[123][1][2]={{2,3,4},{4,5,6}};
                    Function: main
                    Parameter: a, b
                    Body:
                    Var: a = 5;
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: c, d = 6, e, f;
                    Var: x, y[10];
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
        expect = """Program([VarDecl(Id(a),[123,1,2],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),VarDecl(Id(c)),VarDecl(Id(d),IntLiteral(6)),VarDecl(Id(e)),VarDecl(Id(f)),VarDecl(Id(x)),VarDecl(Id(y),[10]),VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][If(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])Else([VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_full_31(self):
        input = """Function: foo
                Parameter: z
                Body:
                Var: x;
                    x = d[y *. z +. t -. c \ 10];
                    b[2][3][3 + foo(a[3 + foo(a[3 + foo(2)])])] = {{2,3,4},{4,5,6}};
                    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 * foo(2)]][3]] + 4;
                EndBody."""
        expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(z))],([VarDecl(Id(x))][Assign(Id(x),ArrayCell(Id(d),[BinaryOp(-.,BinaryOp(+.,BinaryOp(*.,Id(y),Id(z)),Id(t)),BinaryOp(\,Id(c),IntLiteral(10)))])),Assign(ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3),BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))])]))])]))]),ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))])]))])]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(a),[BinaryOp(*,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),IntLiteral(3)])]),IntLiteral(4)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_full_32(self):
        input = """Var: a;
                Function: foo
                Parameter: b
                Body:
                    x = d[y *. z +. t -. c \ 10];
                    b[2][3] = {{2,3,4},{4,5,6}};
                    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 + foo(2)]][3]] + 4;
                EndBody."""
        expect = """Program([VarDecl(Id(a)),FuncDecl(Id(foo)[VarDecl(Id(b))],([][Assign(Id(x),ArrayCell(Id(d),[BinaryOp(-.,BinaryOp(+.,BinaryOp(*.,Id(y),Id(z)),Id(t)),BinaryOp(\,Id(c),IntLiteral(10)))])),Assign(ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))])]))])]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),IntLiteral(3)])]),IntLiteral(4)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_full_33(self):
        input = """Var: x[1][2][3]={1,2,3}, a,b,c,d;
                    Var: y[1][2][3]={1,2,3}, a,b,c,d;"""
        expect = Program([VarDecl(Id('x'), [1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [
        ], None), VarDecl(Id('y'), [1, 2, 3], ArrayLiteral([IntLiteral('1'), IntLiteral('2'), IntLiteral('3')])), VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None), VarDecl(Id('d'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_full_34(self):
        input = """Var:a=1;Var:a=1;Var:a=1;Var:a=1;Var:a=1;"""
        expect = Program([VarDecl(Id('a'), [], IntLiteral('1')), VarDecl(Id('a'), [], IntLiteral('1')), VarDecl(
            Id('a'), [], IntLiteral('1')), VarDecl(Id('a'), [], IntLiteral('1')), VarDecl(Id('a'), [], IntLiteral('1'))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_full_35(self):
        input = """Function: main
                    Body:
                    EndBody.Function: foo
                    Body:
                    EndBody.Function: goo
                    Body:
                    EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([], [])), FuncDecl(
            Id('foo'), [], ([], [])), FuncDecl(Id('goo'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_full_36(self):
        input = """Function: foo
                Parameter: a
                Body:
                    If n > 10 Then
                        Return 5;
                    ElseIf n >5 Then a=a+1; Return a;
                    ElseIf n < 10 Then a=a+1; Return a;
                    Else
                        Return False;
                    EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), [], None)], ([], [If([(BinaryOp('>', Id('n'), IntLiteral('10')), [], [Return(IntLiteral('5'))]), (BinaryOp('>', Id('n'), IntLiteral('5')), [], [Assign(Id('a'), BinaryOp(
            '+', Id('a'), IntLiteral('1'))), Return(Id('a'))]), (BinaryOp('<', Id('n'), IntLiteral('10')), [], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral('1'))), Return(Id('a'))])], ([], [Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_full_37(self):
        input = """Function: main
                Body:
                    Var:x=1;
                    For (i = 0, i < 10, 2) Do
                        While (True) Do
                            For (i = 0, i < 10, 2) Do
                                doSth(i);
                                For (i = 0, i < 10, 2) Do
                                doSth(i);
                                For (i = 0, i < 10, 2) Do
                                doSth(i);
                                EndFor.
                                doSth(i);
                                EndFor.
                            a=b;
                            EndFor.
                        EndWhile.
                    EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], IntLiteral('1'))], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [While(BooleanLiteral('true'), ([], [For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('doSth'), [Id('i')]), For(
            Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('doSth'), [Id('i')]), For(Id('i'), IntLiteral('0'), BinaryOp('<', Id('i'), IntLiteral('10')), IntLiteral('2'), ([], [CallStmt(Id('doSth'), [Id('i')])])), CallStmt(Id('doSth'), [Id('i')])])), Assign(Id('a'), Id('b'))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_full_38(self):
        input = """Function: foo
                Parameter: a
                Body:   
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                    While ((b>=a)==(b!=c)+d*a*b*c) Do
                        While ((b>=a)==(b!=c)+d*a*b*c) Do
                        doSth(i);
                        EndWhile.
                    doSth(i);
                    EndWhile.
                    doSth(i);
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('doSth'),[Id('i')])])),CallStmt(Id('doSth'),[Id('i')])])),CallStmt(Id('doSth'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_full_39(self):
        input = """Function: foo
        Parameter: a
        Body:   
        While ((b>=a)==(b!=c)+d*a*b*c) Do
            For (i = 0, i < 10, 2) Do
                doSth(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                    doSth(i);
                        While ((b>=a)==(b!=c)+d*a) Do
                            doSth(i);
                            goo(a==1);
                        EndWhile.
                    doSth(i);
                EndWhile.
            EndFor.
            While ((b>=a)==(b!=c)+d*a) Do
                doSth(i);
                goo(a==1);
            EndWhile.
            doSth(i);
        EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('doSth'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')))),([],[CallStmt(Id('doSth'),[Id('i')]),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('goo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('doSth'),[Id('i')])]))])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',Id('d'),Id('a')))),([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('goo'),[BinaryOp('==',Id('a'),IntLiteral('1'))])])),CallStmt(Id('doSth'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_full_40(self):
        input = """Function: foo
                Parameter: x
                Body:   Do
                        doSth(i);
                        doSth(i);
                            Do
                                doSth(i);
                                doSth(i);
                                    doSth(i);
                                Do
                                While (a==12+3)
                                EndDo.
                                While (a==12+3)
                            EndDo.
                        While (True)
                        EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),Dowhile(([],[]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('12'),IntLiteral('3'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_full_41(self):
        input = """Function: foo
                Parameter: a
                Body:   Do
                        doSth(i);
                        doSth(i);
                            Do
                                doSth(i);
                                doSth(i);
                                While (True) Do
                                    doSth(i);
                                EndWhile.
                            While(True)
                            EndDo.
                            Do
                                doSth(i);
                            While (a==2+1)
                            EndDo.
                        While (True)
                        EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),While(BooleanLiteral('true'),([],[CallStmt(Id('doSth'),[Id('i')])]))]),BooleanLiteral('true')),Dowhile(([],[CallStmt(Id('doSth'),[Id('i')])]),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral('2'),IntLiteral('1'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_full_42(self):
        input = """Function: foo
                    Parameter: a
                    Body:   Do
                            doSth(i);
                            doSth(i);
                                Do
                                    doSth(i);
                                    doSth(i);
                                        doSth(i);
                                    Do
                                    While ((a==b)==(c==d))
                                    EndDo.
                                    While ((a==b)==(d==d))
                                EndDo.
                            While (True)
                            EndDo.
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),CallStmt(Id('doSth'),[Id('i')]),Dowhile(([],[]),BinaryOp('==',BinaryOp('==',Id('a'),Id('b')),BinaryOp('==',Id('c'),Id('d'))))]),BinaryOp('==',BinaryOp('==',Id('a'),Id('b')),BinaryOp('==',Id('d'),Id('d'))))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_full_43(self):
        input = """Function: main
                Parameter: a
                Body:   
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                    doSth(i);
                    If (a==2) Then
                        Break;
                    EndIf.
                    While ((b>=a)==(b!=c)+d*a*b*c) Do
                        doSth(i);
                    EndWhile.
                    While ((b>=a)==(b!=c)+d*a*b*c) Do
                        doSth(i);
                    EndWhile.
                EndWhile.
                EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('doSth'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Break()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('doSth'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('doSth'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_full_44(self):
        input = """Function: main
                Parameter: a
                Body:   
                Do
                    Continue;
                    While (True)
                    EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[Continue()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_full_45(self):
        input = """Function: foo
                    Parameter: a
                    Body:   
                    Do
                        doSth(i);
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
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('doSth'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Continue()])],([],[Return(BinaryOp('==',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral('2'))),Break()]))]),BooleanLiteral('true')),Return(BinaryOp('==',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral('2')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_full_46(self):
        input = """Function: foo
                Parameter: a
                Body:   
                    For (i = 0, i < 10, 2) Do
                        doSth(i);
                        For (i = 0, i < 10, 2) Do
                            doSth(i);
                            If (a==2) Then
                                Continue;
                            EndIf.
                        EndFor.
                    EndFor.
                    Return1+1;
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('doSth'),[Id('i')]),For(Id('i'),IntLiteral('0'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[CallStmt(Id('doSth'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Continue()])],([],[]))]))])),Return(BinaryOp('+',IntLiteral('1'),IntLiteral('1')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_full_47(self):
        input = """**Random comment**Var: a = "Some random text";
                Var: b = 5, c = False;
                **Random comment**
                Function: main
                Parameter: x
                Body:   
                    Do
                        Break;
                    While (True)
                    EndDo.
                EndBody.
                **Random comment**
                Function: foo
                Parameter: x
                Body:   
                Do
                    Break;
                    While (True)
                    EndDo.
                EndBody."""
        expect = Program([VarDecl(Id('a'),[],StringLiteral('Some random text')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))])),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_full_48(self):
        input = """******Random comment**
                Var: a = "Random text";
                Var: b = 5, c = False;
                **Random comment**
                Function: foo
                Parameter: x
                Body:   
                    Do
                        Break;
                    While (True)
                    EndDo.
                EndBody.
                **terminated by a comment****followed by a comment**"""
        expect = Program([VarDecl(Id('a'),[],StringLiteral('Random text')),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('false')),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_full_49(self):
        input = """Function: foo
                Parameter: x
                Body:   
                    goo((b+1));
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('goo'),[BinaryOp('+',Id('b'),IntLiteral('1'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_full_50(self):
        input = """Function: foo
                Parameter: x
                Body:   goo("String 1","String 2");
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[CallStmt(Id('goo'),[StringLiteral('String 1'),StringLiteral('String 2')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_full_51(self):
        input = """
                Function: foo
                Parameter: a
                Body:   goo(boo(noo(yoo("text",{1,2,3},{{23},{1,3,4}}))),"and second string");
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[CallStmt(Id('goo'),[CallExpr(Id('boo'),[CallExpr(Id('noo'),[CallExpr(Id('yoo'),[StringLiteral('text'),ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')]),ArrayLiteral([ArrayLiteral([IntLiteral('23')]),ArrayLiteral([IntLiteral('1'),IntLiteral('3'),IntLiteral('4')])])])])]),StringLiteral('and second string')])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_full_52(self):
        input = """
                Var: a = "text";
                Var: b = 5, c = True;
                Var: d[1][2][3]={1,2,3}, a,b,c,d;
                Var: d[1][2][3]={1,2,3}, a,b,c,d;
                Var:a=1;
                Function: main
                Parameter: a
                Body:   
                Do
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
                Function: foo
                Parameter: x
                Body:   
                Do
                    Break;
                While (True)
                EndDo.
                EndBody."""
        expect = Program([VarDecl(Id('a'),[],StringLiteral("""text""")),VarDecl(Id('b'),[],IntLiteral('5')),VarDecl(Id('c'),[],BooleanLiteral('true')),VarDecl(Id('d'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('d'),[1,2,3],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None),VarDecl(Id('a'),[],IntLiteral('1')),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true')),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(BooleanLiteral('true')),Break()])],([],[])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])),FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_full_53(self):
        input = """Function: foo
                Parameter: a
                Body:
                    For (a=5,a<10,a+.1) Do
                        goo(a);
                        For (a=2,a==0,a*1) Do
                            If e==f Then
                            a=a+1;
                            EndIf.
                        EndFor.
                    EndFor.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None)],([],[For(Id('a'),IntLiteral('5'),BinaryOp('<',Id('a'),IntLiteral('10')),BinaryOp('+.',Id('a'),IntLiteral('1')),([],[CallStmt(Id('goo'),[Id('a')]),For(Id('a'),IntLiteral('2'),BinaryOp('==',Id('a'),IntLiteral('0')),BinaryOp('*',Id('a'),IntLiteral('1')),([],[If([(BinaryOp('==',Id('e'),Id('f')),[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral('1')))])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_full_54(self):
        input = """Function: foo
            Parameter: n,a[2][3][4],b[4][1],m
            Body:
            a = "Some random text";
                If a > 20 Then
                    Return a + a;
                ElseIf a > 5 Then a=a+.1; Return a;
                Else
                    Return False;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[2,3,4],None),VarDecl(Id('b'),[4,1],None),VarDecl(Id('m'),[],None)],([],[Assign(Id('a'),StringLiteral("""Some random text""")),If([(BinaryOp('>',Id('a'),IntLiteral('20')),[],[Return(BinaryOp('+',Id('a'),Id('a')))]),(BinaryOp('>',Id('a'),IntLiteral('5')),[],[Assign(Id('a'),BinaryOp('+.',Id('a'),IntLiteral('1'))),Return(Id('a'))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_full_55(self):
        input = """Function: foo
                Parameter: n,a[2][3][4],b[4][1],m
                Body:
                    a = 0x123456;
                    If a < b Then
                        While True Do
                            Break;
                        EndWhile.
                    ElseIf a == b Then
                        For (i = 1, i < 10, 1) Do
                            
                            If a < b Then
                                Return a;
                            EndIf.
                        EndFor.
                    Else
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[2,3,4],None),VarDecl(Id('b'),[4,1],None),VarDecl(Id('m'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[Return(Id('a'))])],([],[]))]))])],([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_full_56(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Do
                    While i < 10 Do
                        doSth(a[i]);
                        While j < i Do
                            **doSth(a[j]);**
                            For (i = 1, i < 10, foo(1)) Do
                                For (i = 1, i > 10, i) Do
                                    Return a;
                                EndFor.
                            EndFor.
                        EndWhile.
                        i = i + 1;
                    EndWhile.
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('doSth'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('<',Id('j'),Id('i')),([],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),CallExpr(Id('foo'),[IntLiteral('1')]),([],[For(Id('i'),IntLiteral('1'),BinaryOp('>',Id('i'),IntLiteral('10')),Id('i'),([],[Return(Id('a'))]))]))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
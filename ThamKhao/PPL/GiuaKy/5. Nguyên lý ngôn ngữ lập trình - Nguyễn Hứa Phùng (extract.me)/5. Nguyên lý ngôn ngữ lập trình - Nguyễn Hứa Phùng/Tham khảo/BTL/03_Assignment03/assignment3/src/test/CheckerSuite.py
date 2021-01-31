import unittest
from TestUtils import TestChecker
from AST import *
#-------------------------------------------------------------------------#
#--------------------AUTHOR: Nguyen Minh THAM (1613166)-------------------#
#-------------------------------------------------------------------------#


class CheckerSuite(unittest.TestCase):
    def test_Redeclared_1(self):
        """Redeclared: variable declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("a"), IntType()),
                VarDecl(Id("a"), IntType()),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    []
                )
            ])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_Redeclared_2(self):
        """Redeclared: variable declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("func1"), IntType()),
                FuncDecl(
                    Id("proce1"),
                    [],
                    [],
                    [],
                    IntType()
                )
            ])

        expect = "Redeclared Variable: func1"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_Redeclared_3(self):
        """Redeclared: variable declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    [],
                    IntType()
                ),
                VarDecl(Id("func1"), IntType()),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    []
                )
            ])

        expect = "Redeclared Variable: func1"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_Redeclared_4(self):
        """Redeclared: function declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    [],
                    IntType()
                ),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    [],
                    FloatType()
                )
            ])

        expect = "Redeclared Function: func1"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_Redeclared_5(self):
        """Redeclared: function declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("proce1"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("proce1"),
                    [],
                    [],
                    [],
                    FloatType()
                )
            ])

        expect = "Redeclared Function: proce1"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_Redeclared_6(self):
        """Redeclared: function declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("func1"), IntType()),
                FuncDecl(
                    Id("func1"),
                    [],
                    [],
                    [],
                    IntType()
                )
            ])

        expect = "Redeclared Function: func1"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_Redeclared_7(self):
        """Redeclared: procedure declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("proce"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("proce"),
                    [],
                    [],
                    []
                )
            ])

        expect = "Redeclared Procedure: proce"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_Redeclared_8(self):
        """Redeclared: procedure declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("proce1"),
                    [],
                    [],
                    [],
                    FloatType()
                ),
                FuncDecl(
                    Id("proce1"),
                    [],
                    [],
                    []
                )
            ])

        expect = "Redeclared Procedure: proce1"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_Redeclared_9(self):
        """Redeclared: procedure declaration"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("procedu"), IntType()),
                FuncDecl(
                    Id("procedu"),
                    [],
                    [],
                    []
                )
            ])

        expect = "Redeclared Procedure: procedu"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_Redeclared_10(self):
        """Redeclared: variable declaration in function / procedure"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("a"), IntType()),
                FuncDecl(
                    Id("proce"),
                    [
                        VarDecl(Id("toi"), FloatType()),
                        VarDecl(Id("toi"), StringType())
                    ],
                    [
                        VarDecl(Id("d"), FloatType()),
                        VarDecl(Id("a"), StringType())
                    ],
                    []
                )
            ])

        expect = "Redeclared Parameter: toi"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_Redeclared_11(self):
        """Redeclared: variable declaration in function / procedure"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("a"), IntType()),
                FuncDecl(
                    Id("proce"),
                    [
                        VarDecl(Id("toi"), FloatType()),
                        VarDecl(Id("laTham"), StringType())
                    ],
                    [
                        VarDecl(Id("la"), FloatType()),
                        VarDecl(Id("la"), StringType())
                    ],
                    []
                )
            ])

        expect = "Redeclared Variable: la"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_Redeclared_12(self):
        """Redeclared: variable declaration in function / procedure"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("a"), IntType()),
                FuncDecl(
                    Id("proce"),
                    [
                        VarDecl(Id("toi"), FloatType()),
                        VarDecl(Id("la"), StringType())
                    ],
                    [
                        VarDecl(Id("la"), FloatType()),
                        VarDecl(Id("Tham"), StringType())
                    ],
                    []
                )
            ])

        expect = "Redeclared Variable: la"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_Redeclared_13(self):
        """Redeclared: variable declaration in with statement"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("a"), IntType()),
                FuncDecl(
                    Id("proce"),
                    [
                        VarDecl(Id("toi"), FloatType()),
                    ],
                    [
                        VarDecl(Id("la"), StringType())
                    ],
                    [
                        With(
                            [
                                VarDecl(Id("la"), FloatType()),
                                VarDecl(Id("Tham"), StringType()),
                                VarDecl(Id("Tham"), StringType())
                            ],
                            []
                        )
                    ]
                )
            ])

        expect = "Redeclared Variable: Tham"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_Redeclared_14(self):
        """Redeclared: built in function / procedure"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                VarDecl(Id("putLn"), IntType())
            ])

        expect = "Redeclared Variable: putLn"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_Redeclared_15(self):
        """Redeclared: built in function / procedure"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("putString"),
                    [],
                    [],
                    []
                )
            ])

        expect = "Redeclared Procedure: putString"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_Redeclared_16(self):
        """Redeclared: built in function / procedure"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    [],
                    []
                ),
                FuncDecl(
                    Id("putBool"),
                    [],
                    [],
                    [],
                    IntType()
                )
            ])

        expect = "Redeclared Function: putBool"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_Undeclared_1(self):
        """Undeclared: Procedure"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce();
            BEGIN
                proce1();
            END
        """
        expect = "Undeclared Procedure: proce1"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_Undeclared_2(self):
        """Undeclared: Procedure"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce();
            VAR proce:INTEGER;
            BEGIN
                proce();
            END
        """
        expect = "Undeclared Procedure: proce"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_Undeclared_3(self):
        """Undeclared: Procedure"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce(proce : real);
            BEGIN
                proce();
            END
        """
        expect = "Undeclared Procedure: proce"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_Undeclared_4(self):
        """Undeclared: Procedure"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce();
            BEGIN
                WITH
                    proce : string;
                DO
                    proce();
            END
        """
        expect = "Undeclared Procedure: proce"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_Undeclared_5(self):
        """Undeclared: Procedure"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce();
            BEGIN
                WITH
                    putInt : string;
                DO
                    putInt();
            END
        """
        expect = "Undeclared Procedure: putInt"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_Undeclared_6(self):
        """Undeclared: Function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func():INTEGER;
            VAR callexpr : integer;
            BEGIN
                callexpr := func1();
            END
        """
        expect = "Undeclared Function: func1"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_Undeclared_7(self):
        """Undeclared: Function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func():INTEGER;
            VAR func:INTEGER;
                callexpr : integer;
            BEGIN
                callexpr := func();
            END
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_Undeclared_8(self):
        """Undeclared: Function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(func : real):string;
            VAR callexpr : integer;
            BEGIN
                callexpr := func();
            END
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_Undeclared_9(self):
        """Undeclared: Function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION functi():string;
            VAR callexpr : integer;
            BEGIN
                WITH
                    functi : string;
                DO
                    callexpr := functi();
            END
        """
        expect = "Undeclared Function: functi"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_Undeclared_10(self):
        """Undeclared: Function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce();
            VAR callexpr : integer;
            BEGIN
                WITH
                    getInt : string;
                DO
                    callexpr := getInt();
            END
        """
        expect = "Undeclared Function: getInt"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_Undeclared_11(self):
        """Undeclared: Function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce1(func: INTEGER ; a : INTEGER);
            BEGIN
            END
        PROCEDURE proce2();
            VAR a: INTEGER;
                b: INTEGER;
            BEGIN
                proce1(foo(b),a); //line 6
            END
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_Undeclared_12(self):
        """Undeclared: Identifier of Call Expression"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            BEGIN
                RETURN a*2;
            END
        PROCEDURE proce2();
            VAR bien: INTEGER;
                callexpr: INTEGER;
            BEGIN
                callexpr := func(a);
                RETURN;
            END
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_Undeclared_13(self):
        """Undeclared: Identifier of Array Cell"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            BEGIN
                RETURN a*2;
            END
        PROCEDURE proce2();
            VAR bien: INTEGER;
                callexpr: INTEGER;
            BEGIN
                arry[bien] := 24;
            END
        """
        expect = "Undeclared Identifier: arry"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_Undeclared_14(self):
        """Undeclared: Identifier of Array Cell"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce2();
            VAR bien: INTEGER;
                callexpr: INTEGER;
                arr : ARRAY [-1 .. 5] OF INTEGER;
            BEGIN
                arr[index] := 24;
            END
        """
        expect = "Undeclared Identifier: index"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_Undeclared_15(self):
        """Undeclared: Identifier of Call Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce2();
            VAR a: INTEGER;
            BEGIN
                b := 5;
            END
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_Undeclared_16(self):
        """Undeclared: Identifier of Call Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce2();
            VAR a: INTEGER;
            BEGIN
                a := b;
            END
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_Undeclared_17(self):
        """Undeclared: Identifier of With Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce2();
            VAR a: INTEGER;
            BEGIN
                WITH
                    b: INTEGER;
                DO
                    c := 5;

            END
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_Undeclared_18(self):
        """Undeclared: Identifier of Return Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            BEGIN
                RETURN b;
            END
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_Undeclared_19(self):
        """Undeclared: Identifier of For Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            BEGIN
                FOR b := 2 TO 5 DO
                    CONTINUE;
                RETURN a*2;
            END
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_Undeclared_20(self):
        """Undeclared: Identifier of If Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            BEGIN
                IF -b <= 3 THEN RETURN a;
            END
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_Undeclared_21(self):
        """Undeclared: Identifier of WHILE Statement"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            BEGIN
                WHILE a <= 3 DO RETURN b + a;
            END
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_MismatchInExpression_1(self):
        """Type Mismatch In Expression: Unary Operation (not)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : BOOLEAN):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                a := not true;
                a := not false;
                a := not 2;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: UnaryOp(not,IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_MismatchInExpression_2(self):
        """Type Mismatch In Expression: Unary Operation (-)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER ; b : REAL):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                a := - 23;
                b := - 2.3;
                a := - true;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_MismatchInExpression_3(self):
        """Type Mismatch In Expression: Binary Operation (= <> < <= > >=)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : BOOLEAN):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
            BEGIN
                a := 1 < 2;
                a := 2.2 >= 4;
                a := 56 <> 7.8;
                a := 23.2 = 5.6;
                a := true >= 23;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(True),IntLiteral(23))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_MismatchInExpression_4(self):
        """Type Mismatch In Expression: Binary Operation (+, - , *)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
            BEGIN
                a := 1 + 2;
                b := 2.2 - 4;
                b := 56 * 7.8;
                b := 23.2 - 5.6;
                a := true * 23;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(True),IntLiteral(23))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_MismatchInExpression_5(self):
        """Type Mismatch In Expression: Binary Operation (/)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
            BEGIN
                b := 1 / 2;
                b := 2.2 / 4;
                b := 56 / 7.8;
                b := 23.2 / 5.6;
                a := true / 23;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(True),IntLiteral(23))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_MismatchInExpression_6(self):
        """Type Mismatch In Expression: Binary Operation (div,mod)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
            BEGIN
                a := 1 div 2;
                a := 2 mod 4;
                a := 56 div 7.8;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: BinaryOp(div,IntLiteral(56),FloatLiteral(7.8))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_MismatchInExpression_7(self):
        """Type Mismatch In Expression: Binary Operation (and,or)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : BOOLEAN;
            BEGIN
                b := (1 > 2) and true;
                b := (4 = 5) or (4 + 6 > 11);
                b := 56 and false;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,IntLiteral(56),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_MismatchInExpression_8(self):
        """Type Mismatch In Expression: Binary Operation (and then,or else)"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : BOOLEAN;
            BEGIN
                b := (1 > 2) and then true;
                b := (4 = 5) or else (4 + 6 > 11);
                b := 56 or else false;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(56),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_MismatchInExpression_9(self):
        """Type Mismatch In Expression: ARRAY CELL"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
                d : ARRAY [1 .. 5] OF REAL;
            BEGIN
                a := c[c[2]];
                b := d[d[2]];
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(d),ArrayCell(Id(d),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_MismatchInExpression_10(self):
        """Type Mismatch In Expression: ARRAY CELL"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
                d : ARRAY [1 .. 5] OF REAL;
            BEGIN
                a := c[c[2]];
                b := b[2];
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_MismatchInExpression_11(self):
        """Type Mismatch In Expression: CALL FUNCTION"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: INTEGER ; p2:STRING ; p3: REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
                d : INTEGER;
            BEGIN
                b := foo(d,"123",d);
                b := foo(b);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_MismatchInExpression_12(self):
        """Type Mismatch In Expression: CALL FUNCTION"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: INTEGER ; p2:STRING ; p3: REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
                d : INTEGER;
            BEGIN
                b := foo(d,"123",d);
                b := foo(d,"123",b);
                b := foo(b,"123",b);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b),StringLiteral(123),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_MismatchInExpression_13(self):
        """Type Mismatch In Expression: CALL FUNCTION"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr2 : ARRAY [-1 .. 5] OF INTEGER;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
            BEGIN
                b := foo(b,"123",arr3);
                b := foo(b,"123",arr2);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b),StringLiteral(123),Id(arr2)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_MismatchInExpression_14(self):
        """Type Mismatch In Expression: CALL FUNCTION"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr2 : ARRAY [-1 .. 5] OF INTEGER;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
            BEGIN
                b := foo(b,"123",arr3);
                b := foo(b,"123",arr1);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b),StringLiteral(123),Id(arr1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_MismatchInStatement_1(self):
        """Type Mismatch In Statement: ASSIGNMENT STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
                bool1 : BOOLEAN;
            BEGIN
                b := foo(b,"123",arr3);
                b := d;
                bool1 := true;
                d := b := 3.4;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(d),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_MismatchInStatement_2(self):
        """Type Mismatch In Statement: ASSIGNMENT STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
                bool1 : BOOLEAN;
                str1 : STRING;
            BEGIN
                b := foo(b,"123",arr3);
                b := d;
                bool1 := true;
                arr1[4] := b := 3.4;
                str1 := "214";
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(str1),StringLiteral(214))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_MismatchInStatement_3(self):
        """Type Mismatch In Statement: ASSIGNMENT STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL):REAL;
            BEGIN
                RETURN 10.0;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
                bool1 : BOOLEAN;
                str1 : STRING;
            BEGIN
                b := foo(b,"123",arr3);
                b := d;
                bool1 := true;
                arr1[4] := b := 3.4;
                arr1 := arr1;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr1),Id(arr1))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_MismatchInStatement_4(self):
        """Type Mismatch In Statement: CALL PROCEDURE"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE foo(p1: INTEGER ; p2:STRING ; p3: REAL);
            BEGIN
                RETURN;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
                d : INTEGER;
            BEGIN
                foo(d,"123",d);
                foo(b);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_MismatchInStatement_5(self):
        """Type Mismatch In Statement: CALL PROCEDURE"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE foo(p1: INTEGER ; p2:STRING ; p3: REAL);
            BEGIN
                RETURN ;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR c : ARRAY [1 .. 5] OF INTEGER;
                b : REAL;
                d : INTEGER;
            BEGIN
                foo(d,"123",d);
                foo(d,"123",b);
                foo(b,"123",b);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(b),StringLiteral(123),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_MismatchInStatement_6(self):
        """Type Mismatch In Statement: CALL PROCEDURE"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL);
            BEGIN
                RETURN ;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr2 : ARRAY [-1 .. 5] OF INTEGER;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
            BEGIN
                foo(b,"123",arr3);
                foo(b,"123",arr2);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(b),StringLiteral(123),Id(arr2)])"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_MismatchInStatement_7(self):
        """Type Mismatch In Statement: CALL PROCEDURE"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE foo(p1: REAL ; p2:STRING ; p3: ARRAY [-1 .. 5] OF REAL);
            BEGIN
                RETURN ;
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                arr2 : ARRAY [-1 .. 5] OF INTEGER;
                arr3 : ARRAY [-1 .. 5] OF REAL;
                b : REAL;
                d : INTEGER;
            BEGIN
                foo(b,"123",arr3);
                foo(b,"123",arr1);
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(b),StringLiteral(123),Id(arr1)])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_MismatchInStatement_8(self):
        """Type Mismatch In Statement: IF STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
            BEGIN
                IF -b <= 3 THEN RETURN a;
                IF b <> a THEN b := 5.6; ELSE b := 10;
                IF b = a THEN b := 5.6; ELSE b := 10;
                IF b + a THEN b := 5.6; ELSE b := 10;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(b),Id(a)),[AssignStmt(Id(b),FloatLiteral(5.6))],[AssignStmt(Id(b),IntLiteral(10))])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_MismatchInStatement_9(self):
        """Type Mismatch In Statement: WHILE STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
            BEGIN
                WHILE -b <= 3 DO RETURN a;
                WHILE b <> a DO b := 5.6;       //ELSE b := 10;
                WHILE b = a DO b := 5.6;        //ELSE b := 10;
                WHILE b + a DO b := 5.6;           //ELSE b := 10;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: While(BinaryOp(+,Id(b),Id(a)),[AssignStmt(Id(b),FloatLiteral(5.6))])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_MismatchInStatement_10(self):
        """Type Mismatch In Statement: FOR STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
            BEGIN
                FOR a := 45 TO a DO RETURN a;
                FOR a := func(23) DOWNTO 100 DO b := 5.6;
                FOR b := 4 to 10 DO b := 5.6;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: For(Id(b)IntLiteral(4),IntLiteral(10),True,[AssignStmt(Id(b),FloatLiteral(5.6))])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_MismatchInStatement_11(self):
        """Type Mismatch In Statement: FOR STATEMENT"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
            BEGIN
                FOR a := 45 TO a DO RETURN a;
                FOR a := func(23) DOWNTO 100 DO b := 5.6;
                FOR a := 4 to b DO b := 5.6;
                RETURN 10;
            END
        """
        expect = "Type Mismatch In Statement: For(Id(a)IntLiteral(4),Id(b),True,[AssignStmt(Id(b),FloatLiteral(5.6))])"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_MismatchInStatement_12(self):
        """Type Mismatch In Statement: RETURN STATEMENT in function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):REAL;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
                func : integer;
            BEGIN
                FOR a := 45 TO a DO
                    RETURN a;//integer
                FOR a := (23) DOWNTO 100 DO
                    RETURN arr1[3];//real
                FOR a := 4 to 7 DO
                    RETURN b;//real
                RETURN;                          //error
            END
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_MismatchInStatement_13(self):
        """Type Mismatch In Statement: RETURN STATEMENT in function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):ARRAY [1 .. 5] OF REAL;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
                func : integer;
                arr2 : ARRAY [-1 .. 5] OF REAL;
            BEGIN
                FOR a := 45 TO a DO
                    RETURN arr1;//array
                RETURN arr2;                          //error
            END
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(arr2)))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_MismatchInStatement_14(self):
        """Type Mismatch In Statement: RETURN STATEMENT in function"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        FUNCTION func(a : INTEGER):STRING;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
                func : STRING;
                arr2 : ARRAY [-1 .. 5] OF REAL;
            BEGIN
                RETURN func;
                FOR a := 45 TO a DO
                    RETURN arr2;//error
            END
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(arr2)))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_MismatchInStatement_15(self):
        """Type Mismatch In Statement: RETURN STATEMENT in procedure"""
        input = """
        PROCEDURE main();
            BEGIN
            END
        PROCEDURE proce(a : INTEGER);
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
                func : STRING;
                arr2 : ARRAY [-1 .. 5] OF REAL;
            BEGIN
                RETURN ;
                FOR a := 45 TO a DO
                    RETURN func;//array
            END
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(func)))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_NoEntryPoint_1(self):
        """No Entry Point: parmameter"""
        input = """
        PROCEDURE main(a : INTEGER);
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : REAL;
                main : STRING;
            BEGIN
                RETURN ;
                FOR a := 45 TO a DO
                    RETURN ;//array
            END
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_NoEntryPoint_2(self):
        """No Entry Point: function main"""
        input = """
        FUNCTION main():INTEGER;
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                RETURN 2;
                FOR b := 45 TO a DO
                    RETURN 3;//array
            END
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_BreakContinueNoInLoop_1(self):
        """Break No In Loop: function """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                Break;
            END
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_BreakContinueNoInLoop_2(self):
        """Continue No In Loop: function """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                Continue;
            END
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_BreakContinueNoInLoop_3(self):
        """Break No In Loop: IF """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                IF 23 > 5 THEN Break; Else b:= 1;
            END
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_BreakContinueNoInLoop_4(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                WHILE true DO
                    IF 23 > 5 THEN Break; Else b:= 1;
                Continue;
            END
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_BreakContinueNoInLoop_5(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                FOR b := 5 to 10 DO
                    IF 23 > 5 THEN Break; Else b:= 1;
                Break;
            END
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_BreakContinueNoInLoop_6(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                FOR b := 5 to 10 DO
                    BEGIN
                        IF 23 > 5 THEN Continue; Else b:= 1;
                        arr1[1] := 10;
                        WHILE true DO arr1[2] := 3.4;
                    END
                IF true THEN
                    BEGIN
                        WHILE false DO arr1[3] := 54.3;
                        CONTINUE; //error
                    END
            END
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_BreakContinueNoInLoop_7(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                FOR b := 5 to 10 DO
                    BEGIN
                        IF 23 > 5 THEN Continue; Else b:= 1;
                        arr1[1] := 10;
                        WHILE true DO arr1[2] := 3.4;
                        BREAK;
                    END
                IF true THEN
                    BEGIN
                        WHILE false DO arr1[3] := 54.3;
                        WITH c:String; DO
                        BEGIN
                            WHILE true DO break;
                            CONTINUE; //error
                        END
                    END
            END
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_BreakContinueNoInLoop_8(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                FOR b := 5 to 10 DO
                    BEGIN
                        IF 23 > 5 THEN Continue; Else b:= 1;
                        arr1[1] := 10;
                        WHILE true DO 
                        BEGIN
                            WITH
                                Main: integer;
                            DO
                                BREAK;
                        END
                    END
                putln();
                continue;
            END
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_BreakContinueNoInLoop_9(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                FOR b := 5 to 10 DO
                    BEGIN
                        IF 23 > 5 THEN Continue; Else b:= 1;
                        arr1[1] := 10;
                        WHILE true DO 
                        BEGIN
                            WITH
                                Main: integer;
                            DO
                                BREAK;
                        END
                    END
                While true DO
                BEGIN
                    putln();
                    continue;
                END
                Break;
            END
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_BreakContinueNoInLoop_10(self):
        """Break/Continue No In Loop """
        input = """
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF REAL;
                b : Integer;
                main : STRING;
            BEGIN
                FOR b := 5 to 10 DO
                    BEGIN
                        WHILE true DO 
                        BEGIN
                            WITH
                                Main: integer;
                            DO
                                BREAK;
                        END
                    END
                putln();
                break;
            END
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_FunctionNotReturn_1(self):
        """Function Not Return """
        input = """
        FUNCTION foo1():integer;
            BEGIN
                WITH 
                    toi :string;
                    la : integer;
                    tham: real;
                DO
                    BEGIN
                        la := 12;
                        tham := 10.0;
                    END
            END
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF INTEGER;
                b : Integer;
                main : real;
            BEGIN
                b:= foo1();
            END
        """
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_FunctionNotReturn_2(self):
        """Function Not Return """
        input = """
        FUNCTION foo1():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                FOR a:= 1 to 10 DO
                    BEGIN
                        arr1[3] := 65;
                        a :=1;
                        WITH
                            B: real;
                        DO
                            b:= 5.6;
                    END
                return 12;
            END
        FUNCTION foo2():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                FOR a:= 1 to 10 DO
                    BEGIN
                        arr1[3] := 65;
                        a :=1;
                        WITH
                            b: real;
                        DO
                            RETURN 10;
                    END
            END
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF INTEGER;
                b : Integer;
                main : real;
            BEGIN
                b:= foo1();
                b:= foo2();
            END
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_FunctionNotReturn_3(self):
        """Function Not Return """
        input = """
        FUNCTION foo1():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                WHILE true DO
                    BEGIN
                        arr1[3] := 65;
                        a :=1;
                        WITH
                            b: real;
                        DO
                            b:= 5.6;
                    END
                return 12;
            END
        FUNCTION foo2():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                WHILE true DO
                    BEGIN
                        arr1[3] := 65;
                        a :=1;
                        WITH
                            b: real;
                        DO
                            RETURN 10;
                    END
            END
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF INTEGER;
                b : Integer;
                main : real;
            BEGIN
                b:= foo1();
                b:= foo2();
            END
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_FunctionNotReturn_4(self):
        """Function Not Return """
        input = """
        FUNCTION foo1():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                IF true THEN return 1;
                ELSE return 2;
            END
        FUNCTION foo2():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                IF true THEN return 1;
                ELSE a := 5;
            END
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF INTEGER;
                b : Integer;
                main : real;
            BEGIN
                b:= foo1();
                b:= foo2();
            END
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_FunctionNotReturn_5(self):
        """Function Not Return """
        input = """
        FUNCTION foo1():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                IF true THEN return 1;
                ELSE 
                    BEGIN
                        A:=10;
                        return 2;
                    END
            END
        FUNCTION foo2():integer;
            VAR a :integer;
                arr1 : ARRAY [1 .. 5] OF INTEGER;
            BEGIN
                IF true THEN return 1;
                ELSE 
                    BEGIN
                        While true do
                            a := 5;
                    END
            END
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF INTEGER;
                b : Integer;
                main : real;
            BEGIN
                b:= foo1();
                b:= foo2();
            END
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_FunctionNotReturn_6(self):
        """Function Not Return """
        input = """
        procedure test();
            begin
            end
        function foo1(): Integer; 
            var c1:integer;
            begin
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_FunctionNotReturn_7(self):
        """Function Not Return """
        input = """
        procedure test();
            begin
            end
        function foo2(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                    END
                ELSE
                    BEGIN
                    END
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_FunctionNotReturn_8(self):
        """Function Not Return """
        input = """
        procedure test();
            begin
            end
        function foo2(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                    END
                ELSE
                    Return C1;
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_FunctionNotReturn_9(self):
        """Function Not Return """
        input = """
        function isPrime1(index:integer):integer;
        Var c1,b: Integer;
        begin
            if (c1 <> 5.2) and (c1 >= 10) then return c1;
            FOR b := 2 TO 5 DO
                RETURN c1*2;
            WITH
                proce : string;
                a: integer;
            DO
                begin
                    a := a + 1;
                end
        end
        procedure main();
        begin
            isPrime(5);
        end
        """
        expect = "Function isPrime1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_FunctionNotReturn_10(self):
        """Function Not Return """
        input = """
        function isPrime1(index:integer):integer;
        Var c1,b: Integer;
        begin
            if (c1 <> 5.2) and (c1 >= 10) then return c1;
            FOR b := 2 TO 5 DO
                begin
                    RETURN c1*2;
                end
            while true do 
            begin
                main();
                c1 := b + 4;
                for b := 1 to 3 do return 20;
            end
            WITH
                proce : string;
                a: integer;
            DO
                begin
                    a := a + 1;
                end
        end
        procedure main();
            begin
                isPrime1(5);
            end
        """
        expect = "Function isPrime1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_FunctionNotReturn_11(self):
        input = """
        function foo1(): Integer; 
            var c1:integer;
                c2:real;
                c3:boolean;
                c4:string;
            begin
                if (c1 > 5) then return c1;
            end
        procedure main();
            begin
                foo1();
            end
        """
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_FunctionNotReturn_12(self):
        input = """
        function isPrime(index:integer):integer;
        begin
            for index := 1 to 10 do
            begin
                for index := 1 to 10 do
                    break;
                while index < 10 do
                    continue;
                if index > 1 then break; else continue;
                return 10;
            end
        end
        procedure main();
        begin
            isPrime(5);
        end
        """
        expect = "Function isPrimeNot Return "
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_FunctionNotReturn_13(self):
        input = """
        function foo1(): Integer; 
        var c1:integer;
            c2:real;
            c3:boolean;
            c4:string;
        begin
            if (c1 > 5) then return c1;
            else c2 := c2 + c1;
        end
        procedure main();
        begin
            foo1();
        end
        """
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_FunctionNotReturn_14(self):
        """Function Not Return """
        input = """
        function foo(): Integer; 
        var c1:integer;
            c2:real;
            c3:boolean;
            c4:string;
        begin
            while true do return 5;
        end
        var a: Integer;
        procedure main();
        begin
            a := a + foo();
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_FunctionNotReturn_15(self):
        """Function Not Return """
        input = """
        procedure test();
            begin
                return;
            end
        function foo2(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                        C1 := 45;
                    END
                ELSE
                    Return C1;
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_FunctionNotReturn_16(self):
        """Function Not Return """
        input = """
        procedure test();
            begin
                return;
            end
        function foo2(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                        C1 := 45;
                        return C1;
                    END
                ELSE
                    Return C1;
            end
        function foo1(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                        C1 := 45;
                    END
                ELSE
                    Return C1;
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_FunctionNotReturn_17(self):
        """Function Not Return """
        input = """
        procedure test();
            begin
                return;
            end
        function toilaTham(): Integer; 
            var c1:integer;
            begin
                While false Do return C1;
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function toilaThamNot Return "
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_FunctionNotReturn_18(self):
        """Function Not Return """
        input = """
        function lopp(): Integer; 
            var c1:integer;
            begin
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function loppNot Return "
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_FunctionNotReturn_19(self):
        """Function Not Return """
        input = """
        function foo2(): Integer; 
            var c1:integer;
            begin
                while true do
                Begin 
                    For c1:= 5 to 6 do return 3;
                end
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_FunctionNotReturn_20(self):
        """Function Not Return """
        input = """
        function foo2(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                        C1 := 45;
                    END
                ELSE
                    Return C1;
            end
        procedure main(); 
            Var a : integer;
            begin
            end
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_FunctionNotReturn_21(self):
        """Function Not Return """
        input = """
        function diem10(): Integer; 
            var c1:integer;
            begin
                IF true THEN
                    BEGIN
                        C1 := 45;
                        while false do c1 :=4;
                    END
                ELSE
                    Return C1;
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function diem10Not Return "
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_FunctionNotReturn_22(self):
        """Function Not Return """
        input = """
        function foo2(): Integer; 
            var c1:integer;
            begin
                c1 := 5;
            end
        procedure main(); 
            Var a : integer;
            begin
                a := foo1();
                test();
            end
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input, expect, 499))

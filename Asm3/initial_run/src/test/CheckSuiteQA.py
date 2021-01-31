import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    # check redeclare
    def test_0(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z, x;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i,j,k;
                        i = x;
                    EndBody.
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_1(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f,g,h;
                            f = x;
                        Else
                            Var: n;
                            z = {3,4};
                        EndIf.
                    EndBody.
                    Function: x
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Function: x"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f,g,h;
                            f = x;
                        Else
                            Var: n;
                            z = {3,4};
                        EndIf.
                    EndBody.
                    Function: x
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Function: x"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2], z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f,g,h;
                            f = x;
                        Else
                            Var: n;
                            z = {3,4};
                        EndIf.
                    EndBody.
                    Function: foo
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f,g,h;
                            f = x;
                        Else
                            Var: n;
                            z = {3,4};
                        EndIf.
                    EndBody.
                    Function: main
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c, a
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f,g,h;
                            f = x;
                        Else
                            Var: n;
                            z = {3,4};
                        EndIf.
                    EndBody.
                    Function: main
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                    EndBody.
                    Function: b
                        Body:
                            y = 5.0;
                    EndBody.
                    Function: y
                        Body:
                            y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Function: y"
    def test_7(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: a[1];
                    EndBody.
                    Function: b
                        Body:
                            y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_8(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: x, y, z, c;
                    EndBody.
                    Function: b
                        Body:
                            y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_9(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: x;
                        Var: x = 1;
                    EndBody.
                    Function: b
                        Body:
                            y = 5.0;
                    EndBody.
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,409))

    # check TypeMismatchInStatement

    def test_10(self):
        """Simple program: main"""
        input = """
                    Var: x = 3, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = 1.0;
                    EndBody.
                    Function: b
                        Body:
                            y = 5.0;
                    EndBody.
                """
        expect = "Type Mismatch In Statement: Assign(Id(x),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_11(self):
        """Simple program: main"""
        input = """
                    Var: x = 3, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = y;
                    EndBody.
                    Function: b
                        Body:
                            y = 5.0;
                    EndBody.
                """
        expect = "Type Mismatch In Statement: Assign(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = 3;
                        Return b +. 1.0;
                    EndBody.
                    Function: boo
                        Body:
                            x = main(2,3.0,4);
                            y = main(1,2.0,3);
                    EndBody.
                """
        expect = "Type Mismatch In Statement: Assign(Id(x),CallExpr(Id(main),[IntLiteral(2),FloatLiteral(3.0),IntLiteral(4)]))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = 3;
                        Return b +. 1.0;
                    EndBody.
                    Function: boo
                        Body:
                            y = main(1,2.0,3);
                            x = 1.0 +. y;
                    EndBody.
                """
        expect = "Type Mismatch In Statement: Assign(Id(x),BinaryOp(+.,FloatLiteral(1.0),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        input = """
                    Var: u, d[5];
                    Function: main
                    Parameter: q , x, y, t
                    Body:   
                        y = 1.0;                                    
                        y = foo(1.0);
                        t = foo(1.0);
                    EndBody.
                    Function: foo
                    Parameter: y
                    Body: 
                        Var: x;
                        Return 1;
                    EndBody.
                """
        expect = """Type Mismatch In Statement: Return(IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = 3;
                        Return b +. 1.0;
                    EndBody.
                    Function: boo
                        Body:
                            y = main(1,2.0,3);
                            z[y] = y *. 2.0;
                    EndBody.
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(z),[Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = 3;
                        Return b +. 1.0;
                    EndBody.
                    Function: boo
                        Body:
                            For (x = 1.0, x < 3, 2) Do
                                y = main(1,2.0,3);
                                z[2] = {1,2};
                            EndFor.
                    EndBody.
                """
        expect = "Type Mismatch In Statement: For(Id(x),FloatLiteral(1.0),BinaryOp(<,Id(x),IntLiteral(3)),IntLiteral(2),[],[Assign(Id(y),CallExpr(Id(main),[IntLiteral(1),FloatLiteral(2.0),IntLiteral(3)])),Assign(ArrayCell(Id(z),[IntLiteral(2)]),ArrayLiteral(IntLiteral(1),IntLiteral(2)))])"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z[2];
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: y = 2.0;
                        x = 3;
                        Return b +. 1.0;
                    EndBody.
                    Function: boo
                        Body:
                            While(x < 2) Do
                                x = 1.0;
                                z[2] = {1,2};
                            EndWhile.
                    EndBody.
                """
        expect = "Type Mismatch In Statement: Assign(Id(x),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z;
                    Function: main
                    Body:
                        foo(z,y);
                    EndBody.
                    Function: foo
                    Parameter: a,b,c
                    Body:
                        foo(a,b,c);
                    EndBody.
                """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(z),Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = """
                    Var: x, y[2][2] = {{1,2},{1,2}};
                    Function: main
                    Body:
                        x = 1;
                        foo(x)[1][1] = "a";
                    EndBody.
                    Function: foo
                    Parameter: x
                    Body:
                        Return {{1,2},{1,2}};
                    EndBody.
                """
        expect = """Type Mismatch In Statement: Return(ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(2))))"""
        self.assertTrue(TestChecker.test(input,expect,419))

    # check undeclare
    def test_420(self):
        """Simple program: main"""
        input = """
                    Var: foo;
                    Function: main
                    Parameter: foo
                    Body: 
                        Var: y = 1;
                        foo();
                    EndBody.
                    Function: boo
                    Body:
                        Var: boo, y, z;
                    EndBody.
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        """Simple program: main"""
        input = """
                    Function: main
                    Body: 
                        foo();
                    EndBody.
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,421))
    # check undeclare
    def test_422(self):
        """Simple program: main"""
        input = """
                    Function: main
                    Body: 
                        Var: x, y, z;
                        main();
                    EndBody.
                    Function: foo
                    Body:
                        x = 1;
                    EndBody.
                """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        """Simple program: main"""
        input = """
                    Function: main
                    Body: 
                        y = 1;
                        main();
                    EndBody.
                    Function: foo
                    Body:
                        Var: x, y, z;
                    EndBody.
                """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_424(self):
        """Simple program: main"""
        input = """
                    Var: foo;
                    Function: main
                    Body: 
                        Var: y = 1;
                        main();
                        foo();
                    EndBody.
                    Function: boo
                    Body:
                        Var: x, y, z;
                    EndBody.
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    # check Type Mismatch In Expression
    def test_425(self):
        input = """
                    Var: uh, d[5];
                    Function: main
                    Parameter: q , x, y, t
                    Body:                                       
                        y = foo(string_of_float("1.2") +. foo(1.2));
                        uh = string_of_float(y);
                        t = foo(1.2);
                        d[4] = t;
                    EndBody.
                    Function: foo
                    Parameter: y
                    Body: 
                        Var: x;
                        d[3] = 1;
                    EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(string_of_float),[StringLiteral(1.2)])"""
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_426(self):
        input = """
                    Var: u, d[5];
                    Function: main
                    Parameter: q , x, y, t
                    Body:   
                        y = 1.0;                                    
                        y = foo(1.0);
                        t = foo(1);
                        d[4] = t;
                    EndBody.
                    Function: foo
                    Parameter: y
                    Body: 
                        Var: x;
                        d[3] = 1;
                        Return 1.0;
                    EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_427(self):
        input = """
                    Var: u, d[5];
                    Function: main
                    Parameter: q , x, y, t
                    Body:   
                        y = 1.0;                                    
                        y = foo(1.0);
                        t = foo(1.0);
                    EndBody.
                    Function: foo
                    Parameter: y
                    Body:
                        If ( y < 1) Then
                            Var: x;
                            Return 1;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Expression: BinaryOp(<,Id(y),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_428(self):
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: a;
                        foo(y);
                        a = y + 2.5;
                    EndBody.
                """
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(y),FloatLiteral(2.5))"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_429(self):
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: a;
                        foo(y);
                        a = y +. 2.5;
                    EndBody.
                """
        expect = """Type Mismatch In Expression: BinaryOp(+.,Id(y),FloatLiteral(2.5))"""
        self.assertTrue(TestChecker.test(input,expect,429))

    # check Type Cannot Be Inferred
    def test_430(self):
        input = """
                    Function: foo 
                    Parameter: x
                    Body: 
                        Var: a=1;
                        a=foo(x); 
                    EndBody.
                    Function: main 
                    Body: 
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),CallExpr(Id(foo),[Id(x)]))"""
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_431(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Body:
                        y = x + foo(z);
                    EndBody.
                    Function: foo
                    Parameter: a
                    Body:
                    EndBody.
                """
        expect = "Type Cannot Be Inferred: Assign(Id(y),BinaryOp(+,Id(x),CallExpr(Id(foo),[Id(z)])))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_432(self):
        input = """
                    Var: x[2][2], y[2][2] = {{1,2},{1,2}}, m[3][3];
                    Function: main
                    Parameter: t, q, k
                    Body:
                        t = y[1][1] + 1;
                        q = x[1][1] + 1;
                        x[k][1] = 1;
                        foo(m) = x;
                    EndBody.
                    Function: foo
                    Parameter: x[1][2]
                    Body:
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(CallExpr(Id(foo),[Id(m)]),Id(x))"""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_433(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: t, q, k
                    Body:
                        t = x;
                        q = y;
                    EndBody.
                    Function: foo
                    Parameter: z
                    Body:
                        Return z;
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(t),Id(x))"""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_434(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: t, q, k
                    Body:
                        x = 1;
                        t = x;
                        q = t;
                        y = q;
                    EndBody.
                    Function: foo
                    Parameter: z, a, b
                    Body:
                        a = b;
                        Return z;
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_435(self):
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        Return 1;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: a;
                        foo(a);
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: CallStmt(Id(foo),[Id(a)])"""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_436(self):
        input =  """
                    Function: foo
                    Parameter: x, y, z
                    Body: 
                        x = 1;
                        Return 1;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: a, b;
                        foo(a, b, 1);
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: CallStmt(Id(foo),[Id(a),Id(b),IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_437(self):
        input =  """
                    Function: foo
                    Parameter: x, y, z
                    Body: 
                        x = 1;
                        Return 1;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: a, b;
                        a = foo(a, b, b);
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),CallExpr(Id(foo),[Id(a),Id(b),Id(b)]))"""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_438(self):
        input =  """
                    Function: foo
                    Parameter: x
                    Body: 
                        Return x;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: a, b;
                        b = foo(a);
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Return(Id(x))"""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        input = """
                    Function: main
                    Parameter: x
                    Body: 
                    For (x = 1, True, 2) Do
                        Var: a;
                        x = x + 1;
                        For (x = 1, True, 3) Do
                            Var: b;
                            a = b;
                        EndFor.
                    EndFor.
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_440(self):
        input = """
                    Function: main
                    Parameter: x
                    Body: 
                    Var: y = 1.2;
                    y = main(3);
                    If (x > 2) Then
                        Return 2;
                    Else
                        Return 3.0;
                    EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: Return(IntLiteral(2))"""
        self.assertTrue(TestChecker.test(input,expect,440))


    # random check
    def test_441(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        a = foo(1, 1) +. 1.0;
                        Return True;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If main(1,1) Then
                            Return 1;
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[IntLiteral(1),IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_442(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        a = foo(1, 1) +. 1.0;
                        Return True;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If main(1.1,1) Then
                            Return foo(1, 1);
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: Return(IntLiteral(0))"""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        a = foo(1, 1) + 1;
                        Return True;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If main(1.1,1) Then
                            Return foo(1, 1);
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[FloatLiteral(1.1),IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If x[2][2] Then
                            Return 1;
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: If(ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[Return(IntLiteral(1))])Else([],[Return(IntLiteral(0))])"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf x[2][2] Then
                            Return 1;
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: If(BooleanLiteral(true),[],[Return(IntLiteral(1))])ElseIf(ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[Return(IntLiteral(1))])Else([],[Return(IntLiteral(0))])"""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_446(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf False Then
                            For (y = 1, y + 2, y + 3) Do
                                Return y;
                            EndFor.
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(+,Id(y),IntLiteral(2)),BinaryOp(+,Id(y),IntLiteral(3)),[],[Return(Id(y))])"""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf False Then
                            For (y = 1, True, False) Do
                                Return y;
                            EndFor.
                        Else
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: For(Id(y),IntLiteral(1),BooleanLiteral(true),BooleanLiteral(false),[],[Return(Id(y))])"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_448(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf False Then
                            For (y = 1, True, False) Do
                                Return y;
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (bool_of_string("1"))
                            EndDo.
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: For(Id(y),IntLiteral(1),BooleanLiteral(true),BooleanLiteral(false),[],[Return(Id(y))])"""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_449(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf False Then
                            For (y = 1, True, 3) Do
                                Return y;
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (3)
                            EndDo.
                            Return 0;
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: Dowhile([],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(1)))],IntLiteral(3))"""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;
                    Function: main
                    Parameter: main
                    Body:
                        main(1,2,3);
                    EndBody.

                """
        expect = """Undeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_451(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf False Then
                            For (y = 1, True, 3) Do
                                Return y;
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (False)
                            EndDo.
                            Return float_of_int(5);
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: Return(CallExpr(Id(float_of_int),[IntLiteral(5)]))"""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_452(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf foo(2,3) Then
                            For (y = 1, True, 3) Do
                                Return y;
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (False)
                            EndDo.
                            Return float_of_int(5);
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Statement: If(BooleanLiteral(true),[],[Return(IntLiteral(1))])ElseIf(CallExpr(Id(foo),[IntLiteral(2),IntLiteral(3)]),[],[For(Id(y),IntLiteral(1),BooleanLiteral(true),IntLiteral(3),[],[Return(Id(y))])])Else([],[Dowhile([],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(1)))],BooleanLiteral(false)),Return(CallExpr(Id(float_of_int),[IntLiteral(5)]))])"""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_453(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf f(2,3) Then
                            For (y = 1, True, 3) Do
                                Return y;
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (False)
                            EndDo.
                            Return float_of_int(5);
                        EndIf.
                    EndBody.
                """
        expect = """Undeclared Function: f"""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_454(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g, main
                    Body:
                        If True Then
                            Return 1;
                        ElseIf True Then
                            For (y = 1, True, 3) Do
                                Return main(1,3);
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (False)
                            EndDo.
                            Return float_of_int(5);
                        EndIf.
                    EndBody.
                """
        expect = """Undeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_455(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b, x[2][2]
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf True Then
                            For (y = 1, True, 3) Do
                                Return main(1, 3);
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (False)
                            EndDo.
                            Return float_of_int(5);
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[IntLiteral(1),IntLiteral(3)])"""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b, x[2][2]
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        If True Then
                            Return 1;
                        ElseIf True Then
                            For (y = 1, True, 3) Do
                                Return main(1, 3, {True});
                            EndFor.
                        Else
                            Do
                                y = y + 1;
                            While (False)
                            EndDo.
                            Return main(1, 3, {1});
                        EndIf.
                    EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[IntLiteral(1),IntLiteral(3),ArrayLiteral(IntLiteral(1))])"""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_457(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{True, True},{True, True}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        For (y=1,y<10,x[2][2]) Do 
                            If y<1 Then y=1;
                            EndIf.
                        EndFor.
                    EndBody.
                """
        expect = "Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(<,Id(y),IntLiteral(10)),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_458(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{True, True},{True, True}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return 1;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        For (y=1,y<10,x[2][2]) Do 
                            If y<1 Then
                                y=1;
                            EndIf.
                        EndFor.
                    EndBody.
                """
        expect = "Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(<,Id(y),IntLiteral(10)),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_459(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n > 10 Then
                            Return 5;
                        ElseIf n > 5 Then x=y+z; Return a;
                        ElseIf n < 10 Then a=a+1; Return a;
                        Else
                            Return 1.2;
                        EndIf.
                    EndBody."""
        expect = """Type Mismatch In Statement: Return(FloatLiteral(1.2))"""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_460(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n > 10 Then
                            Return a;
                        ElseIf n > 5 Then x=y+z; Return a;
                        ElseIf n < 10 Then a=a+1; Return a;
                        Else
                            Return 1.2;
                        EndIf.
                    EndBody."""
        expect = """Type Cannot Be Inferred: Return(Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_461(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n > 10 Then
                            Return 1;
                        ElseIf n > 5 Then 
                            x=y+z; 
                            Return x;
                        ElseIf n < 10 Then 
                            a = a +. 1.0; 
                            Return a;
                        Else
                            Return y;
                        EndIf.
                    EndBody."""
        expect = """Type Mismatch In Statement: Return(Id(a))"""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_462(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n > 10 Then
                            Return 1;
                        ElseIf n > 5 Then 
                            x=y+z; 
                            Return x;
                        ElseIf n < 10 Then 
                            a = a +. 1.0; 
                            Return main({1,2,3});
                        Else
                            Return y;
                        EndIf.
                    EndBody."""
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))])"""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_463(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n > 10 Then
                            Return 1;
                        ElseIf n > 5 Then 
                            x=y+z; 
                            Return x;
                        ElseIf n < 10 Then 
                            a = a +. 1.0; 
                            Return main({1,2,3},1,2,3);
                        Else
                            Return y;
                        EndIf.
                    EndBody."""
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),IntLiteral(1),IntLiteral(2),IntLiteral(3)])"""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_464(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n >= x Then
                            Return 1;
                        ElseIf n > 5 Then 
                            x=y+z; 
                            Return x;
                        ElseIf n < 10 Then 
                            a = a +. 1.0; 
                            Return 1.0 +. main(1,2,3,4);
                        Else
                            Return y;
                        EndIf.
                    EndBody."""
        expect = """Type Mismatch In Expression: BinaryOp(+.,FloatLiteral(1.0),CallExpr(Id(main),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))"""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_465(self):
        """Type Cannot Be Inferred"""
        input = """
                    Var: x[2][2] = {{1, 1},{1, 1}}, y;

                    Function: main
                    Parameter: a,b
                    Body:
                        Return;
                    EndBody.

                    Function: foo
                    Parameter: f, g
                    Body:
                        f = main({1,1}, 1);
                    EndBody.
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_466(self):
        input = """ Var:a;
                    Function: main
                    Parameter: n,x,y,z
                    Body:
                        If n >= x Then
                            Return 1;
                        ElseIf n > 5 Then 
                            x=y+z; 
                            Return x;
                        ElseIf n < 10 Then 
                            a = a +. 1.0; 
                            Return 1.0 +. main(1,2,3,4);
                        Else
                            Return y;
                        EndIf.
                    EndBody."""
        expect = """Type Mismatch In Expression: BinaryOp(+.,FloatLiteral(1.0),CallExpr(Id(main),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))"""
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_467(self):
            """Type Cannot Be Inferred"""
            input = """
                        Var: x[2][2] = {{1,1},{1,1}};
                        Var: y;
                        Function: main
                        Parameter: a[2][2],b
                        Body:
                            main({{1,1},{1,1}}, y);
                            main(x, y);
                        EndBody.
                    """
            expect = "Type Cannot Be Inferred: CallStmt(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(1)),ArrayLiteral(IntLiteral(1),IntLiteral(1))),Id(y)])"
            self.assertTrue(TestChecker.test(input,expect,467))

    def test_468(self):
            """Type Cannot Be Inferred"""
            input = """
                        Var: x[2][2] = {{1,1},{1,1}};
                        Var: y;
                        Function: main
                        Parameter: a[2][2],b
                        Body:
                            y = 2;
                            x = main(x, y);
                            Return a;
                        EndBody.
                        Function: foo
                        Parameter: a, b[2][2]
                        Body:
                            a = main(main({{1,1},{1,1}}, y), y);
                        EndBody.
                    """
            expect = "Type Mismatch In Statement: Assign(Id(a),CallExpr(Id(main),[CallExpr(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(1)),ArrayLiteral(IntLiteral(1),IntLiteral(1))),Id(y)]),Id(y)]))"
            self.assertTrue(TestChecker.test(input,expect,468))

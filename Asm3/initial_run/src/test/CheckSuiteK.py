import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(
            CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [
                    CallExpr(Id("read"), [IntLiteral(4)])
                ])]))])
        expect = str(TypeMismatchInExpression(
            CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f;
                            f = x;
                        Else
                            Var: n;
                            f = 3;
                        EndIf.

                    EndBody.
                """
        expect = str(Undeclared(Identifier(),"f"))
        self.assertTrue(TestChecker.test(input,expect,406))
    #
    def test_407(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        y = 2;
                        If (j == 2) Then
                            Var: f;
                            f = x;
                        Else
                            z = 3.0;
                        EndIf.
                    EndBody.
                    Function: foo
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('y'),FloatLiteral(5.0))))
        self.assertTrue(TestChecker.test(input,expect,407))

    # REDECLARE====================================================
    def test_408(self):
        input = """
                    Var: x, y, z, x;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main();
                    EndBody.
                """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_409(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: a, y, z;
                        x = 1;
                        y = 2;
                        main();
                    EndBody.
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c,a
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                    Function: main
                    Body:
                    EndBody.
                """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,411))


    def test_412(self):
        input = """
                    Function: foo
                    Body:
                        Var: foo;
                    EndBody.
                    Function: main
                    Parameter: main
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                    Function: foo
                    Body:
                        Var: foo;
                    EndBody.
                """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = """
                    Var: foo,a,b[1],c;
                    Function: foo
                    Body:
                        Var: foo;
                    EndBody.
                    Function: main
                    Parameter: main
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        input = """
                    Var: a,b[1],c;
                    Function: foo
                    Body:
                        Var: foo;
                    EndBody.
                    Function: b
                    Body:
                        Var: foo;
                    EndBody.
                    Function: main
                    Parameter: main
                    Body:
                        Var: c, e, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                """
        expect = """Redeclared Function: b"""
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_415(self):
        input = """
                    Var: a,b[1],c;
                    Function: int_of_float
                    Body:
                        Var: foo;
                    EndBody.
                    Function: b
                    Body:
                        Var: foo;
                    EndBody.
                    Function: main
                    Parameter: main
                    Body:
                        Var: c, e, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                """
        expect = """Redeclared Function: int_of_float"""
        self.assertTrue(TestChecker.test(input,expect,415))

    # UNDECLARED====================================================

    def test_416(self):
        input = """
                    Function: foo
                    Body:
                        Var: foo;
                    EndBody.
                    Function: main
                    Parameter: main
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                """
        expect = """Undeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_417(self):
        input = """
                    Var: x, y, z;
                    Function: foo
                    Body:
                        Var: foo;
                        a = 1;
                    EndBody.
                    Function: main
                    Parameter: main
                    Body:
                        Var: x, y, z;
                        x = 1;
                        y = 2;
                        main(1,2,3);
                    EndBody.
                """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_418(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Body:
                        Var: foo;
                        foo();
                        a = 1;
                    EndBody.
                """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Body:
                        Var: foo;
                        a = foo() + 1;
                        a = 1;
                    EndBody.
                """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_420(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Body:
                        Var: foo;
                        foo(a)[1][1] = a;
                        a = 1;
                    EndBody.
                """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo;
                        a = 1;
                    EndBody.
                    Function: foo
                    Body:
                        x = 2;
                        a = 1;
                    EndBody.
                """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,421))
    
    # Type Cannot Be Inferred ====================================================
    def test_422(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo;
                        a = y;
                    EndBody.
                    Function: foo
                    Body:
                        x = 2;
                        a = 1;
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        a = foo(x) + 1;
                    EndBody.
                    Function: foo
                    Parameter: a
                    Body:
                        x = 2;
                        a = 1;
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),BinaryOp(+,CallExpr(Id(foo),[Id(x)]),IntLiteral(1)))"""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_424(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        x = 1;
                        a = foo(x) + 1;
                    EndBody.
                    Function: foo
                    Parameter: a
                    Body:
                        x = 2;
                        a = 1;
                    EndBody.
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_425(self):
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        x = foo(x) + z;
                    EndBody.
                    Function: foo
                    Parameter: a
                    Body:
                        x = 2;
                        a = 1;
                    Return x;
                    EndBody.
                """
        expect = """Type Cannot Be Inferred: Assign(Id(x),BinaryOp(+,CallExpr(Id(foo),[Id(x)]),Id(z)))"""
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_426(self):
        input = """
                    Var: x, y, z;
                    Function: foo
                    Parameter: a
                    Body:
                        a = 1.2;
                    Return a;
                    EndBody.

                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        main(foo(x),main(x,y,z),1);
                    EndBody.
                    
                """
        expect = """Type Cannot Be Inferred: CallExpr(Id(main),[Id(x),Id(y),Id(z)])"""
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_427(self):
        input = """
                    Var: x, y, z;
                    Function: foo
                    Parameter: a ,b,c
                    Body:
                        a = 1.2;
                        b = 1;
                    Return a;
                    EndBody.
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        main(foo(x,y,z),1,1);
                    EndBody.
                    
                """
        expect = """Type Cannot Be Inferred: CallExpr(Id(foo),[Id(x),Id(y),Id(z)])"""
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_428(self):
        input = """
                    Var: x, y, z;
                    Function: foo
                    Parameter: a ,b,c
                    Body:
                        a = 1.2;
                        b = 1;
                    Return a;
                    EndBody.
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        main(foo(x,y,z),1,1);
                    EndBody.
                    
                """
        expect = """Type Cannot Be Inferred: CallExpr(Id(foo),[Id(x),Id(y),Id(z)])"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_429(self):
        input = """
                    Var: x, y, z;
                    Function: foo
                    Parameter: a,b,c
                    Body:
                        a = 1.2;
                        b = 1;
                    Return a;
                    EndBody.
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: foo11;
                        a = main(foo(x,y,z),1,1) + 1 ;
                    EndBody.
                    
                """
        expect = """Type Cannot Be Inferred: Assign(Id(a),BinaryOp(+,CallExpr(Id(main),[CallExpr(Id(foo),[Id(x),Id(y),Id(z)]),IntLiteral(1),IntLiteral(1)]),IntLiteral(1)))"""
        self.assertTrue(TestChecker.test(input,expect,429))
    # Type Mismatch In Statement: ====================================================

    def test_430(self):
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
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_431(self):
        input = """ Function: main
        Parameter: n,a[2],b[5][6],m
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+.1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = """Type Mismatch In Expression: BinaryOp(+.,Id(a),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_432(self):
        input = """ Function: main
        Parameter: a[2],b[5][6]
        Body:
            Var:c,d;
            If c > 10 Then
                Return 5;
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_433(self):
        input = """ Function: main
        Parameter: a[2],b[5][6]
        Body:
            Var:c,d;
            If c + 10 Then
                Return 5;
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = """Type Mismatch In Statement: If(BinaryOp(+,Id(c),IntLiteral(10)),[],[Return(IntLiteral(5))])ElseIf(BinaryOp(>,Id(c),IntLiteral(5)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(Id(a))])Else([],[Return(BooleanLiteral(false))])"""
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_434(self):
        input = """ Function: main
        Parameter: a[2],b[5][6]
        Body:
            Var:c,d;
            If c + 10 Then
                Return 5;
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = """Type Mismatch In Statement: If(BinaryOp(+,Id(c),IntLiteral(10)),[],[Return(IntLiteral(5))])ElseIf(BinaryOp(>,Id(c),IntLiteral(5)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(Id(a))])Else([],[Return(BooleanLiteral(false))])"""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_435(self):
        input = """ Function: main
        Parameter: a[2],b[5][6]
        Body:
            Var:c,d;
            If c + 10 Then
                Return 5;
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = """Type Mismatch In Statement: If(BinaryOp(+,Id(c),IntLiteral(10)),[],[Return(IntLiteral(5))])ElseIf(BinaryOp(>,Id(c),IntLiteral(5)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(Id(a))])Else([],[Return(BooleanLiteral(false))])"""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_436(self):
        input = """ Function: main
        Parameter: a[2],b[5][6]
        Body:
            Var:c,d;
            If c + 10 Then
                Return 5;
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = """Type Mismatch In Statement: If(BinaryOp(+,Id(c),IntLiteral(10)),[],[Return(IntLiteral(5))])ElseIf(BinaryOp(>,Id(c),IntLiteral(5)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(Id(a))])Else([],[Return(BooleanLiteral(false))])"""
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_436(self):
        input = """Function: main
        Parameter: x,a,aa
        Body:   For (a=5+a,1,aa+1) Do main(a,a,a); EndFor.
        EndBody."""
        expect = """Type Mismatch In Statement: For(Id(a),BinaryOp(+,IntLiteral(5),Id(a)),IntLiteral(1),BinaryOp(+,Id(aa),IntLiteral(1)),[],[CallStmt(Id(main),[Id(a),Id(a),Id(a)])])"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_437(self):
        input = """Function: main
        Parameter: x,a,aa
        Body:   For (a = 5.0 ,a<10,aa+1) Do main(a,a,a); EndFor.
        EndBody."""
        expect = """Type Mismatch In Statement: For(Id(a),FloatLiteral(5.0),BinaryOp(<,Id(a),IntLiteral(10)),BinaryOp(+,Id(aa),IntLiteral(1)),[],[CallStmt(Id(main),[Id(a),Id(a),Id(a)])])"""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_438(self):
        input = """Function: main
        Parameter: x,a,aa
        Body:   For (a = 5 ,a<10, 1.0) Do main(a,a,a); EndFor.
        EndBody."""
        expect = """Type Mismatch In Statement: For(Id(a),IntLiteral(5),BinaryOp(<,Id(a),IntLiteral(10)),FloatLiteral(1.0),[],[CallStmt(Id(main),[Id(a),Id(a),Id(a)])])"""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        input = """Function: main
        Parameter: x,a
        Body:
            Var:i;
            For (i = 0, i < 10, 2) Do
                While (1) Do
                For (i = 0, i < 10, 2) Do
                Var:a=1;
                main(i,i);
                a=b;
                EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = """Type Mismatch In Statement: While(IntLiteral(1),[],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[VarDecl(Id(a),IntLiteral(1))],[CallStmt(Id(main),[Id(i),Id(i)]),Assign(Id(a),Id(b))])])"""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_440(self):
        input = """Function: main
        Parameter: x,i
        Body:   Do
                main(i);
                While (1)
                EndDo.
        EndBody."""
        expect = """Type Mismatch In Statement: Dowhile([],[CallStmt(Id(main),[Id(i)])],IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_441(self):
        input = """Function: main
        Parameter: i,a
        Body:   Do
                i=1;
                main(i,i);
                Do
                    main(i,i);
                While (a==12+3)
                EndDo.
                Do
                    main(i,i);
                While (a==12+3)
                EndDo.
                While ({1,2,3})
                EndDo.
        EndBody."""
        expect = """Type Mismatch In Statement: Dowhile([],[Assign(Id(i),IntLiteral(1)),CallStmt(Id(main),[Id(i),Id(i)]),Dowhile([],[CallStmt(Id(main),[Id(i),Id(i)])],BinaryOp(==,Id(a),BinaryOp(+,IntLiteral(12),IntLiteral(3)))),Dowhile([],[CallStmt(Id(main),[Id(i),Id(i)])],BinaryOp(==,Id(a),BinaryOp(+,IntLiteral(12),IntLiteral(3))))],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_442(self):
        input = """
        Var: i = 1;
        Function: main
        Parameter: x,i
        Body:   
            x = void();
        EndBody.
        Function: void
        Body:   
            i = 1;
        EndBody."""
        expect = """Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(void),[]))"""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
        input = """
        Var: i = 1,c,a;
        Function: void
        Body:   
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            x = void();
        EndBody.
        """
        expect = """Type Mismatch In Statement: Return(BooleanLiteral(false))"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            If True Then
                Return {1,2,3};
            ElseIf c > 5 Then a=a+1; Return a;
            Else
                Return {1,2,3};
            EndIf.
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void()[1] = x;
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void()[1] = x;
        EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(CallExpr(Id(void),[]),[IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_446(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            x[1] = 1;
            void()[1] = x;
        EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            x = void() + 1;
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(void),[]),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_448(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            Return 1;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void();
        EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(void),[])"""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_449(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(a,b);
        EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(void),[Id(a),Id(b)])"""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(a,b);
        EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(void),[Id(a),Id(b)])"""
        self.assertTrue(TestChecker.test(input,expect,450))


    def test_451(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Parameter: a,c,b
        Body:   
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(a,1,2,3);
        EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(void),[Id(a),IntLiteral(1),IntLiteral(2),IntLiteral(3)])"""
        self.assertTrue(TestChecker.test(input,expect,451))


    def test_452(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Parameter: a,b,c[2]
        Body:   
            a = a+1;
            b = b +. 1.2;
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(1, 1.2, 1);
        EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(void),[IntLiteral(1),FloatLiteral(1.2),IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_453(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Parameter: a,b,c[2]
        Body:   
            a = a+1;
            b = b +. 1.2;
            i = 1;
            Return;
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(1, 1.2, 1);
        EndBody.
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(void),[IntLiteral(1),FloatLiteral(1.2),IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_454(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a,b[1][1],i
Body:
    i = i + main(x[1][1], 1);
EndBody.
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[ArrayCell(Id(x),[IntLiteral(1),IntLiteral(1)]),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_455(self):
        input = """
        Var: i = 1,c,a[1][2];
        Function: void
        Body:   
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a = a+1; Return False;
            Else
                Return False;
            EndIf.
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(a,b);
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        input = """
        Var: i = 1,c,a;
        Function: void
        Body:   
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a = a+1; Return False;
            Else
                Return False;
            EndIf.
        EndBody.
        Function: main
        Parameter: x,i
        Body:   
            void(a,b);
        EndBody.
        """
        expect = """Type Mismatch In Statement: Return(BooleanLiteral(false))"""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_457(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = 1.0 +. void();
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a = a+1; Return False;
            Else
                Return False;
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(IntLiteral(5))"""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_458(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = 1 + void();
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a = a+1; Return False;
            Else
                Return False;
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(BooleanLiteral(false))"""
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_459(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = 1 || void();
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a = a+1; Return False;
            Else
                Return False;
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Expression: BinaryOp(||,IntLiteral(1),CallExpr(Id(void),[]))"""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_460(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = True || void();
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return 5;
            ElseIf c > 5 Then a = a+1; Return False;
            Else
                Return False;
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(IntLiteral(5))"""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_461(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = void()[1] +. 1.0;
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return {1,2,3};
            ElseIf c > 5 Then a = a+1; Return {1,2,4};
            Else
                Return {1,2,3};
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))"""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_462(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = void()[1] || True;
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return {False};
            ElseIf c > 5 Then Return {1,2,4};
            Else
                Return {1,2,3};
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(4)))"""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_463(self):
        input = """
        Var: i = 1,c,a;
        Function: main
        Parameter: x,i
        Body:   
            a = void()[1][2] || True;
        EndBody.
        Function: void
        Body:
            i = 1;
            If True Then
                Return {False};
            ElseIf c > 5 Then Return {1,2,4};
            Else
                Return {1,2,3};
            EndIf.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(ArrayLiteral(BooleanLiteral(false)))"""
        self.assertTrue(TestChecker.test(input,expect,463))


    # Type Mismatch In Expression=========================================

    def test_464(self):
        input = """
        Function: main
        Parameter: x,b,a,c,d,i
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                main(i);
                If (a==2) Then
                Continue;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                main(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                main(i);
                EndWhile.
                EndWhile.
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,BinaryOp(!=,Id(b),Id(c)),BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(d),Id(a)),Id(b)),Id(c)))"""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_465(self):
        input = """Function: main
        Parameter: x
        Body:   
            x[1] = 2;
        EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_466(self):
        input = """Function: main
        Parameter: x[1][2]
        Body:   
            x[1][1.2] = 2;
        EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(1),FloatLiteral(1.2)])"""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_467(self):
        input = """Function: main
        Parameter: x[1]
        Body:   
            x[1][2] = 2;
        EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(1),IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_468(self):
        input = """Function: main
        Parameter: x[1][2][3]
        Body:   
            x[1][2][2] = 2;
            x[1][2] = 4;
        EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(1),IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_469(self):
        input = """Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = x[1][2][2] +. 1.0;
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+.,ArrayCell(Id(x),[IntLiteral(1),IntLiteral(2),IntLiteral(2)]),FloatLiteral(1.0))"""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_470(self):
        input = """Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = x +. 1.0;
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+.,Id(x),FloatLiteral(1.0))"""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_471(self):
        input = """Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = x + y;
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(x),Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_472(self):
        input = """
        Var: b = 5, c = False;
        Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment****followed by a comment**
        """
        expect = """Type Mismatch In Expression: BinaryOp(||,Id(x),BooleanLiteral(true))"""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_473(self):
        input = """
        Var: b = 5, c = False;
        Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = !(2+y);
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment****followed by a comment**
        """
        expect = """Type Mismatch In Expression: UnaryOp(!,BinaryOp(+,IntLiteral(2),Id(y)))"""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_474(self):
        input = """
        Var: b = 5, c = False;
        Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = !(True);
            y = -.z;
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment****followed by a comment**
        """
        expect = """Type Mismatch In Expression: UnaryOp(-.,Id(z))"""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_475(self):
        input = """
        Var: b = 5, c = False;
        Function: main
        Parameter: x[1][2][3],y,z
        Body:   
            x[1][2][2] = 2;
            z = !(True);
            z = main(1,2,3);
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_476(self):
        input = """
        Var: b = 5, c = False;
        Function: main
        Parameter: x[1][2],y,z
        Body:   
            x[1][2] = 2;
            z = !(True);
            z = main({{1,2}},2,True) + main({{1,2}}, 2 ,2);
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2))),IntLiteral(2),IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_477(self):
        input = """
        Var: b = 5, c = False;
        Function: main
        Parameter: x[1][2],y,z
        Body:   
            x[1][2] = 2;
            z = !(True);
            z = main({{1,2}},2,True , 12);
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        """
        expect = """Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2))),IntLiteral(2),BooleanLiteral(true),IntLiteral(12)])"""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_478(self):
        input = """
        Var: b = 5, c = False;
        Function: foo
        Parameter: x[1][2],y,z
        Body:   
            x[1][2] = 2;
            z = !(True);
            z = main({{1,2}},2,True , 12);
            z = x[1][2][2] + y;
            foo(x||True);
        EndBody.
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_479(self):
        input = """
        **Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[3]={1,2,3},d;
        Var:a=1;
        **Declare variable**
        Function: foo
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
        Function: foo2
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_480(self):
        input = """
        Var: b = 5, c = False,main;
        Function: foo
        Parameter: x[1][2],y,z
        Body:   
        EndBody.
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_481(self):
        input = """
        Function: main
        Parameter: x
        Body: 
        x = 1;
        While True Do 
            While False Do
            Var: a;
            a = x;
            a = 10.0;
            EndWhile.
        EndWhile.
        EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(Id(a),FloatLiteral(10.0))"""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_482(self):
        input = """
        Var: z;
        Function: main
        Parameter: x
        Body: 
        x = 1.0;
        While True Do 
            While False Do
            Var: a[3] = {1.0,23.0,4.0};
            a[1] = x +. z;
            EndWhile.
        EndWhile.
        EndBody.
        Function: foo
        Parameter: a,b
        Body:
            z = 2;
        EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(Id(z),IntLiteral(2))"""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_483(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a,b
        Body:
            z = 2;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1.0;
        While True Do 
            While False Do
            Var: a[3] = {1.0,23.0,4.0};
            a[1] = foo(1,2)[1] +. 2.0;
            a[1] = x +. z;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Expression: BinaryOp(+.,Id(x),Id(z))"""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_484(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a[2], b
        Body:
            z = 2;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1.0;
        While True Do 
            While False Do
            Var: a[3] = {1.0,23.0,4.0};
            a[1] = foo(1,2)[1] +. 2.0;
            a[1] = x +. z;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_485(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a[2][3], b
        Body:
            a = 1;
            z = 2;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1.0;
        While True Do 
            While False Do
            Var: a[3] = {1.0,23.0,4.0};
            a[1] = foo(1,2)[1] +. 2.0;
            a[1] = x +. z;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Assign(Id(a),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_486(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1;
            z = 2;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1.0;
        While True Do 
            While False Do
            Var: a[1][2] = {{1.0,23.0}};
            a[1][1] = foo(a,2)[1] +. 2.0;
            a[1] = x +. z;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_487(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1.0;
        While True Do 
            While False Do
            Var: a[1][2] = {{1,23}};
            a[1][1] = foo(a,2)[1] +. 2.0;
            a[1] = x +. z;
            Return 1;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Assign(Id(x),FloatLiteral(1.0))"""
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_488(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1;
        While True Do 
            While False Do
            Var: a[1][2] = {{1,23}};
            a[1][1] = foo(a,2)[1] +. 2.0;
            a[1] = x +. z;
            Return 1;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_489(self):
        input = """
        Var: z;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1;
        While True Do 
            While False Do
            Var: a[1][2] = {{1,23}};
            a[1][1] = foo(a,2.0)[1] +. 2.0;
            For (y=1,y<10,a[2][2]) Do 
                If y<1 Then y=1;
                EndIf.
            EndFor.
            Return 1;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Assign(ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]),BinaryOp(+.,ArrayCell(CallExpr(Id(foo),[Id(a),FloatLiteral(2.0)]),[IntLiteral(1)]),FloatLiteral(2.0)))"""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_489(self):
        input = """
        Var: z,y;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1.0;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1;
            While True Do 
                While False Do
                Var: a[1][2] = {{1.0,23.0}},b[1][2] = {{1,23}};
                a[1][1] = foo(a,2.0)[1] +. 2.0;
                For (y=1,y<10,a[2][2]) Do 
                    If y<1 Then y=1;
                    EndIf.
                EndFor.
                Return 1.2;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(<,Id(y),IntLiteral(10)),ArrayCell(Id(a),[IntLiteral(2),IntLiteral(2)]),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_490(self):
        input = """
        Var: z,y;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1.0;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1;
            While True Do 
                While False Do
                Var: a[1][2] = {{1.0,23.0}},b[1][2] = {{1,23}};
                a[1][1] = foo(a,2.0)[1] +. 2.0;
                For (y=1,y<10,b[2][2]) Do 
                    If y<1 Then y=1;
                    EndIf.
                EndFor.
                Return 1;
            EndWhile.
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_491(self):
        input = """Var: a[3][4], b[2][2] = {{1,2},{1,2}};
            Function: main
            Parameter: x, y, k
            Body:
                x = b[1][1] + 1;
                a[1][1] = 1.2;
                y = a[1][1] + 1;
            EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_492(self):
        input = """Var: a[3][4], b[2][2] = {{1,2},{1,2}};
            Function: main
            Parameter: x, y
            Body:
                x = b[1][1] + 1;
                y = a[1][1] + 1;
                a[1][1] = 1.2;
            EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]),FloatLiteral(1.2))"""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_493(self):
        input = """
        Function: main
                    Parameter: x
                    Body: 
                        x = True;
                        If x Then 
                        x = 1;
                        EndIf.
                    EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(Id(x),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_494(self):
        input = """
        Function: foo
        Parameter: x
        Body: 
            x = True;
            If x Then 
            x = 1;
            EndIf.
        EndBody.
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_494(self):
        input = """
        Var: x;  
        Function: main
        Parameter: a[1], b
        Body: 
            Var: m = 1.0;
            b = -1.0;
        EndBody.
        """
        expect = """Type Mismatch In Expression: UnaryOp(-,FloatLiteral(1.0))"""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_495(self):
        input = """
        Var: x;  
        Function: main
        Parameter: a[4], b, c
        Body: 
            Var: m = 1.0;
            m = m + 1;
            b = -m;
        EndBody.
        """
        expect = """Type Mismatch In Expression: BinaryOp(+,Id(m),IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_496(self):
        input = """
        Var: z,y;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1.0;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1;
            While True Do 
                While False Do
                Var: a[1][2] = {{1.0,23.0}},b[1][2] = {{1,23}};
                a[1][1] = foo(a,2.0)[1] +. 2.0;
                For (y=1,y<10,b[2][2]) Do 
                    If y<1 Then y=1;
                    EndIf.
                EndFor.
                Return 1.2;
            EndWhile.
            Return 1;
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(IntLiteral(1))"""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_496(self):
        input = """
        Var: z,y;
        Function: foo
        Parameter: a[1][2], b
        Body:
            a[2][3] = 1.0;
            z = 2;
            b = main(z) +. 1.0;
            Return {1.0,2.0};
        EndBody.
        Function: main
        Parameter: x
        Body: 
        x = 1;
            While True Do 
                While False Do
                Var: a[1][2] = {{1.0,23.0}},b[1][2] = {{1,23}};
                a[1][1] = foo(a,2.0)[1] +. 2.0;
                For (y=1,y<10,b[2][2]) Do 
                    If y<1 Then y=1;
                    EndIf.
                EndFor.
                Return 1.2;
            EndWhile.
            Return y;
        EndWhile.
        EndBody.
        
        """
        expect = """Type Mismatch In Statement: Return(Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_497(self):

        input = """
                    Var: x;    
                    Function: main
                    Parameter: a[2], b[2], c
                    Body: 
                        a = b;
                    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_498(self):

        input = """
                    Var: x;    
                    Function: main
                    Parameter: a[2], b[2], c
                    Body: 
                        a[1] = b[1] + 1;
                        b[1] = c + 1;
                        c = 0.2;
                    EndBody."""
        expect = "Type Mismatch In Statement: Assign(Id(c),FloatLiteral(0.2))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_499(self):

        input = """
                    Var: x;    
                    Function: main
                    Parameter: a[2], b[2], c
                    Body: 
                        main( {1,2} , {"True", "True"} , 1 );
                        b[1] = "a";
                        a[1] = "a";
                    EndBody."""
        expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(a),[IntLiteral(1)]),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,499))


    
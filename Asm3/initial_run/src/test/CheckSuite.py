import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_400(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_401(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_402(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_403(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_404(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_405(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        """Redeclare Variable"""
        input = """
Var: x, x;
Function: main
Body:
    Var: x=1;
EndBody."""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        """Redeclare Variable"""
        input = """
Var: x[1][1], y;
Function: main
Body:
    If x[1][1] == 0 Then
        Var: a[2][2] = {{1,1},{1,1}};
        Var: a[1] = {1};
        Return 1;
    Else
        Return 0;
    EndIf.
EndBody."""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_408(self):
        input = """
Var: x[1][1], y;
Function: main
Body:
    If x[1][1] == 0 Then
        Var: a[2][2] = {{1,1},{1,1}};
        Var: b[1] = {1};
        Do
            Var: f = "a";
            Var: f[1] = {"b"};
            Break;
        While (True)
        EndDo.
        Return 1;
    Else
        Return 0;
    EndIf.
EndBody."""
        expect = "Redeclared Variable: f"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_409(self):
        """Redeclare Function"""
        input = """
Var: x[1][1], main[2] = {2,2};
Function: main
Body:
    Var: x=1;
EndBody."""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        """Redeclare Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Body:
    Var: x=1;
EndBody.
Function: main
Parameter: a,b
Body:
    Var: x=1;
EndBody."""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        """Redeclare Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: x=1;
EndBody.
Function: foo
Parameter: a,b
Body:
    Var: x=1;
EndBody.
Function: foo
Parameter: a,b
Body:
    Var: x=1;
EndBody.
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_412(self):
        """Redeclare Parameter"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: x=1;
EndBody.
Function: foo
Parameter: a,b,a
Body:
    Var: c=1;
EndBody.
"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        """Redeclare Variable"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: x=1;
EndBody.
Function: foo
Parameter: a,b
Body:
    Var: a[2][2]={{1,1},{2,2}};
EndBody.
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        """Undeclared Identifier"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + d;
EndBody.
"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_415(self):
        """Undeclared Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + b;
    foo();
EndBody.
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_416(self):
        """Undeclared Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + b;
    foo();
EndBody.
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_417(self):
        """Undeclared Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + b;
    a = a + foo()[1][1];
EndBody.
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_418(self):
        """Undeclared Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + b;
    While True
    Do
        foo();
    EndWhile.
EndBody.
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        """Undeclared Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + b;
    While True
    Do
        foo();
    EndWhile.
EndBody.
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_420(self):
        """Undeclared Function"""
        input = """
Var: x[1][1], y[2] = {2,2};
Function: main
Parameter: a,b
Body:
    Var: c[2][2]={{1,1},{2,2}};
    x[0][1] = a + b;
    While True
    Do
        main(1,1);
        foo();
    EndWhile.
EndBody.
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[1][1];
Var: y;
Function: main
Parameter: a,b
Body:
    y = x[1][1];
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(y),ArrayCell(Id(x),[IntLiteral(1),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_422(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[1][1];
Var: y = 1;
Function: main
Parameter: a,b
Body:
    y = x[1][1];
    a = b;
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[1][1];
Var: y = 1;
Function: main
Parameter: a,b
Body:
    main(x[1][1], y);
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[ArrayCell(Id(x),[IntLiteral(1),IntLiteral(1)]),Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_424(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1,1},{1,1}};
Var: y;
Function: main
Parameter: a[2][2],b
Body:
    main({{1,1},{1,1}}, y);
    main(x, y);
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(1)),ArrayLiteral(IntLiteral(1),IntLiteral(1))),Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_425(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1,1},{1,1}};
Var: y;
Function: main
Parameter: a,b
Body:
    x[2][2] = b;
    y = a;
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(y),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_426(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1,1},{1,1}};
Var: y;
Function: main
Parameter: a,b
Body:
    x[2][2] = b;
    y = "a";
    Return;
EndBody.
Function: foo
Parameter: f,g
Body:
    main(f, g);
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[Id(f),Id(g)])"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_427(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1,1},{1,1}};
Var: y;

Function: main
Parameter: a,b
Body:
    x[2][2] = b;
    Return;
EndBody.

Function: foo
Parameter: f,g
Body:
    y = foo(1, 1);
    Return "a";
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(y),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_428(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a,b
Body:
    y = 1;
    Return 1;
EndBody.

Function: foo
Parameter: f,g
Body:
    y = foo(main(1,1), g);
    Return 1;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(y),CallExpr(Id(foo),[CallExpr(Id(main),[IntLiteral(1),IntLiteral(1)]),Id(g)]))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_429(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b
Body:
    main({{2,2},{2,2}}, b);
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(2)),ArrayLiteral(IntLiteral(2),IntLiteral(2))),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_430(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b
Body:
    Var: x[1] = {1};
    Var: y;
    y = b;
    Return {{1,1},{1,1}};
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(y),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_431(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b[1][1]
Body:
    Var: x[1][1] = {1};
    a[1][1] = b[1][1];
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]),ArrayCell(Id(b),[IntLiteral(1),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_432(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b[1][1]
Body:
    a = x;
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(a),Id(x))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_433(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b[1][1]
Body:
    y = a[1][1];
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(Id(y),ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_434(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b[1][1]
Body:
    a[1][1] = y;
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: Assign(ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_435(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a[1][1],b[1][1]
Body:
    main(x, 1);
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[Id(x),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_436(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a,b[1][1]
Body:
    main(x[1][1], 1);
    Return;
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[ArrayCell(Id(x),[IntLiteral(1),IntLiteral(1)]),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_437(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2];
Var: y;

Function: main
Parameter: a,b[1][1]
Body:
    a = a + main(x[1][1], 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[ArrayCell(Id(x),[IntLiteral(1),IntLiteral(1)]),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_438(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x, y;

Function: main
Parameter: a,b
Body:
    Return 1;
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
        expect = "Type Mismatch In Statement: If(CallExpr(Id(main),[IntLiteral(1),IntLiteral(1)]),[],[Return(IntLiteral(1))])Else([],[Return(IntLiteral(0))])"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x, y;

Function: main
Parameter: a,b
Body:
    Return 1;
EndBody.

Function: foo
Parameter: f, g
Body:
    If (2+f) Then
       Return 1;
    Else
        Return 0;
    EndIf.
EndBody.
"""
        expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLiteral(2),Id(f)),[],[Return(IntLiteral(1))])Else([],[Return(IntLiteral(0))])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_440(self):
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
        expect = "Type Mismatch In Statement: If(ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[Return(IntLiteral(1))])Else([],[Return(IntLiteral(0))])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_441(self):
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
        expect = "Type Mismatch In Statement: If(ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[Return(IntLiteral(1))])Else([],[Return(IntLiteral(0))])"
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
        expect = "Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(void),[]))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
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
    For (y=1,y<10,True) Do 
        If y<1 Then y=1;
        EndIf.
    EndFor.
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(<,Id(y),IntLiteral(10)),BooleanLiteral(true),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
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
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(<,Id(y),IntLiteral(10)),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
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
    While x[2][2] Do 
        If y<1 Then y=1;
        EndIf.
    EndWhile.
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: While(ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
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
    While (1.0+.1.0) Do 
        If y<1 Then y=1;
        EndIf.
    EndWhile.
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: While(BinaryOp(+.,FloatLiteral(1.0),FloatLiteral(1.0)),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        """Type Cannot Be Inferred"""
        input = """
Var:a;
Function: main
Parameter: n,x,y,z
Body:
    If n > 10 Then
        Return 5;
    ElseIf n > 5 Then x=y+z; Return a;
    ElseIf n < 10 Then a=a+1; Return True;
    Else
        Return 1;
    EndIf.
EndBody.
"""
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
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
    While x Do 
        If y<1 Then y=1;
        EndIf.
    EndWhile.
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: While(Id(x),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_449(self):
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
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return;
EndBody.

Function: foo
Parameter: f, g
Body:
    f = main({1,1}, 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(Id(f),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_451(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    f[2][2] = main({1,1}, 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(f),[IntLiteral(2),IntLiteral(2)]),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_452(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return True;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    f[2][2] = "a";
    f[2][2] = main({1,1}, 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(f),[IntLiteral(2),IntLiteral(2)]),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_453(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return True;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    f[2][2] = "a";
    f[2][2] = main({1,1}, 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(f),[IntLiteral(2),IntLiteral(2)]),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_454(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return True;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    f[2][2] = "a";
    f[2][2] = main({1,1}, 1) + main({2,2}, 2);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]),CallExpr(Id(main),[ArrayLiteral(IntLiteral(2),IntLiteral(2)),IntLiteral(2)]))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_455(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2][2],b
Body:
    Return True;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1}, 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        input = """
Var: i = 1;
Function: main
Parameter: x,i
Body:   
    x = void();
    Return;
EndBody.
Function: void
Body:   
    i = 1;
    Return;
EndBody."""
        expect = "Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(void),[]))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_457(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2][2],b
Body:
    Return;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1}, 1 , 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_458(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a,b
Body:
    Return;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1}, 1);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_459(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    b = "a";
    Return;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    Var: x[2] = {1,2}, y = True;
    main(x, y);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[Id(x),Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_460(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: foo
Parameter: f[2][2], g
Body:
    Var: x[2] = {1,2}, y = True;
    main(x, y);
    Return;
EndBody.

Function: main
Parameter: a[2],b
Body:
    b = "a";
    Return;
EndBody.


"""
        expect = "Type Mismatch In Statement: Assign(Id(b),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_461(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: foo
Parameter: f[2][2], g
Body:
    Var: x[2] = {1,2}, y = True;
    main(x, y);
    Return;
EndBody.

Function: main
Parameter: a[2],b
Body:
    b = False;
    main(1,1);
    Return;
EndBody.


"""
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[IntLiteral(1),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_462(self):
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
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(void),[]),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_463(self):
        input = """
Var: i = 1, c, a[1][2];
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
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(void),[IntLiteral(1),FloatLiteral(1.2),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_464(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return "a";
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    g = f[2][2] + main({1,1}, x[2][2]);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(f),[IntLiteral(2),IntLiteral(2)]),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)])]))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_465(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    g = main({1,1}, x[2][2]);
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(Id(g),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)])]))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_466(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    x[2] = f[2][2];
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_467(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return "a";
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    x[2][main({1,1},1)] = 1;
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(2),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_468(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return 1;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    x[2][main({1,1},1)] = "a";
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(x),[IntLiteral(2),CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])]),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_469(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1},1)[1][1] = {1};
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(ArrayCell(CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]),[IntLiteral(1),IntLiteral(1)]),ArrayLiteral(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_470(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1},1)[1][1] = 1;
    f[2][2] = foo({1,1},1) + g;
    g = False;
    Return;
EndBody.
"""
        expect = "Type Mismatch In Statement: Assign(Id(g),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_471(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1},1)[1][1] = 1;
    f[2][2][2] = foo({1,1},1) + g;
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),[IntLiteral(2),IntLiteral(2),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_472(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1},1)[1][1] = 1;
    g = 1 + f[2]["a"];
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),[IntLiteral(2),StringLiteral(a)])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_473(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return x;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    main({1,1},1)[1][1] = 1;
    g = 1 + f[2]["a"];
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),[IntLiteral(2),StringLiteral(a)])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_474(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return True;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    g = main({1,1},1) || False;
    f[2][2] = g + 1;
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(g),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_475(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1.0, 1.0},{1.0, 1.0}}, y;

Function: main
Parameter: a[2],b
Body:
    Return 2.0;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    g = main({1,1},1) *. x[2][2];
    f[2][2] = g == 1;
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(g),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_476(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return 2.0;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    g = main({1,1},1) *. x[2][2];
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: BinaryOp(*.,CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)]),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_477(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2],b
Body:
    Return 2.0;
EndBody.

Function: foo
Parameter: f[2][2], g
Body:
    g = main({1,1},1,1) *. x[2][2];
    f[2][2] = g == 1;
    Return;
EndBody.
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_478(self):
        input = """Var: x[2][2], y[2][2] = {{1,2},{1,2}};
                    Function: main
                    Parameter: t, q, k
                    Body:
                        t = y[1][1] + 1;
                        q = x[1][1] + 1;
                        x[k][1] = 1;
                        goo(x);
                    EndBody.
                    Function: goo
                    Parameter: x[1][2]
                    Body:
                        Return 1 + goo(x);
                    EndBody.
                """
        expect = """Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),CallExpr(Id(goo),[Id(x)]))"""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_479(self):
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
                    For (y=1,y+10,y+1) Do 
                        If y<1 Then y=1;
                        EndIf.
                    EndFor.
                    Return;
                EndBody.
                """
        expect = "Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(+,Id(y),IntLiteral(10)),BinaryOp(+,Id(y),IntLiteral(1)),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_480(self):
        input = """Var: z;
                Function: main
                Parameter: q , d[5], x, y, t
                Body:                                       
                    y = foo(1.2 +. foo(1.2));
                    z = string_of_float(y);
                EndBody.
                Function: foo
                Parameter: y
                Body: 
                    Var: x;
                    x = 1;
                    z = 1.;
                EndBody.
                """
        expect = """Type Mismatch In Statement: Assign(Id(z),FloatLiteral(1.0))"""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_481(self):
        input = """Var: uh, d[5];
                Function: main
                Parameter: q , x, y, t
                Body:                                       
                    y = goo(string_of_float("1.2") +. goo(1.2));
                    uh = string_of_float(y);
                    t = goo(1.2);
                    d[4] = t;
                EndBody.
                Function: goo
                Parameter: y
                Body: 
                    Var: x;
                    d[3] = 1;
                EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(string_of_float),[StringLiteral(1.2)])"""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_482(self):
        input = """Var: a, d[5];
                Function: main
                Parameter: q , x, y, t
                Body:                                       
                    y = foo(float_of_string("1.2") +. foo(1.2));
                    a = string_of_float(y);
                    t = foo(1.2);
                    d = {2,2,3};
                EndBody.
                Function: foo
                Parameter: y
                Body: 
                    Var: x, f[3] = {1,2,3};
                    d[3] = f[1.2];
                EndBody.
                """
        expect = """Type Mismatch In Expression: ArrayCell(Id(f),[FloatLiteral(1.2)])"""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_483(self):
        input = """Var: a = 0,b,f[3] = {1.2,2.2,3.2};
                Function: main
                Body:
                    Var: d = 1.2;
                    Do
                        Do
                            Do
                                printStrLn("Hello World!");
                            While a > b
                            EndDo.
                            printStrLn("Hello World!");
                        While a > b
                        EndDo.
                        printStrLn("Hello World!");
                    While a > d
                    EndDo.
                EndBody."""
        expect = """Type Mismatch In Expression: BinaryOp(>,Id(a),Id(d))"""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_484(self):
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
        expect = """Type Mismatch In Expression: ArrayCell(Id(z),[Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_485(self):
        input = """Function: foo 
                Parameter: x, y
                Body: 
                    Var: a=1;
                    y=foo(x); 
                EndBody.
                Function: main 
                Body: 
                EndBody.
                """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo),[Id(x)])"""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_486(self):
        input = """Var: x, y[2][2] = {{1,2},{1,2}};
                Function: main
                Parameter: t
                Body:
                    t = y[2] + 2;
                EndBody.
                        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(y),[IntLiteral(2)])"""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_487(self):
        input = """Var: x[2][2], y[2][2] = {{1,2},{1,2}};
                Function: main
                Parameter: t, q, k
                Body:
                    t = y[1][1] + 1;
                    q = x[1][1] + 1;
                    k = 1.2;
                    x[k][1] = 1;
                EndBody.
                """
        expect = """Type Mismatch In Expression: ArrayCell(Id(x),[Id(k),IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_488(self):
        input = """
            Var: x, y, z[2];
            Function: main
            Parameter: a,b,c
            Body:
                Var: i, j, k;
                If (j == 2) Then
                    Var: f,g,h;
                Else
                    Var: n;
                EndIf.
            EndBody.
            Function: main
            Body:
                y = 5.0;
            EndBody.
                """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_489(self):
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
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_490(self):
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
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_491(self):
        """Simple program: main"""
        input = """
                Var: x, y, z;
                Function: main
                Body:
                    goo(z,y);
                EndBody.
                Function: goo
                Parameter: a,b,c
                Body:
                    goo(a,b,c);
                EndBody.
                """
        expect = "Type Mismatch In Statement: CallStmt(Id(goo),[Id(z),Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_492(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                    foo();
                EndBody.
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_493(self):
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
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(y),FloatLiteral(2.5))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_494(self):
        input =  """
                Function: foo
                Parameter: y
                Body: 
                    Return y;
                EndBody.
                Function: main
                Parameter: y
                Body: 
                    Var: a, b;
                    b = foo(a);
                EndBody.
                """
        expect = """Type Cannot Be Inferred: Return(Id(y))"""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_495(self):
        """Type Cannot Be Inferred"""
        input = """
                Var: x[2][2] = {{1, 1},{1, 1}}, y;
                Function: main
                Parameter: main
                Body:
                    main(1, 2, 3);
                EndBody.
                """
        expect = """Undeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_496(self):
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
        expect = "Type Cannot Be Inferred: Assign(Id(a),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_497(self):
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
        expect = "Type Cannot Be Inferred: Assign(Id(a),BinaryOp(+,CallExpr(Id(main),[CallExpr(Id(foo),[Id(x),Id(y),Id(z)]),IntLiteral(1),IntLiteral(1)]),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_498(self):
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
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(c),IntLiteral(10)),[],[Return(IntLiteral(5))])ElseIf(BinaryOp(>,Id(c),IntLiteral(5)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(Id(a))])Else([],[Return(BooleanLiteral(false))])"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_499(self):
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
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(void),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,499))

#     def test_481(self):
#         input = """Var: uh, d[5];
# Function: main
# Parameter: q , x, y, t
# Body:                                       
#     y = foo(string_of_float("1.2") +. foo(1.2));
#     uh = string_of_float(y);
#     t = foo(1.2);
#     d[4] = t;
# EndBody.
# Function: foo
# Parameter: y
# Body: 
#     Var: x;
#     d[3] = 1;
# EndBody.
# """
#         expect = """Type Mismatch In Expression: CallExpr(Id(string_of_float),[StringLiteral(1.2)])"""
#         self.assertTrue(TestChecker.test(input,expect,481))

    # def test_482(self):
    #     input = """
    #                 Var: x, y, z[2];
    #                 Function: main
    #                 Parameter: a,b,c
    #                 Body:
    #                     Var: y = 2.0;
    #                     x = 3;
    #                     Return b +. 1.0;
    #                 EndBody.
    #                 Function: boo
    #                     Body:
    #                         y = main(1,2.0,3);
    #                         z[y] = y *. 2.0;
    #                 EndBody.
    #             """
    #     expect = """Type Mismatch In Expression: ArrayCell(Id(z),[Id(y)])"""
    #     self.assertTrue(TestChecker.test(input,expect,482))
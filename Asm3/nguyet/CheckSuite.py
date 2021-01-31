#1927029
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_redeclared_gobal_1(self):
        """Simple program: main"""
        input = """
                   Var: main;
                   Var: main;
                   """
        expect = str(Redeclared(Variable(),"main"))
        self.assertTrue(TestChecker.test(input,expect,400))
    
    
    def test_redeclared_gobal_2(self):
        """Simple program: main"""
        input = """
                   Var: main;
                   Function: main
                   Body: 
                        
                   EndBody.
                   """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_gobal_3(self):
        """Simple program: main"""
        input = """                   
                   Function: main
                   Body: 
                   EndBody.
                   Function: main
                   Body: 
                   EndBody.
                   """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclared_parameter_1(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: x, x
                    Body: 
                        
                    EndBody."""
        expect = str(Redeclared(Parameter(),"x"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_parameter_2(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a, a
                    Body: 
                        
                    EndBody."""
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_parameter_3(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a, b, c, a
                    Body: 
                        
                    EndBody."""
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_parameter_4(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a, b, c, a[1]
                    Body: 
                        
                    EndBody."""
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_varInFunction_1(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a, b, c
                    Body: 
                        Var: a;
                    EndBody."""
        expect = str(Redeclared(Variable(),"a"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_varInFunctionr_2(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a, b, c
                    Body: 
                        Var: x;
                        Var: x;
                    EndBody."""
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_redeclared_varInFunctionr_3(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a, b, c
                    Body: 
                        Var: x;
                        Var: x[5];
                    EndBody."""
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_varInFunctionr_4(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a, b, c
                    Body: 
                        Var: m;
                        Var: n;
                        Var: n[5];
                    EndBody."""
        expect = str(Redeclared(Variable(),"n"))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_varInFunctionr_5(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a, b, c
                    Body: 
                        Var: m;
                        Var: n;
                        Var: b[5];
                    EndBody."""
        expect = str(Redeclared(Variable(),"b"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_varInFunctionr_6(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m;
                        Var: a;
                        Var: n[5];
                    EndBody."""
        expect = str(Redeclared(Variable(),"a"))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclared_Functionr_1(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m;
                    EndBody.

                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m;
                    EndBody.
                    """

        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_TypeMismatchInStatement_1(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m;
                        b = 2;
                        x = 3.0;
                        x = b;
                    EndBody."""

        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_TypeMismatchInStatement_2(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m;
                        b = 2;
                        a = b;
                    EndBody."""

        expect = str(TypeMismatchInStatement(Assign(Id("a"), Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_TypeMismatchInStatement_3(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m;
                        b = a;
                    EndBody."""

        expect = str(TypeMismatchInStatement(Assign(Id("b"), Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_TypeMismatchInStatement_4(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1.0;
                        b = a[m];
                    EndBody."""

        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"), [Id("m")])))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_TypeMismatchInStatement_5(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1.0;
                        b = a[2 + m];
                    EndBody."""

        expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral("2") ,Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_TypeMismatchInStatement_6(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1;
                        b = a[1][2 + m];
                    EndBody."""

        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[IntLiteral(1),BinaryOp("+",IntLiteral(2),Id("m"))])))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_UnaryOp_1(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1.0;
                        b = -1.0;
                    EndBody."""

        expect = str(TypeMismatchInExpression(UnaryOp("-", FloatLiteral("1.0"))))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_UnaryOp_2(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1;
                        b = -.m;
                    EndBody."""

        expect = str(TypeMismatchInExpression(UnaryOp("-.", Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_UnaryOp_3(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1;
                        b = !m;
                    EndBody."""
        expect = str(TypeMismatchInExpression(UnaryOp("!", Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_function_1(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_undeclared_function_2(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        Var: foo;
                        foo(1);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_function_3(self):
        """Simple program: main"""
        input = """
                   Var: foo;
                   Function: main
                   Body: 
                        foo(1);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_function_4(self):
        """Simple program: main"""
        input = """
                   
                   Function: main
                   Parameter: foo
                   Body: 
                        foo(1);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_function_5(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = True;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        foo(y);
                        y = 1;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_function_6(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                       x = 2;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        foo(1,2);
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_function_7(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        foo(1,2);
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undeclared_function_8(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        foo(y);
                        y = True;
                    EndBody.
                   """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undeclared_function_9(self):
        """Simple program: main"""
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
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("a")])))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undeclared_function_10(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While x Do EndWhile.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(While(Id("x"),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_undeclared_function_11(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While (x + 1) Do EndWhile.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(While(BinaryOp("+",Id("x"),IntLiteral(1)),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_undeclared_function_12(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While True Do x = 1.0; EndWhile.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_undeclared_function_13(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While True Do 
                    Var: a;
                    Var: a;
                    x = 1.0; 
                    EndWhile.
                    EndBody.
                   """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_undeclared_function_14(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While True Do 
                        While 1 Do
                        EndWhile.

                    EndWhile.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(While(IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_undeclared_function_15(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While True Do 
                        While False Do
                        Var: a;
                        EndWhile.
                    a = 10;
                    EndWhile.
                    EndBody.
                   """
        expect = str(Undeclared (Identifier(), "a"))
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_undeclared_function_16(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While True Do 
                        While False Do
                        Var: a;
                        EndWhile.
                    EndWhile.
                    x = a + 10;
                    EndBody.
                   """
        expect = str(Undeclared (Identifier(), "a"))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_undeclared_function_17(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    While True Do 
                        While False Do
                        Var: a;
                        x = a + 12;
                        a = 5.5;
                        EndWhile.
                    EndWhile.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement( Assign(Id("a"),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_undeclared_function_18(self):
        """Simple program: main"""
        input = """
                    Function: foo
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
        expect = str(TypeMismatchInStatement( Assign(Id("a"),FloatLiteral(10.0))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_undeclared_function_19(self):
        """Simple program: main"""
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
                        foo(a);
                        a = 2.5;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_undeclared_function_20(self):
        """Simple program: main"""
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
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_function_21(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    Do                        
                    While 10;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Dowhile(([],[]), IntLiteral(10) )))
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_undeclared_function_22(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    Do                        
                    While x + 10;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Dowhile(([],[]), BinaryOp("+",Id("x"),IntLiteral(10)) )))
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_undeclared_function_23(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    Do       
                    x = x + 10.5;                 
                    While True;
                    EndBody.
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),FloatLiteral(10.5)) ))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_undeclared_function_24(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    Do       
                        Var: a;
                        a = x;
                        a = 10.5;                 
                    While True;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(10.5))))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_undeclared_function_25(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    Do       
                        Var: a;
                        a = x;               
                    While True;
                    x = a;
                    EndBody.
                   """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_undeclared_function_26(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    For (x = 1.0, True, x = 2) Do
                        
                    EndFor.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(For(Id("x"),FloatLiteral(1.0),BooleanLiteral("true"),Id("x"),IntLiteral(2),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_undeclared_function_27(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    x = 1;
                    For (x = 1, True, x = 2.0) Do
                        
                    EndFor.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BooleanLiteral("true"),Id("x"),FloatLiteral(2.0),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_undeclared_function_28(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    For (x = 1, True, x = x + 1) Do
                        x = x + 2.5;
                    EndFor.
                    EndBody.
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_undeclared_function_29(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    For (x = 1, True, x = x + 1) Do
                        Var: a;
                        x = x + 1;
                        For (x = 1, True, x = x + 1) Do
                            Var: b;
                            a = b;
                        EndFor.
                    EndFor.
                    EndBody.
                   """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_undeclared_function_30(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                    For (x = 1, True, x = x + 1) Do
                        Var: a;
                        For (x = a, True, x = x + 2) Do
                            Var: b;
                            b = 1.0;
                            a = b;
                        EndFor.
                    EndFor.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_undeclared_function_30(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        If x Then 
                        x = 1;
                        EndIf.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_undeclared_function_31(self):
        """Simple program: main"""
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
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_undeclared_function_32(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        If x Then 
                        x = False;
                        ElseIf 10 Then
                        EndIf.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(If
            ([
            (Id("x"),
            [],
            [Assign(Id("x"),BooleanLiteral("false"))]
            ),
            (IntLiteral(10),
            [],
            []
            )
            ],
        ([],[])
        )))
            
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_undeclared_function_33(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        If x Then 
                        x = False;
                        ElseIf False Then
                        x = 10.5;
                        EndIf.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(10.5))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_undeclared_function_34(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x, y
                    Body: 
                    For (x = y, True, x = x + 1) Do
                        x = y + 2.5;
                    EndFor.
                    EndBody.
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_undeclared_function_35(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_undeclared_function_36(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,460))
    

    def test_diff_numofparam_expr_use_ast_61(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_diff_numofparam_stmt_use_ast_62(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_undeclared_function_63(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x, y[5]
                    Body: 
                        x = y;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_undeclared_function_64(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x, y[5]
                    Body: 
                        x = y[1] + 1;
                        y[2] = 5.5;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("y"),[IntLiteral(2)]),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_undeclared_function_65(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x, y[5]
                    Body: 
                        x = y[1] + 1;
                        x = 10.5;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(10.5))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_undeclared_function_66(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        If x Then 
                        Var: x;
                        x = 5;
                        ElseIf False Then
                        Var: x;
                        x = 5.5;
                        x = True;
                        EndIf.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_undeclared_function_67(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        If x Then 
                        Var: x;
                        x = 5;
                        ElseIf False Then
                        Var: x;
                        x = 5.5;
                        Else
                            x = 16.5;
                        EndIf.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(16.5))))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_undeclared_function_68(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        If x Then 
                        Var: x;
                        x = 5;
                        ElseIf False Then
                        Var: x;
                        x = 5.5;
                        Else
                            Var: x;
                            x = 10;
                            x = True;
                        EndIf.
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_undeclared_function_69(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        Return 1;
                    EndBody.                    
                    Function: main
                    Parameter: x
                    Body: 
                        x = foo(1);
                        x = True;
                    EndBody.                   

                   """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_undeclared_function_70(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        Return 1;
                    EndBody.                    
                    Function: main
                    Parameter: x
                    Body: 
                        x = foo(1);
                        x = True;
                    EndBody.                   

                   """
        expect = str(TypeMismatchInExpression(IntLiteral(1)))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_undeclared_function_71(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                        x = True;
                        Return 1;
                    EndBody.                    
                    Function: main
                    Parameter: x
                    Body: 
                        x = True;
                        x = foo(x) + True;
                        x = True;
                    EndBody.                   
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral("true"))))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_undeclared_function_72(self):
        """Simple program: main"""
        input = """
                    Var: x;
                    Function: fact
                    Parameter: n
                    Body:
                        n = 0;
                        If n == 0 Then
                            Return 1;
                        EndIf.
                    EndBody.
                    Function: main
                    Body:
                        x = 10.5;
                        fact(x);
                    EndBody.                 
                   """
        expect = str(TypeMismatchInExpression(Id("x")))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_undeclared_function_73(self):
        input = Program([VarDecl(Id("a"),[2,3],None),VarDecl(Id("x"),[],None),VarDecl(Id("b"),[2,3],None),VarDecl(Id("x"),[],None)])
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_undeclared_function_74(self):
        input = Program([VarDecl(Id("a"),[2,3],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[2,3],None),VarDecl(Id("x"),[],None)])
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_undeclared_function_75(self):
        input = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("int_of_float"),[],([],[]))])
        expect = str(Redeclared(Function(), "int_of_float"))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_undeclared_function_76(self):
        input = Program([VarDecl(Id("x"),[2,3],None),FuncDecl(Id("x"),[],([],[]))])
        expect = str(Redeclared(Function(), "x"))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_undeclared_function_77(self):
        input = Program([VarDecl(Id("x"),[2,3],None),VarDecl(Id("a"),[],None),FuncDecl(Id("x"),[],([],[]))])
        expect = str(Redeclared(Function(), "x"))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_undeclared_function_78(self):
        input = Program([VarDecl(Id("x"),[2,3],None),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        expect = str(Redeclared(Parameter(), "x"))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_undeclared_function_79(self):
        input = Program([VarDecl(Id("x"),[2,3],None),FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        expect = str(Redeclared(Parameter(), "x"))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_undeclared_function_80(self):
        input = Program([VarDecl(Id("x"),[2,3],None),FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("a"),[],None)],([],[]))])
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_undeclared_function_81(self):
        input = Program([VarDecl(Id("int_of_float"),[],None),FuncDecl(Id("x"),[],([],[]))])
        expect = str(Redeclared(Variable(), "int_of_float"))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_undeclared_function_82(self):
        input = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[Assign(Id("x"),Id("y"))]))])
        expect = str(Undeclared(Identifier(), "y"))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_undeclared_function_83(self):
        input = Program([
            VarDecl(Id("x"),[2,3],None),
            FuncDecl(Id("main"),[
            VarDecl(Id("y"),[],None)],([],[Assign(Id("x"),Id("y")),Assign(Id("z"),Id("y"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_undeclared_function_84(self):
        input = Program(
            [VarDecl(Id("x"),[2,3],None),
            VarDecl(Id("a"),[],None),
            FuncDecl(Id("main"),[],([VarDecl(Id("y"),[],None)],[Assign(Id("x"),Id("a")),Assign(Id("y"),Id("z"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('x'),Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_undeclared_function_85(self):
        input = Program([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x")),Assign(Id("z"),Id("y"))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('z'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_undeclared_function_86(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],IntLiteral(3))],[Assign(Id("t"),Id("x")),Assign(Id("z"),Id("y"))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('z'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_undeclared_function_87(self):
        input = Program([
            VarDecl(Id("x"),[],None),
            VarDecl(Id("y"),[],None),
            VarDecl(Id("z"),[],None),
            FuncDecl(Id("main"),[],(
                [VarDecl(Id("t"),[],None)],
                [Assign(Id("x"),IntLiteral(3)),
                Assign(Id("t"),Id("x")),
                Assign(Id("z"),Id("y"))]))])
        expect = str(TypeCannotBeInferred(Assign(Id('z'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_undeclared_function_88(self):
        input = Program([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],None)],[Assign(Id("t"),Id("x")),Assign(Id("z"),BinaryOp("+",Id("y"),IntLiteral(4))),Assign(Id("z"),BinaryOp("+.",Id("y"),FloatLiteral(4.0)))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('y'),FloatLiteral('4.0'))))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_undeclared_function_89(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],IntLiteral(3))],[Assign(Id("t"),Id("x")),Assign(Id("z"),BinaryOp("-",Id("y"),IntLiteral(3))),Assign(Id("z"),BinaryOp("-",Id("y"),FloatLiteral(3.0)))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('-',Id('y'),FloatLiteral('3.0'))))
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_undeclared_function_90(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],None),VarDecl(Id("m"),[],FloatLiteral(2.1))],[Assign(Id("x"),IntLiteral(3)),Assign(Id("t"),Id("x")),Assign(Id("z"),BinaryOp("\\",Id("y"),Id("x"))),Assign(Id("z"),BinaryOp("\\",Id("m"),Id("x")))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('\\',Id('m'),Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_undeclared_function_91(self):
        input = Program([VarDecl(Id("x"),[],None),
            VarDecl(Id("y"),[],None),
            VarDecl(Id("z"),[],None),
            FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],IntLiteral(3))],
            [Assign(Id("t"),BinaryOp("*",IntLiteral(2),IntLiteral(0))),
            Assign(Id("t"),BinaryOp("*",IntLiteral(2),FloatLiteral(0.2)))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('*',IntLiteral('2'),FloatLiteral('0.2'))))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_undeclared_function_92(self):
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],None)],[Assign(Id("t"),BinaryOp("+.",FloatLiteral(2.0),FloatLiteral(0.2))),Assign(Id("t"),BinaryOp("-.",IntLiteral(2),FloatLiteral(0.2)))]))])
        expect = str(TypeMismatchInExpression(BinaryOp('-.',IntLiteral('2'),FloatLiteral('0.2'))))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_undeclared_function_93(self):
        input = Program([VarDecl(Id("x"),[],IntLiteral(3)),
            VarDecl(Id("y"),[],None),
            VarDecl(Id("z"),[],None),
            FuncDecl(Id("main"),[],([VarDecl(Id("t"),[],None)],
            [Assign(Id("t"),Id("x")),
            Assign(Id("z"),FloatLiteral(3.0)),
            Assign(Id("z"),Id("x"))]))])
        expect = str(TypeMismatchInStatement(Assign(Id('z'),Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_undeclared_function_94(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a[2], b[2], c
                    Body: 
                        a[2] = 1;
                        a[2] = 1.2;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[IntLiteral('2')]),FloatLiteral('1.2'))))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_undeclared_function_93(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a[2], b[2], c
                    Body: 
                        a[2][3] = 1;
                    EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral('2'),IntLiteral('3')])))
        self.assertTrue(TestChecker.test(input,expect,495))
        
    def test_undeclared_function_96(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a[2], b[2], c
                    Body: 
                        a = b;
                    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_undeclared_function_97(self):
        """Simple program: main"""
        input = """
                    Var: x;    
                    Function: main
                    Parameter: a, b, c
                    Body: 
                        Var: a;
                    EndBody."""
        expect = str(Redeclared(Variable(),"a"))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_undeclared_function_98(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        a = b;
                    EndBody."""

        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_undeclared_function_99(self):
        """Simple program: main"""
        input = """
                    Var: x;  
                    Function: main
                    Parameter: a[4], b, c
                    Body: 
                        Var: m = 1.0;
                        b = -1.0;
                    EndBody."""

        expect = str(TypeMismatchInExpression(UnaryOp('-',FloatLiteral('1.0'))))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_undeclared_function_100(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body: 
                       x = 0;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: z = 2.1;
                        y = 1 + foo(2.1);
                    EndBody.
                    
                   """

        expect = str(TypeMismatchInExpression(FloatLiteral(2.1)))
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_undeclared_function_101(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: a
                    Body: 
                    a = True;
                    EndBody.
                    Function: main
                    Parameter: y
                    Body: 
                        Var: x;
                        x = 1;
                        foo(y);
                        y = 2;
                    EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(Id('y'),IntLiteral('2'))))
        self.assertTrue(TestChecker.test(input,expect,501))

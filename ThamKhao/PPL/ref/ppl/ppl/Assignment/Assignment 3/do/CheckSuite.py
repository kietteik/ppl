import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
# Total: 105

#.......................................................................
#                 1. Redeclared Variable/Function/Parameter (15: 400 -> 414)

    # Test Redeclared Variable
    def test_RedeclaredVariable_1(self):
        input = """
        int a;
        int a;
        void main() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_RedeclaredVariable_2(self):
        input = """
        int a;
        boolean a;
        void main() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_RedeclaredVariable_3(self):
        input = """
        int a;
        void main() {}
        string a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_RedeclaredVariable_4(self):
        input = """
        int a, b;
        void main() {}
        int b;
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_RedeclaredVariable_5(self):
        input = """
        int a, b, a;
        void main() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_RedeclaredVariable_6(self):
        input = """
        void main() 
        {
            int a;
            int a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_RedeclaredVariable_7(self):
        input = """
        void main() 
        {
            int a;
            float a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_RedeclaredVariable_8(self):
        input = """
        void main() 
        {
            int a, b, c;
            float c;
        }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_RedeclaredVariable_9(self):
        input = """
        void foo() 
        {
            int a;
            {
                int a;
                int b;
                int b;
            }
        }
        void main() 
        {
            foo();
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_RedeclaredVariable_10(self):
        """Don't have bug"""
        input = """
        void foo() 
        {
            int a;
            {
                int a;
                int b;
                {
                    int b;
                }
                
            }
        }
        void main() 
        {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,409))

    # Test Redeclared Function
    def test_RedeclaredFunction_1(self):
        input = """
        void foo() {}
        int foo() 
        {
            return 1;
        }
        void main() 
        {
            foo();
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_RedeclaredFunction_2(self):
        input = """
        int foo() 
        {
            return 1;
        }
        void main() {
            foo();
        }
        float foo(){
            return 1.1;
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    # Test Redeclared Parameter
    def test_RedeclaredParameter_1(self):
        input = """
        int main(int a, int a)
        {
            return 0;
        } 
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_RedeclaredParameter_2(self):
        input = """
        void foo(int a, float a) {}
        void main() 
        {
            foo();
        } """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_RedeclaredParameter_3(self):
        input = """
        int foo(int a, int b, int a[])
        {
            return b;
        }
        void main() {}
         """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,414))



#.......................................................................
#                 2. Undeclared Identiﬁer/Function (12: 415 -> 426)

    # Test Undeclared Identifier
    def test_UndeclaredIdentifier_1(self):
        input = """ 
        void main() 
        {
            a = 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_UndeclaredIdentifier_2(self):
        input = """ 
        void foo(int a)
        {
            b = 1;
        }
        void main() 
        {
            foo(1);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_UndeclaredIdentifier_3(self):
        input = """ 
        int a;
        void foo(int c) 
        {
            a = 1; c = 2;
            b = 3;
        }
        void main() 
        {
            foo(6);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_UndeclaredIdentifier_4(self):
        input = """ 
        int foo() 
        {
            return a;
        }
        void main() 
        {
            foo();
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_UndeclaredIdentifier_5(self):
        input = """ 
        int foo(int a) 
        {
            return 1;
        }
        void main() 
        {
            foo(b);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_UndeclaredIdentifier_6(self):
        input = """ 
        void main() 
        {
            int a[5];
            a[b] = 1;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_UndeclaredIdentifier_7(self):
        input = """
        int a;
        void main()
        {
            int b;
            {
                    a = 1; b = 2;
                    c = 3;
            }
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_UndeclaredIdentifier_8(self):
        """Don't have bug"""
        input = """
        int a;
        void main()
        {
            int b;
            {
                    a = 1; 
                    b = 2;
                    {
                        int c;
                        c = 3;
                        a = 4;
                    }
                    a = 5;
            }
            b = 6;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))

    #Test Undeclared Function
    def test_UndeclaredFunction_1(self):
        input = """
        void main() 
        {
            foo();
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_UndeclaredFunction_2(self):
        input = """
        void foo()
        {
            foo1();
        }
        void main()
        {
            foo();
        }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_UndeclaredFunction_3(self):
        input = """
        void foo() {}
        void foo1()
        {
            foo();
            {
                foo2();
            }
        }
        void main()
        {
            foo1();
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_UndeclaredFunction_4(self):
        """Don't have bug."""
        input = """
        void foo1() {}
        void foo2() {}
        void foo()
        {
            foo1();
            {
                foo2();
            }
        }
        void main()
        {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,426))



#.......................................................................
#                 3. Type Mismatch In Statement (24: 427 -> 450)

    # Test Type Mismatch In Statement: If
    def test_TypeMismatchInStatement_If_1(self):
        """Conditional expression."""
        input = """
        void main()
        {
            int a;
            if (a = 1) {}
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(1)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,427)) 

    def test_TypeMismatchInStatement_If_2(self):
        """Conditional expression."""
        input = """
        void main()
        {
            int a;
            if (a - 1) {}
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(-,Id(a),IntLiteral(1)),Block([]))" 
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_TypeMismatchInStatement_If_3(self):
        """Conditional expression."""
        input = """
        void foo() {}
        void main()
        {
            if (foo()) {}
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(foo),[]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_TypeMismatchInStatement_If_4(self):
        """Conditional expression."""
        input = """
        int foo() 
        {
            return 1;
        }
        void main()
        {
            int a;
            if (a = foo()) {}
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),CallExpr(Id(foo),[])),Block([]))" #########################
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_TypeMismatchInStatement_If_5(self):
        """Conditional expression."""
        input = """
        void main()
        {
            if (1.1) {}
        }
        """
        expect = "Type Mismatch In Statement: If(FloatLiteral(1.1),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_TypeMismatchInStatement_If_6(self):
        """Conditional expression."""
        input = """
        void main()
        {
            if ("false") {}
        }
        """ 
        expect = "Type Mismatch In Statement: If(StringLiteral(false),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_TypeMismatchInStatement_If_7(self):
        """Conditional expression."""
        input = """
        void main()
        {
            int a;
            if (a = 1 + 1) {}
        }
        """ 
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),BinaryOp(+,IntLiteral(1),IntLiteral(1))),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_TypeMismatchInStatement_If_8(self):
        """Conditional expression. Don't have bug."""
        input = """
        void main()
        {
            if (true) {}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    # Test Type Mismatch In Statement: For
    def test_TypeMismatchInStatement_For_1(self):
        """Exp1 in for loop."""
        input = """
        void main()
        {
            int i;
            for (i == 1; i < 2; i = i + 3) {}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(3)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TypeMismatchInStatement_For_2(self):
        """Exp2 in for loop."""
        input = """
        void main()
        {
            int i;
            for (i = 1; i = 2; i = i + 3) {}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(3)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_TypeMismatchInStatement_For_3(self):
        """Exp3 in for loop."""
        input = """
        void main()
        {
            int i;
            for (i = 1; i < 2; i < 3) {}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(2));BinaryOp(<,Id(i),IntLiteral(3));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_TypeMismatchInStatement_For_4(self):
        """Don't have bug."""
        input = """
        void main()
        {
            int i;
            for (i = 1; i < 2; i = i + 3) 
            {
                // Do something.
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,438))

    # Test Type Mismatch In Statement: Dowhile
    def test_TypeMismatchInStatement_Dowhile_1(self):
        """Conditional expression."""
        input = """
        void main()
        {
            int i;
            do {} 
            while (i = 1);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],BinaryOp(=,Id(i),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_TypeMismatchInStatement_Dowhile_2(self):
        """Conditional expression."""
        input = """
        void foo() {}
        void main()
        {
            do {} while (foo());
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_TypeMismatchInStatement_Dowhile_3(self):
        """Conditional expression."""
        input = """ 
        void main() 
        {
            do {} while (1.1);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_TypeMismatchInStatement_Dowhile_4(self):
        """Don't have bug."""
        input = """ 
        void main() 
        {
            int n, m;
            do {
                n = n - 1;
                m = m + n;
                break;
            } while (true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,442))

    # Test Type Mismatch In Statement: Return
    def test_TypeMismatchInStatement_Return_1(self):
        input = """
        int foo()
        {
            return 1.1;
        }
        void main()
        {
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_TypeMismatchInStatement_Return_2(self):
        input = """ 
        void main() 
        {
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_TypeMismatchInStatement_Return_3(self):
        input = """
        int main()
        {
            return "1";
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_TypeMismatchInStatement_Return_4(self):
        input = """
        float foo()
        {
            return true;
        }
        void main()
        {
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_TypeMismatchInStatement_Return_5(self):
        input = """ 
        boolean foo() 
        {
            int a;
            a = 1;
            if (a < 2) 
            {
                return true;
            } 
            for (a = 0; a <= 1; a = a + 2) 
            {
                return 1;
            }
            do { return false; } while (true);
            return false;
        }
        void main() 
        {
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_TypeMismatchInStatement_Return_6(self):
        input = """ 
        int[] foo()
        {
            int arr[10];
            return arr[0];
        }
        void main() 
        {
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(arr),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_TypeMismatchInStatement_Return_7(self):
        """Don't have bug."""
        input = """ 
        void main() 
        {
            // Do something.
            return ;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_TypeMismatchInStatement_Return_8(self):
        """Don't have bug."""
        input = """
        float[] foo()
        {
            float arr[10];
            return arr;
        }
        void main()
        {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))



#.......................................................................
#                 4. Type Mismatch In Expression (14: 451 -> 464)

    #Test Type Mismatch in Expression: ArrayCell
    def test_TypeMismatchInExpression_ArrayCell_1(self):
        input = """
        void main()
        {
            int a;
            a[1] = 2;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_TypeMismatchInExpression_ArrayCell_2(self):
        input = """
        void main()
        {
            int a[10];
            a[1.1] = 1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_TypeMismatchInExpression_ArrayCell_3(self):
        input = """
        void main()
        {
            int a[10];
            float b;
            a[b] = 1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_TypeMismatchInExpression_ArrayCell_4(self):
        """Don't have bug."""
        input = """
        int[] foo()
        {
            int arr[10];
            return arr;
        }
        void main()
        {
            foo()[1] = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))

    #Test Type Mismatch in Expression: Binary and Unary Expression
    def test_TypeMismatchInExpression_BinaryUnary_1(self):
        """Binary Expression."""
        input = """
        void main()
        {
            int a;
            a == 1.1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_TypeMismatchInExpression_BinaryUnary_2(self):
        """Binary Expression."""
        input = """
        void main()
        {
            float a;
            a - "1.1";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),StringLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TypeMismatchInExpression_BinaryUnary_3(self):
        """Binary Expression."""
        input = """
        void main()
        {
            int a;
            if (a == 1.1) {}
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_TypeMismatchInExpression_BinaryUnary_4(self):
        """Binary Expression."""
        input = """ 
        void main() 
        {
            int a;
            float b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_TypeMismatchInExpression_BinaryUnary_5(self):
        """Unary Expression."""
        input = """
        void main()
        {
            int a;
            a = 1;
            string str;
            str = "ABC";
            a = -str;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(str))"
        self.assertTrue(TestChecker.test(input,expect,459))

    #Test Type Mismatch in Expression: Assignment
    def test_TypeMismatchInExpression_Assignment_1(self):
        input = """
        void main()
        {
            int arr[10];
            arr = 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_TypeMismatchInExpression_Assignment_2(self):
        input = """
        void main()
        {
            boolean a;
            a = "true";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_TypeMismatchInExpression_Assignment_3(self):
        """Don't have bug."""
        input = """
        void main()
        {
            boolean a;
            a = true;
            int b;
            b = 10;
            float c;
            c = b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))   

    #Test Type Mismatch in Expression: Function Call
    def test_TypeMismatchInExpression_Funccall_1(self):
        input = """
        int foo(int a)
        {
            return a;
        }
        void main()
        {
            foo();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_TypeMismatchInExpression_Funccall_2(self):
        input = """
        void foo() {}
        void main()
        {
            foo(1);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,464))



#.......................................................................
#                 5. Function not return (6: 465 -> 470)

    def test_FunctionNotReturn_1(self):
        input = """
        int main()
        {
            int a;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_FunctionNotReturn_2(self):
        input = """
        int foo()
        {
            int a;
            a = 3;
        }
        void main()
        {
            foo(0);
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,466))
        
    def test_FunctionNotReturn_3(self):
        input = """
        int main()
        {

            int a;
            int b;
            a = 0; b = foo();
            if (a > 1)
            {
                return a;
            }
            else
            {
                return b;
            }
        }
        int foo()
        {
            int a;
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_FunctionNotReturn_4(self):
        input = """ 
        int main() 
        {
            int a;
            a = 1;
            if (a == 1) 
            {
                a = 2;
            }
            else 
            {
                return a;
            }
        }        
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_FunctionNotReturn_5(self):
        input = """
        int foo() {}
        int main()
        {
            foo();
            return 0;
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_FunctionNotReturn_6(self):
        """Don't have bug."""
        input = """
        void foo() {}
        void main()
        {
            foo();
            return;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))



#.......................................................................
#               6. Break/Continue not in loop (8: 471 -> 478)

    #Test Break not in Loop
    def test_BreakNotInLoop_1(self):
        input = """
        void main()
        {
            int x;
            for (x = 1; x < 10; x = x + 1) {}
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_BreakNotInLoop_2(self):
        input = """ 
        void main() 
        {
            int x;
            if (x > 10) 
            {
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_BreakNotInLoop_3(self):
        input = """
        void main()
        {
            int x;
            do {} while (x != 1);
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_BreakNotInLoop_4(self):
        input = """
        void main()
        {
            int x;
            do 
            {
                for (x = 1; x < 10; x = x + 1) {}
            } while (x != 1);
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,474))

    # Test Continue not in Loop
    def test_ContinueNotInLoop_1(self):
        input = """
        void main()
        {
            int x;
            for (x = 1; x < 10; x = x + 1) {}
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_ContinueNotInLoop_2(self):
        input = """ 
        void main() 
        {
            int a;
            if (a < 10) 
            {
                a = 1;
            }
            else 
            {
                continue;
            }

        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_ContinueNotInLoop_3(self):
        input = """ 
        void main() {
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_ContinueNotInLoop_4(self):
        """Don't have bug."""
        input = """
        void main()
        {
            int a;
            for(a = 0; a < 10; a = a + 1)
            {
                do {} while (a > 5);
                continue;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,478))



#.......................................................................
#                 7. No Entry Point (5: 479 -> 483)

    def test_NoEntryPoint_1(self):
        input = """
        void foo() {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_NoEntryPoint_2(self):
        input = """ 
        void Main() {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_NoEntryPoint_3(self):
        input = """
        void foo() {}
        void MAIN()
        {
            foo();
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_NoEntryPoint_4(self):
        input = """
        void foo()
        {
            Main();
        }
        void foo1()
        {
            foo();
        }
        void Main() {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_NoEntryPoint_5(self):
        """Don't have bug."""
        input = """
        void main() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483)) 

    def test(self):
        """Don't have bug."""
        input = """
        void foo(float a, int b)
        {

        }
        void main() {
            foo(1, 5);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500)) 

#.......................................................................
#                 8. Unreachable function (6: 484 -> 489)

    def test_UnreachableFunction_1(self):
        input = """ 
        void foo() {}       
        void main() {}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_UnreachableFunction_2(self):
        input = """ 
        void foo() {} 
        void foo1() 
        {
            foo();
        }      
        void main() {}
        """
        expect = "Unreachable Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_UnreachableFunction_3(self):
        input = """ 
        void foo() {} 
        void foo1() 
        {
            foo();
        }
        void foo2()
        {
            foo1();
        }
        void main() {}
        """
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_UnreachableFunction_4(self):
        input = """ 
        void foo() 
        {
            foo();
        }       
        void main() {}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_UnreachableFunction_5(self):
        """Don't have bug."""
        input = """ 
        void foo() {}       
        void main() 
        {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488)) 

    def test_UnreachableFunction_6(self):
        """Don't have bug."""
        input = """ 
        void foo() 
        {
            foo1();
        }    
        void foo1()
        {
            foo();
        }   
        void main() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489)) 



#.......................................................................
#                 9. Not Left Value (10: 490 -> 499)

    def test_NotLeftValue_1(self):
        input = """
        void main()
        {
            1 = 2;
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_NotLeftValue_2(self):
        input = """
        void main()
        {
            int a;
            a = 2;
            1 = a;
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_NotLeftValue_3(self):
        input = """
        void foo() {}
        void main()
        {
            foo() = 1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_NotLeftValue_4(self):
        input = """
        void main()
        {
            int a;
            a = foo();
        }
        int foo() 
        {
            foo1() = 1;
            return 2;
        }
        int foo1() 
        {
            return 1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo1),[])"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_NotLeftValue_5(self):
        input = """
        int foo()
        {
            return 1;
        }
        void main()
        {
            do
            {
                foo() = 1;
            } while(foo() < 1);
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_NotLeftValue_6(self):
        input = """
        void main()
        {
            if ((1 = 2) < 3) {}
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_NotLeftValue_7(self):
        input = """
        void main()
        {
            int i;
            for (i = 1; i < 5; 1 = i + 1) {}
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_NotLeftValue_8(self):
        input = """
        void main()
        {
            int i;
            for (i = 1; i < 5; i = i + 1) 
            {
                i = i * 2;
                1 = i;
            }
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_NotLeftValue_9(self):
        input = """
        void main()
        {
            int i;
            for(i = 0; i < 5; i = i + 1)
            {
                do 
                {  
                    i = i / 2;
                    1 = 3 + 2 * i;
                } while (i > 2);
            }
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_NotLeftValue_10(self):
        """Don't have bug."""
        input = """
        int[] foo(int a)
        {
            int arr[10];
            arr[a] = a;
            return arr;
        }
        void main()
        {
            int x; 
            x = foo(1)[1];
            foo(3)[3] = x;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))


#.......................................................................
#                 10. Unreachable statement (0)
#.......................................................................
#                 11. Index out of range (0)
#.......................................................................
#                 12. Uninitialized Variable (0)
# Well, not my job cuz I'm not a gifted student.


#                 Bonus. Complex Program (5: 500 -> 504)
#.......................................................................
    def test_ComplexProgram_z(self):
        """Don't have bug."""
        input = """

        int main()
        {
            float a;
            a = -(1.5 + 2.3);
            putIntLn(1);
            putFloat(1.1);
            putBool(true);
            putString("str");
            return getInt();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))   

    def test_ComplexProgram_2(self):
        """Check mismatch: not match type (int - boolean)."""
        input = """
        void main()
        {
            int a[10];
            boolean b[10];
            a[0] = 2;
            b[1] = true;
            a[2] = b[1];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(2)),ArrayCell(Id(b),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_ComplexProgram_3(self):
        """Check mismatch: not match type (float - int) in 'return'."""
        input = """
        int foo(float a)
        {
            int b;
            b = 1;
            a = b;
            return a + 1;
        }
        void main()
        {
            int x;
            x = foo(1);
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_ComplexProgram_4(self):
        """Check mismatch: not match type (boolean - float) in if statement."""
        input = """
        float foo(int a)
        {
            if (true) return a + 1.1;
            else return false;
        }
        void main()
        {
            float a;
            a = foo(a);
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_ComplexProgram_4(self):
        """Check scope: Don't have bug."""
        input = """
        void foo()
        {
            int a;
            a = 1;
            {
                a = 1;
                int a;
                {
                    int a;
                    int b;
                }
                a = 1;
            }
        }
        void main()
        {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,504))      



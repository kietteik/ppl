import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # test variable declaration
    def test_var_dec_1(self):
        input = """Var: x = 20;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_var_dec_2(self):
        input = """Var: x = 20, y=50, z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_var_dec_3(self):
        input = """Var: x = "This is string", y = 2.2e-1;  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_dec_4(self):
        input = """Var: x[1][2] = {1,2,3}, y[3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_var_dec_5(self):
        input = """Var: x = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_var_dec_6(self):
        input = """Var: x[1] = 20;"""
        expect = "Error on line 1 col 12: 20"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_var_dec_7(self):
        input = """Var: x = {20};"""
        expect = "Error on line 1 col 9: {20}"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_var_dec_8(self):
        input = """Var: x[a] = {20};"""
        expect = "Error on line 1 col 7: a"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_var_dec_9(self):
        input = """Var: x[1+1] = {20};"""
        expect = "Error on line 1 col 8: +"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_var_dec_10(self):
        input = """Var: x = "String include quote \'"text\'" ";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))


    # test variable declaration
        # if statement
    def test_if_stmt_1(self):
        input = """Function: foo
                    Parameter: a,b,c
                    Body:
                        Return a+b+c;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_if_stmt_2(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    Return a+b+c;
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_if_stmt_3(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a <= b Then
                    Return a+b+c;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_if_stmt_4(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a >=. b Then
                    Return a+b+c;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_if_stmt_5(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = "Error on line 9 col 20: Return"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_if_stmt_6(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf
            EndBody."""
        expect = "Error on line 13 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_if_stmt_7(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                
            EndBody."""
        expect = "Error on line 13 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_if_stmt_8(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a =/= b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else.
                    Return a;
                EndIf.
            EndBody."""
        expect = "Error on line 10 col 20: ."
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_if_stmt_9(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a == b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf;
            EndBody."""
        expect = "Error on line 12 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_if_stmt_10(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a == b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    If a % b = 1 Then
                        Return a;
                EndIf.
            EndBody."""
        expect = "Error on line 11 col 29: ="
        self.assertTrue(TestParser.checkParser(input,expect,220))

        # for statement
    def test_for_stmt_1(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, 2) Do
                    If a % b == 1 Then
                        Return a;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_for_stmt_2(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, 2) Do
                    For (i = 1, i > 10, 3) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_for_stmt_3(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, foo(1)) Do
                    For (i = 1, i > 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_for_stmt_4(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = foo(1), i < foo(10), foo(1)) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_for_stmt_5(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i , i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_for_stmt_6(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i , i) Do
                    For (j == i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 5 col 27: =="
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_for_stmt_7(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i, i, i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 4 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_for_stmt_8(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i)
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 5 col 20: For"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_for_stmt_9(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor
                EndFor.
            EndBody."""
        expect = "Error on line 8 col 16: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_for_stmt_10(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i, j < i + 10, i = i + 1) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 5 col 46: ="
        self.assertTrue(TestParser.checkParser(input,expect,230))

        # test while statmenet
    def test_while_stmt_1(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While True Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_while_stmt_2(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While a == b Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_while_stmt_3(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While foo(a,b) == b Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_while_stmt_4(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_while_stmt_5(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_while_stmt_6(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile
            EndBody."""
        expect = "Error on line 12 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_while_stmt_7(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "Error on line 7 col 24: print"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_while_stmt_8(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
                EndWhile.
                EndWhile.
                EndWhile.
            EndBody."""
        expect = "Error on line 12 col 16: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_while_stmt_9(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;



                EndWhile;
            EndBody."""
        expect = "Error on line 14 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_while_stmt_10(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While (((i < 10))) Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "Error on line 10 col 20: i"
        self.assertTrue(TestParser.checkParser(input,expect,240))

        # test do while
    def test_do_while_stmt_241(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                While (((i < 10)))
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_do_while_stmt_242(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                While ( False )
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_do_while_stmt_243(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    ** Empty While **
                While ( False )
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_do_while_stmt_244(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While ( False )
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_do_while_stmt_245(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While ( 2 + 3 < 4 )
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_do_while_stmt_246(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = "Error on line 8 col 20: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_do_while_stmt_247(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While(True)
                    EndDo
                While ( False )
                EndDo.
            EndBody."""
        expect = "Error on line 9 col 16: While"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_do_while_stmt_248(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do.
                        Return a;
                    While(True)
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = "Error on line 5 col 22: ."
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_do_while_stmt_249(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While(True)
                    EndDo.
                While ( False  = 1)
                EndDo.
            EndBody."""
        expect = "Error on line 9 col 31: ="
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_do_while_stmt_250(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    
                        Return a;
                    While(True)
                    EndDo.
                While ( False  == 1)
                EndDo.
            EndBody."""
        expect = "Error on line 10 col 16: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,250))

        # test break statement
    def test_break_stmt_1(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break;
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_break_stmt_2(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break
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
        expect = "Error on line 7 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,252))


        # test continue statement
    def test_continue_stmt_1(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Continue;
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_continue_stmt_2(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Continue
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
        expect = "Error on line 7 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,254))

        # test function call
    def test_func_call_1(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = boo(1,2.3);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_func_call_2(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = boo(1, boo(1, foo(1)));
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_func_call_3(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( a[12] );
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_func_call_4(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo(  );
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_func_call_5(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( ( () ) );
            EndBody."""
        expect = "Error on line 4 col 31: )"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_func_call_6(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( ( (1) ) );
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))


        # summary test
    def test_summary_dec_1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_summary_dec_2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_summary_dec_3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_summary_dec_4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_summary_dec_5(self):
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
                    While (a \\. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_summary_dec_6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_summary_dec_7(self):
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
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_summary_dec_8(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1; i < 10; 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 10 col 30: ;"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_summary_dec_9(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True && False && True Do
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
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_summary_dec_10(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b < c Then
                    While True && False && True Do
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
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 25: <"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_summary_dec_11(self):
        input = """Function: foo
            Body:
                foo()goo();
            EndBody."""
        expect = "Error on line 3 col 21: goo"
        self.assertTrue(TestParser.checkParser(input, expect, 271))
    def test_summary_dec_12(self):
        input = """Var: a = 1.2e-3;
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
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))
    def test_summary_dec_13(self):
        input = """Function: foo
            Body:
                a = a && b > c;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))
    def test_summary_dec_14(self):
        input = """Function: foo
            Body:
                a[1.2] = a && b > c;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))
    def test_summary_dec_15(self):
        input = """Var: a[1.2] = {1};
            Function: foo
            Body:
                a[1.2] = a && b < c;
            EndBody."""
        expect = "Error on line 1 col 7: 1.2"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_summary_dec_16(self):
        input = """Function: foo
            Body:
                a = !-a && b < c + d*e;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))
    def test_summary_dec_17(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < 20, 2) Do
                        foo(b,a,c);
                    EndFor.
            EndBody."""
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 277))
    def test_summary_dec_18(self):
        input = """Function: foo
        Body:
            For (i = 5, a*.b\\.c-.d-.e=/=f , goo(g,h)) Do
                For (j = 0, j < 20, 1) Do
                    writeln(i);
                    If a && b Then
                        While True Do
                            foo(a,b,c);
                        EndWhile.
                    Else
                        Return a + b;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 278))
    def test_summary_dec_19(self):
        input = """Function: foo
            Body:
                Do
                    a = c+.d;
                    If (a<=.b) Then
                        Continue;
                    EndIf.
                    doThis();
                While (a<.c)
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 279))
    def test_summary_dec_20(self):
        input = """Continue;
            Function: foo
            Body:

            EndBody."""
        expect = "Error on line 1 col 0: Continue"
        self.assertTrue(TestParser.checkParser(input,expect, 280))
    def test_summary_dec_21(self):
        input = """Var: int a;
            Function: foo
            Body:

            EndBody."""
        expect = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.checkParser(input,expect, 281))
    def test_summary_dec_22(self):
        input = """Var: int, float, string, boolean;
            Function: foo
            Body:

            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 282))
    def test_summary_dec_23(self):
        input = """Function: foo
            Parameter: a,b,c, e = 911911
            Body:
                a = 0x123456;
                If a < b < c Then
                    While True && False && True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5))) + boo() * goo(a[abc]);
                        If a < b < c Then
                            Return a;
                        EndIf
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 2 col 32: ="
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_summary_dec_24(self):
        input = """Function: foo
            Parameter: a,b,c, e
            Body:
                a = 0x123456;
                If a < b < c Then
                    While True && False && True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5))) + boo() * goo(a[abc]);
                        If a < b < c Then
                            Return a;
                        EndIf
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 25: <"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_summary_dec_25(self):
        input = """Function: foo
            Parameter: a,b,c, e
            Body:
                a = 0x123456;
                If a < b Then
                    While True && False && True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5))) + boo() * goo(a[abc]);
                        If a < b Then
                            Return a;
                        EndIf
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 11 col 41: +"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_summary_dec_26(self):
        input = """Function: abctest
            Parameter: n,a[2][3][4],b[4][1],m
            Body:
                If n > 20 Then
                    Return 5;
                ElseIf n >5 Then a=a+.1; Return a;
                Else
                    Return False;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))
    def test_summary_dec_27(self):
        input = """Function: abctest
            Parameter: n,a[2][3][4],b[4][1],m
            Body:
            n = "Lorem Ipsum is simply dummy text of the printing and typesetting";
                If n > 20 Then
                    Return n + n;
                ElseIf n >5 Then a=a+.1; Return a;
                Else
                    Return False;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))
    def test_summary_dec_28(self):
        input = """Function: main
            Body:
                Var:a[2]={12,3,4},b=2,c=True;
                Var:c=4;
            EndBody.Function: foo
            Body:
                a=b+1;b=a==b;r=a+b+c-e-.d;
                foo((a+b+.12e10));
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
    def test_summary_dec_29(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < foo(), 2) Do
                        foo() = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 30: ="
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test_summary_dec_30(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < blackpink(do, do, do), 2) Do
                        blackpink(howYouLikeThat) = foo();
                    EndFor.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 50: ="
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_summary_dec_31(self):
        input = """Function: foo
            Body:
                ** Empty body **
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    def test_summary_dec_32(self):
        input = """Function: foo
            Body:
                a[** Empty body **] = {1};
            EndBody."""
        expect = "Error on line 3 col 34: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    def test_summary_dec_33(self):
        input = """Function: foo
            Body:
                str = "** Empty body";
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test_summary_dec_34(self):
        input = """Function: foo
            Body:
                str = ** Empty body "123456" **;
            EndBody."""
        expect = "Error on line 3 col 47: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    def test_summary_dec_35(self):
        input = """Function: foo
            Body:
                str = ** "string" * "string" **;
            EndBody."""
        expect = "Error on line 3 col 47: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test_summary_dec_36(self):
        input = """Function: foo
            Body:
                ** "string" ** ** "string" **
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test_summary_dec_37(self):
        input = """Var: b[2][3] = {{2,3,4}};
        Function: foo
        Parameter: a, b
        Body:
            **  
            * This is a block comment 
            * This is a block comment
            * This is a block comment 
            **
            b = a[2][1];
            a = b;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test_summary_dec_38(self):
        input = """Function: foo
            Body:
                If (a < b) && (!b <= c) Then
                    For (i = 1, i < foo(), 2) Do
                        foo() = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 30: ="
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test_summary_dec_39(self):
        input = """Function: foo
            Body:
                If (a < b) && !b <= c Then
                    For (i = 1, i < foo(), 2) Do
                        foo() = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 30: ="
        self.assertTrue(TestParser.checkParser(input, expect, 299))
    def test_summary_dec_40(self):
        input = """Function: foo
            Body:
                If a < b && !b <= c Then
                    For (i = 1, i < foo(), 2) Do
                        foo() = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = "Error on line 3 col 31: <="
        self.assertTrue(TestParser.checkParser(input, expect, 300))
    
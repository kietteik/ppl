import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_dec_1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_var_dec_2(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_var_dec_3(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_dec_4(self):
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_var_dec_5(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_var_dec_6(self):
        input = """Var: n[10], m;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_assignment_stm_1(self):
        input = """Var: a = 0;
Function: main
Body:
    a[3 + foo(2)] = a[b [2][3]] + 4;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_assignment_stm_2(self):
        input = """Var: a = 0;
Function: main
Body:
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_callee_stm_1(self):
        input = """Var: a = 0;
Function: main
Body:
    foo(a[1][2] + 2, x + 1);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_callee_stm_2(self):
        input = """Var: a = 0;
Function: main
Body:
    x = foo(a[1][2] + 2, x + 1);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_function_1(self):
        input = """Function: foo
Parameter: a[5], b
Body:
    Var: i = 0;
    While (i < 5) Do
        a[i] = b +. 1.0;
        i = i + 1;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_for_1(self):
        input = """Var: a = 0;
Function: main
Body:
    For (i = 0, i < 10, 2) Do
        writeln(i);
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_var_dec_7(self):
        input = """Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_simple_program_1(self):
        input = """Var: x;
Function: fact
    Parameter: n
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * fact (n - 1);
        EndIf.
    EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_var_dec_8(self):
        input = """Var: a[5] = {1,4,3,2,0};
Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_simple_program_2(self):
        input = """Var: x;
Function: fact
    Parameter: n
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * fact (n - 1);
        EndIf.
    EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_callee_stm_3(self):
        input = """Var: a = 0;
Function: main
Body:
    foo(a[1][2] + 2, x + 1);
    foo (2 + x, 4. \. y);
    goo ();
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_type_coercions_1(self):
        input = """Var: a = 0;
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_simple_program_3(self):
        input = """Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_var_dec_9(self):
        input = """Var: a = 1, b[2][3] = {5}, c[2] = {{1,3},{1,5,7}};
Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_simple_program_4(self):
        input = """Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return a[4][5 + b[2][3]];
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_var_dec_10(self):
        input = """Var: a = "Xin chao moi nguoi!";
Var: b = 5, c = False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_if_stm_1(self):
        input = """Function: test
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_if_stm_2(self):
        input = """Function: test
Body:
    If n > 10 Then
        Return n;
    ElseIf n > 8 Then
        Return n + 1;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_if_stm_3(self):
        input = """Function: test
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
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_simple_program_5(self):
        input = """Var:x;
Function: x 
Body: 
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_simple_program_6(self):
        input = """Var: x[1] = {5}, y[5] = {6.}, z[1][2] = {0O56};
Function: x 
Body:
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_for_2(self):
        input = """ Var: x;
Function: fact
Parameter: n
Var: i;
Body:
For(i = 1, i < 3, i = i+5)
Do
    x = i +7;
    If n > 100 Then
        Break;
    EndIf.
EndFor.
EndBody."""
        expect = "Error on line 4 col 0: Var"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_for_3(self):
        input = """Var: x;
Function: fact
Parameter: n

Body:
    Var: i, x = 0;
    For (i = 1, i < 3, -. 5) Do
        x = i +7;
        If n > 100 Then
            Break;
        EndIf.
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_assignment_stm_3(self):
        input = """Var: x = {{1,2},{{2}};"""
        expect = "Error on line 1 col 9: {"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_for_4(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, -. 2) Do
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_for_5(self):
        input = """Var: x;
Function: fact
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_simple_program_7(self):
        input = """Var: a = 5;
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_simple_program_8(self):
        input = """Var: a = 5;
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    Var: b[5];
    Var: c, d = 6, e;
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_simple_program_9(self):
        input = """Var: a = 5;
Var: b[5];
Var: c, d = 6, e;
Function: main
Var: b[5];
Var: c, d = 6, e;
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = "Error on line 5 col 0: Var"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_while_1(self):
        input = """Function: main
Body:
    While True print("Hello World!"); EndWhile.
EndBody."""
        expect = "Error on line 3 col 15: print"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_while_2(self):
        input = """Function: main
Body:
    While True Do print("Hello World!"); EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_while_3(self):
        input = """Function: main
Body:
    While True Do EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_simple_program_10(self):
        input = """Var: a = "a string";
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_simple_program_11(self):
        input = """Var: a = "a string";
Var: b[5];
Var: c, d = 6, e;
Function: main
Body:
    x = y + (z -q) *. 10 +. 100.;
    x = n >=. z;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_simple_program_12(self):
        input = """Var: a = "a string";
** Day la comment
* Day cung la comment
* Comment luon **
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_simple_program_13(self):
        input = """Var: a = "a string";
** Day la comment
* Day cung la comment
* Comment luon 
* Day cung la comment nhung chua dong lai**
Function: main
Body:
    x = y + (z -q) *. 10;
    x = n >=. z;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_simple_program_14(self):
        input = """**This is program
* Here is declare
* Here for function**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_simple_program_15(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_simple_program_16(self):
        input = """Var: x, y = 2., z = 3.5;
Function: you
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_simple_program_17(self):
        input = """Var: x, y = 1, z = 3.5;
Var: t;
Var: sp, yz;
Function: you
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_simple_program_18(self):
        input = """Var: a;
Function: main
Parameter: q , d[5]
Body:                                       
    x = foo(0XAB) + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_simple_program_19(self):
        input = """Var: a;
Function: main
Parameter: q , d[5]
Body:                                       
    x = foo("ahihi") + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_simple_program_20(self):
        input = """Var: uh;
Function: main
Parameter: q , d[5]
Body:                                       
    x = foo("ahihi") + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_simple_program_21(self):
        input = """Var: a;
Function: main
Parameter: q , d[5]
    Body: 
    Var: x, y = 1, z = 3.5;
    If((a > b) && (c < d)) Then
        Break;
    EndIf.                                          
    x = foo("ahihi") + goo(0o12);
    y = foo(x + goo(True));
    print(x + y);
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_simple_program_22(self):
        input = """Var: x;
Function: fact
Parameter: n, y
Body:
    While n[1] == a[2] Do
        **Check**
        Break;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_while_4(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a  >= 5) Do 
        a = a + 1;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_while_5(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        a = a + - 1;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_while_6(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <-= - 5) Do 
        a = a + - 1;
    EndWhile.
EndBody."""
        expect = "Error on line 4 col 15: ="
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_while_7(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do
        a = a + - 1;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_while_8(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        a = a + - 1 + - 5 - -5;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_do_while_1(self):
        input = """Var: a = 0;
Function: main
Body:
    Do 
        a = a + - 1 + - 5 - -5;
    While (a <= - 5) 
    EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_do_while_2(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
    While a <= - 5
    EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_do_while_3(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
    While True
    EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_do_while_4(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        print("Hello World!");
    While True
    EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_do_while_5(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        print("Hello World!");
    While
    EndDo.
EndBody."""
        expect = "Error on line 7 col 4: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_do_while_6(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        print("Hello World!");
    While (a > b) && (c < d)
    EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_do_while_7(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        print("Hello World!");
    While (a > b)
    EndDo
EndBody."""
        expect = "Error on line 8 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_do_while_8(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        print("Hello World!");
    While a = b
    EndDo
EndBody."""
        expect = "Error on line 6 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_do_while_9(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        a >= 6 + b;
    While a > b
    EndDo
EndBody."""
        expect = "Error on line 5 col 10: >="
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_do_while_10(self):
        input = """Var: a = 0;
Function: main
Body:
    Do
        Do
            Do
                print("Hello World!");
            While a > b
            EndDo.
            print("Hello World!");
        While a > b
        EndDo.
        print("Hello World!");
    While a > b
    EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_while_9(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        print("Hello World!");
        While (a <= - 5) Do 
            print("Hello World!");
            While (a <= - 5) Do 
                print("Hello World!");
                While (a <= - 5) Do 
                    print("Hello World!");
                EndWhile.
            EndWhile.
        EndWhile.
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_while_10(self):
        input = """Var: a = 0;
Function: main
Body:
    While (a <= - 5) Do 
        print("Hello World!");
        While (a <= - 5) Do
            Do
                Do
                    Do
                        print("Hello World!");
                    While a > b
                    EndDo.
                    print("Hello World!");
                While a > b
                EndDo.
                print("Hello World!");
            While a > b
            EndDo.
            print("Hello World!");
            While (a <= - 5) Do 
                print("Hello World!");
                While (a <= - 5) Do 
                    Do
                        Do
                            Do
                                print("Hello World!");
                            While a > b
                            EndDo.
                            print("Hello World!");
                        While a > b
                        EndDo.
                        print("Hello World!");
                    While a > b
                    EndDo.
                    print("Hello World!");
                EndWhile.
            EndWhile.
        EndWhile.
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_for_6(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        print("Hello World!");
        For (i = 0, i < 10, -2) Do
            For (i = 0, i < 10, 2) Do
                print("Hello World!");
                For (i = 0, i < 10, 2) Do
                    For (i = 0, i < 10, 2) Do
                        print("Hello World!");
                    EndFor.
                    print("Hello World!");
                EndFor.
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_for_7(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!");
            EndIf. 
            For (i = 0, i < 10, 2) Do         
                For (i = 0, i < 10,-. 2) Do
                    For (i = 0, i < 10, 2) Do  
                        If((a > b) && (c < d)) Then
                            If((a > b) && (c < d)) Then
                                print("Hello World!");
                            EndIf. 
                            print("Hello World!");
                        EndIf.     
                    EndFor.
                    print("Hello World!");
                EndFor.
                If((a > b) && (c < d)) Then
                    print("Hello World!");
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_for_8(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, -2) Do
        For (i = 0, i < 10,-.2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!")
            EndIf. 
            For (i = 0, i < 10, 2) Do         
                If((a > b) && (c < d)) Then
                    print("Hello World!");
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "Error on line 9 col 12: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_for_9(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!");
            EndIf. 
            For (i = 0, i < 10, - 2) Do         
                If((a = b) && (c < d)) Then
                    print("Hello World!");
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "Error on line 11 col 22: ="
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_for_10(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                Break;
            EndIf. 
            For (i = 0, i < 10, -2) Do         
                If((a == b) && (c < d)) Then
                    Break;
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_if_stm_4(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n > 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    EndIf.
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    ElseIf n > 8 Then
        print("Hello World!");
    ElseIf n > 2 Then
        print("Hello World!");
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_if_stm_5(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n = 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    EndIf.
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 10 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_if_stm_6(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    EndIf.
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!")
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 25 col 4: Else"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_if_stm_7(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!")
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 24 col 4: Else"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_if_stm_8(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_if_stm_9(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                        print("Hello World!");
                    ElseIf n >=. 8 Then
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 35 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_if_stm_10(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                        print("Hello World!");
                    ElseIf n >=. 8a Then
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 19 col 34: a"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_assignment_stm_4(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_assignment_stm_5(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n =. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "Error on line 11 col 10: ="
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_assignment_stm_6(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [[2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "Error on line 7 col 25: ["
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_assignment_stm_7(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c = 10];
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
        expect = "Error on line 5 col 27: ="
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_assignment_stm_8(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x != n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "Error on line 11 col 6: !="
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_assignment_stm_9(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 != r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_assignment_stm_10(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z -q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + - b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_if_stm_11(self):
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
                    While (a \. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
    def test_if_stm_12(self):
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
                        While (a \. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test_simple_program_23(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( ( () ) );
            EndBody."""
        expect = "Error on line 4 col 31: )"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_if_stm_13(self):
        input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n > 10 Then
                    print("Hello World!");
                ElseIf n = 8 Then
                    If n > 10 Then
                        print("Hello World!");
                    ElseIf n > 8 Then
                        print("Hello World!");
                    EndIf.
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    Else
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 12 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    def test_for_11(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!");
            EndIf. 
            For (i = 0, i < 10, - 2) Do         
                If((a != b) >= (c < d)) Then
                    print("Hello World!");
                EndIf. 
            EndFor.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    def test_for_12(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    For (i = 0, i < 10, 2) Do
        For (i = 0, i < 10, 2) Do
            If((a > b) && (c < d)) Then
                print("Hello World!");
            EndIf. 
            For (i = 0, i < 10, - 2) Do         
                If((a != b) >= (c < d)) Then
                    print("Hello World!");
                EndIf.
            print("Hello World!");
        EndFor.
    EndFor.
EndBody."""
        expect = "Error on line 17 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test_assignment_stm_11(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z - *q) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c \ 10];
    x = (a + - b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "Error on line 10 col 17: *"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    def test_assignment_stm_12(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(2)] = a[b [2][3]] + 4;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    x = foo(a[1][2] + 2, x + 1);
    x = y + (z - q - 1 - 4 + 6) *. 10;
    x = n >=. z;
    x = d[y *. z +. t -. c % 10];
    x = (a + - b) * y - z + (sp *. yz);
    a = a + - 1 + - 5 - -5;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test_assignment_stm_13(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 + foo(2)]][3]] + 4;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test_assignment_stm_14(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    x = d[y *. z +. t -. c \ 10];
    b[2][3] = {{2,3,4},{4,5,6}};
    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3  foo(2)]][3]] + 4;
EndBody."""
        expect = "Error on line 7 col 54: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test_assignment_stm_15(self):
        input = """Function: fact
Parameter: n
Body:
Var: x;
    x = d[y *. z +. t -. c \ 10];
    b[2][3][3 + foo(a[3 + foo(a[3 + foo(2)])])] = {{2,3,4},{4,5,6}};
    a[3 + foo(a[3 + foo(a[3 + foo(2)])])] = a[b [a[3 * foo(2)]][3]] + 4;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test_complex_program_1(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
Function: test
** Day la comment
* Day cung la comment
* Comment luon 
* Day cung la comment nhung chua dong lai**
Body:
    Var: b[2][3] = {{2,3,4},{4,5,6}};
    Var: c, d = 6, e, f;
    Var: m, n[10];
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                        x = d[y *. z +. t -. c \ 10];
                        b[2][3] = {{2,3,4},{4,5,6}};
                        a[3 + foo(2)] = a[b [2][3]] + 4;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        x = foo(a[1][2] + 2, x + 1);
                        x = y + (z -q) *. 10;
                        x = n >=. z;
                        x = d[y *. z +. t -. c \ 10];
                        x = (a + - b) * y - z + (sp *. yz);
                        a = a + - 1 + - 5 - -5;
                        print("Hello World!");
                    ElseIf n >=. 8-.a Then
                        ** Day la comment
                        * Day cung la comment
                        * Comment luon 
                        * Day cung la comment nhung chua dong lai**
                        For (i = 0, i < 10, 2) Do
                            For (i = 0, i < 10, 2) Do
                                If((a > b) && (c < d)) Then
                                    Break;
                                EndIf. 
                                For (i = 0, i < 10, -2) Do         
                                    If((a == b) && (c < d)) Then
                                        Break;
                                    EndIf. 
                                EndFor.
                                print("Hello World!");
                            EndFor.
                        EndFor.
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                ** Day la comment**
                print("Hello World!");
            EndIf.
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                foo(a[1][2] + 2, x + 1);
                foo (2 + x, 4. \. y);
                goo ();
                If bool_of_string ("True") Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                    Do
                        Do
                            Do
                                print("Hello World!");
                            While a > b
                            EndDo.
                            print("Hello World!");
                        While a > b
                        EndDo.
                        print("Hello World!");
                    While a > b
                    EndDo.
                    foo(a[1][2] + 2, x + 1);
                    foo (2 + x, 4. \. y);
                    goo ();
                EndIf.
            EndWhile.
            ** *Day la comment**
            print("Hello World!");
        EndIf.
        For (i = 0, i < 10,  2) Do
            Return 1;
            Break;
            Continue;
            foo(float_of_int (a) + 2);
            goo(a+1);
        EndFor.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_complex_program_2(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
Function: test
** Day la comment
* Day cung la comment
* Comment luon 
* Day cung la comment nhung chua dong lai**
Body:
    Var: b[2][3] = {{2,3,4},{4,5,6}};
    Var: c, d = 6, e, f;
    Var: m, n[10];
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                        x = d[y *. z +. t -. c \ 10];
                        b[2][3] = {{2,3,4},{4,5,6}};
                        a[3 + foo(2)] = a[b [2][3]] + 4;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        x = foo(a[1][2] + 2, x + 1);
                        x = y + (z -q) *. 10;
                        x = n >=. z;
                        x = d[y *. z +. t -. c \ 10];
                        x = (a + - b) * y - z + (sp *. yz);
                        a = a + - 1 + - 5 - -5;
                        print("Hello World!");
                    ElseIf n >=. 8-.a Then
                        ** Day la comment
                        * Day cung la comment
                        * Comment luon 
                        * Day cung la comment nhung chua dong lai**
                        For (i = 0, i < 10, 2) Do
                            For (i = 0, i < 10, 2) Do
                                If((a > b) && (c < d)) Then
                                    Break;
                                EndIf 
                                For (i = 0, i < 10, -2) Do         
                                    If((a == b) && (c < d)) Then
                                        Break;
                                    EndIf. 
                                EndFor.
                                print("Hello World!");
                            EndFor.
                        EndFor.
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                ** Day la comment**
                print("Hello World!");
            EndIf.
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                foo(a[1][2] + 2, x + 1);
                foo (2 + x, 4. \. y);
                goo ();
                If bool_of_string ("True") Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                    Do
                        Do
                            Do
                                print("Hello World!");
                            While a > b
                            EndDo.
                            print("Hello World!");
                        While a > b
                        EndDo.
                        print("Hello World!");
                    While a > b
                    EndDo.
                    foo(a[1][2] + 2, x + 1);
                    foo (2 + x, 4. \. y);
                    goo ();
                EndIf.
            EndWhile.
            ** *Day la comment**
            print("Hello World!");
        EndIf.
        For (i = 0, i < 10,  2) Do
            Return 1;
            Break;
            Continue;
            foo(float_of_int (a) + 2);
            goo(a+1);
        EndFor.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
        expect = "Error on line 49 col 32: For"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    
    

        
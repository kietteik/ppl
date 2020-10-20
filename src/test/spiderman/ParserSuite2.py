import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_vardec_1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_vardec_2(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_vardec_3(self):
        input = """Var: b[123][123] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_vardec_4(self):
        input = """Var: a,tes=123,  b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_vardec_5(self):
        input = """Var: m=12, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_vardec_6(self):
        input = """Var: n[10]={1,2,3}, m;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_assignment_statement_1(self):
        input = """Function: main
        Body:
        a[3 + foo(2)] = a[b [2][3]] + 4;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_assignment_statement_2(self):
        input = """Function: main
        Body:
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_callee_statement_1(self):
        input = """Function: main
        Body:
        foo(a[1][2] + 2, x + 1);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_callee_statement_2(self):
        input = """Function: main
        Body:
        x = foo(a[1][2] + 2, x + 1);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

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
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_for_1(self):
        input = """Function: main
        Body:
        For (i = 0, i < 10, 2) Do
    writeln(i);
EndFor.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_var_dec_7(self):
        input = """Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_var_dec_func_dec_1(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_var_dec_8(self):
        input = """Var: a[5] = {1,4,3,2,0};
Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_var_dec_func_dec_2(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_callee_stm_3(self):
        input = """Function: main
        Body:
        foo (2 + x, 4. \. y);
goo ();EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_type_coercions_1(self):
        input = """Function: main
        Body:
        If bool_of_string ("True") Then
a = int_of_string (read ());
b = float_of_int (a) +. 2.0;
EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_var_dec_func_dec_3(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_var_dec_9(self):
        input = """Function: main
        Body:
        a = 1;
b[2][3] = 5;
c[2] = {{1,3},{1,5,7}};
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_var_dec_func_dec_4(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_var_dec_10(self):
        input = """Var: he = "hello";
Var: b = 5, c = False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

        # addmore

    def test_comment_in_program_1(self):
        input = """**Declare variable**Var: he = "hello";
Var: b = 5, c = False;
**Program over "over"**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_comment_in_program_2(self):
        input = """**Declare variable**Var: he = "hello";
Var: b = 5, c = False;
**Program over "over"** Var: a = {"bk","c","d"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_comment_in_program_3(self):
        input = """**Declare variable**Var: he = "hello";
Var: b = 5, c = False;
**Program over "over"** Var: a = {"bk","c","d"},ac,ab,ad=8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_simple_wrong_string(self):
        input = """Var: i;
        AAA"""
        expect = "A"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_func_elseif_1(self):
        input = """Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    ElseIf n >5 Then a=a+1; Return a;
    ElseIf n < 10 Then a=a+1; Return a;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_func_dec_elseif_2(self):
        input = """Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    ElseIf n >5 then a=a+1; Return a;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "Error on line 6 col 16: then"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_func_dec_param_1(self):
        input = """Function: abctest
Parameter: n,a[2],b[5][6],m
Body:
    If n > 10 Then
        Return 5;
    ElseIf n >5 Then a=a+.1; Return a;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_func_dec_1(self):
        input = """Function: abctest
Parameter: a[2],b[5][6]
Body:
    Var:b;
    Var:b,c,d;
    If n > 10 Then
        Return 5;
    ElseIf n >5 Then a=a+1; Return a;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_func_dec_2(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            Function: funcinsidefunc
            Body:
            EndBody.
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "Error on line 5 col 12: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_func_dec_3(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            If n > 10 Then
                Return 5;
            EndIf.
            Var:c=2;
        EndBody."""
        expect = "Error on line 8 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_func_dec_param_2(self):
        input = """Function: abctest
    Parameter: a[2],b[5][6]
    Body:
        If n > 10 Then
            Return 5;
        ElseIf n >5 Then aa+1; Return a;
        Else
            Return False;
        EndIf.
    EndBody."""
        expect = "Error on line 6 col 27: +"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_for_statement_1(self):
        input = """Function: main
        Parameter: x
        Body:   For (a=5,a<10,aa+1) Do abc(a); EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_for_statement_2(self):
        input = """Function: main
        Parameter: x
        Body:
            For (a=5,a<10,a+.1) Do 
                abc(a);
                For (a=2,a==0,a*1) Do
                    If ab==cd Then
                    a=a+1;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_for_statement_3(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
            writeln(i);
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))


# reference


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
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
    expect = "successful"
    self.assertTrue(TestParser.checkParser(input, expect, 279))

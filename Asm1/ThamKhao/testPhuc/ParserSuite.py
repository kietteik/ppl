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
        input = """a[3 + foo(2)] = a[b [2][3]] + 4;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_assignment_stm_2(self):
        input = """v = (4. \. 3.) *. 3.14 *. r *. r *. r;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_callee_stm_1(self):
        input = """foo(a[1][2] + 2, x + 1);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_callee_stm_2(self):
        input = """x = foo(a[1][2] + 2, x + 1);"""
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
        input = """For (i = 0, i < 10, 2) Do
    writeln(i);
EndFor."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_var_dec_7(self):
        input = """Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
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
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_var_dec_8(self):
        input = """Var: a[5] = {1,4,3,2,0};
Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
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
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_callee_stm_3(self):
        input = """foo (2 + x, 4. \. y);
goo ();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_type_coercions_1(self):
        input = """If bool_of_string ("True") Then
a = int_of_string (read ());
b = float_of_int (a) +. 2.0;
EndIf."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
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
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_var_dec_9(self):
        input = """a = 1;
b[2][3] = 5;
c[2] = {{1,3},{1,5,7}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
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
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_var_dec_10(self):
        input = """Var: a = "Xin chao moi nguoi!";
Var: b = 5, c = False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

        
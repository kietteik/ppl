import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_glb_var_1(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_glb_var_2(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_glb_var_3(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_glb_var_4(self):
        input = """Var x;"""
        expect = "Error on line 1 col 4: x"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_glb_var_5(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_glb_var_6(self):
        input = """Var: c, d = 6, e, f = "abcdef";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_glb_var_7(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_glb_var_8(self):
        input = """Var: n[10], m;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_glb_var_9(self):
        input = """n[10], m;"""
        expect = "Error on line 1 col 0: n"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_glb_var_10(self):
        input = """Var: n = m;"""
        expect = "Error on line 1 col 9: m"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_assignment_1(self):
        input = """
        Function: foo
        Body:
            a = 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_assignment_2(self):
        input = """
        Function: foo
        Body:
            a = goo(a,b);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_assignment_3(self):
        input = """
        Function: foo
        Body:
            a[3 + foo(2)] = a[b [2][3]] + 4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_assignment_4(self):
        input = """
        Function: foo
        Body:
            a = (4. \\. 3.) *. 3.14 *. r *. r *. r;
        EndBody.  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_assignment_5(self):
        input = """
        Function: foo
        Body:
            a = b = c;
        EndBody.  
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_call_stm_1(self):
        input = """
        Function: foo
        Body:
            foo(a, b + 1);
        EndBody.  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_call_stm_2(self):
        input = """
        Function: foo
        Body:
            foo(a[1][2] + 2, x + 1);
        EndBody.  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_call_stm_3(self):
        input = """
        Function: foo
        Body:
            foo(goo(a, b + 1));
        EndBody.  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_call_stm_4(self):
        input = """
        Function: foo
        Body:
            foo(());
        EndBody.  
        """
        expect = "Error on line 4 col 17: )"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_call_stm_5(self):
        input = """
        Function: foo
        Body:
            foo()goo();
        EndBody.  
        """
        expect = "Error on line 4 col 17: goo"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_func_dec_1(self):
        input = """
        Function: foo
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_func_dec_2(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_func_dec_3(self):
        input = """
        Function: foo
        Parameter: a, 1
        Body:
        EndBody.
        """
        expect = "Error on line 3 col 22: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_func_dec_4(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            a = b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_func_dec_5(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_func_dec_6(self):
        input = """

        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        Function: main
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_func_dec_7(self):
        input = """
        Var: a = 1.2e-3;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        Function: goo
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_func_dec_8(self):
        input = """
        Var: a = 1.2e-3;
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
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_func_dec_9(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            b = a[2][1];
            a = b;
        EndBody.
        Var: a = 1.2e-3;
        Function: goo
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = "Error on line 9 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_func_dec_10(self):
        input = """
        Var: a = 1.2e-3;
        Function: goo
        Parameter: c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
        EndBody.
        """
        expect = "Error on line 8 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_func_dec_11(self):
        input = """
        Function: goo
        c, d
        Body:
            c[2] = {3,2};
            d = 2.e+1;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
        EndBody.
        """
        expect = "Error on line 3 col 8: c"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_func_dec_12(self):
        input = """
        Var: a = 1.2e-3;
        Function: goo
        Parameter: c, d
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_func_dec_13(self):
        input = """
        Var: a = 1.2e-3;
        Function: goo
        Parameter: c, d
        Body:
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            c[2] = {3,2};
            d = 2.e+1;
        EndBody
        """
        expect = "Error on line 10 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_func_dec_14(self):
        input = """
        Var: a = 1.2e-3;
        Function: goo
        Parameter: c, d
        Body:
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            c[2] = {3,2};
            d = 2.e+1;
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_func_dec_15(self):
        input = """
        Var: a = 1.2e-3;
        Function: goo
        Parameter:
        Body:
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            c[2] = {3,2};
            d = 2.e+1;
        EndBody.
        """
        expect = "Error on line 5 col 8: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_expression_1(self):
        input = """
        Function: foo
        Body:
            a = a > b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_expression_2(self):
        input = """
        Function: foo
        Body:
            a = a && b > c;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_expression_3(self):
        input = """
        Function: foo
        Body:
            a = a && b > c + d;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_expression_4(self):
        input = """
        Function: foo
        Body:
            a = a && b > c + d*e;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_expression_5(self):
        input = """
        Function: foo
        Body:
            a = !-a && b > c + d*e;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_expression_6(self):
        input = """
        Function: foo
        Body:
            a = foo(a[1][2]);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_expression_7(self):
        input = """
        Function: foo
        Body:
            a = foo(a[1][2]*3.2e-3 + {{2},{2}} +goo());
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_expression_8(self):
        input = """
        Function: foo
        Body:
            a = (a*2.e3 > 4 + 5)\\.b*.d -. f;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_expression_9(self):
        input = """
        Function: foo
        Body:
            a = (b;
        EndBody.
        """

        expect = "Error on line 4 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_expression_10(self):
        input = """
        Function: foo
        Body:
            a = ;
        EndBody.
        """
        expect = "Error on line 4 col 16: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_if_1(self):
        input = """
        Function: foo
        Body:
            If a < b Then
                While True Do
                    foo(a,b);
                EndWhile.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_if_2(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                While True Do
                    foo(a,b);
                EndWhile.
            Else
                Return a;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_if_3(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                While True Do
                    foo(a,b);
                EndWhile.
            ElseIf a != b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
            Else
                Return a;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_if_4(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                While True Do
                    foo(a,b);
                EndWhile.
            ElseIf a != b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
            ElseIf a == b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
            Else
                Return a;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_if_5(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                If a == (b + 1) Then
                    foo(b,a);
                ElseIf a == b Then
                    For (i = 1, i < 10, 2) Do
                        foo(b,a);
                    EndFor.
                Else
                    Return a;
                EndIf.
            ElseIf a != b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
            ElseIf a == b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
            Else
                Return a;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_if_6(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                If a == (b + 1) Then
                    foo(b,a);
                ElseIf a == b Then
                    For (i = 1, i < 10, 2) Do
                        foo(b,a);
                    EndFor.
                Else
                    Return a;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_if_7(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                For (i = 1, i < 10, 2) Do
                    foo(b,a);
                EndFor.
        EndBody.
        """
        expect = "Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_if_8(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                If a == (b + 1) Then
                    foo(b,a);
                Else
                    Return a;
                ElseIf a == b Then
                    For (i = 1, i < 10, 2) Do
                        foo(b,a);
                    EndFor.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "Error on line 9 col 16: ElseIf"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_if_9(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                If a == (b + 1) Then
                    foo(b,a);
                Else
                    Return a;
                Else
                    Return a;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "Error on line 9 col 16: Else"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_if_10(self):
        input = """
        Function: foo
        Body:
            If a && b Then
                ElseIf a == (b + 1) Then
                    foo(b,a);
                    goo(c,d);
                ElseIf a == b Then
                    For (i = 1, i < 10, 2) Do
                        foo(b,a);
                    EndFor.
                Else
                    Return a;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 16: ElseIf"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_for_1(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 256))

    def test_for_2(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                For (j = 0, j < 10, 1) Do
                    writeln(i);
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 257))

    def test_for_3(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                For (j = 0, j < 10, 1) Do
                    writeln(i);
                    If a && b Then
                        While True Do
                            foo(a,b);
                        EndWhile.
                    Else
                        Return a;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 258))

    def test_for_4(self):
        input = """
        Function: foo
        Body:
            For (i = 0, a*.b\\.c+.d-.e=/=f , goo(g,h)) Do
                For (j = 0, j < 10, 1) Do
                    writeln(i);
                    If a && b Then
                        While True Do
                            foo(a,b);
                        EndWhile.
                    Else
                        Return a;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 259))

    def test_for_5(self):
        input = """
        Function: foo
        Body:
            For (i = 0, a*.b\\.c+.d-.e=/=f , goo(g,h)) Do
                foo(a,b);
                fun2(d,e);
                fun3(f,g);
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 260))

    def test_for_6(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do

            EndFor.
        EndBody."""
        expect = "Error on line 6 col 12: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect, 261))

    def test_for_7(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                Var: m, n[10];
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect, 262))

    def test_for_8(self):
        input = """
        Function: foo
        Parameter: i
        Body:
            For (i, i < 10, 1) Do
                iterate10Times();
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect, 263))

    def test_for_9(self):
        input = """
        Function: foo
        Body:
            For (i = 0, i < 10, 1) Do
                iterate10Times();;
            EndFor.
        EndBody."""
        expect = "Error on line 5 col 33: ;"
        self.assertTrue(TestParser.checkParser(input,expect, 264))

    def test_for_10(self):
        input = """
        Function: foo
        Body:
            For (i = 0, True) Do
                iterate10Times();;
            EndFor.
        EndBody."""
        expect = "Error on line 4 col 28: )"
        self.assertTrue(TestParser.checkParser(input,expect, 265))

    def test_while_1(self):
        input = """
        Function: foo
        Body:
            While True Do
                doThis();
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 266))

    def test_while_2(self):
        input = """
        Function: foo
        Body:
            While True Do
                doThis();
                doThat();
                While (a+b\\-d*e\\f || g) Do
                    doOtherThings();
                EndWhile.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 267))

    def test_while_3(self):
        input = """
        Function: foo
        Body:
            While True Do
            
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 268))

    def test_while_4(self):
        input = """
        Function: foo
        Body:
            While True
                doOtherThings();
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 16: doOtherThings"
        self.assertTrue(TestParser.checkParser(input,expect, 269))

    def test_while_5(self):
        input = """
        Function: foo
        Body:
            While a = b Do
                doOtherThings();
            EndWhile.
        EndBody."""
        expect = "Error on line 4 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect, 270))

    def test_do_while_1(self):
        input = """
        Function: foo
        Body:
            Do
                doOtherThings();
            While a > b
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 271))

    def test_do_while_2(self):
        input = """
        Function: foo
        Body:
            Do
                doOtherThings();
                Do
                    doThat();
                While c > d
                EndDo.
            While a > b
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 272))

    def test_do_while_3(self):
        input = """
        Function: foo
        Body:
            Do
                
            While e > f
            EndDo.
            Do
                doOtherThings();
                Do
                    doThat();
                While c > d
                EndDo.
            While a > b
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 273))

    def test_do_while_4(self):
        input = """
        Function: foo
        Body:
            Do
                doThat();
            While e > f
        EndBody."""
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect, 274))

    def test_do_while_5(self):
        input = """
        Function: foo
        Body:
            Do
                doOtherThings();
                Do
                    doThat();
                While c > d
                EndDo.
            While
            EndDo.
        EndBody."""
        expect = "Error on line 11 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect, 275))

    def test_full_1(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_full_2(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_full_3(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_full_4(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_full_5(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_full_6(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_full_7(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_full_8(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_full_9(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_full_10(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_full_11(self):
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
    def test_full_12(self):
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
    def test_full_13(self):
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

    def test_full_14(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < blackpink(do, do, do), 2) Do
                        blackpink[3][4] = foo();
                    EndFor.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_full_15(self):
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
        self.assertTrue(TestParser.checkParser(input,expect, 290))

    def test_comment_1(self):
        input = """
        ** This is a block comment **
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_comment_2(self):
        input = """
        ** This is a block comment **
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_comment_3(self):
        input = """
        ** This is a block comment **
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            ** This is a block comment **
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_comment_4(self):
        input = """
        ** This is a block comment **
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            ** This is a block comment **** This is a block comment **
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_comment_5(self):
        input = """
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Function: foo
        Parameter: a, b
        Body:
            **  This is a block comment 
                This is a block comment
                This is a block comment 
            **
            b = a[2][1];
            a = b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_return_1(self):
        input = """
        Function: foo
        Body:
            Do
                a = c+d;
                If (a<b) Then
                    Return;
                EndIf.
                doThat();
            While (a<c)
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 296))

    def test_return_2(self):
        input = """
        Var: c, d = 6, e, f = "abcdef";
        Function: foo
        Body:
            
        EndBody.
        Return a+b;
        """
        
        expect = "Error on line 7 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect, 297))

    def test_skip_1(self):
        input = """
        Function: foo
        Body:
            Do
                a = c+d;
                If (a<b) Then
                    Continue;
                EndIf.
                doThat();
            While (a<c)
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 298))

    def test_skip_2(self):
        input = """
        Function: foo
        Body:
            For(a = 1, a< b, 2) Do
                a = c+d;
                If (a<b) Then
                    Break;
                EndIf.
                doThat();
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 299))

    def test_skip_3(self):
        input = """
        Continue;
        Function: foo
        Body:

        EndBody."""
        expect = "Error on line 2 col 8: Continue"
        self.assertTrue(TestParser.checkParser(input,expect, 300))
    # def test_func_dec_4(self):
    #     input = """
    #     Function: foo
    #         Parameter: a,b,c
    #         Body:
    #             If a < b Then
    #                 While True Do
    #                     foo(a,b);
    #                 EndWhile.
    #             ElseIf a == b Then
    #                 For (i = 1, i < 10, i = i + 1) Do
    #                     foo(b,a);
    #                 EndFor.
    #             Else
    #                 Return a;
    #             EndIf.
    #         EndBody.
    #     """
    #     expect = "Error on line 3 col 22: 1"
    #     self.assertTrue(TestParser.checkParser(input,expect,224))

    # def test_function_1(self):
    #     input = """
    #     Function: foo
    #     Parameter: a[5], b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,215))
    # def test_for_1(self):
    #     input = """
    #     Function: foo
    #     Body:
    #         For (i = 0, i < 10, 2) Do
    #             writeln(i);
    #         EndFor.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,216))
    # def test_var_dec_7(self):
    #     input = """
    #     Var: a = 5;
    #     Var: b[2][3] = {{2,3,4},{4,5,6}};
    #     Var: c, d = 6, e, f;
    #     Var: m, n[10];
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,217))
    # def test_var_dec_func_dec_1(self):
    #     input = """
    #     Var: x;
    #     Function: fact
    #         Parameter: n
    #         Body:
    #             If n == 0 Then
    #                 Return 1;
    #             Else
    #                 Return n * fact (n - 1);
    #             EndIf.
    #         EndBody.
    #     Function: main
    #     Body:
    #         x = 10;
    #         fact (x);
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,218))
    # def test_var_dec_8(self):
    #     input = """Var: a[5] = {1,4,3,2,0};
    #                 Var: b[2][3]={{1,2,3},{4,5,6}};"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,219))
    # def test_var_dec_func_dec_2(self):
    #     input = """
    #     Var: x;
    #     Function: fact
    #         Parameter: n
    #         Body:
    #             If n == 0 Then
    #                 Return 1;
    #             Else
    #                 Return n * fact (n - 1);
    #             EndIf.
    #         EndBody.
    #     Function: main
    #         Body:
    #             x = 10;
    #             fact (x);
    #         EndBody.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,220))
    # def test_callee_stm_3(self):
    #     input = """
    #     Function: foo
    #     Body:
    #         foo (2 + x, 4. \\. y);
    #         goo ();
    #     EndBody.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,221))
    # def test_type_coercions_1(self):
    #     input = """
    #     Function: fact
    #     Body:
    #         If bool_of_string ("True") Then
    #         a = int_of_string (read ());
    #         b = float_of_int (a) +. 2.0;
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,222))
    # def test_var_dec_func_dec_3(self):
    #     input = """
    #     Function: test
    #     Parameter: n
    #     Body:
    #         If n > 10 Then
    #             Return 5;
    #         Else
    #             Return False;
    #         EndIf.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,223))
    # def test_var_dec_9(self):
    #     input = """
    #     Function: foo
    #     Body:
    #         a = 1;
    #         b[2][3] = 5;
    #         c[2] = {{1,3},{1,5,7}};
    #     EndBody.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,224))
    # def test_var_dec_func_dec_4(self):
    #     input = """
    #     Function: test
    #     Parameter: n
    #     Body:
    #         If n > 10 Then
    #             Return 5;
    #         Else
    #             Return a[4][5 + b[2][3]];
    #         EndIf.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,225))
    # def test_var_dec_10(self):
    #     input = """
    #     Var: a = "Xin chao moi nguoi!";
    #     Var: b = 5, c = False;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,226))

    # def test_str_1(self):
    #     input = """
    #     Function: foo
    #     Body:
    #         a = "\\b";
    #     EndBody.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,227))

    # def test_str_2(self):
    #     input = """
    #     Function: foo
    #     Body:
    #         a = "\\";
    #     EndBody.
    #     """
    #     expect = '\\"'
    #     self.assertTrue(TestParser.checkParser(input,expect,228))

    # # def test_cmt_1(self):
    # #     input = 'a = "\\";'
    # #     expect = '\\"'
    # #     self.assertTrue(TestParser.checkParser(input,expect,224))

    # def test_if_stm_9(self):
    #     input = """
    #     Function: test
    #     Body:
    #         If n > 10 Then
    #             If n > 10 Then
    #                 print("Hello World!");
    #             ElseIf n > 8 Then
    #                 If n > 10 Then
    #                     print("Hello World!");
    #                 ElseIf n > 8 Then
    #                     If n != 10 Then
    #                         print("Hello World!");
    #                     ElseIf n > 8 Then
    #                         If n > 10 Then
    #                             While (i < 5) Do
    #                                 a[i] = b +. 1.0;
    #                                 i = i + 1;
    #                             EndWhile.
    #                             print("Hello World!");
    #                         ElseIf n >=. 8 Then
    #                             print("Hello World!");
    #                         print("Hello World!");
    #                     EndIf.
    #                     print("Hello World!");
    #                 EndIf.
    #                 While (i < 5) Do
    #                     a[i] = b +. 1.0;
    #                     i = i + 1;
    #                 EndWhile.
    #                 print("Hello World!");
    #             EndIf.
    #             print("Hello World!");
    #         EndIf.
    #             print("Hello World!");
    #         EndIf.
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,229))

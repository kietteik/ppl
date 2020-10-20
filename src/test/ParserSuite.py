import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    # variables declaration
    def test_vardec_1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_vardec_2(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_vardec_3(self):
        input = """Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];"""
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
        input = """Var: n[10]={1,2,3}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_vardec_7(self):
        input = """Var: n[10]={1,2,3}, a2[3],b123[123],c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_vardec_8(self):
        input = """Var: n[10][2]={{1},{2},{3}}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_vardec_9(self):
        input = """Var: a[1],b[1],c[1],d[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_vardec_10(self):
        input = """Var: n[10][1][2][3]={1,2,3}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_vardec_11(self):
        input = """Var: a[1],b[1],c[1],d[1];
        Var: a[1],b[1],c[1],d[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_vardec_12(self):
        input = """Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_vardec_13(self):
        input = """Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_vardec_14(self):
        input = """Var:a=1;Var:a=1;Var:a=1;Var:a=1;Var:a=1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_vardec_15(self):
        input = """Var: n[10][1][2][3]={{123,2,3,4},{2},3};"""
        expect = "Error on line 1 col 20: {"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    # function declaration
    def test_funcdec_1(self):
        input = """Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_funcdec_2(self):
        input = """Function: main
        Body:Var:a=1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_funcdec_3(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_funcdec_4(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        EndIf
        EndBody."""
        expect = "Error on line 4 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_funcdec_5(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        a=b+1;b=a==b;r=a+b+c-e-.d;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_funcdec_6(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        a=b+1;b=a==b;r=a+b+c-e-.d;
        foo(foo((a+b+.12e10))+foo());
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_funcdec_7(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        EndBody.Function: foo
        Body:a=b+1;b=a==b;r=a+b+c-e-.d;
        foo((a+b+.12e10));EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_funcdec_8(self):
        input = """Function: main
        Body:
        Function:fooBody:EndBody.
        EndBody."""
        expect = "Error on line 3 col 8: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_funcdec_9(self):
        input = """Function: main
        Body:
        EndBody.Function: main
        Body:
        EndBody.Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_funcdec_10(self):
        input = """
        Var: a = 5;Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;Var: m, n[10];
        Function: main
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    # STATEMENT

    def test_param_1(self):
        input = """Function: abctest
        Parameter: n,a[2],b[5][6]m
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+.1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "Error on line 2 col 33: m"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_elseif_1(self):
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

    def test_elseif_2(self):
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
        expect = "Error on line 6 col 24: then"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_param_0(self):
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

    def test_ifelse_1(self):
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

    def test_ifelse_2(self):
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

    def test_ifelse_3(self):
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

    def test_param_2(self):
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
        expect = "Error on line 6 col 31: +"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_for_1(self):
        input = """Function: main
        Parameter: x
        Body:   For (a=5,a<10,aa+1) Do abc(a); EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_for_2(self):
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

    def test_for_3(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
            writeln(i);
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_for_4(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_for_5(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
                While (True) Do
                For (i = 0, i < 10, 2) Do
                Var:a=1;
                writeln(i);
                a=b;
                EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_for_6(self):
        input = """Function: main
        Body:
            Var:var=2;
            For (i = 0, i < 10, 2) Do
                While (True) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                    writeln(i);
                    EndFor.
                a=b;
                EndFor.
                EndWhile.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_for_7(self):
        input = """Function: main
        Body:
            Var:var=2;
            For (i = 0, i < 10, 2) Do
                While (True) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                    writeln(i);
                    EndFor.
                a=b;
                EndWhile.
                EndFor.
            EndFor.
        EndBody."""
        expect = "Error on line 16 col 16: EndWhile"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_while_1(self):
        input = """Function: main
        Parameter: x
        Body:   While (True) Do
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_while_2(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(c<=d)) Do
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_while_3(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_while_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_while_5(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_while_6(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_while_7(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                foo(a==1);
                EndWhile.
                writeln(i);
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_while_8(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                foo(a==1);
                EndWhile.
                writeln(i);
                EndWhile.
                EndFor.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_while_9(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a*b) Do
                writeln(i);
                While ((b>=a)==(b!=c)+d*a) Do
                writeln(i);
                foo(a==1);
                EndWhile.
                writeln(i);
                EndFor.
                EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "Error on line 13 col 16: EndFor"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_while_10(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                For (i = 0, i < 10, 2) Do
                writeln(i);
                    While ((b>=a)==(b!=c)+d*a*b) Do
                    writeln(i);
                        While ((b>=a)==(b!=c)+d*a) Do
                        writeln(i);
                        foo(a==1);
                        EndWhile.
                    writeln(i);
                    EndWhile.
                EndFor.
                        While ((b>=a)==(b!=c)+d*a) Do
                        writeln(i);
                        foo(a==1);
                        EndWhile.
                writeln(i);
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_dowhile_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_dowhile_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_dowhile_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_dowhile_4(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                While (True)
                Do
                    writeln(i);
                    While (a==12+3)
                EndDo.
                EndDo.
        EndBody."""
        expect = "Error on line 9 col 16: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_dowhile_5(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Do
                    writeln(i);
                While (a==12+3)
                EndDo.
                Do
                    writeln(i);
                While (a==12+3)
                EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_dowhile_6(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                            writeln(i);
                        Do
                        While (a==12+3)
                        EndDo.
                        While (a==12+3)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_dowhile_7(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                        While (True) Do
                        EndWhile.
                        Do
                        While (a==12+3)
                        EndDo.
                        While (a==12+3)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_dowhile_8(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                        While (True) Do
                            Do
                            writeln(i);
                            While(True)
                            EndDo.
                        EndWhile.
                        Do
                        While (a==2+1)
                        EndDo.
                        While (a==2+1)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_dowhile_9(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                        While (True) Do
                            writeln(i);
                            While(True)
                            EndDo.
                        EndWhile.
                        Do
                        While (a==2+1)
                        EndDo.
                        While (a==2+1)
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = "Error on line 12 col 28: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_dowhile_10(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                writeln(i);
                    Do
                        writeln(i);
                        writeln(i);
                            writeln(i);
                        Do
                        While ((a==b)==(c==d))
                        EndDo.
                        While ((a==b)==(d==d))
                    EndDo.
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_break_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_break_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_break_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    Break;
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                Break;
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_break_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                If (a==2) Then
                Break;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_break_5(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Break;
                EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_continue_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Continue;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_continue_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Continue;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_continue_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    Continue;
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                Continue;
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_continue_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                If (a==2) Then
                Continue;
                EndIf.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                writeln(i);
                EndWhile.
                EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_continue_5(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Continue;
                EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_return_1(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Return True;
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_return_2(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                writeln(i);
                Return True;
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_return_3(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                Do
                    Return True;
                    Break;
                    writeln(i);
                    While (a==12+3)
                EndDo.
                writeln(i);
                Return True;
                Break;
                While (a==12+3)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_return_4(self):
        input = """Function: main
        Parameter: x
        Body:   While ((b>=a)==(b!=c)+d*a*b*c) Do
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
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_return_5(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
            writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Return True;
                Break;
                EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_return_6(self):
        input = """Function: main
        Parameter: x
        Body:
                Return a+b+c==2;
                Do
                Continue;
                If (a==2) Then
                Return;
                Break;
                EndIf.
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_return_7(self):
        input = """Function: main
        Parameter: x
        Body:   Do
                    writeln(i);
                    If (a==2) Then
                        Continue;
                    Else
                        Return a+b+c==2;
                        Break;
                    EndIf.
                While (True)
                EndDo.
                Return a+b+c==2;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_return_8(self):
        input = """Function: main
        Parameter: x
        Body:   Return;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_return_9(self):
        input = """Function: main
        Parameter: x
        Body:   Return1+1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_return_10(self):
        input = """Function: main
        Parameter: x
        Body:   For (i = 0, i < 10, 2) Do
                writeln(i);
                For (i = 0, i < 10, 2) Do
                writeln(i);
                If (a==2) Then
                Continue;
                EndIf.
                EndFor.
                EndFor.
                Return1+1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_comment_in_program_1(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_comment_in_program_2(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"** Var: a[1] = {"bk","c","d"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_comment_in_program_3(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Declare variable**
        Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_comment_in_program_4(self):
        input = """******Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_comment_in_program_5(self):
        input = """******Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody.
        **terminated by a comment****followed by a comment**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_funccall_0(self):
        input = """Function: main
        Parameter: x
        Body:   fooo((a+1));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_funccall_1(self):
        input = """Function: main
        Parameter: x
        Body:   fooo((a+1));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_funccall_2(self):
        input = """Function: main
        Parameter: x
        Body:   fooo((a+1)+True+abcd);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_funccall_3(self):
        input = """Function: main
        Parameter: x
        Body:   fooo("this is a string param","and second string");
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_funccall_4(self):
        input = """Function: main
        Parameter: x
        Body:   fooo("this is a string param",funct("string",12));
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_funccall_5(self):
        input = """Function: main
        Parameter: x
        Body:   fooo(fucn1(func2(func3("string",{1,2,3},{{23},{1,3,4}}))),"and second string");
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_funccall_6(self):
        input = """Function: main
        Parameter: x
        Body:   fooo();
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_assignment_1(self):
        input = """Function: main
        Parameter: x
        Body:   a=12;a[2][3][4]={1,2,34};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_assignment_2(self):
        input = """Function: main
        Parameter: x
        Body:   a=12;a[2][3][4]=2;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_assignment_3(self):
        input = """Function: main
        Parameter: x
        Body:   a="string string";
                b=foo();
                c[1]=foo(foo());
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_parser_1(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable**
        Function: main
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
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_parser_2(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable**
        Function: main
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                    writeln(i);
                    If (a==2) Then
                        Return True;
                        If n > 10 Then
                            Return 5;
                        ElseIf n >5 Then a=a+1; Return a;
                        ElseIf n < 10 Then a=a+1; Return a;
                        ElseIf n < 100 Then a=a+1; Return b;
                        Else
                            Return False;
                        EndIf.
                        Break;
                    EndIf.
                    While ((b>=a)==(b!=c)+d*a*b*c) Do
                        writeln(i);
                        If n > 10 Then
                            Return 5;
                        ElseIf n >5 Then a=a+1; Return a;
                        ElseIf n < 10 Then a=a+1; Return a;
                        Else
                            Return False;
                        EndIf.
                    EndWhile.
                EndWhile.
        EndBody.
        **Program over "over" foo dec**
        Function: foo
        Parameter: x
        Body:   Do
                Break;
                While (True)
                EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_parser_3(self):
        input = """
        **Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable**
        Function: main
        Parameter: x
        Body:   a="string string \\n \\t *commetn****unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_parser_4(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable******
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Function: main
        Parameter: x
        Body:   a="string string \\n \\t *commetn****unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        EndBody.
        Function: main2
        Parameter: x,a[2],b[2][3]
        **comment**
        Body:   a="string string'"'" ***unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        **comment**
        EndBody.
        **comment**
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_parser_5(self):
        input = """
        Var: he = "hello\\t\\n\\b\\t\\\\abce***string{}{}{2,3,4,}}'"string in string'"";
        Var: b = 5, c = False;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;
        **Declare variable******
        Function: main
        **Declare variable******
        Parameter: x
        Body:   a="string string";
                x=n >=.z;
                x=d[y *.z +. t -.c\ 10];
                x=(a + -b) * y -z+ (sp *. yz);
                a=a + -1 + - 5--5;
        **Declare variable******
                b=foo();
                c[1]=foo(foo());
        EndBody.
        **Declare variable******
        Function: main2
        Parameter: x,a[2],b[2][3]
        **comment**
        Body:   a="string string'"'" ***unclosing comment";
                b=foo();
                c[1]=foo(foo());
                **comment insidefuntion**
                **comment insidefuntion****comment insidefuntion**
        **comment**
        EndBody.
        **comment**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_assignment_stm_60(self):
        input = """Function: main
        Body:
a[3+foo(2)]=a[b[[2][3]]]+4;
        EndBody."""
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.checkParser(input, expect, 301))

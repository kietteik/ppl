import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        procedure abc ();
            var x  : real  ;
        begin
            if x = y then
                a:= 100;
            else;
                b:= 999;
        end
        """
        expect = "Error on line 7 col 16: ;"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4;
            End
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_more_complex_program(self):
        """More complex program"""
        input = """proceDure main () ;BEGIN
            putIntLn(4);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_variable_declaration(self):
        input = """PROCEDURE main() ;
                  var a, b, c : integer ;
                    d: array [1 .. 5] of integer ;
                    e , f : real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_function_declaration(self):
        input = """FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_procedure_declaration(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_assign_statement1(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    a := 1;
                    b := a[12] ;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_assign_statement2(self):
        input = """proCeduRe foo() ;
                  var x,y: real ;
                  BEGIN
                    a := "conga";
                    b := func(1,a+1) ;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_assign_statement3(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    3 := 1;
                   END"""
        expect = "Error on line 4 col 22: :="
        self.assertTrue(TestParser.test(input,expect,209))
    def test_assign_statement4(self):
        input = """function foo(c: real): real ;
                   var x,y: array[1 .. 7] of real;
                   BEGIN
                    foo()[m*1] := a[a div 3] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_assign_statement5(self):
        input = """function foo(c: real): real ;
                   var x: integer ;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_assign_statement6(self):
        input = """function foo(c: real): real ; x:=a[1]"""
        expect = "Error on line 1 col 30: x"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_if_statement1(self):
        input = """function foo(c: real): real ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_if_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else foo();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_if_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_if_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_if_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    if (1<2) then beGin x:=1 ; end
                    else foo(a+1,2);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_if_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then beGin
                        a:=1 ;
                        if(1=1) then a:= b[1];
                        else b:=a[1]:= 1;
                    end
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_while_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_while_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_while_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_while_statement4(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                        if(a=1) then begin end
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_with_statement1(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do
                    d := c [a] + b ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_with_statement2(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_with_statement3(self):
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    with a , b : integer ; do begin
                        foo2(a,b,"anc");
                    end
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_with_statement4(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; do
                        foo2(a,b,"anc");
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_for_statement1(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do 
                        s := s + 1;
                   END"""
        expect = "successful"
    def test_for_statement1(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do BEGIN
                        s := s + 1;
						END
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_for_statement2(self):
        input = """procedure main(c: integer): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        if(a=1) Then BEGIN s:=s-1;END
                    end
                   END"""
        expect = "Error on line 1 col 26: :"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_for_statement3(self):
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        for j:=m+1 doWnTO 100 do beGin
                            s := s + 1;
                            if(a=1) then s:=s-1;
                        eND
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_for_statement4(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_break_statement(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        Continue;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_continue_statement(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do continuE ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_return_statement1(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do reTuRn ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_return_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1) do reTuRn foo(a+1);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_compound_statement(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1=1) do begin eND
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_call_statement1(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_call_statement2(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_call_statement3(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return foo2();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_call_statement3(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_call_statement4(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    textbackground(brown); {background colour}
                    ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
                    return func(a(1,2));
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_multi1(self):
        input = """
                procedure test1() ;
                begin
                   if a=b then
                   begin
                         b := c ;
                         if(e <> f) then foo(a,c) ;
                   end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_multi2(self):
        input = """
                procedure test2() ;
                begin
                   if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_multi3(self):
        input = """
                var i: integer ;
                function f(): integer ;
                begin
                   return 200;
                end
                procedure main() ;
                var
                   main: integer ;
                begin
                end
                var g: real ;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_multi4(self):
        input = """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_multi5(self):
        input = """
                Var
                    Num1, Num2, Sum : Integer;
                Procedure concaheo(a, c:Real);
                Begin {no semicolon}
                    Write("nhap so 1:");
                    Readln(Num1);
                    Writeln("nhap so 2:");
                    Readln(Num2);
                    Sum := Num1 + Num2; {phep cong}
                    Write(Sum);
                    Readln();
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_multi6(self):
        input = """
                Var name, surname: String;
                Procedure Main();
                Begin
                   write("Nhap ten cua ban:");
                   write("Nhap ho cua ban:");
                   writeln();(*new line*)
                   writeln();//new line}
                   writeln("Ten day du cua ban la : ",name," ",surname);
                   readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_multi7(self):
        input = """
                Var PD, Dnakme, Ckmodel : String;
                CostPD, TCokstPD, Distance : Real;
                {real is a decimal (described later on)}
                Procedure main();
                Begin
                    textbackground(brown); {background colour}
                    ClrSjcr(); {Clear screen with a brown colour. Try run the program without this..}
                    TextColor(lightgreen); {text colour}
                    TCostPD := 0;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_multi8(self):
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 name();
                 return ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_multi9(self):
        input = """
                procedure main() ;
                beGin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_multi10(self):
        input = """
                procedure main() ;
                var a: array[0 .. -1] of integer;
                 i,j,temp: integer;
                beGin
         
                            
                    print(a);
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_multi11(self):
        input = """
                function sum_real_array(a: array[0 .. m-1] of real;n:integer):real;
                var i:integer;s:real;
                beGin
                    s:=0.;
                    for i:=n-1 doWnTO 0 do s:=s+a[i];
                    reTuRn s;
                eND
                procedure main() ;
                var a: array[0 .. m-1] of real; n:integer;
                beGin
                    Writeln("Sum of real array: "+sum_real_array(a,n));
                eND
                """
        expect = "Error on line 2 col 54: m"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_multi12(self):
        input = """
                Function Arrays(A : array[0 .. 10] of integer;N:Integer);
                Var i: string;
                Begin
                Write("So luong phan tu:");
                Readln( N);
                For i:=0 to N do
                    Begin
                        Write("Nhap phan tu thu", i," ");
                        Readln( A[i] );
                    End
                End
                """
        expect = "Error on line 2 col 72: ;"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_multi13(self):
        input = """
                Function Tong_So_Chia_Het_Cho5(A:array[0 .. 10] of integer ; N:Integer):Integer;
                Var S,i :Integer;
                Begin
                    S:=0;
                    For i:=0 to N do
                    If(A[i] mod 5=0) then
                    S := S+A[i];
                    return S;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_multi14(self):
        input = """
                Function LaSoNT(N:Integer) :Integer;
                Var i:Integer;
                Begin
                 For i:=2 to N-1 do
                  If(N mod i = 0) then
                    return 0;
                  Else
                    return 1;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_multi15(self):
        input = """
                Function DemPtuX(A:array[0 .. 10] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=0 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_multi16(self):
        input = """
                Procedure ThayTheTatCa (A:array[0 .. 10] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                 For i:=0 to N do
                  If(A[i] = x) then { Tim thay x ==> thay the thanh y }
                  A[i] := y;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_multi17(self):
        input = """
                Procedure ThayTheBangTong(A:array[0 .. 10] of integer; N:Integer; X, Y:Integer);
                Var i,k:Integer;
                Begin
                 For i:=0 to N do
                 If( (A[i-1]+A[i]) mod 10 = 0) then
                 Begin
                  k := (A[i-1]+A[i]);
                  A[i-1] := k;
                  A[i] := k;
                 End
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_multi18(self):
        input = """
                Function KtraDoiXung (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
                Var Flag:Boolean;
                    i :Integer;
                Begin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                 return flag;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_multi19(self):
        input = """
                Function KtraMangTang ( A:array[0 .. 10] of REAL; N :Integer) : Boolean;
                Var Flag : Boolean;
                 i :Integer;
                Begin
                 Flag := True;
                 i:= 0;
                 while(i<n) do begin
                  If(A[i] < A[i-1]) Then
                   Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
                  i:=i+1;
                 end
                 return Flag;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_multi20(self):
        input = """
                Function KtraMangCapSoCong (A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                 for i:=1 to N do
                 if(A[i] <> A[i-1] + k) then
                  flag:=false;     // Cham dut, ket qua: khong phai
                 return flag; {Ket qua kiem tra la mang cap so cong}
                End
                """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_multi21(self):
        input = """
                Procedure ChenPhanTu(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
                Var i :Integer;
                Begin
                 For i:=N downto k+ 1 do
                  A[i] := A[i-1];
                 A[k] := X;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_multi22(self):
        input = """
                function gt(x:integer):integer;
                begin
                if x = 0 then
                 return 1;
                else
                 return x+gt(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_multi23(self):
        input = """
                function fibo(x: integer): integer;
                var f1,f2: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_multi24(self):
        input = """
                function ok(i : integer):boolean;
                var k : integer;
                begin
                 ok := true;
                 for k := 2 to i div 2 do
                  if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    ok := false;
                    exit();
                   end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_multi25(self):
        input = """
                Procedure Daoso(n: integer);
                Begin
                 Assign(f,fo);
                  Rewrite(f);
                 If n > 0 then
                  Begin
                  Write(f,n mod 10);
                  Daoso(n mod 10);
                  End
                 Close(f);
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_multi26(self):
        input = """
                Function UCLN(m,n:integer):integer;
                Begin
                 If(m=n) then RETURN m ;
                 else
                  If (m>n) then return UCLN(m-n,n);
                  else return UCLN(m,n-m);
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_multi27(self):
        input = """
                Var r,dt,cv:real;
                pROCEDURE main() ;
                Begin
                 Clrscr();
                 Writeln("TINH DIEN TICH & CHU VI HINH TRON:");
                 Writeln("--------------------------------------------------");
                 Write ("Nhap ban kinh R="); readln(r);
                 dt:=pi*r*r;
                 cv:=2*pi*r;
                 Writeln("Dien tich hinh tron la:",dt);
                 Writeln("Chu vi hinh tron la:",cv);
                 Readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_multi28(self):
        input = """
                pROCEDURE main() ;
                Var a,b,x:real;
                Begin
                Clrscr();
                Writeln("GIAI PHUONG TRINH BAC NHAT: AX + B=0");
                Writeln("-------------------------------------------------------");
                Write ("Nhap a= "); readln(a);
                Write ("Nhap b= ");readln(b);
                If(a=0) then 
				 begin
                 If(b=0) then Writeln(" Phuong trinh co vo so nghiem");
				 end
                 Else writeln("Phuong tring vo nghiem");
                Else Writeln("Phuong trinh co nghiem x=",-b/a);
                Readln();
                End
                """
        expect = "Error on line 15 col 16: Else"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_multi29(self):
        input = """
                Var a,b,c,s,p: real;
                pROCEDURE main();
                Begin
                Clrscr();
                Else Writeln(a,", ", b,", ", c, " khong phai la ba canh cua tam giac");
                Readln();
                End
                """
        expect = "Error on line 6 col 16: Else"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_multi30(self):
        input = """
                Procedure Caclua(X : Integer; Y : Integer);
                Var Counter : Integer; { this is called a local variable }
                Begin
                 GotoXy(X,Y);
                 textcolor(green);
                 For Counter := 1 to 10 do
                 Begin
                  Write(chr(196));
                 End
                End
                procedure main();
                Begin
                 Readkey();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_multi71(self):
        input= """
               var a,b,c:integer;
				procedure host(a:integer;b:integer;c:integer);
				begin
				readln(a,b,c); 
				if (a*a=1) 
				or(b*b=1)or(c*c=1) then 
				write("a=b=c=1") 
				else write("Ko la bo so"); 
				readln; 
				end
               """
        expect = "Error on line 9 col 4: else"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_multi72(self):
        input= """
               var a,b,c:integer;
				procedure(a:integer;b:integer;c:integer);
				begin
				readln(a,b,c); 
				if (a*a=b*b+c*c) 
				or(b*b=a*a+c*c)or(c*c=a*a+b*b) then 
				write("Day la bo so Pytago") 
				else write("Ko la bo so Pytago"); 
				readln; 
				end
               """
        expect = "Error on line 3 col 13: ("
        self.assertTrue(TestParser.test(input,expect,272))
    def test_multi73(self):
        input= """
		function namnhuan(a:integer):integer;
               begin 
					write("Nhap nam : "); 
					readln(n); 
					if (n mod 400 = 0) or else ((n mod 4 = 0) and then(n mod 100 <> 0)) then write("namnhuan");
					else write("Ko fai nam nhuan"); 
					readln; 
				end
               """
        expect = "Error on line 8 col 11: ;"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_multi74(self):
        input= """
		function namnhuan(a:integer):integer;
               begin 
					write("Nhap nam : "); 
					if (n mod 400 = 0) or else ((n mod 4 = 0) and then (n mod 100 <> 0)) then write("namnhuan");
					else write("Ko fai nam nhuan"); 
					readln; 
				end
               """
        expect = "Error on line 7 col 11: ;"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_multi75(self):
        input= """
		function namnhuan(a:integer):integer;
               begin 
					write("Nhap nam : "); 

				end 
                a
               """
        expect = "Error on line 7 col 16: a"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_multi77(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin

			End
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_multi77(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin
				 For j:=1 To nk Do
				 If (true) Then
				  Begin
				   If k=n Then 
				   Else THU(k+1); {Quay lui}
				  End
			End
			"""
        expect = "Error on line 9 col 7: Else"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_multi78(self):
        input= """	   
			var a,b,c:integer; 
					S,p:real; 
					begin 
					clrscr; 
					write("Nhap canh a,b,c:"); 
					readln(a,b,c); 
					p:=(a+b+c)/2; 
					S:=sqrt[p*(p-a)*(p-b)*(p-c)]; 
					write("dien tich tam giac la:",S:3:3); 
					readln; 
					end.
			"""
        expect = "Error on line 4 col 5: begin"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_multi79(self):
        input= """	   
			function max(num1, num2: integer): integer;
			var
			(* local variable declaration *)
			result: integer;
			begin
			if (num1 > num2) then
			result := num1;
			else
			result := num2;
			max := result;
			end
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_multi80(self):
        input= """	   
			function myLine(x: real): real;
			begin
				myLine := 0.5 * x + 2;
			end
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_multi81(self):
        input= """	   
			function myParabola(x: real): real;
			begin
				result := sqr(x) - 1;
			end
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_multi82(self):
        input= """	   
			function even(x: longint): boolean;
			begin
				exit(not odd(x));
			end
			"""
        expect = "Error on line 2 col 20: longint"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_multi83(self):
        input= """	   
			procedure Main();
				begin
					WriteLn("Hello World");
				end
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_multi84(self):
        input= """	   
			procedure SillyName();
					var
						name: String;
					begin
						Write("Enter your name: ");
						ReadLn(name);
					 
						if name == "Fred" then
						begin
							SayHello(name);
						end
						else
						begin
							WriteLn("I dont know you...");
						end;
					end;
			"""
        expect = "Error on line 9 col 15: ="
        self.assertTrue(TestParser.test(input,expect,284))
    def test_multi85(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin
				 For j:=1 To nk Do
				 If (true) Then
				  Begin
				   If k=n Then 
				   Else THU(k+1); {Quay lui}
				  End
			End
			"""
        expect = "Error on line 9 col 7: Else"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_multi86(self):
        input= """	   
			procedure PrintMultiple(message: String; times: Integer);
				var
					i: Integer;
				begin
					for i := 1 to times do
					begin
						WriteLn(message);
					end
				end
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_multi87(self):
        input= """	   
			function Highest(v1, v2, v3: Integer): Integer;
					begin
						if (v1 > v2) and (v1 > v3) then
						begin
							result := v1;
						end 
						else if v2 > v3 then
						begin
							result := v2;
						end
						else
						begin
							result := v3;
						end
					end
			"""
        expect = "Error on line 4 col 23: ("
        self.assertTrue(TestParser.test(input,expect,287))
    def test_multi88(self):
        input= """
			X:integer;
			Function Weird(A : Integer) : Integer;
				Var
				 S : Integer;
				Begin
					S := A/2;
					If S < 10 Then
						Weird := 1;
						S := S + 9;
					If S >= 10 Then
						Weird := 0;
					Weird := 2;
				End
			"""
        expect = "Error on line 2 col 3: X"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_multi89(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin
				 For j:=1 To nk Do
				 If (true) Then
				  Begin
				   If k=n Then 
				   Else THU(k+1); {Quay lui}
				  End
			End
			"""
        expect = "Error on line 9 col 7: Else"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_multi90(self):
        input= """	   
			Function Weird(A : Integer) : Integer;
					Var
					 S : Integer;
					Begin
					 S := A/2;
					 If S < 10 Then
					 Begin
					  Weird := 1;
					  Exit;
					End
			"""
        expect = "Error on line 10 col 11: ;"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_multi91(self):
        input= """	   
			Procedure EnterUserInfo(TxtCol : SmallInt; TxtBck : SmallInt);
				Begin
					textcolor(TxtCol);
					textbackground(TxtBck);
					ClrScr;
					Readln(UMail);
					Write(" Thank you for entering your personal information!!");
					Readkey;
				End;
			"""
        expect = "Error on line 2 col 36: SmallInt"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_multi92(self):
        input= """	   
			procedure foo();
				begin
					exit;
					inc(x);
				end
			"""
        expect = "Error on line 4 col 9: ;"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_multi93(self):
        input= """	   
			procedure Take(f: TFuncOneArgsString); overload;
				begin
				  WriteLn(f("there!!!"));
				end
			"""
        expect = "Error on line 2 col 21: TFuncOneArgsString"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_multi94(self):
        input= """	   
			procedure pause();
			begin
			  writeln("Press any key when ready ...");
			  readkey;
			end
			"""
        expect = "Error on line 5 col 12: ;"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_multi95(self):
        input= """	   
			procedure foo();
				var  a : byte;
				begin
				  a:=10;
				  writeln(a);
				end
			"""
        expect = "Error on line 3 col 13: byte"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_multi96(self):
        input= """	   
			procedure foo;
			var a : byte;
			begin
			  a:=15;
			  writeln("foo is ",a);
			end
			"""
        expect = "Error on line 2 col 16: ;"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_multi97(self):
        input= """	   
			function yesno():boolean;
				var c : char;
				begin
				  write("Are you sure (Y/N) ? ");
				  repeat
					c:=upcase(readkey);      { Make it upcase letters }
				  until (c="Y") or (c="N");
				  writeln(c);
				  if c="Y" then yesno:=true else yesno:=false;
				end
			"""
        expect = "Error on line 3 col 12: char"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_multi98(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin
				 For j:=1 To nk Do
				 If (false) Then
				  Begin
				   If k:=10 Then 
				   Else THU(k+1); {Quay lui}
				  End
			End
			"""
        expect = "Error on line 8 col 11: :="
        self.assertTrue(TestParser.test(input,expect,298))
    def test_multi99(self):
        input= """	   
			procedure calculateideal(input1 : real; input2 : real);
				begin
				obc := "abcs";
				end
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_multi100(self):
        input= """	   
			var
            x : boolean; { Don"t be tricked, this is a LOCAL variable of main block }
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
    def test_multi101(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin
				 j:="Integer"+"Integer";
			End
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,301))
    def test_multi105(self):
        input= """	   
			Procedure THU(k:Integer);
			Var j:Integer;
			Begin
				 j:=array[10+1];
			End
			"""
        expect = "Error on line 5 col 8: array"
        self.assertTrue(TestParser.test(input,expect,302))
    def test_multi102(self):
        input= """	   
			var
            x;y : real; { Don"t be tricked, this is a LOCAL variable of main block }
			"""
        expect = "Error on line 3 col 13: ;"
        self.assertTrue(TestParser.test(input,expect,303))
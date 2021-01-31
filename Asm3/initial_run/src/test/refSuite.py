def test_4540(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1, 1},{1, 1}}, y;

Function: main
Parameter: a[2][2],b
Body:
    Return True;
EndBody.

Function: foo
Parameter: f[2], g
Body:
    main({1,1}, 1);
EndBody.
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,4540))

    def test_4490(self):
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
EndBody.
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[ArrayLiteral(IntLiteral(1),IntLiteral(1)),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,4490))


    def test_4440(self):
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
    EndBody.
    """
        expect = "Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(<,Id(y),IntLiteral(10)),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(2)]),[],[If(BinaryOp(<,Id(y),IntLiteral(1)),[],[Assign(Id(y),IntLiteral(1))])Else([],[])])"
        self.assertTrue(TestChecker.test(input,expect,4440))
    def test_4540(self):
        """Type Cannot Be Inferred"""
        input = """
Var: x[2][2] = {{1,1},{1,1}};
Var: y;
Function: main
Parameter: a[2][2],b
Body:
    main({{1,1},{1,1}}, y);
    main(x, y);
EndBody.
"""
        expect = "Type Cannot Be Inferred: CallStmt(Id(main),[ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(1)),ArrayLiteral(IntLiteral(1),IntLiteral(1))),Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,4540))





    
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
    def test_408(self):
        input = """Var: x, y[2][2] = {{1,2},{1,2}};
Function: main
Body:
    x = 1;
    foo(x)[1][1] = "a";
EndBody.
Function: foo
Parameter: x
Body:
    Return {{1,2},{1,2}};
EndBody.
        """
        expect = """Type Mismatch In Statement: Return(ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(2))))"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """Function: main
Parameter: x[1][2]
Body:
    Var: y[1][1] = {{1}};
    x = {{1,2}};
    main();
EndBody."""
        expect = """Type Mismatch In Statement: CallStmt(Id(main),[])"""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        input = """Function: foo
Body:
    Var: a=1,x;
    a=foo(x);
EndBody. """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        input = """Function: foo
Parameter: x
Body:
    Var: a=1;
    a=foo(x);
EndBody.
Function: main
Body:
EndBody.
 """
        expect = """Type Cannot Be Inferred: Assign(Id(a),CallExpr(Id(foo),[Id(x)]))"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_412(self):
        input = """Var: x, y, z, main;
Function: foo0
Parameter: a,b,c
Body:
    Var: i, j, k;
    a = 1;
    b = 2;
    If (j == 2) Then
        Var: f;
        f = a;
    EndIf.
EndBody.
Function: foo
Body:
EndBody."""
        expect = expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = """Var: x, y, z;
Function: main
Body:
    y = x + foo(z);
EndBody.
Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = str(TypeCannotBeInferred(Assign(Id('y'),BinaryOp('+',Id('x'),CallExpr(Id('foo'),[Id('z')])))))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        input = """Var: x, y, z;
Function: main
Body:
    z = 1.0;
    y = x + foo(z);
EndBody.
Function: foo
Parameter: a
Body:
    foo(z);
EndBody.
"""
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[Id('z')])))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_415(self):
        input = """Var: x, y, z;
Function: main
Body:
    foo(z,y);
EndBody.
Function: foo
Parameter: a,b,c
Body:
    foo(a,b,c);
EndBody.
"""
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[Id('z'),Id('y')])))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_416(self):
        input = """Var: x, y[2] = {{1,2},{1,2}};
Function: main
Body:
    x = 1;
    foo(x)[1][1] = "a";
EndBody.
Function: foo
Parameter: x
Body:
    Return {{1,2},{1,2}};
EndBody.
        """
        expect = """Type Mismatch In Expression: VarDecl(Id(y),[2],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(2))))"""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_417(self):
        input = """Var: x, y[2][2] = {{1,2},{1,2}};
Function: main
Parameter: t
Body:
    t = y[1] + 1;
EndBody.
        """
        expect = """Type Mismatch In Expression: ArrayCell(Id(y),[IntLiteral(1)])"""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_418(self):
        input = """Var: x[2][2], y[2][2] = {{1,2},{1,2}};
Function: main
Parameter: t, q, k
Body:
    t = y[1][1] + 1;
    q = x[1][1] + 1;
    x[1][1] = 1.2;
EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(ArrayCell(Id(x),[IntLiteral(1),IntLiteral(1)]),FloatLiteral(1.2))"""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = """Var: x[2][2], y[2][2] = {{1,2},{1,2}};
Function: main
Parameter: t, q, k
Body:
    t = y[1][1] + 1;
    q = x[1][1] + 1;
    x[k][1] = 1;
    k = 1.2;
EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(Id(k),FloatLiteral(1.2))"""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_420(self):
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
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        input = """Var: x, y[2][2] = {{1,2},{1,2}};
Function: main
Body:
    x = 1;
    foo(x)[1][1][1] = 1;
EndBody.
Function: foo
Parameter: x
Body:
    Return {{1,2},{1,2}};
EndBody.
        """
        expect = """Type Mismatch In Statement: Return(ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(2))))"""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_422(self):
        input = """Var: x, y[2][2] = {{1,2},{1,2}};
Function: main
Body:
    x = 1;
EndBody.
Function: foo
Parameter: x
Body:
    Return y;
EndBody.
Function: foo1
Parameter: z
Body:
    z = 1;
    z = 3;
EndBody.
Function: foo2
Parameter: z
Body:
    z = foo1(x);
EndBody.
        """
        expect = """Type Mismatch In Statement: Assign(Id(z),CallExpr(Id(foo1),[Id(x)]))"""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        input = """Var: x[2][2], y[2][2] = {{1,2},{1,2}}, m[3][3];
Function: main
Parameter: t, q, k
Body:
    t = y[1][1] + 1;
    q = x[1][1] + 1;
    x[k][1] = 1;
    foo(m) = x;
EndBody.
Function: foo
Parameter: x[1][2]
Body:
EndBody.
        """
        expect = """Type Cannot Be Inferred: Assign(CallExpr(Id(foo),[Id(m)]),Id(x))"""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_482(self):
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
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_483(self):
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
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_481(self):
            input = """Var: uh, d[5];
    Function: main
    Parameter: q , x, y, t
    Body:                                       
        y = foo(string_of_float("1.2") +. foo(1.2));
        uh = string_of_float(y);
        t = foo(1.2);
        d[4] = t;
    EndBody.
    Function: foo
    Parameter: y
    Body: 
        Var: x;
        d[3] = 1;
    EndBody.
    """
            expect = """Type Mismatch In Expression: CallExpr(Id(string_of_float),[StringLiteral(1.2)])"""
            self.assertTrue(TestChecker.test(input,expect,481))
import unittest
from TestUtils import TestAST
from AST import *
#..........1613166: Nguyen Minh Tham............
class ASTGenSuite(unittest.TestCase):
    
    def test_many_declaration_1(self):
        """Test Many Declaration"""
        input = """ Function foo():integer; Begin END
                    var x,y: real; 
                    var m:integer;
                    var a,b: real; 
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[]),VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(m),IntType),VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,301))

    def test_many_declaration_2(self):
        """Test Many Declaration"""
        input = """ var x,y: real; 
                    Procedure foo(a,b:integer); Begin END
                    Function foo(a,b:integer):integer; Begin END
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType(),[],[]),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_many_declaration_3(self):
        """Test Many Declaration"""
        input = """ var x,y: real; 
                    Procedure foo(a,b:integer); Begin END
                    var z: real; 
                    Function foo(a,b:integer):integer; Begin END
                    var a: real;                    
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType(),[],[]),VarDecl(Id(z),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],IntType,[],[]),VarDecl(Id(a),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_decl_1(self):
        """Test Variable Declaration: many declaration"""
        input = """ var x,y: real; 
                        z: sTring;
                    var a,b: boolean;                        
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),StringType),VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType)])"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_var_decl_2(self):
        """Test Variable Declaration: many declaration"""
        input = """ var x,y: real; 
                        z: sTring;
                    var a,b: boolean;
                    var c: string;
                        d,e,f: integer;
                        h:real;                        
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),StringType),VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType),VarDecl(Id(c),StringType),VarDecl(Id(d),IntType),VarDecl(Id(e),IntType),VarDecl(Id(f),IntType),VarDecl(Id(h),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_var_decl_3(self):
        """Test Variable Declaration: Array type"""
        input = """ var x,y: real; 
                        z: array [-0 .. 5] of integer;                      
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),ArrayType(0,5,IntType))])"
        self.assertTrue(TestAST.test(input,expect,306))


    def test_var_decl_4(self):
        """Test Variable Declaration: Array type"""
        input = """ var x,y: real; 
                    var    z: array [-1 .. -5] of integer;                      
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),ArrayType(-1,-5,IntType))])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_func_decl_1(self):
        """Test function declaration: parameter list"""
        input = """ Function foo():integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_func_decl_2(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a,b,c:real):integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_func_decl_3(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a,b:real;x,y:Boolean):integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_func_decl_4(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a,b:real;x,y:Boolean;z:string):integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType),VarDecl(Id(z),StringType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_func_decl_5(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a:real;z: array [-1 .. 5] of boolean):integer;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(z),ArrayType(-1,5,BoolType))],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_func_decl_6(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(z: array [-1 .. -55] of boolean):integer;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(z),ArrayType(-1,-55,BoolType))],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_func_decl_7(self):
        """Test function declaration: return type"""
        input = """ Function foo():boolean;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],BoolType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_func_decl_8(self):
        """Test function declaration: return type"""
        input = """ Function foo():real;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],FloatType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_func_decl_9(self):
        """Test function declaration: return type"""
        input = """ Function foo():string;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],StringType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_func_decl_10(self):
        """Test function declaration: return type"""
        input = """ Function foo():array [-1 .. -55] of string;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],ArrayType(-1,-55,StringType),[],[])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_func_decl_11(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType)],[])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_func_decl_12(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                            z: boolean;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),BoolType)],[])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_func_decl_13(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                            z: boolean;
                             a: array [1 .. -5] of integer;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),BoolType),VarDecl(Id(a),ArrayType(1,-5,IntType))],[])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_func_decl_14(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                            z: boolean;
                            a: array [1 .. -5] of integer;
                            b: array [1 .. -5] of real;
                        
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),BoolType),VarDecl(Id(a),ArrayType(1,-5,IntType)),VarDecl(Id(b),ArrayType(1,-5,FloatType))],[])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_expression_1(self):
        """Test expression:  andthen, orelse"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 anD then 1.2;
                            return "nm" or else true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(andthen,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(orelse,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_expression_2(self):
        """Test expression:  =, <>"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 = 1.2;
                            return "nm" > true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(=,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(>,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_expression_3(self):
        """Test expression:  <, <="""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 < 1.2;
                            return "nm" <= true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(<,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(<=,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test_expression_4(self):
        """Test expression:  >, >="""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 > 1.2;
                            return "nm" >= true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(>,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(>=,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_expression_5(self):
        """Test expression:  +, -"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 + 1.2;
                            return "nm" - true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(+,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(-,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,326))
        
    def test_expression_6(self):
        """Test expression:  or, /"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 or 1.2;
                            return "nm" / true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(or,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(/,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,327))
        
    def test_expression_7(self):
        """Test expression:  *, div"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 * 1.2;
                            return "nm" div true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(*,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(div,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,328))

    def test_expression_8(self):
        """Test expression:  mod, and"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 mod 1.2;
                            return "nm" and true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(mod,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(and,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,329))

    def test_expression_9(self):
        """Test expression:  unary: -, not"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - 1.2;
                            return not true;
                            return  -2;
                            return not"nm";
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,FloatLiteral(1.2)))),Return(Some(UnaryOp(not,BooleanLiteral(True)))),Return(Some(UnaryOp(-,IntLiteral(2)))),Return(Some(UnaryOp(not,StringLiteral(nm))))])])"
        self.assertTrue(TestAST.test(input,expect,330))

    def test_expression_10(self):
        """Test expression:  call function"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - foo();
                            return  - foo(x);

                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,CallExpr(Id(foo),[])))),Return(Some(UnaryOp(-,CallExpr(Id(foo),[Id(x)]))))])])"
        self.assertTrue(TestAST.test(input,expect,331))

    def test_expression_11(self):
        """Test expression:  call function"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - foo(x,y);
                            return  not foo(x,y,int(2,int1()));
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,CallExpr(Id(foo),[Id(x),Id(y)])))),Return(Some(UnaryOp(not,CallExpr(Id(foo),[Id(x),Id(y),CallExpr(Id(int),[IntLiteral(2),CallExpr(Id(int1),[])])]))))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_expression_12(self):
        """Test expression:  index expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - 1[a];
                            return  - "2"[3][5];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,ArrayCell(IntLiteral(1),Id(a))))),Return(Some(UnaryOp(-,ArrayCell(ArrayCell(StringLiteral(2),IntLiteral(3)),IntLiteral(5)))))])])"
        self.assertTrue(TestAST.test(input,expect,333))
        
    def test_expression_13(self):
        """Test expression:  index expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - ("ab"[tham])[123];
                            return  not true[false[23]];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,ArrayCell(ArrayCell(StringLiteral(ab),Id(tham)),IntLiteral(123))))),Return(Some(UnaryOp(not,ArrayCell(BooleanLiteral(True),ArrayCell(BooleanLiteral(False),IntLiteral(23))))))])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test_expression_14(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return  not true[false[23]] + ("ab"[tham])[123];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(+,UnaryOp(not,ArrayCell(BooleanLiteral(True),ArrayCell(BooleanLiteral(False),IntLiteral(23)))),ArrayCell(ArrayCell(StringLiteral(ab),Id(tham)),IntLiteral(123)))))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_expression_15(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return (1 - true[false[23]]) - ("ab"[tham])[123];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(-,BinaryOp(-,IntLiteral(1),ArrayCell(BooleanLiteral(True),ArrayCell(BooleanLiteral(False),IntLiteral(23)))),ArrayCell(ArrayCell(StringLiteral(ab),Id(tham)),IntLiteral(123)))))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_expression_16(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return -1 and then true[1] - ("ab"=8)[123] * 1 = 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(andthen,UnaryOp(-,IntLiteral(1)),BinaryOp(=,BinaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)),BinaryOp(*,ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123)),IntLiteral(1))),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,337))

    def test_expression_17(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return 1 >= false[23] + da(1[2],3) mod 1.3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(>=,IntLiteral(1),BinaryOp(+,ArrayCell(BooleanLiteral(False),IntLiteral(23)),BinaryOp(mod,CallExpr(Id(da),[ArrayCell(IntLiteral(1),IntLiteral(2)),IntLiteral(3)]),FloatLiteral(1.3))))))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test_expression_18(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return -1 and -true[1] or ("ab"=8)[123] or else 1 > 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(orelse,BinaryOp(or,BinaryOp(and,UnaryOp(-,IntLiteral(1)),UnaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)))),ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123))),BinaryOp(>,IntLiteral(1),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,339))

    def test_expression_19(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return 1 - - true[1] or not ("ab"=8)[123] and then 1 = 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(andthen,BinaryOp(or,BinaryOp(-,IntLiteral(1),UnaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)))),UnaryOp(not,ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123)))),BinaryOp(=,IntLiteral(1),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test_expression_20(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return - a[9] - - true[1] + foo(1,2) or not ("ab"=8)[123] ;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(or,BinaryOp(+,BinaryOp(-,UnaryOp(-,ArrayCell(Id(a),IntLiteral(9))),UnaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)))),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])),UnaryOp(not,ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123))))))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test_statement_1(self):
        """Test statement:  continue"""
        input = """ Function foo():integer;                      
                        Begin
                            continue;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Continue])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test_statement_2(self):
        """Test statement:  Break"""
        input = """ Function foo():integer;                      
                        Begin
                            Break;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Break])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test_statement_3(self):
        """Test statement:  For statement"""
        input = """ Function foo():integer;                      
                        Begin
                            for i := 1 to 2 do break; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)IntLiteral(1),IntLiteral(2),True,[Break])])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test_statement_4(self):
        """Test statement:  For statement"""
        input = """ Function foo():integer;                      
                        Begin
                            for i := a[1] to foo(2) do break; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)ArrayCell(Id(a),IntLiteral(1)),CallExpr(Id(foo),[IntLiteral(2)]),True,[Break])])])"
        self.assertTrue(TestAST.test(input,expect,345))


    def test_statement_5(self):
        """Test statement:  For statement"""
        input = """ Function foo():integer;                      
                        Begin
                            for i := kk() downto 2[4] do break; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)CallExpr(Id(kk),[]),ArrayCell(IntLiteral(2),IntLiteral(4)),False,[Break])])])"
        self.assertTrue(TestAST.test(input,expect,346))


    def test_statement_6(self):
        """Test statement:  For statement"""
        input = """ Function foo():integer;                      
                        Begin
                            for i := kk() downto 2[4] do 
                                Begin
                                    continue;
                                    break;
                                    a := b := n := 5 ;
                                    begin end
                                end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)CallExpr(Id(kk),[]),ArrayCell(IntLiteral(2),IntLiteral(4)),False,[Continue,Break,AssignStmt(Id(n),IntLiteral(5)),AssignStmt(Id(b),Id(n)),AssignStmt(Id(a),Id(b))])])])"
        self.assertTrue(TestAST.test(input,expect,347))          
    def test_statement_7(self):
        """Test statement:  While statement"""
        input = """ Function foo():integer;                      
                        Begin
                            While i = 1 do break; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[While(BinaryOp(=,Id(i),IntLiteral(1)),[Break])])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test_statement_8(self):
        """Test statement:  While statement"""
        input = """ Function foo():integer;                      
                        Begin
                            While foo() and then a [1] do continue; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[While(BinaryOp(andthen,CallExpr(Id(foo),[]),ArrayCell(Id(a),IntLiteral(1))),[Continue])])])"
        self.assertTrue(TestAST.test(input,expect,349))

    def test_statement_9(self):
        """Test statement:  While statement"""
        input = """ Function foo():integer;                      
                        Begin
                            While foo(a,r) do 
                            begin 
                                t := n := 4;
                                begin
                                    adf := 0;
                                end
                            end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[While(CallExpr(Id(foo),[Id(a),Id(r)]),[AssignStmt(Id(n),IntLiteral(4)),AssignStmt(Id(t),Id(n)),AssignStmt(Id(adf),IntLiteral(0))])])])"
        self.assertTrue(TestAST.test(input,expect,350))

    def test_statement_10(self):
        """Test statement:  While statement"""
        input = """ Function foo():integer;                      
                        Begin
                            While i = 1 do 
                            begin
                            end 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[While(BinaryOp(=,Id(i),IntLiteral(1)),[])])])"
        self.assertTrue(TestAST.test(input,expect,351))

    def test_statement_11(self):
        """Test statement:  While statement"""
        input = """ Function foo():integer;                      
                        Begin
                            While i = 1 do 
                            begin
                                if a <> 1 then begin end
                            end
                     
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[While(BinaryOp(=,Id(i),IntLiteral(1)),[If(BinaryOp(<>,Id(a),IntLiteral(1)),[],[])])])])"
        self.assertTrue(TestAST.test(input,expect,352))

    def test_statement_12(self):
        """Test statement:  If statement"""
        input = """ Function foo():integer;                      
                        Begin
                            If (1) then return 2;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(IntLiteral(1),[Return(Some(IntLiteral(2)))],[])])])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test_statement_13(self):
        """Test statement:  If statement"""
        input = """procedure proc();
		        begin
			        if a > 3 then
				        if a < 7 then 
				            b := b + 2;
				        else 
					        b := "huhuhu";
		        end"""
        expect = "Program([FuncDecl(Id(proc),[],VoidType(),[],[If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),StringLiteral(huhuhu))])],[])])])"
        self.assertTrue(TestAST.test(input,expect,354))
        
    def test_statement_14(self):
        """Test statement:  If statement"""
        input = """procedure proc();
		        begin
			        if a > 3 then
				        if a < 7 then 
				            b := b + 2;
				        else 
					        b := b + 1;
                    else
                        a:= b := 6;
		        end"""
        expect = "Program([FuncDecl(Id(proc),[],VoidType(),[],[If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))])],[AssignStmt(Id(b),IntLiteral(6)),AssignStmt(Id(a),Id(b))])])])"
        self.assertTrue(TestAST.test(input,expect,355))


    def test_statement_15(self):
        """Test statement:  If statement"""
        input = """ Function foo():integer;                      
		        begin
			        if a <> 3 then
				        if a < 7 then 
                            begin
				                b := b + 2;
                                if a=1 then b:= b + 1;
                            end
				        else 
					        b := b + 1;
                    else
                        a:= b := 6;
                END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(<>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2))),If(BinaryOp(=,Id(a),IntLiteral(1)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))],[])],[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))])],[AssignStmt(Id(b),IntLiteral(6)),AssignStmt(Id(a),Id(b))])])])"
        self.assertTrue(TestAST.test(input,expect,356))

    def test_statement_16(self):
        """Test statement:  If statement"""
        input = """procedure proc();
		        begin
			        if a > 3 then
                        begin
				             if a < 7 then 
				                b := b + 2;
				            else 
					            b := "toi ten";
                            if a <> 5 then
                                t := j:= k;
                            else
                                return false;
                        end
		        end"""
        expect = "Program([FuncDecl(Id(proc),[],VoidType(),[],[If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),StringLiteral(toi ten))]),If(BinaryOp(<>,Id(a),IntLiteral(5)),[AssignStmt(Id(j),Id(k)),AssignStmt(Id(t),Id(j))],[Return(Some(BooleanLiteral(False)))])],[])])])"
        self.assertTrue(TestAST.test(input,expect,357))
        
    def test_statement_17(self):
        """Test statement:  If statement"""
        input = """procedure proc();
		        begin
			        if a > 3 then
				        if a < 7 then 
				            b := b + 2;
				        else 
					        b := "huhuhu";
                    else
                        begin 
                            return true;
                        end
		        end"""
        expect = "Program([FuncDecl(Id(proc),[],VoidType(),[],[If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),StringLiteral(huhuhu))])],[Return(Some(BooleanLiteral(True)))])])])"
        self.assertTrue(TestAST.test(input,expect,358))

    def test_statement_18(self):
        """Test statement:  With statement"""
        input = """ Function foo():integer;                      
                        Begin
                            with a:integer;  do break;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType)],[Break])])])"
        self.assertTrue(TestAST.test(input,expect,359))

    def test_statement_19(self):
        """Test statement:  With statement"""
        input = """ Function foo():integer;                      
                        Begin
                            with a:integer; b: boolean; do break;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),BoolType)],[Break])])])"
        self.assertTrue(TestAST.test(input,expect,360))

    def test_statement_20(self):
        """Test statement:  With statement"""
        input = """ Function foo():integer;                      
                        Begin
                            with a:integer; b: boolean; c: array [1 .. -6] of string; do 
                                begin
                                    return true;
                                    continue;
                                    break;
                                end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),BoolType),VarDecl(Id(c),ArrayType(1,-6,StringType))],[Return(Some(BooleanLiteral(True))),Continue,Break])])])"
        self.assertTrue(TestAST.test(input,expect,361))

    def test_statement_21(self):
        """Test statement:  With statement"""
        input = """ Function foo():integer;                      
                        Begin
                            with a:integer; b: boolean; do 
                                begin
                                    return true;
                                    continue;
                                    break;
                                    if a <> 1 then
                                        a := 6;
                                    else
                                        begin
                                            if b = true then return true;
                                            a:=5;
                                        end
                                end                                
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),BoolType)],[Return(Some(BooleanLiteral(True))),Continue,Break,If(BinaryOp(<>,Id(a),IntLiteral(1)),[AssignStmt(Id(a),IntLiteral(6))],[If(BinaryOp(=,Id(b),BooleanLiteral(True)),[Return(Some(BooleanLiteral(True)))],[]),AssignStmt(Id(a),IntLiteral(5))])])])])"
        self.assertTrue(TestAST.test(input,expect,362))

    def test_statement_22(self):
        """Test statement:  Call statement"""
        input = """ Function foo():integer;                      
                        Begin
                            foo(x,y,int(2,int1()));
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(foo),[Id(x),Id(y),CallExpr(Id(int),[IntLiteral(2),CallExpr(Id(int1),[])])])])])"
        self.assertTrue(TestAST.test(input,expect,363))

    def test_statement_23(self):
        """Test statement:  Call statement"""
        input = """ Function foo():integer;                      
                        Begin
                            foo(x,y,int(2,int1()),a[2][6]);
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(foo),[Id(x),Id(y),CallExpr(Id(int),[IntLiteral(2),CallExpr(Id(int1),[])]),ArrayCell(ArrayCell(Id(a),IntLiteral(2)),IntLiteral(6))])])])"
        self.assertTrue(TestAST.test(input,expect,364))

    def test_statement_24(self):
        """Test statement:  Call statement"""
        input = """ Function foo():integer;                      
                        Begin
                            foo();
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(foo),[])])])"
        self.assertTrue(TestAST.test(input,expect,365))

    def test_statement_25(self):
        """Test statement:  Call statement"""
        input = """ Function foo():integer;                      
                        Begin
                            foo(fora(1,foraaa(2,foraaaa())));
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(foo),[CallExpr(Id(fora),[IntLiteral(1),CallExpr(Id(foraaa),[IntLiteral(2),CallExpr(Id(foraaaa),[])])])])])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test_statement_26(self):
        """Test statement:  Call statement"""
        input = """ Function foo():integer;                      
                        Begin
                            myFunc(a[4],y,int(2,int1()));
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(myFunc),[ArrayCell(Id(a),IntLiteral(4)),Id(y),CallExpr(Id(int),[IntLiteral(2),CallExpr(Id(int1),[])])])])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test_statement_27(self):
        """Test statement:  Assignment statement"""
        input = """ Function foo():integer;                      
                        Begin
                            a := de := d := 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(d),IntLiteral(3)),AssignStmt(Id(de),Id(d)),AssignStmt(Id(a),Id(de))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test_statement_28(self):
        """Test statement:  Assignment statement"""
        input = """ Function foo():integer;                      
                        Begin
                            a := b[10] := foo()[3] := x := (23+3) and then 6 or else 7;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),BinaryOp(orelse,BinaryOp(andthen,BinaryOp(+,IntLiteral(23),IntLiteral(3)),IntLiteral(6)),IntLiteral(7))),AssignStmt(ArrayCell(CallExpr(Id(foo),[]),IntLiteral(3)),Id(x)),AssignStmt(ArrayCell(Id(b),IntLiteral(10)),ArrayCell(CallExpr(Id(foo),[]),IntLiteral(3))),AssignStmt(Id(a),ArrayCell(Id(b),IntLiteral(10)))])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test_statement_29(self):
        """Test statement:  Assignment statement"""
        input = """ Function foo():integer;                      
                        Begin
                            forr()[78] := 56 and 0 mod 343 + 34 / 3243 * 5;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(ArrayCell(CallExpr(Id(forr),[]),IntLiteral(78)),BinaryOp(+,BinaryOp(mod,BinaryOp(and,IntLiteral(56),IntLiteral(0)),IntLiteral(343)),BinaryOp(*,BinaryOp(/,IntLiteral(34),IntLiteral(3243)),IntLiteral(5))))])])"
        self.assertTrue(TestAST.test(input,expect,370))

    def test_statement_30(self):
        """Test statement:  Assignment statement"""
        input = """ Function foo():integer;                      
                        Begin
                            a := de[123]["asdas"] := d := 6*5 + 76 div 6 mod  1.4 and 6.7;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(d),BinaryOp(+,BinaryOp(*,IntLiteral(6),IntLiteral(5)),BinaryOp(and,BinaryOp(mod,BinaryOp(div,IntLiteral(76),IntLiteral(6)),FloatLiteral(1.4)),FloatLiteral(6.7)))),AssignStmt(ArrayCell(ArrayCell(Id(de),IntLiteral(123)),StringLiteral(asdas)),Id(d)),AssignStmt(Id(a),ArrayCell(ArrayCell(Id(de),IntLiteral(123)),StringLiteral(asdas)))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test_complex_program_1(self):
        """Test complex program"""
        input = """ VAR X, Y1, Y2,  First, Last, Incr, Factor: REAL;
                        Q1, Q2, Step:  INTEGER;
                    PROCEDURE main();
                        BEGIN
                            { Input plot  parameters }
                            Write("Enter  first value: ");
                            Read(First);
                            Write("Enter  last value: ");
                            Read(Last);
                            Write("Enter  scale factor: ");
                            Read(Factor);
                            Write("Enter an  increment: ");
                            Read(Incr);
                            WriteLn();
                            { Draw  horizontal Y axis }
                            FOR Step := 0 TO  MaxY DO
                            IF (Step MOD 5 =  0) THEN
                            Write("+");
                            ELSE
                            Write("-");
                            Write(" Y ");
                            WriteLn();
                            { Do the Plot on  its side }
                            X := First;
                            WHILE X <=  Last DO BEGIN
                                Y1 :=  SIN(3.14159 * X / 180.0);
                                Y1 := Factor *  Y1;
                                Q1 := ROUND(Y1);
                                Y2 := 0.005 * X;
                                Y2 := Factor *  Y2;
                                Q2 := ROUND(Y2);
                            end
                        end

                """
        expect = "Program([VarDecl(Id(X),FloatType),VarDecl(Id(Y1),FloatType),VarDecl(Id(Y2),FloatType),VarDecl(Id(First),FloatType),VarDecl(Id(Last),FloatType),VarDecl(Id(Incr),FloatType),VarDecl(Id(Factor),FloatType),VarDecl(Id(Q1),IntType),VarDecl(Id(Q2),IntType),VarDecl(Id(Step),IntType),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(Write),[StringLiteral(Enter  first value: )]),CallStmt(Id(Read),[Id(First)]),CallStmt(Id(Write),[StringLiteral(Enter  last value: )]),CallStmt(Id(Read),[Id(Last)]),CallStmt(Id(Write),[StringLiteral(Enter  scale factor: )]),CallStmt(Id(Read),[Id(Factor)]),CallStmt(Id(Write),[StringLiteral(Enter an  increment: )]),CallStmt(Id(Read),[Id(Incr)]),CallStmt(Id(WriteLn),[]),For(Id(Step)IntLiteral(0),Id(MaxY),True,[If(BinaryOp(=,BinaryOp(MOD,Id(Step),IntLiteral(5)),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(+)])],[CallStmt(Id(Write),[StringLiteral(-)])])]),CallStmt(Id(Write),[StringLiteral( Y )]),CallStmt(Id(WriteLn),[]),AssignStmt(Id(X),Id(First)),While(BinaryOp(<=,Id(X),Id(Last)),[AssignStmt(Id(Y1),CallExpr(Id(SIN),[BinaryOp(/,BinaryOp(*,FloatLiteral(3.14159),Id(X)),FloatLiteral(180.0))])),AssignStmt(Id(Y1),BinaryOp(*,Id(Factor),Id(Y1))),AssignStmt(Id(Q1),CallExpr(Id(ROUND),[Id(Y1)])),AssignStmt(Id(Y2),BinaryOp(*,FloatLiteral(0.005),Id(X))),AssignStmt(Id(Y2),BinaryOp(*,Id(Factor),Id(Y2))),AssignStmt(Id(Q2),CallExpr(Id(ROUND),[Id(Y2)]))])])])"
        self.assertTrue(TestAST.test(input,expect,372))

    def test_complex_program_2(self):
        """Test complex program"""
        input = """                      
                    Var
                        f : String; { file var of type byte }
                        sz : Integer;  { var for the size }

                    Procedure Main();
                    Begin
                        Assign(f,"C:\\\\anyfile.txt");
                        {$I-} Reset(f); {$I+}
                        If (IOResult <> 0) Then
                        Begin     { file found? }
                            Writeln("File not found.. exiting");
                            Readln();
                        End Else
                        Begin
                                { Return the file size in Kilobytes }
                            sz := Round(FileSize(f)/1024);
                            Writeln("Size of the file in Kilobytes: ",sz," Kb");
                            Readln();
                            Close(f); 
                        End
                    End
                """
        expect = "Program([VarDecl(Id(f),StringType),VarDecl(Id(sz),IntType),FuncDecl(Id(Main),[],VoidType(),[],[CallStmt(Id(Assign),[Id(f),StringLiteral(C:\\\\anyfile.txt)]),CallStmt(Id(Reset),[Id(f)]),If(BinaryOp(<>,Id(IOResult),IntLiteral(0)),[CallStmt(Id(Writeln),[StringLiteral(File not found.. exiting)]),CallStmt(Id(Readln),[])],[AssignStmt(Id(sz),CallExpr(Id(Round),[BinaryOp(/,CallExpr(Id(FileSize),[Id(f)]),IntLiteral(1024))])),CallStmt(Id(Writeln),[StringLiteral(Size of the file in Kilobytes: ),Id(sz),StringLiteral( Kb)]),CallStmt(Id(Readln),[]),CallStmt(Id(Close),[Id(f)])])])])"
        self.assertTrue(TestAST.test(input,expect,373))

    def test_complex_program_3(self):
        """Test complex program"""
        input = """                      
                    Var Sel: String;
                        N1,N2, Total : Real;
                        YN : String;  { this is a character variable type, which holds single characters ONLY }
                    procedure main();
                    Begin
                        Total := 0;  { always initialise integer/real variables }
                        GotoXy(4,3);
                        Writeln("1.Addition");
                        GotoXy(4,4);
                        Writeln("2.Subtraction");
                        GotoXy(4,5);
                        Writeln("3.Exit");
                        GotoXy(6,8);
                        Write("Select: ");
                        Sel := Readkey();

                        If Sel = "1" {condition} Then 
                        Begin  {more than one statement}
                            ClrScr();
                            Write("Input No.1:");
                            Readln(N1);
                            Write("Input No.2:");
                            Readln(N2);
                            Total := N1 + N2;
                            Writeln("Addition: ",N1," + ",N2," = ",Total);
                            Write("Press any key to continue...");
                            Readkey();
                        end { Closing the if statement }



                        If Sel = "3" Then 
                        Begin
                            ClrScr();
                            Write("Are you sure?(Y/N)");
                            YN := Readkey();
                            If YN = "y" Then Halt(); { 1 instruction, so no need of Begin..End }
                            If YN = "n" Then Goto1(); { the goto statement is not recommended for frequent use }
                        End
                    End 
                """
        expect = "Program([VarDecl(Id(Sel),StringType),VarDecl(Id(N1),FloatType),VarDecl(Id(N2),FloatType),VarDecl(Id(Total),FloatType),VarDecl(Id(YN),StringType),FuncDecl(Id(main),[],VoidType(),[],[AssignStmt(Id(Total),IntLiteral(0)),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(3)]),CallStmt(Id(Writeln),[StringLiteral(1.Addition)]),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(4)]),CallStmt(Id(Writeln),[StringLiteral(2.Subtraction)]),CallStmt(Id(GotoXy),[IntLiteral(4),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(3.Exit)]),CallStmt(Id(GotoXy),[IntLiteral(6),IntLiteral(8)]),CallStmt(Id(Write),[StringLiteral(Select: )]),AssignStmt(Id(Sel),CallExpr(Id(Readkey),[])),If(BinaryOp(=,Id(Sel),StringLiteral(1)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(+,Id(N1),Id(N2))),CallStmt(Id(Writeln),[StringLiteral(Addition: ),Id(N1),StringLiteral( + ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[]),If(BinaryOp(=,Id(Sel),StringLiteral(3)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Are you sure?(Y/N))]),AssignStmt(Id(YN),CallExpr(Id(Readkey),[])),If(BinaryOp(=,Id(YN),StringLiteral(y)),[CallStmt(Id(Halt),[])],[]),If(BinaryOp(=,Id(YN),StringLiteral(n)),[CallStmt(Id(Goto1),[])],[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,374))

    def test_complex_program_4(self):
        """Test complex program"""
        input = """                      
                    var a, b, c: real;

                    var x, y, z: Boolean;
                        g, h, y: Integer;

                    function nty(): Real;
                    var x, y, z: Integer;
                    begin
                        readLine();
                        // This is readLine()

                        fs := readStdin();
                        
                        with i: integer; do begin
                            for i := 4 downto -5 do h := 6;
                            if i > 6 then return 0;
                        end

                        return 1;
                    end

                    var q, w : integer;
                """
        expect = "Program([VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType),VarDecl(Id(z),BoolType),VarDecl(Id(g),IntType),VarDecl(Id(h),IntType),VarDecl(Id(y),IntType),FuncDecl(Id(nty),[],FloatType,[VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType)],[CallStmt(Id(readLine),[]),AssignStmt(Id(fs),CallExpr(Id(readStdin),[])),With([VarDecl(Id(i),IntType)],[For(Id(i)IntLiteral(4),UnaryOp(-,IntLiteral(5)),False,[AssignStmt(Id(h),IntLiteral(6))]),If(BinaryOp(>,Id(i),IntLiteral(6)),[Return(Some(IntLiteral(0)))],[])]),Return(Some(IntLiteral(1)))]),VarDecl(Id(q),IntType),VarDecl(Id(w),IntType)])"
        self.assertTrue(TestAST.test(input,expect,375))

    def test_complex_program_5(self):
        """Test complex program"""
        input = """                       
                    var x, y, z: Boolean;
                        g, h, y: Integer;

                    function nty(): Real;
                    Var       
                        Num1, Num2, Sum : Integer;

                    Begin {no semicolon}
                        Write("Input number 1:"); 
                        Readln("Num1");
                        Writeln("Input number 2:");
                        Readln(Num2);
                        Sum := Num1 + Num2; {addition} 
                        Writeln(Sum);
                        Readln(Sum);

                    End
                """
        expect = "Program([VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType),VarDecl(Id(z),BoolType),VarDecl(Id(g),IntType),VarDecl(Id(h),IntType),VarDecl(Id(y),IntType),FuncDecl(Id(nty),[],FloatType,[VarDecl(Id(Num1),IntType),VarDecl(Id(Num2),IntType),VarDecl(Id(Sum),IntType)],[CallStmt(Id(Write),[StringLiteral(Input number 1:)]),CallStmt(Id(Readln),[StringLiteral(Num1)]),CallStmt(Id(Writeln),[StringLiteral(Input number 2:)]),CallStmt(Id(Readln),[Id(Num2)]),AssignStmt(Id(Sum),BinaryOp(+,Id(Num1),Id(Num2))),CallStmt(Id(Writeln),[Id(Sum)]),CallStmt(Id(Readln),[Id(Sum)])])])"
        self.assertTrue(TestAST.test(input,expect,376))

    def test_complex_program_6(self):
        """Test complex program"""
        input = """                      
                    procedure foo();
                    begin
                        if True then begin
                        end else begin end
                    end

                    function hgt(): Boolean;
                    var a: string;
                    begin 
                        (*
                            =======================================
                            Comment here
                            =======================================
                        *)
                        If Sel = "2" Then { note that here we do not use an assignment statement } 
                        Begin 
                            ClrScr();
                            Write("Input No.1:");
                            Readln(N1);
                            Write("Input No.2:");
                            Readln(N2);
                            Total := N1 - N2;
                            Write("Subtraction: ");
                            Write(N1," - ",N2," = ",Total);
                            Write("Press any key to continue...");
                            Readkey();
                        end  { Closing the if statement }                        
                    end
                """
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[If(BooleanLiteral(True),[],[])]),FuncDecl(Id(hgt),[],BoolType,[VarDecl(Id(a),StringType)],[If(BinaryOp(=,Id(Sel),StringLiteral(2)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(-,Id(N1),Id(N2))),CallStmt(Id(Write),[StringLiteral(Subtraction: )]),CallStmt(Id(Write),[Id(N1),StringLiteral( - ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,377))

    def test_complex_program_7(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                Begin
                        FOR Step := 0 TO  MaxY DO
                            IF Step = 0 THEN
                                Write( "|");
                            ELSE
                                IF Step = Q1  THEN
                                    Write( "*");
                                ELSE
                                    IF Step = Q2  THEN
                                        Write( "+");
                                    ELSE
                                        Write( " ");
                                    WriteLn();
                                    X := X + Incr;
               END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(Step)IntLiteral(0),Id(MaxY),True,[If(BinaryOp(=,Id(Step),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(|)])],[If(BinaryOp(=,Id(Step),Id(Q1)),[CallStmt(Id(Write),[StringLiteral(*)])],[If(BinaryOp(=,Id(Step),Id(Q2)),[CallStmt(Id(Write),[StringLiteral(+)])],[CallStmt(Id(Write),[StringLiteral( )])])])])]),CallStmt(Id(WriteLn),[]),AssignStmt(Id(X),BinaryOp(+,Id(X),Id(Incr)))])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test_complex_program_8(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            if n=1 then
                                fibonacci := 0;
                            
                            else if n=2 then
                                fibonacci := 1;
                            
                            else
                                fibonacci := fibonacci(n-1) + fibonacci(n-2);
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(=,Id(n),IntLiteral(1)),[AssignStmt(Id(fibonacci),IntLiteral(0))],[If(BinaryOp(=,Id(n),IntLiteral(2)),[AssignStmt(Id(fibonacci),IntLiteral(1))],[AssignStmt(Id(fibonacci),BinaryOp(+,CallExpr(Id(fibonacci),[BinaryOp(-,Id(n),IntLiteral(1))]),CallExpr(Id(fibonacci),[BinaryOp(-,Id(n),IntLiteral(2))])))])])])])"
        self.assertTrue(TestAST.test(input,expect,379))

    def test_complex_program_10(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            a := 100;
                            b := 200;
                            writeln("Before swap, value of a : ", a );
                            writeln("Before swap, value of b : ", b );
                            
                            (* calling the procedure swap  by value   *)
                            swap(a, b);
                            writeln("After swap, value of a : ", a );
                            writeln("After swap, value of b : ", b );
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),CallStmt(Id(writeln),[StringLiteral(Before swap, value of a : ),Id(a)]),CallStmt(Id(writeln),[StringLiteral(Before swap, value of b : ),Id(b)]),CallStmt(Id(swap),[Id(a),Id(b)]),CallStmt(Id(writeln),[StringLiteral(After swap, value of a : ),Id(a)]),CallStmt(Id(writeln),[StringLiteral(After swap, value of b : ),Id(b)])])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test_complex_program_11(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            (* local variables *)
                            x := 10;
                            y := 20;
                            z := x + y;
                            
                            (*global variables *)
                            a := 30;
                            b:= 40;
                            c:= a + b;
                           END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(x),IntLiteral(10)),AssignStmt(Id(y),IntLiteral(20)),AssignStmt(Id(z),BinaryOp(+,Id(x),Id(y))),AssignStmt(Id(a),IntLiteral(30)),AssignStmt(Id(b),IntLiteral(40)),AssignStmt(Id(c),BinaryOp(+,Id(a),Id(b)))])])"
        self.assertTrue(TestAST.test(input,expect,381))

    def test_complex_program_12(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            writeln("Winthin the procedure display");
                            writeln(" Displaying the global variables a, b, and c");
                            
                            writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
                            writeln("Displaying the local variables x, y, and z");
                            
                            writeln("value of x = ", x , " y =  ",  y, " and z = ", z);
                           END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(writeln),[StringLiteral(Winthin the procedure display)]),CallStmt(Id(writeln),[StringLiteral( Displaying the global variables a, b, and c)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(writeln),[StringLiteral(Displaying the local variables x, y, and z)]),CallStmt(Id(writeln),[StringLiteral(value of x = ),Id(x),StringLiteral( y =  ),Id(y),StringLiteral( and z = ),Id(z)])])])"
        self.assertTrue(TestAST.test(input,expect,382))

    def test_complex_program_13(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            a:= 100;
                            b:= 200;
                            c:= 300;
                            
                            writeln("Winthin the program exlocal");
                            writeln("value of a = ", a , " b =  ",  b, " and c = ", c);   
                            
                            display();               
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(c),IntLiteral(300)),CallStmt(Id(writeln),[StringLiteral(Winthin the program exlocal)]),CallStmt(Id(writeln),[StringLiteral(value of a = ),Id(a),StringLiteral( b =  ),Id(b),StringLiteral( and c = ),Id(c)]),CallStmt(Id(display),[])])])"
        self.assertTrue(TestAST.test(input,expect,383))

    def test_complex_program_14(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            (* copy str1 into str3 *)
                            str3 := str1;
                            writeln("appendstr( str3, str1) :  ", str3 );
                            
                            (* concatenates str1 and str2 *)
                            appendstr( str1, str2);
                            writeln( "appendstr( str1, str2) " , str1 );
                            str4 := str1 + str2;
                            writeln("Now str4 is: ", str4);
                            
                            (* total lenghth of str4 after concatenation  *)
                            len := byte(str4[0]);
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(str3),Id(str1)),CallStmt(Id(writeln),[StringLiteral(appendstr( str3, str1) :  ),Id(str3)]),CallStmt(Id(appendstr),[Id(str1),Id(str2)]),CallStmt(Id(writeln),[StringLiteral(appendstr( str1, str2) ),Id(str1)]),AssignStmt(Id(str4),BinaryOp(+,Id(str1),Id(str2))),CallStmt(Id(writeln),[StringLiteral(Now str4 is: ),Id(str4)]),AssignStmt(Id(len),CallExpr(Id(byte),[ArrayCell(Id(str4),IntLiteral(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,384))

    def test_complex_program_15(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            (* initialize elements of array n to 0 *)        
                            for i := 1 to 10 do
                                n[ i ] := i + 100;   (* set element at location i to i + 100 *)
                                (* output each array element"s value *)
                            
                            for j:= 1 to 10 do
                                writeln("Element[", j, "] = ", n[j] );
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)IntLiteral(1),IntLiteral(10),True,[AssignStmt(ArrayCell(Id(n),Id(i)),BinaryOp(+,Id(i),IntLiteral(100)))]),For(Id(j)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(writeln),[StringLiteral(Element[),Id(j),StringLiteral(] = ),ArrayCell(Id(n),Id(j))])])])])"
        self.assertTrue(TestAST.test(input,expect,385))

    def test_complex_program_16(self):
        """Test complex program"""
        input = """ procedure foo();                      
                        Begin
                            begin
                            if x < y then
                                m := x;
                            else
                                m := y;                         
                            if z <m then{ end of procedure findMin }  
                                m := z;
                            end 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],VoidType(),[],[If(BinaryOp(<,Id(x),Id(y)),[AssignStmt(Id(m),Id(x))],[AssignStmt(Id(m),Id(y))]),If(BinaryOp(<,Id(z),Id(m)),[AssignStmt(Id(m),Id(z))],[])])])"
        self.assertTrue(TestAST.test(input,expect,386))

    def test_complex_program_17(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            if x=0 then
                                fact := 1;
                            else
                                fact := x * fact(x-1); (* recursive call *)
                            begin
                            writeln(" Enter a number: ");
                            readln(num);
                            f := fact(num);
                            end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(=,Id(x),IntLiteral(0)),[AssignStmt(Id(fact),IntLiteral(1))],[AssignStmt(Id(fact),BinaryOp(*,Id(x),CallExpr(Id(fact),[BinaryOp(-,Id(x),IntLiteral(1))])))]),CallStmt(Id(writeln),[StringLiteral( Enter a number: )]),CallStmt(Id(readln),[Id(num)]),AssignStmt(Id(f),CallExpr(Id(fact),[Id(num)]))])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test_complex_program_18(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            if (num1 > num2) then
                                result := num1;
                            
                            else
                                result := num2;
                            max := result;
                            begin
                            a := 100;
                            b := 200;
                            (* calling a function to get max value *)
                            ret := max(a, b);
                            
                            writeln( "Max value is : ", ret );
                            end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(>,Id(num1),Id(num2)),[AssignStmt(Id(result),Id(num1))],[AssignStmt(Id(result),Id(num2))]),AssignStmt(Id(max),Id(result)),AssignStmt(Id(a),IntLiteral(100)),AssignStmt(Id(b),IntLiteral(200)),AssignStmt(Id(ret),CallExpr(Id(max),[Id(a),Id(b)])),CallStmt(Id(writeln),[StringLiteral(Max value is : ),Id(ret)])])])"
        self.assertTrue(TestAST.test(input,expect,388))

    def test_complex_program_19(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            For Counter := 1 to 5 do 
                            Begin      
                                gotoxy(25, 5 + Counter);
                                Writeln("I");
                            End

                            For Counter := 5 Downto 1 do
                            Begin  {an example of 'downto' instead of 'to', note the 'gotoxy(_,_)'}
                                gotoxy(32, 11 - Counter);
                            End

                            For Counter := 1 to 6 do
                            Begin
                                gotoxy(25 + Counter, 11);
                                Writeln("-");
                            End

                            For Counter := 6 Downto 1 do
                            Begin
                                gotoxy(32 - Counter, 5);
                                Writeln("-");
                            End
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(Counter)IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(gotoxy),[IntLiteral(25),BinaryOp(+,IntLiteral(5),Id(Counter))]),CallStmt(Id(Writeln),[StringLiteral(I)])]),For(Id(Counter)IntLiteral(5),IntLiteral(1),False,[CallStmt(Id(gotoxy),[IntLiteral(32),BinaryOp(-,IntLiteral(11),Id(Counter))])]),For(Id(Counter)IntLiteral(1),IntLiteral(6),True,[CallStmt(Id(gotoxy),[BinaryOp(+,IntLiteral(25),Id(Counter)),IntLiteral(11)]),CallStmt(Id(Writeln),[StringLiteral(-)])]),For(Id(Counter)IntLiteral(6),IntLiteral(1),False,[CallStmt(Id(gotoxy),[BinaryOp(-,IntLiteral(32),Id(Counter)),IntLiteral(5)]),CallStmt(Id(Writeln),[StringLiteral(-)])])])])"
        self.assertTrue(TestAST.test(input,expect,389))

    def test_complex_program_20(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            Writeln("Press  to exit...");
                            Ch := Readkey;
                            While Ch <> "q" do 
                            Begin
                                Writeln("Please press  to exit");
                                Ch := Readkey;
                            End 
                       END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(Writeln),[StringLiteral(Press  to exit...)]),AssignStmt(Id(Ch),Id(Readkey)),While(BinaryOp(<>,Id(Ch),StringLiteral(q)),[CallStmt(Id(Writeln),[StringLiteral(Please press  to exit)]),AssignStmt(Id(Ch),Id(Readkey))])])])"
        self.assertTrue(TestAST.test(input,expect,390))

    def test_complex_program_21(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            textcolor(green);

                            GotoXy(10,5);
                            For Counter := 1 to 10 do
                            Begin 
                                Write(chr(196));
                            End

                            GotoXy(10,6);
                            For Counter := 1 to 10 do
                            Begin 
                                Write(chr(196)); 
                            End

                            GotoXy(10,7);
                            For Counter := 1 to 10 do
                            Begin 
                                Write(chr(196)); 
                            End

                            GotoXy(10,10);
                            For Counter := 1 to 10 do
                            Begin 
                                Write(chr(196)); 
                            End
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(textcolor),[Id(green)]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(5)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(6)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(7)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(10)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])])])])"
        self.assertTrue(TestAST.test(input,expect,391))

    def test_complex_program_22(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            Begin
                                textcolor(green);
                                For Counter := 1 to 10 do
                                Begin 
                                    Write(chr(196)); 
                                End 
                            End

                            Begin
                                GotoXy(10,5);
                                DrawLine();
                                GotoXy(10,6);
                                DrawLine();
                                GotoXy(10,7);
                                DrawLine();
                                GotoXy(10,10);
                                DrawLine();
                                Readkey();
                            End
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(textcolor),[Id(green)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(GotoXy),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id(DrawLine),[]),CallStmt(Id(Readkey),[])])])"
        self.assertTrue(TestAST.test(input,expect,392))

    def test_complex_program_23(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            
                                GotoXy(X,Y); {here I use the arguments of X and Y}
                                textcolor(green);
                                For Counter := 1 to 10 do
                                    Write(chr(196));
                            
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(GotoXy),[Id(X),Id(Y)]),CallStmt(Id(textcolor),[Id(green)]),For(Id(Counter)IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(Write),[CallExpr(Id(chr),[IntLiteral(196)])])])])])"
        self.assertTrue(TestAST.test(input,expect,393))

    def test_complex_program_24(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            InfoCor := True;
                            ClrScr();
                            TextBackground(cyan);
                            TextColor(green);
                            Write("A list of colours is being displayed...");
                            begin
                                textcolor(i);
                                Writeln(i,": This is Colour No",i);
                            End
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(InfoCor),BooleanLiteral(True)),CallStmt(Id(ClrScr),[]),CallStmt(Id(TextBackground),[Id(cyan)]),CallStmt(Id(TextColor),[Id(green)]),CallStmt(Id(Write),[StringLiteral(A list of colours is being displayed...)]),CallStmt(Id(textcolor),[Id(i)]),CallStmt(Id(Writeln),[Id(i),StringLiteral(: This is Colour No),Id(i)])])])"
        self.assertTrue(TestAST.test(input,expect,394))

    def test_complex_program_25(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            Write("Enter your name: ");
                            ReadLn(name);
                        
                            if name = "Fred" then
                            begin
                                SayHello(name);
                            end
                            else
                            begin
                                WriteLn("I dont know you...");
			            if a > 3 then
                        begin
				             if a < 7 then 
				                b := b + 2;
				            else 
					            b := "toi ten";
                            if a <> 5 then
                                t := j:= k;
                            else
                                return false;
                        end
                            end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(Write),[StringLiteral(Enter your name: )]),CallStmt(Id(ReadLn),[Id(name)]),If(BinaryOp(=,Id(name),StringLiteral(Fred)),[CallStmt(Id(SayHello),[Id(name)])],[CallStmt(Id(WriteLn),[StringLiteral(I dont know you...)]),If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),StringLiteral(toi ten))]),If(BinaryOp(<>,Id(a),IntLiteral(5)),[AssignStmt(Id(j),Id(k)),AssignStmt(Id(t),Id(j))],[Return(Some(BooleanLiteral(False)))])],[])])])])"
        self.assertTrue(TestAST.test(input,expect,395))

    def test_complex_program_26(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            Begin {no semicolon}
                                Write("Input number 1:"); 
                                Readln("Num1");
                                Writeln("Input number 2:");
                                Readln(Num2);
                                Sum := Num1 + Num2; {addition} 
                                Writeln(Sum);
                                Readln(Sum);
                            FOR Step := 0 TO  MaxY DO
                            IF (Step MOD 5 =  0) THEN
                            Write("+");
                            ELSE
                            Write("-");
                            Write(" Y ");
                            WriteLn();
                            { Do the Plot on  its side }
                            X := First;
                            WHILE X <=  Last DO BEGIN
                                Y1 :=  SIN(3.14159 * X / 180.0);
                                Y1 := Factor *  Y1;
                                Q1 := ROUND(Y1);
                                Y2 := 0.005 * X;
                                Y2 := Factor *  Y2;
                                Q2 := ROUND(Y2);
                            end
                            End
                                
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(Write),[StringLiteral(Input number 1:)]),CallStmt(Id(Readln),[StringLiteral(Num1)]),CallStmt(Id(Writeln),[StringLiteral(Input number 2:)]),CallStmt(Id(Readln),[Id(Num2)]),AssignStmt(Id(Sum),BinaryOp(+,Id(Num1),Id(Num2))),CallStmt(Id(Writeln),[Id(Sum)]),CallStmt(Id(Readln),[Id(Sum)]),For(Id(Step)IntLiteral(0),Id(MaxY),True,[If(BinaryOp(=,BinaryOp(MOD,Id(Step),IntLiteral(5)),IntLiteral(0)),[CallStmt(Id(Write),[StringLiteral(+)])],[CallStmt(Id(Write),[StringLiteral(-)])])]),CallStmt(Id(Write),[StringLiteral( Y )]),CallStmt(Id(WriteLn),[]),AssignStmt(Id(X),Id(First)),While(BinaryOp(<=,Id(X),Id(Last)),[AssignStmt(Id(Y1),CallExpr(Id(SIN),[BinaryOp(/,BinaryOp(*,FloatLiteral(3.14159),Id(X)),FloatLiteral(180.0))])),AssignStmt(Id(Y1),BinaryOp(*,Id(Factor),Id(Y1))),AssignStmt(Id(Q1),CallExpr(Id(ROUND),[Id(Y1)])),AssignStmt(Id(Y2),BinaryOp(*,FloatLiteral(0.005),Id(X))),AssignStmt(Id(Y2),BinaryOp(*,Id(Factor),Id(Y2))),AssignStmt(Id(Q2),CallExpr(Id(ROUND),[Id(Y2)]))])])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test_complex_program_27(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
			                if a > 3 then
                                begin
				             if a < 7 then 
				                b := b + 2;
				            else 
					            b := "toi ten";
                            if a <> 5 then
                                t := j:= k;
                            else
                                return false;
                        end
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
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),StringLiteral(toi ten))]),If(BinaryOp(<>,Id(a),IntLiteral(5)),[AssignStmt(Id(j),Id(k)),AssignStmt(Id(t),Id(j))],[Return(Some(BooleanLiteral(False)))])],[]),If(BinaryOp(and,BinaryOp(>,Id(v1),Id(v2)),BinaryOp(>,Id(v1),Id(v3))),[AssignStmt(Id(result),Id(v1))],[If(BinaryOp(>,Id(v2),Id(v3)),[AssignStmt(Id(result),Id(v2))],[AssignStmt(Id(result),Id(v3))])])])])"
        self.assertTrue(TestAST.test(input,expect,397))

    def test_complex_program_28(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            if a <> 3 then
                                if a < 7 then 
                                    begin
                                        b := b + 2;
                                        if a=1 then b:= b + 1;
                                    end
                                else 
                                    b := b + 1;
                            else
                                a:= b := 6;
                            Begin {no semicolon}
                                Write("Input number 1:"); 
                                Readln("Num1");
                                Writeln("Input number 2:");
                                Readln(Num2);
                                Sum := Num1 + Num2; {addition} 
                                Writeln(Sum);
                                Readln(Sum);

                            End
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(<>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2))),If(BinaryOp(=,Id(a),IntLiteral(1)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))],[])],[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(1)))])],[AssignStmt(Id(b),IntLiteral(6)),AssignStmt(Id(a),Id(b))]),CallStmt(Id(Write),[StringLiteral(Input number 1:)]),CallStmt(Id(Readln),[StringLiteral(Num1)]),CallStmt(Id(Writeln),[StringLiteral(Input number 2:)]),CallStmt(Id(Readln),[Id(Num2)]),AssignStmt(Id(Sum),BinaryOp(+,Id(Num1),Id(Num2))),CallStmt(Id(Writeln),[Id(Sum)]),CallStmt(Id(Readln),[Id(Sum)])])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test_complex_program_29(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                        If Sel = "1" {condition} Then 
                        Begin  {more than one statement}
                            ClrScr();
                            Write("Input No.1:");
                            Readln(N1);
                            Write("Input No.2:");
                            Readln(N2);
                            Total := N1 + N2;
                            Writeln("Addition: ",N1," + ",N2," = ",Total);
                            Write("Press any key to continue...");
                            Readkey();
                        end { Closing the if statement }
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(BinaryOp(=,Id(Sel),StringLiteral(1)),[CallStmt(Id(ClrScr),[]),CallStmt(Id(Write),[StringLiteral(Input No.1:)]),CallStmt(Id(Readln),[Id(N1)]),CallStmt(Id(Write),[StringLiteral(Input No.2:)]),CallStmt(Id(Readln),[Id(N2)]),AssignStmt(Id(Total),BinaryOp(+,Id(N1),Id(N2))),CallStmt(Id(Writeln),[StringLiteral(Addition: ),Id(N1),StringLiteral( + ),Id(N2),StringLiteral( = ),Id(Total)]),CallStmt(Id(Write),[StringLiteral(Press any key to continue...)]),CallStmt(Id(Readkey),[])],[])])])"
        self.assertTrue(TestAST.test(input,expect,399))

    def test_complex_program_30(self):
        """Test complex program"""
        input = """ Function foo():integer;                      
                        Begin
                            write("Nhap nam : "); 
                            readln(n); 
                            if (n mod 400 = 0) or else ((n mod 4 = 0) and then(n mod 100 <> 0)) then write("namnhuan");
                            else write("Ko fai nam nhuan"); 
                            readln(); 
			                 if a > 3 then
                        begin
				             if a < 7 then 
				                b := b + 2;
				            else 
					            b := "toi ten";
                            if a <> 5 then
                                t := j:= k;
                            else
                                return false;
                        end
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(write),[StringLiteral(Nhap nam : )]),CallStmt(Id(readln),[Id(n)]),If(BinaryOp(orelse,BinaryOp(=,BinaryOp(mod,Id(n),IntLiteral(400)),IntLiteral(0)),BinaryOp(andthen,BinaryOp(=,BinaryOp(mod,Id(n),IntLiteral(4)),IntLiteral(0)),BinaryOp(<>,BinaryOp(mod,Id(n),IntLiteral(100)),IntLiteral(0)))),[CallStmt(Id(write),[StringLiteral(namnhuan)])],[CallStmt(Id(write),[StringLiteral(Ko fai nam nhuan)])]),CallStmt(Id(readln),[]),If(BinaryOp(>,Id(a),IntLiteral(3)),[If(BinaryOp(<,Id(a),IntLiteral(7)),[AssignStmt(Id(b),BinaryOp(+,Id(b),IntLiteral(2)))],[AssignStmt(Id(b),StringLiteral(toi ten))]),If(BinaryOp(<>,Id(a),IntLiteral(5)),[AssignStmt(Id(j),Id(k)),AssignStmt(Id(t),Id(j))],[Return(Some(BooleanLiteral(False)))])],[])])])"
        self.assertTrue(TestAST.test(input,expect,400))



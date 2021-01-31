from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce
#..........1613166: Nguyen Minh Tham............
class ASTGeneration(MPVisitor):

#..........................................................
#.....................DECLARATION..........................
#..........................................................
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.many_decl()))

    def visitMany_decl(self, ctx:MPParser.Many_declContext):
        if ctx.many_decl():
            return self.visit(ctx.decl()) + self.visit(ctx.many_decl())
        else:
            return self.visit(ctx.decl())

    def visitFunc_decl(self,ctx:MPParser.Func_declContext):
        return [FuncDecl(Id(ctx.ID().getText()),
                        self.visit(ctx.param_list()),
                        self.visit(ctx.var_decl()) if ctx.var_decl() else [],
                        self.visit(ctx.compound_statem()),
                        self.visit(ctx.typeIdentifer()))]
    def visitProce_decl(self,ctx:MPParser.Proce_declContext):
        return [FuncDecl(Id(ctx.ID().getText()),
                        self.visit(ctx.param_list()),
                        self.visit(ctx.var_decl())if ctx.var_decl() else [],
                        self.visit(ctx.compound_statem()))]


    def visitParam_list(self,ctx:MPParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return  self.visit(ctx.param()) +  self.visit(ctx.many_param())     

    def visitMany_param(self,ctx:MPParser.Many_paramContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return  self.visit(ctx.param()) +  self.visit(ctx.many_param())         

    def visitParam(self,ctx:MPParser.ParamContext):
        listID= self.visit(ctx.id_list())
        typeId = self.visit(ctx.typeIdentifer())
        return [VarDecl(_id,typeId) for _id in listID]


    def visitVar_decl(self,ctx:MPParser.Var_declContext):#OK Rut gon Var_decl
        return self.visit(ctx.many_var_decl()) 

    def visitMany_var_decl(self, ctx:MPParser.Many_var_declContext):#OK
        if ctx.many_var_decl():
            return self.visit(ctx.one_var_decl()) + self.visit(ctx.many_var_decl())
        else:
            return self.visit(ctx.one_var_decl())

    def visitOne_var_decl(self,ctx:MPParser.One_var_declContext):#OK
        listID= self.visit(ctx.id_list())
        typeId = self.visit(ctx.typeIdentifer())
        return [VarDecl(_id,typeId) for _id in listID]

    def visitId_list(self,ctx:MPParser.Id_listContext):#OK
        return [Id(_id.getText()) for _id in ctx.ID()]

#..........................................................
#................IDENTIFER TYPE............................
#..........................................................

    def visitPrimitive_type(self,ctx:MPParser.Primitive_typeContext):
        if ctx.BOOLEAN() is not None:
            return BoolType()
        elif ctx.INTEGER() is not None:
            return IntType()
        elif ctx.REAL() is not None:
            return FloatType()
        elif ctx.STRING() is not None:
            return StringType()

    def visitArray_type(self,ctx:MPParser.Array_typeContext):
        return ArrayType( self.visit(ctx.sub_intLit(0)), self.visit(ctx.sub_intLit(1)),self.visit(ctx.primitive_type()))

    def visitSub_intLit(self,ctx:MPParser.Sub_intLitContext):
        return int("-" + ctx.int_literal().getText()) if ctx.SUB()  else int(ctx.int_literal().getText())


#..........................................................
#.....................STATEMENT..........................
#..........................................................  


    def visitMany_statement_type(self,ctx:MPParser.Many_statement_typeContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return  self.visit(ctx.statement_type()) +  self.visit(ctx.many_statement_type()) 

    def visitCompound_statem(self,ctx:MPParser.Compound_statemContext):
        return self.visit(ctx.many_statement_type()) 

    def visitReturn_statem(self,ctx:MPParser.Return_statemContext):
        return [Return(self.visit(ctx.exp()))] if ctx.exp() else [Return(None)]

    def visitBreak_statem(self,ctx:MPParser.Break_statemContext):
        return [Break()]

    def visitContinue_statem(self,ctx:MPParser.Continue_statemContext):
        return [Continue()]

    def visitFor_statem(self,ctx:MPParser.For_statemContext):
        if ctx.TO():
            return [For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),"True",self.visit(ctx.statement_type()))]
        else:
            return [For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),"False",self.visit(ctx.statement_type()))]

    def visitWhile_statem(self,ctx:MPParser.While_statemContext):
        return [While(self.visit(ctx.exp()),self.visit(ctx.statement_type()))]

    def visitIf_statem(self,ctx:MPParser.If_statemContext):
        if ctx.ELSE():
            return [If(self.visit(ctx.exp())   ,  self.visit(ctx.statement_type(0)),self.visit(ctx.statement_type(1)))]
        else:
            return [If( self.visit(ctx.exp())  ,  self.visit(ctx.statement_type(0))  )]

    def visitWith_statem(self,ctx:MPParser.With_statemContext):
        return [With(self.visit(ctx.many_var_decl())   ,  self.visit(ctx.statement_type()))]

    def visitCall_statem(self,ctx:MPParser.Call_statemContext):
        return [CallStmt(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()] if ctx.exp() else [])]
        
    def visitAssign_statem(self,ctx:MPParser.Assign_statemContext):
        index_assign = [x for x in range(1,int(ctx.getChildCount()))]
        even_index_assign = list(filter(lambda x: x%2==0,index_assign))
        even_index_assign.reverse()
        return [Assign(self.visit(ctx.getChild(i-2)) , self.visit(ctx.getChild(i))) for i in even_index_assign]

    def visitLhs(self,ctx:MPParser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.index_exp())








#..........................................................
#.....................EXPRESSION..........................
#..........................................................

    #Binary operator: and then, or else
    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.AND():
            return BinaryOp("andthen",self.visit(ctx.exp()),self.visit(ctx.exp1()))
        elif ctx.OR():
            return BinaryOp("orelse",self.visit(ctx.exp()),self.visit(ctx.exp1()))
        else:
            return self.visit(ctx.exp1())

    #Binary operator: = , <> , < , <= , > , >=
    def visitExp1(self,ctx:MPParser.Exp1Context):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.LTHAN():
            return BinaryOp(ctx.LTHAN().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.LEQUAL():
            return BinaryOp(ctx.LEQUAL().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.GTHAN():
            return BinaryOp(ctx.GTHAN().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        elif ctx.GEQUAL():
            return BinaryOp(ctx.GEQUAL().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))

    #Binary operator: +,-,or
    def visitExp2(self,ctx:MPParser.Exp2Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    #Binary operator: /,*,div,mod,and
    def visitExp3(self,ctx:MPParser.Exp3Context):
        if ctx.DIVISION():
            return BinaryOp(ctx.DIVISION().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif ctx.MUL():
            return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif ctx.DIV_INT():
            return BinaryOp(ctx.DIV_INT().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif ctx.AND():
            return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    #Unary opertor: -, not
    def visitExp4(self,ctx:MPParser.Exp4Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp4()))
        elif ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self,ctx:MPParser.Exp5Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.index_exp():
            return self.visit(ctx.index_exp())
        elif ctx.invocation_exp():
            return self.visit(ctx.invocation_exp())

    def visitInvocation_exp(self,ctx:MPParser.Exp4Context):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()] if ctx.exp() else [])

    def visitIndex_exp(self,ctx:MPParser.Index_expContext):
        if ctx.index_exp():
            return ArrayCell(self.visit(ctx.index_exp()),self.visit(ctx.exp()))
        else:
            return ArrayCell(self.visit(ctx.replace_exp()),self.visit(ctx.exp()))

    def visitReplace_exp(self,ctx:MPParser.Replace_expContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.invocation_exp():
            return self.visit(ctx.invocation_exp())


#..........................................................
#.....................LITERAL..........................
#..........................................................

    def visitInt_literal(self, ctx:MPParser.Int_literalContext):
        return IntLiteral(int(ctx.INT_LITERAL().getText()))

    def visitFloat_literal(self, ctx:MPParser.Float_literalContext):
        return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))

    def visitBool_literal(self, ctx:MPParser.Bool_literalContext):
        return BooleanLiteral(bool(True)) if ctx.TRUE() else BooleanLiteral(bool(False))

    def visitString_literal(self, ctx:MPParser.String_literalContext):
        return StringLiteral(str(ctx.STRING_LITERAL().getText()))
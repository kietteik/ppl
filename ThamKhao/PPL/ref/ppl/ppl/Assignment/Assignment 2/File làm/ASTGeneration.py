from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import *

class ASTGeneration(MCVisitor):

    def visitProgram(self,ctx:MCParser.ProgramContext):
        alldecls = [self.visit(x) for x in ctx.declaration()]
        lst_decls = []
        for i in alldecls:
            if not isinstance(i,list):
                lst_decls.append(i)
            else:
                for j in i:
                    lst_decls.append(j)
        return Program(lst_decls)

    def visitDeclaration(self,ctx:MCParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        lst = []
        for var in self.visit(ctx.variables()):
            if len(var) == 2 :
                lst+= [VarDecl(var[0],ArrayType(int(var[1]),self.visit(ctx.primitiveType())))]
            else:
                lst+= [VarDecl(var[0],self.visit(ctx.primitiveType()))]           
        return lst 

    def visitVariables(self,ctx:MCParser.VariablesContext):
    	return [self.visit(x) for x in ctx.var()]

    def visitVar(self,ctx:MCParser.VarContext): 
        return [ctx.ID().getText(),ctx.INTLIT().getText()] if ctx.INTLIT() else [ctx.ID().getText()]

    def visitPrimitiveType(self,ctx:MCParser.PrimitiveTypeContext):
        if ctx.FLOATTYPE():
            return FloatType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()

    # Function declaration
    def visitFuncdecls(self,ctx:MCParser.FuncdeclsContext):
    	return FuncDecl(Id(ctx.ID().getText()),
    					self.visit(ctx.paraList()) if ctx.paraList() else [],
    					self.visit(ctx.type1()),
    					self.visit(ctx.blockStmt()))

    def visitType1(self,ctx:MCParser.Type1Context):
        return VoidType() if ctx.VOIDTYPE() else self.visit(ctx.getChild(0))

    def visitParaList(self,ctx:MCParser.ParaListContext):
        return [self.visit(x) for x in ctx.paradecls()]

    def visitParadecls(self,ctx:MCParser.ParadeclsContext):
        return VarDecl(str(ctx.ID().getText()),self.visit(ctx.primitiveType())) if ctx.getChildCount() == 2 else VarDecl(str(ctx.ID().getText()),ArrayPointerType(self.visit(ctx.primitiveType())))

    def visitArrpointertype(self,ctx:MCParser.ArrpointertypeContext):
        return ArrayPointerType(self.visit(ctx.primitiveType()))

    # Statements and Control Flow
    def visitStatement(self,ctx:MCParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitIfStmt(self,ctx:MCParser.IfStmtContext):
        return If(self.visit(ctx.exp()),
                    self.visit(ctx.statement(0)),
                    self.visit(ctx.statement(1)) if ctx.ELSE() else None)

    def visitDowhileStmt(self,ctx:MCParser.DowhileStmtContext):
        return Dowhile([self.visit(x) for x in ctx.statement()],
                        self.visit(ctx.exp()))

    def visitForStmt(self,ctx:MCParser.ForStmtContext):
        return For(self.visit(ctx.exp(0)),
                    self.visit(ctx.exp(1)),
                    self.visit(ctx.exp(2)),
                    self.visit(ctx.statement()))

    def visitBreakStmt(self,ctx:MCParser.BreakStmtContext):
        return Break()

    def visitContinueStmt(self,ctx:MCParser.ContinueStmtContext):
        return Continue()

    def visitReturnStmt(self,ctx:MCParser.ReturnStmtContext):
        return Return(self.visit(ctx.exp()) if ctx.exp() else None)

    def visitExpStmt(self, ctx:MCParser.ExpStmtContext):
        return self.visit(ctx.exp())
    
    def visitBlockStmt(self,ctx:MCParser.BlockStmtContext):
        if ctx.vardecl_statement() :
            return Block(reduce(lambda x, y: x + self.visit(y), ctx.vardecl_statement()[1:], self.visit(ctx.vardecl_statement()[0])))         
        else:
            return Block([])

    def visitVardecl_statement(self,ctx:MCParser.Vardecl_statementContext):
        lst = self.visit(ctx.getChild(0))
        if isinstance(lst, list) is not True:
            lst = [lst]
        return lst    

    # Expressions
    def visitExp(self, ctx:MCParser.ExpContext):
        return BinaryOp(ctx.ASSIGNOP().getText(),
                    self.visit(ctx.exp1()),
                    self.visit(ctx.exp())) if ctx.getChildCount() != 1 else self.visit(ctx.exp1())

    def visitExp1(self, ctx:MCParser.Exp1Context):
        return BinaryOp(ctx.OROP().getText(),
                    self.visit(ctx.exp1()),
                    self.visit(ctx.exp2())) if ctx.getChildCount() != 1 else self.visit(ctx.exp2())

    def visitExp2(self, ctx:MCParser.Exp2Context):
        return BinaryOp(ctx.ANDOP().getText(),
                    self.visit(ctx.exp2()),
                    self.visit(ctx.exp3())) if ctx.getChildCount() != 1 else self.visit(ctx.exp3())

    def visitExp3(self, ctx:MCParser.Exp3Context):
        return BinaryOp(ctx.getChild(1).getText() if ctx.getChildCount() != 1 else None,
                    self.visit(ctx.exp4(0)),
                    self.visit(ctx.exp4(1))) if ctx.getChildCount() != 1 else self.visit(ctx.exp4(0))

    def visitExp4(self, ctx:MCParser.Exp4Context):
        return BinaryOp(ctx.getChild(1).getText() if ctx.getChildCount() != 1 else None,
                    self.visit(ctx.exp5(0)),
                    self.visit(ctx.exp5(1))) if ctx.getChildCount() != 1 else self.visit(ctx.exp5(0))

    def visitExp5(self, ctx:MCParser.Exp5Context):
        return BinaryOp(ctx.getChild(1).getText() if ctx.getChildCount() != 1 else None,
                    self.visit(ctx.exp5()),
                    self.visit(ctx.exp6())) if ctx.getChildCount() != 1 else self.visit(ctx.exp6())

    def visitExp6(self, ctx:MCParser.Exp6Context):
        return BinaryOp(ctx.getChild(1).getText() if ctx.getChildCount() != 1 else None,
                    self.visit(ctx.exp6()),
                    self.visit(ctx.exp7())) if ctx.getChildCount() != 1 else self.visit(ctx.exp7())

    def visitExp7(self, ctx:MCParser.Exp7Context):
        return UnaryOp(ctx.getChild(0).getText() if ctx.getChildCount() != 1 else None,
                    self.visit(ctx.exp7())) if ctx.getChildCount() != 1 else self.visit(ctx.exp8())

    def visitExp8(self, ctx:MCParser.Exp8Context):
        return ArrayCell(self.visit(ctx.exp9()), 
                    self.visit(ctx.exp())) if ctx.exp() else self.visit(ctx.exp9())

    def visitExp9(self,ctx:MCParser.Exp9Context):
        return self.visit(ctx.exp()) if ctx.getChildCount() != 1 else self.visit(ctx.exp10())

    def visitExp10(self,ctx:MCParser.Exp10Context):
        return self.visit(ctx.getChild(0))

    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.ID():
            return Id(str(ctx.ID().getText()))
        else:
            return ArrayCell(self.visit(ctx.ID()).getText(),
                        self.visit(ctx.INTLIT()).getText())

    def visitFunccall(self,ctx:MCParser.FunccallContext):
        return CallExpr(Id(ctx.ID().getText()),
                    self.visit(ctx.paralist_call()) if ctx.paralist_call() else [])

    def visitParalist_call(self,ctx:MCParser.Paralist_callContext):
        return [self.visit(x) for x in ctx.para_call()]

    def visitPara_call(self,ctx:MCParser.Para_callContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.ID():
            return Id(str(ctx.ID().getText()))
        else:
            return self.visit(ctx.exp())

    def visitLiterals(self,ctx:MCParser.LiteralsContext):
        if ctx.BOOLLIT():
            return BooleanLiteral(str(ctx.BOOLLIT().getText()) == "true")
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        else:
            return StringLiteral(str(ctx.STRINGLIT().getText()))

    def visitElementArray(self,ctx:MCParser.ElementArrayContext):
        return ArrayCell(self.visit(ctx.ID()).getText(),
                        self.visit(ctx.INTLIT()).getText())

        

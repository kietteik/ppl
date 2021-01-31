from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        varDecList = []
        funcDecList = []
        if ctx.varDecList():
            varDecList = self.visit(ctx.varDecList())
        if ctx.funcDecList():
            funcDecList = self.visit(ctx.funcDecList())
        return Program(varDecList + funcDecList)

    # Variable declaration

    def visitVarDecList(self, ctx: BKITParser.VarDecListContext):
        if ctx.varDecList():
            return self.visit(ctx.varDec()) + self.visit(ctx.varDecList())
        return self.visit(ctx.varDec())

    def visitVarDec(self, ctx: BKITParser.VarDecContext):
        return self.visit(ctx.varList())

    def visitVarList(self, ctx: BKITParser.VarListContext):
        if ctx.varList():
            if ctx.varLit():
                return self.visit(ctx.varLit()) + self.visit(ctx.varList())
            if ctx.varArray():
                return self.visit(ctx.varArray()) + self.visit(ctx.varList())
            else:
                raise("Error from VarList")
        else:
            if ctx.varLit():
                return self.visit(ctx.varLit())
            if ctx.varArray():
                return self.visit(ctx.varArray())
            else:
                raise("Error from VarList")

    def visitVarLit(self, ctx: BKITParser.VarLitContext):
        if ctx.ASSIGN():
            if ctx.INTLIT():
                return [VarDecl(Id(ctx.ID().getText()), [], IntLiteral(int(ctx.INTLIT().getText(),0)))]
            if ctx.FLOATLIT():
                return [VarDecl(Id(ctx.ID().getText()), [], FloatLiteral(float(ctx.FLOATLIT().getText())))]
            if ctx.BOOLLIT():
                return [VarDecl(Id(ctx.ID().getText()), [], BooleanLiteral('True'==ctx.BOOLLIT().getText()))]
            if ctx.STRING():
                return [VarDecl(Id(ctx.ID().getText()), [], StringLiteral(ctx.STRING().getText()))]
            else:
                raise("Error from varLit")
        else:
            return [VarDecl(Id(ctx.ID().getText()), [], varInit=None)]

    def visitVarArray(self, ctx: BKITParser.VarArrayContext):
        if ctx.ASSIGN():
            return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.varArrayIndex()), self.visit(ctx.array()))]
        return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.varArrayIndex()), None)]

    def visitVarArrayIndex(self, ctx: BKITParser.VarArrayIndexContext):
        if ctx.varArrayIndex():
            return [int(ctx.INTLIT().getText(),0)] + self.visit(ctx.varArrayIndex())
        return [int(ctx.INTLIT().getText(),0)]

    def visitArray(self, ctx: BKITParser.ArrayContext):
        if ctx.INTLIT():
            return ArrayLiteral([IntLiteral(int(x.getText(),0)) for x in ctx.INTLIT()])
        if ctx.FLOATLIT():
            return ArrayLiteral([FloatLiteral(float(x.getText())) for x in ctx.FLOATLIT()])
        if ctx.BOOLLIT():
            return ArrayLiteral([BooleanLiteral("True"==x.getText()) for x in ctx.BOOLLIT()])
        if ctx.STRING():
            return ArrayLiteral([StringLiteral(x.getText()) for x in ctx.STRING()])
        if ctx.array():
            return ArrayLiteral([self.visit(x) for x in ctx.array()])

    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText(),0))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLLIT():
            return BooleanLiteral('True'==ctx.BOOLLIT().getText())
        if ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        if ctx.array():
            return self.visit(ctx.array())
        else:
            raise("Error from literal")

    # Function declaration

    def visitFuncDecList(self, ctx: BKITParser.FuncDecListContext):
        funcDec = self.visit(ctx.funcDec())
        if ctx.funcDecList():
            return [funcDec] + self.visit(ctx.funcDecList())
        return [funcDec]

    def visitFuncDec(self, ctx: BKITParser.FuncDecContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paramSection()), self.visit(ctx.bodySection()))

    def visitParamSection(self, ctx: BKITParser.ParamSectionContext):
        if ctx.paramList():
            return self.visit(ctx.paramList())
        return []

    def visitParamList(self, ctx: BKITParser.ParamListContext):
        param = self.visit(ctx.param())
        if ctx.CM():
            return [param] + self.visit(ctx.paramList())
        return [param]

    def visitParam(self, ctx: BKITParser.ParamContext):
        ide = Id(ctx.ID().getText())
        if ctx.varArrayIndex():
            return VarDecl(ide, self.visit(ctx.varArrayIndex()), None)
        return VarDecl(ide, [], None)

    def visitBodySection(self, ctx: BKITParser.BodySectionContext):
        return self.visit(ctx.varDecWithStatementList())

    def visitVarDecWithStatementList(self, ctx: BKITParser.VarDecWithStatementListContext):
        varDecList = []
        nullableStatementList = self.visit(ctx.nullableStatementList())
        if ctx.varDecList():
            varDecList = self.visit(ctx.varDecList())
        return (varDecList, nullableStatementList)

    def visitNullableStatementList(self, ctx: BKITParser.NullableStatementListContext):
        statementList = []
        if ctx.statementList():
            statementList = self.visit(ctx.statementList())
        return statementList

    def visitStatementList(self, ctx: BKITParser.StatementListContext):
        oneStatement = self.visit(ctx.oneStatement())
        if ctx.statementList():
            return [oneStatement] + self.visit(ctx.statementList())
        return [oneStatement]

    def visitOneStatement(self, ctx: BKITParser.OneStatementContext):
        return self.visit(ctx.getChild(0))

    def visitAssignStatement(self, ctx: BKITParser.AssignStatementContext):
        return Assign(self.visit(ctx.variable()), self.visit(ctx.expression()))

    def visitIfStatement(self, ctx: BKITParser.IfStatementContext):
        if ctx.ELSE():
            listExpression = ctx.expression()
            listVarDecStatement = ctx.varDecWithStatementList()[:-1]
            zipper = zip(listExpression, listVarDecStatement)
            listOfIfStatement = list(map(lambda x: (
                self.visit(x[0]), *self.visit(x[1])), zipper))
            elseStatement = self.visit(ctx.varDecWithStatementList()[-1])
            return If(listOfIfStatement, elseStatement)
        listExpression = ctx.expression()
        listVarDecStatement = ctx.varDecWithStatementList()
        listOfIfStatement = list(map(lambda x: (self.visit(
            x[0]), *self.visit(x[1])), zip(listExpression, listVarDecStatement)))
        return If(listOfIfStatement, ([],[]))

    def visitForStatement(self, ctx: BKITParser.ForStatementContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.expression(2)), self.visit(ctx.varDecWithStatementList()))

    def visitWhileStatement(self, ctx: BKITParser.WhileStatementContext):
        return While(self.visit(ctx.expression()), self.visit(ctx.varDecWithStatementList()))

    def visitDowhileStatement(self, ctx: BKITParser.DowhileStatementContext):
        return Dowhile(self.visit(ctx.varDecWithStatementList()), self.visit(ctx.expression()))

    def visitBreakStatement(self, ctx: BKITParser.BreakStatementContext):
        return Break()

    def visitContinueStatement(self, ctx: BKITParser.ContinueStatementContext):
        return Continue()

    def visitCallStatement(self, ctx: BKITParser.CallStatementContext):
        return CallStmt(*self.visit(ctx.funcCall()))

    def visitReturnStatement(self, ctx: BKITParser.ReturnStatementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)

    def visitRelational(self, ctx: BKITParser.RelationalContext):
        return ctx.getChild(0).getText()

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.getChild(1)), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))

    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))

    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp4()))
        return self.visit(ctx.exp5())

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())

    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.exp6()),self.visit(ctx.indexOperators()))
        return self.visit(ctx.exp7())

    def visitExp7(self, ctx: BKITParser.Exp7Context):
        if ctx.funcCall():
            return CallExpr(*self.visit(ctx.funcCall()))
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.literal():
            return self.visit(ctx.literal())

    def visitVariable(self, ctx: BKITParser.VariableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.arrayElement())

    def visitArrayElement(self, ctx: BKITParser.ArrayElementContext):
        # if ctx.ID():
        #     return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexOperators()))
        # else:
        #     return ArrayCell(self.visit(ctx.funcCall()), self.visit(ctx.indexOperators()))
        return self.visit(ctx.exp6())

    def visitIndexOperators(self, ctx: BKITParser.IndexOperatorsContext):
        exp = self.visit(ctx.expression())
        if ctx.indexOperators():
            return [exp] + self.visit(ctx.indexOperators())
        return [exp]

    def visitFuncCall(self, ctx: BKITParser.FuncCallContext):
        if ctx.expList():
            return (Id(ctx.ID().getText()), self.visit(ctx.expList()))
        return (Id(ctx.ID().getText()), [])

    def visitExpList(self, ctx: BKITParser.ExpListContext):
        expr = self.visit(ctx.expression())
        if ctx.expList():
            return [expr] + self.visit(ctx.expList())
        return [expr]

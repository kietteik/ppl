# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDecList.
    def visitVarDecList(self, ctx:BKITParser.VarDecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDecList.
    def visitFuncDecList(self, ctx:BKITParser.FuncDecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDec.
    def visitVarDec(self, ctx:BKITParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varList.
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varLit.
    def visitVarLit(self, ctx:BKITParser.VarLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varArray.
    def visitVarArray(self, ctx:BKITParser.VarArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varArrayIndex.
    def visitVarArrayIndex(self, ctx:BKITParser.VarArrayIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDec.
    def visitFuncDec(self, ctx:BKITParser.FuncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramSection.
    def visitParamSection(self, ctx:BKITParser.ParamSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramList.
    def visitParamList(self, ctx:BKITParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bodySection.
    def visitBodySection(self, ctx:BKITParser.BodySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#nullableStatementList.
    def visitNullableStatementList(self, ctx:BKITParser.NullableStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statementList.
    def visitStatementList(self, ctx:BKITParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#oneStatement.
    def visitOneStatement(self, ctx:BKITParser.OneStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignStatement.
    def visitAssignStatement(self, ctx:BKITParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStatement.
    def visitIfStatement(self, ctx:BKITParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStatement.
    def visitForStatement(self, ctx:BKITParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStatement.
    def visitWhileStatement(self, ctx:BKITParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhileStatement.
    def visitDowhileStatement(self, ctx:BKITParser.DowhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStatement.
    def visitBreakStatement(self, ctx:BKITParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStatement.
    def visitContinueStatement(self, ctx:BKITParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStatement.
    def visitCallStatement(self, ctx:BKITParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStatement.
    def visitReturnStatement(self, ctx:BKITParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational.
    def visitRelational(self, ctx:BKITParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrayElement.
    def visitArrayElement(self, ctx:BKITParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexOperators.
    def visitIndexOperators(self, ctx:BKITParser.IndexOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcCall.
    def visitFuncCall(self, ctx:BKITParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expList.
    def visitExpList(self, ctx:BKITParser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)



del BKITParser
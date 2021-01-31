# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
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


    # Visit a parse tree produced by BKITParser#listVarDeclar.
    def visitListVarDeclar(self, ctx:BKITParser.ListVarDeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listFuncDeclar.
    def visitListFuncDeclar(self, ctx:BKITParser.ListFuncDeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#noNullListVarDeclar.
    def visitNoNullListVarDeclar(self, ctx:BKITParser.NoNullListVarDeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#noNullListFuncDeclar.
    def visitNoNullListFuncDeclar(self, ctx:BKITParser.NoNullListFuncDeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardeclara.
    def visitVardeclara(self, ctx:BKITParser.VardeclaraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listvar.
    def visitListvar(self, ctx:BKITParser.ListvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#nonInitVar.
    def visitNonInitVar(self, ctx:BKITParser.NonInitVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initVar.
    def visitInitVar(self, ctx:BKITParser.InitVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varArrayIdentifier.
    def visitVarArrayIdentifier(self, ctx:BKITParser.VarArrayIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_index_operators.
    def visitVar_index_operators(self, ctx:BKITParser.Var_index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdeclara.
    def visitFuncdeclara(self, ctx:BKITParser.FuncdeclaraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listparam.
    def visitListparam(self, ctx:BKITParser.ListparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcbody.
    def visitFuncbody(self, ctx:BKITParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listStatement.
    def visitListStatement(self, ctx:BKITParser.ListStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listOtherStatements.
    def visitListOtherStatements(self, ctx:BKITParser.ListOtherStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#noNullListOtherStatements.
    def visitNoNullListOtherStatements(self, ctx:BKITParser.NoNullListOtherStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assigment.
    def visitAssigment(self, ctx:BKITParser.AssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
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


    # Visit a parse tree produced by BKITParser#element_exp.
    def visitElement_exp(self, ctx:BKITParser.Element_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#listExp.
    def visitListExp(self, ctx:BKITParser.ListExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#noNullListExp.
    def visitNoNullListExp(self, ctx:BKITParser.NoNullListExpContext):
        return self.visitChildren(ctx)



del BKITParser
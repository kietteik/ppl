# Generated from main/mC/parser/mC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mCParser import mCParser
else:
    from mCParser import mCParser

# This class defines a complete generic visitor for a parse tree produced by mCParser.

class mCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mCParser#program.
    def visitProgram(self, ctx:mCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#var_dec.
    def visitVar_dec(self, ctx:mCParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#func_dec.
    def visitFunc_dec(self, ctx:mCParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#one_param.
    def visitOne_param(self, ctx:mCParser.One_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#param_list.
    def visitParam_list(self, ctx:mCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#func_body.
    def visitFunc_body(self, ctx:mCParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#stmt.
    def visitStmt(self, ctx:mCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#assignment.
    def visitAssignment(self, ctx:mCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#call.
    def visitCall(self, ctx:mCParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#return_stmt.
    def visitReturn_stmt(self, ctx:mCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#exp.
    def visitExp(self, ctx:mCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mCParser#type_stmt.
    def visitType_stmt(self, ctx:mCParser.Type_stmtContext):
        return self.visitChildren(ctx)



del mCParser
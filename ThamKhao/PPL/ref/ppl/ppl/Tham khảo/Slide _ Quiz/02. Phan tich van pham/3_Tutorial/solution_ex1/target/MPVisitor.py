# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#many_decl.
    def visitMany_decl(self, ctx:MPParser.Many_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_decl.
    def visitVar_decl(self, ctx:MPParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_id.
    def visitList_id(self, ctx:MPParser.List_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#id_type.
    def visitId_type(self, ctx:MPParser.Id_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_decl.
    def visitFunc_decl(self, ctx:MPParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#para_decl.
    def visitPara_decl(self, ctx:MPParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#para_list.
    def visitPara_list(self, ctx:MPParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#many_para.
    def visitMany_para(self, ctx:MPParser.Many_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#para.
    def visitPara(self, ctx:MPParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#members.
    def visitMembers(self, ctx:MPParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#member.
    def visitMember(self, ctx:MPParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ass_stmt.
    def visitAss_stmt(self, ctx:MPParser.Ass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_stmt.
    def visitCall_stmt(self, ctx:MPParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_stmt.
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_exp.
    def visitList_exp(self, ctx:MPParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#many_exp.
    def visitMany_exp(self, ctx:MPParser.Many_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)



del MPParser
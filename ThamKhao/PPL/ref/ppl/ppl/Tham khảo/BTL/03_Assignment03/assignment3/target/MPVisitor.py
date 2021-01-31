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


    # Visit a parse tree produced by MPParser#many_var_decl.
    def visitMany_var_decl(self, ctx:MPParser.Many_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#one_var_decl.
    def visitOne_var_decl(self, ctx:MPParser.One_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_decl.
    def visitFunc_decl(self, ctx:MPParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proce_decl.
    def visitProce_decl(self, ctx:MPParser.Proce_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param_list.
    def visitParam_list(self, ctx:MPParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#many_param.
    def visitMany_param(self, ctx:MPParser.Many_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param.
    def visitParam(self, ctx:MPParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#id_list.
    def visitId_list(self, ctx:MPParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#typeIdentifer.
    def visitTypeIdentifer(self, ctx:MPParser.TypeIdentiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array_type.
    def visitArray_type(self, ctx:MPParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#sub_intLit.
    def visitSub_intLit(self, ctx:MPParser.Sub_intLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement_type.
    def visitStatement_type(self, ctx:MPParser.Statement_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#many_statement_type.
    def visitMany_statement_type(self, ctx:MPParser.Many_statement_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_statem.
    def visitCompound_statem(self, ctx:MPParser.Compound_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assign_statem.
    def visitAssign_statem(self, ctx:MPParser.Assign_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_statem.
    def visitIf_statem(self, ctx:MPParser.If_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_statem.
    def visitFor_statem(self, ctx:MPParser.For_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_statem.
    def visitWhile_statem(self, ctx:MPParser.While_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_statem.
    def visitReturn_statem(self, ctx:MPParser.Return_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_statem.
    def visitBreak_statem(self, ctx:MPParser.Break_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_statem.
    def visitContinue_statem(self, ctx:MPParser.Continue_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_statem.
    def visitCall_statem(self, ctx:MPParser.Call_statemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_statem.
    def visitWith_statem(self, ctx:MPParser.With_statemContext):
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


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_exp.
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#replace_exp.
    def visitReplace_exp(self, ctx:MPParser.Replace_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invocation_exp.
    def visitInvocation_exp(self, ctx:MPParser.Invocation_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#int_literal.
    def visitInt_literal(self, ctx:MPParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#float_literal.
    def visitFloat_literal(self, ctx:MPParser.Float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#bool_literal.
    def visitBool_literal(self, ctx:MPParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#string_literal.
    def visitString_literal(self, ctx:MPParser.String_literalContext):
        return self.visitChildren(ctx)



del MPParser
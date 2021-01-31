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


    # Visit a parse tree produced by BKITParser#variable_declaration.
    def visitVariable_declaration(self, ctx:BKITParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declaration.
    def visitFunction_declaration(self, ctx:BKITParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_body.
    def visitFunction_body(self, ctx:BKITParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:BKITParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_parameter.
    def visitVariable_parameter(self, ctx:BKITParser.Variable_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
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


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#in_parameters.
    def visitIn_parameters(self, ctx:BKITParser.In_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_function.
    def visitCall_function(self, ctx:BKITParser.Call_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment.
    def visitAssignment(self, ctx:BKITParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#data_type.
    def visitData_type(self, ctx:BKITParser.Data_typeContext):
        return self.visitChildren(ctx)



del BKITParser
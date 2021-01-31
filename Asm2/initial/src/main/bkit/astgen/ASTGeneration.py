from BKITVisitor import BKITVisitor
from functools import reduce
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self, ctx: BKITParser.ExpContext):

        if len(ctx.ASSIGN()) != 0:
            terms = ctx.term()
            assigns = ctx.ASSIGN()
            zipper = list(zip(assigns, terms))[::-1]
            return reduce(lambda a, b: Binary(b[0].getText(), self.visit(b[1]), a), zipper, self.visit(terms[-1]))
        return self.visit(ctx.term(0))

    def visitTerm(self, ctx: BKITParser.TermContext):

        if (ctx.COMPARE()):
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: BKITParser.FactorContext):

        if len(ctx.ANDOR()) != 0:
            andorList = ctx.ANDOR()
            operandList = ctx.operand()
            zipper = list(zip(andorList, operandList[1:]))
            return reduce(lambda a, b: Binary(b[0].getText(), a, self.visit(b[1])), zipper, self.visit(operandList[0]))
        return self.visit(ctx.operand(0))

    def visitOperand(self, ctx: BKITParser.OperandContext):
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        if (ctx.BOOLIT()):
            return BooleanLiteral(bool(ctx.BOOLIT().getText()))
        else:
            return self.visit(ctx.exp())

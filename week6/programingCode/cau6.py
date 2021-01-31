# program: exp EOF;

# exp: (term ASSIGN)* term;

# [1, 2, 3, 4]
# ['=', '=', '=']
# 1 = (2 = (3 = 4))

# term: factor COMPARE factor | factor;

# factor: operand (ANDOR operand)*;

# [1, 2, 3, 4]
# ['and', 'or', 'and']
# (((1 and 2) or 3) and 4)

# operand: ID | INTLIT | BOOLIT | '(' exp ')';

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):

        if len(ctx.ASSIGN()) != 0:
            terms = ctx.term()
            assigns = ctx.ASSIGN()
            zipper = list(zip(assigns, terms))[::-1]
            return reduce(lambda a, b: Binary(b[0].getText(), self.visit(b[1]), a), zipper, self.visit(terms[-1]))
        return self.visit(ctx.term(0))

    def visitTerm(self, ctx: MPParser.TermContext):

        if (ctx.COMPARE()):
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: MPParser.FactorContext):

        if len(ctx.ANDOR()) != 0:
            andorList = ctx.ANDOR()
            operandList = ctx.operand()
            zipper = list(zip(andorList, operandList[1:]))
            return reduce(lambda a, b: Binary(b[0].getText(), a, self.visit(b[1])), zipper, self.visit(operandList[0]))
        return self.visit(ctx.operand(0))

    def visitOperand(self, ctx: MPParser.OperandContext):
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        if (ctx.BOOLIT()):
            return BooleanLiteral(bool(ctx.BOOLIT().getText()))
        else:
            return self.visit(ctx.exp())

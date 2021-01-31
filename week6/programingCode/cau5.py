# program: vardecl+ EOF;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID (',' ID)*; 

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        vardeclList = [self.visit(i) for i in ctx.vardecl()]
        return Program(reduce(lambda a, b: a+b, vardeclList))

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        mptype = self.visit(ctx.mptype())
        return [VarDecl(x, mptype) for x in self.visit(ctx.ids())]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if (ctx.INTTYPE()):
            return IntType()
        else:
            return FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        return [Id(i.getText()) for i in ctx.ID()]

# program: vardecls EOF;

# vardecls: vardecl vardecltail;

# vardecltail: vardecl vardecltail | ;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID ',' ids | ID;

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if (ctx.vardecl()):
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else:
            return 1

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 1

    def visitMptype(self, ctx: MPParser.MptypeContext):

        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if (ctx.ids()):
            return 2 + self.visit(ctx.ids())
        return 1

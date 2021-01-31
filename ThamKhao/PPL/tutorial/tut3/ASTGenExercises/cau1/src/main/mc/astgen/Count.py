from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return 1 + self.visitVardecls(ctx.vardecls()) 

    # mctype: INTTYPE | FLOATTYPE | ARRAY LB INTLIT RB OF mctype ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.getChildCount() == 6:
            return 6 # return number of leaf nodes from the third right hand side
        else:
            return 1 # return number of leaf nodes from the first or second right hand side

    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return self.visitVardecl(ctx.vardecl()) + self.visitVardecls(ctx.vardecls()) # return number of leaf nodes from the first right hand side
        else:
            return self.visitVardecl(ctx.vardecl())# return number of leaf nodes from the second right hand side
  	
    # vardecl: mctype ids SEMI ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return self.visitMctype(ctx.mctype()) + self.visitIds(ctx.ids()) + 1

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return len(ctx.ID()) + len(ctx.COMMA())
        # return ctx.ID().len() + ctx.COMMA().len()


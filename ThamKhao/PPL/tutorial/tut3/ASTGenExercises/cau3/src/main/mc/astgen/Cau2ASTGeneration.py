from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))  # return a Program object
    
    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        vardecl = [] + ctx.vardecl().accept(self) 
        if ctx.getChildCount() == 2:
            return  vardecl + ctx.vardecls().accept(self) # return the list of VarDecl for the first right hand side
        else:
            return vardecl # return the list of VarDecl for the second right hand side  

    # vardecl: mctype ids ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        mctype = ctx.mctype().accept(self)
        ids = ctx.ids().accept(self)

        return [VarDecl(mctype, item_id) for item_id in ids] # return VarDecl object
  
  	# mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        mctype = ctx.getChild(0).getText()
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return [item.getText() for item in ctx.ID()] # return the list of identifier's lexemes
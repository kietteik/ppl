from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,x: acc+ self.visit(x,acc), ctx.decl,[] )
        
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        else:
            return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        else:
            return [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
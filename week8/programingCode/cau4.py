from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,x: (acc[0] + self.visit(x,acc), acc[1] + self.visit(x,acc)), ctx.decl, ([],[]) )
        
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        else:
            return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        else:
            return [ctx.name]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        else:
            acc=  reduce(lambda acc,x: (acc[0]+ self.visit(x,acc), acc[1]+ self.visit(x,acc)), ctx.param+ctx.body[0], ([],[ctx.name]+o[1]))
            temp = [self.visit(x,acc[1]) for x in ctx.body[1]]
            return [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
        
    def visitId(self,ctx:Id,o:object):
        if ctx.name in o:
            return ctx.name
        else:
            raise UndeclaredIdentifier(ctx.name)
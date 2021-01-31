from functools import reduce

class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o):
        varList = reduce(lambda acc,x: acc + self.visit(x,acc), ctx.decl, [] )
        #print(varList)
        return Program(varList, self.visit(ctx.exp, varList))
        
        
    def visitVarDecl(self,ctx:VarDecl,o):
        #print(ctx.typ)
        return [(ctx.name, ctx.typ)]
        
    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        
        if ctx.op in ['+','-','*']:
            
            if (type(e1) == BoolLit or type(e2) == BoolLit):
                raise TypeMismatchInExpression(ctx)
            elif(type(e1) == FloatLit or type(e2) == FloatLit):
                return FloatLit(ctx)
            else:
                return IntLit(ctx)
        elif ctx.op == '/':
            if (type(e1) == BoolLit or type(e2) == BoolLit):
                raise TypeMismatchInExpression(ctx)
            else:
                return FloatLit(ctx)
        elif ctx.op in ['||', '&&']:
            if (type(e1) != BoolLit or type(e2) != BoolLit):
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
        elif ctx.op in ['>', '<', '==', '!=']:
            if (type(e1) != type(e2)):
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
                
    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e, o)
        if ctx.op == '!':
            if type(e) !=  BoolLit:
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
        elif ctx.op == '-':
            if type(e) == BoolLit:
                raise TypeMismatchInExpression(ctx)
            elif type(e) == FloatLit:
                return FloatLit(ctx)
            elif type(e) == IntLit:
                return IntLit(ctx)
    def visitIntLit(self,ctx:IntLit,o): 
        return IntLit(ctx.val)

    def visitFloatLit(self,ctx,o): 
        return FloatLit(ctx.val)

    def visitBoolLit(self,ctx,o): 
        return BoolLit(ctx.val)
        
    def visitId(self,ctx,o):
        for vardecl in o:
            if ctx.name == vardecl[0]:
                if type(vardecl[1]) == BoolType:
                    return BoolLit(0)
                elif type(vardecl[1]) == IntType:
                    return IntLit(0)
                elif type(vardecl[1]) == FloatType:
                    return FloatLit(0)
                    
        #if ctx.name in o:
        #    return ctx.typ
        #else:
        raise UndeclaredIdentifier(ctx.name)
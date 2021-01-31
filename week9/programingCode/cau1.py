class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,[])
        e2 = self.visit(ctx.e2,[])
        if ctx.op in ['+','-','*']:
            if (type(e1)==BoolLit or type(e2)==BoolLit):
                raise TypeMismatchInExpression(ctx)
            elif(type(e1)==FloatLit or type(e2)==FloatLit):
                return FloatLit(ctx)
            else:
                return IntLit(ctx)
        elif ctx.op in ['/']:
            if (type(e1)==BoolLit or type(e2)==BoolLit):
                raise TypeMismatchInExpression(ctx)
            else:
                return FloatLit(ctx)
        elif ctx.op in ['||','&&']:
            if (type(e1)!=BoolLit or type(e2)!=BoolLit):
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
        elif ctx.op in ['>','<','==','!=']:
            if (type(e1)==type(e2)):
                return BoolLit(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
            

    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e,[])
        if ctx.op == '!':
            if type(e)!=BoolLit:
                raise TypeMismatchInExpression(ctx)
            return BoolLit(ctx)
        elif ctx.op == '-':
            if type(e)==BoolLit:
                raise TypeMismatchInExpression(ctx)
            elif type(e)==FloatLit:
                return FloatLit(ctx)
            else:
                return IntLit(ctx)

    def visitIntLit(self,ctx:IntLit,o): 
        return IntLit(ctx.val)

    def visitFloatLit(self,ctx,o): 
        return FloatLit(ctx.val)

    def visitBoolLit(self,ctx,o): 
        return BoolLit(ctx.val)
from functools import reduce

class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        varList = {}
        a = [self.visit(x,varList) for x in ctx.decl]
        b = [self.visit(x,varList) for x in ctx.stmts]
    def visitVarDecl(self,ctx:VarDecl,o): 
        o[ctx.name] = None
    def visitAssign(self,ctx:Assign,o): 
        lhsName = self.visit(ctx.lhs,o)
        rhsType = self.visit(ctx.rhs,o)
        if o[lhsName] == None and type(rhsType) == type:
            o[lhsName] = rhsType
        elif o[lhsName] == None:
            if o[rhsType] == None:
                raise TypeCannotBeInferred(ctx)
            else:
                o[lhsName]=o[rhsType]
        elif type(rhsType) == type:
            if o[lhsName]!= rhsType:
                raise TypeMismatchInStatement(ctx)
        elif o[lhsName]!=o[rhsType]:
            if o[rhsType] == None:
                raise TypeCannotBeInferred(ctx)
            raise TypeMismatchInStatement(ctx)
    def visitBinOp(self,ctx:BinOp,o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*', '/']:
            if e1==int and e1 ==int:
                return int
            elif type(e1)==str and type(e2)==str:
                if o[e1] in [int,None] and o[e2] in [int,None]:
                    o[e1]=int
                    o[e2]=int
                    return int
                else:
                    raise TypeMismatchInExpression(ctx)
            elif type(e1)==str and e2==int:
                if o[e1] in [None,int]:
                    o[e1]=int
                    return int
                raise TypeMismatchInExpression(ctx)
            elif type(e2)==str and e1==int:
                if o[e2] in [None,int]:
                    o[e2]=int
                    return int
                raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)

        elif ctx.op in ['+.', '-.', '*.', '/.']:
            if e1==float and e1 ==float:
                return float
            elif type(e1)==str and type(e2)==str:
                if o[e1] in [float,None] and o[e2] in [float,None]:
                    o[e1]=float
                    o[e2]=float
                    return float
                else:
                    raise TypeMismatchInExpression(ctx)
            elif type(e1)==str and e2==float:
                if o[e1] in [None,float]:
                    o[e1]=float
                    return float
                raise TypeMismatchInExpression(ctx)
            elif type(e2)==str and e1==float:
                if o[e2] in [None,float]:
                    o[e2]=float
                    return float
                raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)

        elif ctx.op in ['>', '=']:
            if e1==int and e1 ==int:
                return bool
            elif type(e1)==str and type(e2)==str:
                if o[e1] in [int,None] and o[e2] in [int,None]:
                    o[e1]=int
                    o[e2]=int
                    return bool
                else:
                    raise TypeMismatchInExpression(ctx)
            elif type(e1)==str and e2==int:
                if o[e1] in [None,int]:
                    o[e1]=int
                    return bool
                raise TypeMismatchInExpression(ctx)
            elif type(e2)==str and e1==int:
                if o[e2] in [None,int]:
                    o[e2]=int
                    return bool
                raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
        
        elif ctx.op in ['>.', '=.']:
            if e1==float and e1 ==float:
                return bool
            elif type(e1)==str and type(e2)==str:
                if o[e1] in [float,None] and o[e2] in [float,None]:
                    o[e1]=float
                    o[e2]=float
                    return bool
                else:
                    raise TypeMismatchInExpression(ctx)
            elif type(e1)==str and e2==float:
                if o[e1] in [None,float]:
                    o[e1]=float
                    return bool
                raise TypeMismatchInExpression(ctx)
            elif type(e2)==str and e1==float:
                if o[e2] in [None,float]:
                    o[e2]=float
                    return bool
                raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
        
        elif ctx.op in ['&&', '||', '>b', '=b']:
            if e1==bool and e1 ==bool:
                return bool
            elif type(e1)==str and type(e2)==str:
                if o[e1] in [bool,None] and o[e2] in [bool,None]:
                    o[e1]=bool
                    o[e2]=bool
                    return bool
                else:
                    raise TypeMismatchInExpression(ctx)
            elif type(e1)==str and e2==bool:
                if o[e1] in [None,bool]:
                    o[e1]=bool
                    return bool
                raise TypeMismatchInExpression(ctx)
            elif type(e2)==str and e1==bool:
                if o[e2] in [None,bool]:
                    o[e2]=bool
                    return bool
                raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
        
    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e, o)
        if ctx.op == '!':
            if e==bool:
                return bool
            elif type(e)==str:
                if o[e] in [None,bool]:
                    o[e]=bool
                    return bool
                else:
                    raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == '-':
            if e==int:
                return int
            elif type(e)==str:
                if o[e] in [None,int]:
                    o[e]=int
                    return int
                else:
                    raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
          
        elif ctx.op == '-.':
            if e==float:
                return float
            elif type(e)==str:
                if o[e] in [None,float]:
                    o[e]=float
                    return float
                else:
                    raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
     
        elif ctx.op == 'i2f':
            if e==int:
                return float
            elif type(e)==str:
                if o[e] in [None,int]:
                    o[e]=int
                    return float
                else:
                    raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
         
        elif ctx.op == 'floor':
            if e==float:
                return int
            elif type(e)==str:
                if o[e] in [None,float]:
                    o[e]=float
                    return int
                else:
                    raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
          
    def visitIntLit(self,ctx:IntLit,o): 
        return int
    def visitFloatLit(self,ctx,o): 
        return float
    def visitBoolLit(self,ctx,o): 
        return bool
    def visitId(self,ctx,o): 
        if ctx.name in o.keys():
            return ctx.name
        else:
            raise UndeclaredIdentifier(ctx.name)
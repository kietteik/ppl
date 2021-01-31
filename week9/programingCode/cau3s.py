from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = {}
        env = [x.accept(self, o) for x in ctx.decl]
        env2 = [x.accept(self, o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): 
        o[ctx.name] = ctx.name

    def visitAssign(self,ctx:Assign,o):
        rtype = ctx.rhs.accept(self, o)
        ltype = ctx.lhs.accept(self, o)
        if ltype not in ['int', 'float', 'bool']:
            if rtype not in ['int', 'float', 'bool']:
                raise TypeCannotBeInferred(ctx)
            o[ltype] = rtype
            ltype = rtype
        if ltype != rtype:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o):
        ltype = ctx.e1.accept(self, o)
        rtype = ctx.e2.accept(self, o)
        if ctx.op in ['+', '-', '*', '/']:
            if ltype in ['bool', 'float'] or rtype in ['bool', 'float']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'int':
                o[ltype] = 'int'
            if rtype != 'int':
                o[rtype] = 'int'
            return 'int'
            
        elif ctx.op in ['+.', '-.', '*.', '/.']:
            if ltype in ['bool', 'int'] or rtype in ['bool', 'int']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'float':
                o[ltype] = 'float'
            if rtype != 'float':
                o[rtype] = 'float'
            return 'float'
        elif ctx.op in ['>', '=']:
            if ltype in ['bool', 'float'] or rtype in ['bool', 'float']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'int':
                o[ltype] = 'int'
            if rtype != 'int':
                o[rtype] = 'int'
            return 'bool'
        elif ctx.op in ['>.','=.']:
            if ltype in ['bool', 'int'] or rtype in ['bool', 'int']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'float':
                o[ltype] = 'float'
            if rtype != 'float':
                o[rtype] = 'float'
            return 'bool'
        elif ctx.op in ['&&','||','>b','=b']:
            if ltype in ['int', 'float'] or rtype in ['int', 'float']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'bool':
                o[ltype] = 'bool'
            if rtype != 'bool':
                o[rtype] = 'bool'
            return 'bool'
            
    def visitUnOp(self,ctx:UnOp,o):
        exp = ctx.e.accept(self, o)
        if ctx.op == '-':
            if exp in ['float', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'int':
                o[exp] = 'int'
            return 'int'
       	elif ctx.op == '-.':
       	    if exp in ['int', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'float':
                o[exp] = 'float'
            return 'float'
        elif ctx.op == '!':
            if exp in ['float', 'int']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'bool':
                o[exp] = 'bool'
            return 'bool'
       	elif ctx.op == 'i2f':
       	    if exp in ['float', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'int':
                o[exp] = 'int'
            return 'float'  
       	elif ctx.op == 'floor':
       	    if exp in ['int', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'float':
                o[exp] = 'float'
            return 'int' 

    def visitIntLit(self,ctx:IntLit,o):
        return 'int'

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o): 
        return 'bool'

    def visitId(self,ctx,o):
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)
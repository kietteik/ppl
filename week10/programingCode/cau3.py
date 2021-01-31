from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = ({},{})
        env = [x.accept(self, o) for x in ctx.decl]
        env2 = [x.accept(self, o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = o[1][ctx.name] = ctx.name

    #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def visitFuncDecl(self,ctx:FuncDecl,o): 
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        paramList = ({},{})
        env = [x.accept(self, paramList) for x in ctx.param]
        o[0][ctx.name] = dict(enumerate(paramList[1].values()))
        o[1][ctx.name] = dict(enumerate(paramList[1].values()))
        decList = (paramList[0],paramList[1])
        env2 = [x.accept(self, decList) for x in ctx.local]
        scopeVar = ({},{})
        scopeVar[1].update(o[1])
        scopeVar[0].update(decList[0])
        scopeVar[1].update(decList[1])
        env3 = [x.accept(self, scopeVar) for x in ctx.stmts]

        for kp,vp in enumerate(paramList[1].values()):
            for k,v in scopeVar[1].items():
                if vp==k:
                    o[1][ctx.name][kp]=v
        for k,v in scopeVar[1].items():
            if (k in decList[1]) or type(v)==dict:
                continue
            o[1][k]=v

    #name:str,args:List[Exp]
    def visitCallStmt(self,ctx:CallStmt,o):
        if ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
        for i in range(len(ctx.args)):
            arg = ctx.args[i].accept(self, o)
            if o[1][ctx.name][i] not in ['int','float','bool']:
                if arg not in ['int','float','bool']:
                    raise TypeCannotBeInferred(ctx)
                o[1][ctx.name][i] = arg
            elif arg not in ['int','float','bool']:
                o[1][arg] = o[1][ctx.name][i]
            elif arg != o[1][ctx.name][i]:
                raise TypeMismatchInStatement(ctx)
                
    def visitAssign(self,ctx:Assign,o):
        rtype = ctx.rhs.accept(self, o)
        ltype = ctx.lhs.accept(self, o)
        if ltype not in ['int', 'float', 'bool']:
            if rtype not in ['int', 'float', 'bool']:
                raise TypeCannotBeInferred(ctx)
            o[1][ltype] = rtype
        elif rtype not in ['int','float','bool']:
            o[1][rtype] = ltype
        elif ltype != rtype:
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return 'int'

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o): 
        return 'bool'

    def visitId(self,ctx,o):
        if ctx.name in o[1]:
            return o[1][ctx.name]
        raise UndeclaredIdentifier(ctx.name)
#cau 1
    def visitVarDecl(self,ctx,o):
        frame = o.frame
        if frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False, ""))
            return Symbol(ctx.name, ctx.typ, CName(self.className))
        else:
            index = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ctx.name, ctx.typ, frame.getStartLabel(), frame.getEndLabel()))
            return Symbol(ctx.name, ctx.typ, Index(index))
 #cau2
    def visitId(self,ctx,o):
        sym = list(filter(lambda x: x.name.lower() == ctx.name.lower(), o.sym))[0]
        if o.isLeft:
            if type(sym.value) is CName:
                #print(self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name,sym.mtype,o.frame))
                return self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name,sym.mtype,o.frame), sym.mtype #store
            else:
                #print(self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame))
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            if type(sym.value) is CName:
                #print(self.emit.emitGETSTATIC(sym.value.value + "." + sym.name,sym.mtype,o.frame))
                return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name,sym.mtype,o.frame), sym.mtype #load
            else:
                #print(self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame))
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        
 
 #cau3
     def visitAssign(self,ctx,o) :
        rightCode, typeRight = self.visit(ctx.rhs, Access(o.frame, o.sym, False, True))
        leftCode, typeLeft = self.visit(ctx.lhs, Access(o.frame, o.sym, True, False))
        if type(typeLeft) is FloatType and type(typeRight) is IntType:
            self.emit.printout(rightCode + self.emit.emitI2F(o.frame) + leftCode)
        else:
            self.emit.printout(rightCode + leftCode)
        return None,typeRight
        
 #cau4
     def visitIf(self,ctx,o):
        ctxt = o
        frame = o.frame
        expCode, expType = self.visit(ctx.expr, Access(o.frame, o.sym, False, True))
        self.emit.printout(expCode)
        labelF = frame.getNewLabel()
        labelT = frame.getNewLabel() if ctx.estmt else None
    
        self.emit.printout(self.emit.emitIFFALSE(labelF, frame))
        thenStmt = list(map(lambda x: self.visit(x, ctxt), [ctx.tstmt]))
        self.emit.printout(self.emit.emitGOTO(labelT,frame)) if ctx.estmt and (len(thenStmt)==0 or str(thenStmt[-1]) != "Return") else None
        self.emit.printout(self.emit.emitLABEL(labelF, frame))

        elseStmt = []
        if ctx.estmt:
            elseStmt = list(map(lambda x: self.visit(x, ctxt), [ctx.estmt]))
            self.emit.printout(self.emit.emitLABEL(labelT, frame))

        if thenStmt != [] and elseStmt != [] and str(thenStmt[-1]) == "Return" and str(elseStmt[-1]) == "Return":
            return "Return"        
        else:
            return None  
#cau5
    def visitWhile(self, ast, o):
        ctxt = o
        frame = o.frame
        sym = o.sym
        frame.enterLoop()
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        labelStart = frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(labelStart,frame))
        expCode, expType = self.visit(ast.expr, Access(frame, sym, False, True))
        [self.visit(x, ctxt) for x in ast.stmt.stmts]
        self.emit.printout(self.emit.emitLABEL(labelContinue,frame))
        
        self.emit.printout(expCode + self.emit.emitIFTRUE(labelStart, frame) + self.emit.emitLABEL(labelBreak,frame))
        frame.exitLoop()
        return None 
        
#cau6
    def visitFuncDecl(self, ctx, o):
        #import inspect
        #print(inspect.getmembers(Frame, lambda a:not(inspect.isroutine(a))))
        parTypes = [varDecl.typ for varDecl in ctx.param]
        self.emit.printout(self.emit.emitMETHOD(ctx.name, MType(parTypes, ctx.returnType), True))
        
        frame = Frame(ctx.name, ctx.returnType)
        frame.enterScope(True)
        visitedSyms = o.sym[::-1]
        subBody = SubBody(frame, visitedSyms)

        for varDecl in ctx.param:
            sym = self.visit(varDecl, subBody)
            subBody.sym = [sym] + subBody.sym
            
        for decl in ctx.body[0]:
            sym = self.visit(decl, subBody)
            subBody.sym = [sym] + subBody.sym
        
        self.emit.printout(self.emit.emitLABEL(subBody.frame.getStartLabel(), subBody.frame))
        for stmt in ctx.body[1]:
            self.visit(stmt, subBody)
        self.emit.printout(self.emit.emitLABEL(subBody.frame.getEndLabel(), subBody.frame))
        
        frame.exitScope()            
        self.emit.printout(self.emit.emitENDMETHOD(subBody.frame))
        return Symbol(ctx.name, MType([],ctx.returnType), CName(self.className))

 
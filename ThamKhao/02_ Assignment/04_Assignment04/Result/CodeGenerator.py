'''
*   Author: NGUYEN MINH THAM
*   MSSV: 1613166
*	Version: 16:49 30/11/2018 (v2.1)
'''

from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
            Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("putLn", MType([], VoidType()), CName(self.libName))
        ]
    def gen(self, ast, dir_):
        #ast: AST
        # dir_: String => path solution file

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft # expresion is Left in assign statement
        self.isFirst = isFirst


class Val(ABC):
    pass
class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value
    
    def __str__(self):
        return str(self.value)
class CName(Val):
    def __init__(self, value):
        #value: String
        self.value = value
    def __str__(self):
        return str(self.value)

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def callBody(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ""
        merge = list(zip(ctype.partype, ast.param))
        for x in merge:
            str1, typ1 = self.visit(x[1], Access(frame, nenv, False, True))
            if type(x[0]) is FloatType and type(typ1) is IntType:
                str1 += self.emit.emitI2F(frame)
            in_ +=  str1

        return in_ + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), ctype.rettype

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for x in ast.decl:
            if type(x) is VarDecl:
                self.visit(x, SubBody(None, self.env))
            else:
                isMain = x.name.name == "main" and len(x.param) == 0 and type(x.returnType) is VoidType
                intype = [ArrayPointerType(StringType())] if isMain else [self.visit(x.varType,c) for x in x.param]
                self.env.insert(0,Symbol(x.name.name, MType(intype, x.returnType), CName(self.className)))
        list(map(lambda x: self.visit(x, SubBody(None, self.env)) if type(x) is not VarDecl else None, ast.decl))

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), [], [], [], None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c
#----------------------------------------------------------------------------#
#----------------------------Declaration-------------------------------------#

    def visitFuncDecl(self, ast, o):
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym.copy(), frame)
        return None

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        isFunc = (not isMain) and (not isInit)

        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [self.visit(x.varType,o) for x in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)
        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            list(map(lambda x: self.visit(x, SubBody(frame, glenv)), consdecl.local))
        if isFunc:
            list(map(lambda x: self.visit(x, SubBody(frame, glenv)), consdecl.param + consdecl.local))

        # Generate code for statements
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitVarDecl(self, ast, o):
        frame = o.frame
        nenv = o.sym 
        if frame is None:# var declaration in golbal
            nenv.insert(0,Symbol(ast.variable.name, self.visit(ast.varType,o), CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, self.visit(ast.varType, o), False, ""))
        else:# var declaration in function or with statement
            index = frame.getNewIndex()
            nenv.insert(0, Symbol(ast.variable.name, self.visit(ast.varType,o), Index(index))) #chu y varType
            self.emit.printout(self.emit.emitVAR(index, ast.variable.name, self.visit(ast.varType, o), frame.getStartLabel(), frame.getEndLabel(),frame))

#----------------------------------------------------------------------------#
#-----------------------------Statements-------------------------------------#

    def visitAssign(self, ast, o):
        rightCode, typeRight = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        leftCode, typeLeft = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
        if type(typeLeft) is FloatType and type(typeRight) is IntType:
            self.emit.printout(rightCode + self.emit.emitI2F(o.frame) + leftCode)
        else:
            self.emit.printout(rightCode + leftCode)
        return None
    
    def visitWith(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym.copy()
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, SubBody(frame, sym)), ast.decl))
        stmt = list(map(lambda x: self.visit(x, SubBody(frame, sym)), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        return stmt[-1] if stmt != [] else None
        
    def visitReturn(self, ast, o):
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        else:
            rettype = o.frame.returnType
            ecode, etype = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            if type(rettype) is FloatType and type(etype) is IntType:
                self.emit.printout(ecode + self.emit.emitI2F(o.frame) + self.emit.emitRETURN(rettype, o.frame)) 
            else:
                self.emit.printout(ecode + self.emit.emitRETURN(rettype, o.frame))
        return "Return"                

    def visitCallStmt(self, ast, o):
        self.emit.printout(self.callBody(ast, o)[0])
        return None        

    def visitIf(self, ast, o):
        ctxt = o
        frame = o.frame
        expCode, expType = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
        labelF = frame.getNewLabel()
        labelT = frame.getNewLabel() if ast.elseStmt else None
        self.emit.printout(expCode  + self.emit.emitIFFALSE(labelF, frame))
        thenStmt = list(map(lambda x: self.visit(x, ctxt), ast.thenStmt))
        self.emit.printout(self.emit.emitGOTO(labelT,frame)) if ast.elseStmt and (len(thenStmt)==0 or str(thenStmt[-1]) != "Return") else None
        self.emit.printout(self.emit.emitLABEL(labelF, frame))

        elseStmt = []
        if ast.elseStmt:
            elseStmt = list(map(lambda x: self.visit(x, ctxt), ast.elseStmt))
            self.emit.printout(self.emit.emitLABEL(labelT, frame))

        if thenStmt != [] and elseStmt != [] and str(thenStmt[-1]) == "Return" and str(elseStmt[-1]) == "Return":
            return "Return"        
        else:
            return None    
    
    def visitFor(self, ast, o):
        ctxt = o
        frame = o.frame
        sym = o.sym
        frame.enterLoop()

        labelCondition = frame.getNewLabel()
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()

        exp1Code, exp1Type = self.visit(ast.expr1, Access(frame, sym, False))
        idLCode, idLType = self.visit(ast.id, Access(frame, sym, True))
        self.emit.printout(exp1Code + idLCode + self.emit.emitLABEL(labelCondition, frame))

        idRCode, idRType = self.visit(ast.id, Access(frame, sym, False))
        exp2Code, exp2Type = self.visit(ast.expr2, Access(frame, sym, False))
        compare = self.emit.emitIFICMPGT(labelBreak, frame) if str(ast.up) == "True" else self.emit.emitIFICMPLT(labelBreak, frame) #true: to <= -> >
        self.emit.printout(idRCode + exp2Code + compare)
        list(map(lambda x: self.visit(x, Access(frame, sym, False)), ast.loop))

        self.emit.printout(self.emit.emitLABEL(labelContinue, frame))
        byOne = idRCode + self.emit.emitPUSHCONST(1, IntType(), o.frame) + self.emit.emitADDOP("+" if str(ast.up) == "True" else "-", IntType(), frame) + idLCode
        self.emit.printout(byOne + self.emit.emitGOTO(labelCondition, frame) + self.emit.emitLABEL(labelBreak, frame))

        frame.exitLoop()
        return None        
    
    def visitWhile(self, ast, o):
        ctxt = o
        frame = o.frame
        sym = o.sym
        frame.enterLoop()

        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        expCode, expType = self.visit(ast.exp, Access(frame, sym, False, True))
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame) + expCode + self.emit.emitIFFALSE(labelBreak, frame))
        list(map(lambda x: self.visit(x, ctxt), ast.sl))
        self.emit.printout(self.emit.emitGOTO(labelContinue,frame) + self.emit.emitLABEL(labelBreak, frame))
        frame.exitLoop()
        return None        

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
        return None        
    
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        return None        

#----------------------------------------------------------------------------#
#-----------------------------Expression-------------------------------------#

    def visitCallExpr(self, ast, o):
        return self.callBody(ast, o)

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        leftCode, typeLeft = self.visit(ast.left, Access(frame, nenv, False, True))
        rightCode, typeRight = self.visit(ast.right, Access(frame, nenv, False, True))
        if type(typeLeft) != type(typeRight):
            if type(typeLeft) is IntType:
                leftCode += self.emit.emitI2F(frame)
                typeLeft = FloatType()
            elif type(typeRight) is IntType:
                rightCode += self.emit.emitI2F(frame)
                typeRight = FloatType()
        if ast.op in ['+','-','*', '/']:
            if type(typeLeft) is IntType and type(typeRight) is IntType and ast.op == '/':
                op_str = leftCode + self.emit.emitI2F(frame) + rightCode + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame)
                resType = FloatType()
            else:
                op_str = leftCode + rightCode
                op_str +=  self.emit.emitADDOP(ast.op, typeLeft, frame) if ast.op in ['+','-'] else self.emit.emitMULOP(ast.op, typeLeft, frame)
                resType = typeLeft
        elif ast.op.lower() in ['div','mod']:
            op_str = leftCode + rightCode
            op_str +=  self.emit.emitDIV(frame) if ast.op.lower() =='div' else self.emit.emitMOD(frame)
            resType = IntType()
        elif ast.op.lower() in ['and','or']:
            op_str = leftCode + rightCode 
            op_str +=  self.emit.emitANDOP(frame) if ast.op.lower() =='and' else self.emit.emitOROP(frame)
            resType = BoolType()
        elif ast.op in ['=', '<>', '<', '<=', '>', '>='] :
            op_str = leftCode + rightCode +  self.emit.emitREOP(ast.op.lower(), typeLeft, frame)
            resType = BoolType()
        elif ast.op.lower() in ['andthen','orelse']:
            labelCondition = frame.getNewLabel()
            labelExit = frame.getNewLabel()
            if ast.op.lower() == "andthen":
                op_str = leftCode + self.emit.emitIFFALSE(labelCondition, frame) + rightCode + self.emit.emitIFFALSE(labelCondition, frame)
                op_str += self.emit.emitPUSHICONST(1, frame) +  self.emit.emitGOTO(labelExit, frame) 
                op_str += self.emit.emitLABEL(labelCondition, frame) + self.emit.emitPUSHICONST(0, frame) + self.emit.emitLABEL(labelExit, frame) 
            else:
                op_str = leftCode + self.emit.emitIFTRUE(labelCondition, frame) + rightCode + self.emit.emitIFTRUE(labelCondition, frame)
                op_str += self.emit.emitPUSHICONST(0, frame) +  self.emit.emitGOTO(labelExit, frame) 
                op_str += self.emit.emitLABEL(labelCondition, frame) + self.emit.emitPUSHICONST(1, frame) + self.emit.emitLABEL(labelExit, frame)                
            resType = BoolType()
            
        return op_str, resType

    def visitUnaryOp(self, ast, o):
        expCode, expType = self.visit(ast.body, Access(o.frame, o.sym, False, True))
        if ast.op.lower() == "not":
            op_str = expCode + self.emit.emitNOT(expType, o.frame)
        else:
            op_str = expCode + self.emit.emitNEGOP(expType, o.frame)
        return op_str ,expType
    
    def visitId(self, ast, o):
        sym = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())
        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name,sym.mtype,o.frame), sym.mtype #store
            else:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name,sym.mtype,o.frame), sym.mtype #load
            else:
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
    
#----------------------------------------------------------------------------#
#-----------------------------Literal----------------------------------------#

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, IntType(), o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, FloatType(), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame), BoolType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

#----------------------------------------------------------------------------#  
#--------------------------------Type----------------------------------------#

    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitArrayType(self, ast, o):
        return ArrayPointerType(self.visit(ast.eleType,o))
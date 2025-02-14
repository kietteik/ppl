'''
*   Author: NGUYEN MINH THAM
*   MSSV: 1613166
*	Version: 16:49 30/11/2018 (v2.1)
'''

from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from CodeGenError import *


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is cgen.StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is BoolType:
            return "Z"            
        elif typeIn is cgen.ArrayPointerType:
            return "[" + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType:
            return "L" + inType.cname + ";"

    def getFullType(inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is cgen.StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is FloatType:
            return "float"
#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------LOAD & SOTRE INSTRUCTIONS---------------------------------------------------#
    ''' 
    *    generate code to push a constant onto the operand stack.
    *       @param in the lexeme of the constant
    *       @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        #in_: String
        #typ: Type
        #frame: Frame
        
        if type(typ) is IntType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is BoolType:
            return self.emitPUSHICONST(str(in_), frame)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(str(in_),frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC("\"" + in_ + "\"")
        else:
            raise IllegalOperandException(in_)

    def emitPUSHICONST(self, in_, frame):
        #in: Int or Sring
        #frame: Frame
        
        frame.push();
        if type(in_) is int:                    # INTEGER
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(str(i))                
        elif type(in_) is str:                  # BOOLEAN
            if in_.lower() == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_.lower() == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame): #chu y phep cong khong chinh xac
        #in_: String
        #frame: Frame

        frame.push()
        f = float(in_)
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)           
    #---------------------------------------------------------------------#

    ''' 
    *    generate code to push a local variable onto the operand stack.
    '''
    def emitALOAD(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()            
        elif type(in_) in [cgen.ArrayPointerType, cgen.ClassType, StringType]:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitREADVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #... -> ..., value
        
        frame.push()
        if type(inType) in [IntType, BoolType]:
            return self.jvm.emitILOAD(index)
        if type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)            
        elif type(inType) in [cgen.ArrayPointerType, cgen.ClassType, StringType]:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)
    #---------------------------------------------------------------------#

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    '''
    def emitASTORE(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop() # array address
        frame.pop() # index array
        frame.pop() # value
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) in [cgen.ArrayPointerType, cgen.ClassType, StringType]:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    def emitWRITEVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #..., value -> ...
        
        frame.pop()
        if type(inType) in [IntType, BoolType]:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)                 
        elif type(inType) in [cgen.ArrayPointerType, cgen.ClassType, StringType]:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------ARITHMETIC INSTRUCTIONS-----------------------------------------------------#
    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        #in_: Type
        #frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    def emitANDOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    def emitOROP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        #op: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        compareF = self.jvm.emitFCMPL()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(labelF) if type(in_) is IntType else compareF + self.jvm.emitIFLE(labelF)) # <=
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(labelF) if type(in_) is IntType else compareF + self.jvm.emitIFLT(labelF)) # >
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(labelF) if type(in_) is IntType else compareF + self.jvm.emitIFGE(labelF)) # >=
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(labelF) if type(in_) is IntType else compareF + self.jvm.emitIFGT(labelF)) # >
        elif op == "<>":
            result.append(self.jvm.emitIFICMPEQ(labelF) if type(in_) is IntType else compareF + self.jvm.emitIFEQ(labelF)) # =
        elif op == "=": 
            result.append(self.jvm.emitIFICMPNE(labelF) if type(in_) is IntType else compareF + self.jvm.emitIFNE(labelF)) # <>
            
        result.append(self.emitPUSHCONST("1", IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------CONTROL TRANFER INSTRUCTIONS------------------------------------------------#

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFEQ(label)

    def emitIFICMPGT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)    

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitGOTO(str(label))

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------TYPE CONVERSION INSTRUCTIONS------------------------------------------------#
    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        #frame: Frame

        return self.jvm.emitI2F()

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------OPERAND STACK MANAGEMENT INSTRUCTIONS---------------------------------------#
    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''
    def emitDUP(self, frame):
        #frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------OPJECT CREATION AND MANIPULATION INSTRUCTIONS-------------------------------#

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------FIELD INSTRUCTIONS----------------------------------------------------------#
    def emitGETSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))#load

    def emitPUTSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))#store 

    def emitGETFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------METHOD INVOCATION INSTRUCTIONS----------------------------------------------#
    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        #lexeme: String
        #in_: Type
        #frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))       

#-----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------JASMIN DIRECTIVES-----------------------------------------------------------#

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''
    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        #lexeme: String
        #in_: Type
        #isStatic: Boolean
        #frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        #frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''
    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        #in_: Int
        #varName: String
        #inType: Type
        #fromLabel: Int
        #toLabel: Int
        #frame: Frame
        
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitATTRIBUTE(self, lexeme, in_, isFinal, value):
        #lexeme: String
        #in_: Type
        #isFinal: Boolean
        #value: String

        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), False)        

    def emitPROLOG(self, name, parent):
        #name: String
        #parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        #num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        #num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

#-----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------OTHERS---------------------------------------------------------------------#
    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''
    def emitRETURN(self, in_, frame):
        #in_: Type
        #frame: Frame

        if type(in_) in [IntType, BoolType]:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()                       
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        else:
            frame.pop()
            return self.jvm.emitARETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitLABEL(label)

    def getConst(self, ast):
        #ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())


    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        #in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()










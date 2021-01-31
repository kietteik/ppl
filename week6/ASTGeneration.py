from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    # def visitProgram(self,ctx:BKITParser.ProgramContext):
    #     return Program([VarDecl(Id(ctx.ID().getText()),[],None)])

    # program: listVarDeclar listFuncDeclar EOF;
    # This function return Program object
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        listVarDeclar = self.visit(ctx.listVarDeclar())
        listFuncDeclar = self.visit(ctx.listFuncDeclar())

        return Program(listVarDeclar + listFuncDeclar)


    # listVarDeclar: noNullListVarDeclar | ;
    # This function return a list
    def visitListVarDeclar(self, ctx:BKITParser.ListVarDeclarContext):
        if(ctx.noNullListVarDeclar()):
            return self.visit(ctx.noNullListVarDeclar())

        return []


    # listFuncDeclar: noNullListFuncDeclar | ;
    # This function return a list
    def visitListFuncDeclar(self, ctx:BKITParser.ListFuncDeclarContext):
        if(ctx.noNullListFuncDeclar()):
            return self.visit(ctx.noNullListFuncDeclar())

        return []

    # noNullListVarDeclar: vardeclara noNullListVarDeclar | vardeclara;
    # This function return a list
    # vardeclara is already a list
    def visitNoNullListVarDeclar(self, ctx:BKITParser.NoNullListVarDeclarContext):
        vardeclara = self.visit(ctx.vardeclara())

        if(ctx.noNullListVarDeclar()):
            return vardeclara + self.visit(ctx.noNullListVarDeclar())

        return vardeclara


    # noNullListFuncDeclar: funcdeclara noNullListFuncDeclar | funcdeclara;
    # This function return a list
    # funcdeclare is already a list
    def visitNoNullListFuncDeclar(self, ctx:BKITParser.NoNullListFuncDeclarContext):
        funcdeclara = self.visit(ctx.funcdeclara())

        if(ctx.noNullListFuncDeclar()):
            return [funcdeclara] + self.visit(ctx.noNullListFuncDeclar())

        return [funcdeclara]


    # vardeclara: KEY_VAR CL listvar SM;
    # this function return a list of VarDecl object
    # call self.visit(ctx.listvar()) to get the list of varDecl object
    def visitVardeclara(self, ctx:BKITParser.VardeclaraContext):
        return self.visit(ctx.listvar())


    # listvar: var CM listvar | var;
    # this function return a list of VarDecl object
    def visitListvar(self, ctx:BKITParser.ListvarContext):
        var = self.visit(ctx.var())
        if(ctx.listvar()):
            return [var] + self.visit(ctx.listvar())

        return [var]


    # var: nonInitVar | initVar;
    # this function return a VarDecl object
    def visitVar(self, ctx:BKITParser.VarContext):
        if(ctx.nonInitVar()):
            return self.visit(ctx.nonInitVar())
        
        return self.visit(ctx.initVar())


    # nonInitVar: ID | varArrayIdentifier;
    # this function return a VarDecl object
    def visitNonInitVar(self, ctx:BKITParser.NonInitVarContext):
        if(ctx.ID()):
            return VarDecl(Id(ctx.ID().getText()), [], None)
        
        identifier, listIndex = self.visit(ctx.varArrayIdentifier())

        return VarDecl(identifier, listIndex, None)


    # initVar: ID ASSIGN literal | varArrayIdentifier ASSIGN literal;
    # this function return a VarDecl object
    def visitInitVar(self, ctx:BKITParser.InitVarContext):
        if(ctx.ID()):
            return VarDecl(Id(ctx.ID().getText()), [], self.visit(ctx.literal()))

        identifier, listIndex = self.visit(ctx.varArrayIdentifier())
        return VarDecl(identifier, listIndex, self.visit(ctx.literal()))


    # varArrayIdentifier: ID var_index_operators;
    # this function return a tuple (ID, list[int])
    def visitVarArrayIdentifier(self, ctx:BKITParser.VarArrayIdentifierContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.var_index_operators()))
        # return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.var_index_operators()), None)


    # var_index_operators: LSB INTLIT RSB| LSB INTLIT RSB var_index_operators;
    # this function return a list of index operators, which type is List[int]
    def visitVar_index_operators(self, ctx:BKITParser.Var_index_operatorsContext):
        intlit = int(ctx.INTLIT().getText(), 0)
        if(ctx.var_index_operators()):
            return [intlit] + self.visit(ctx.var_index_operators())

        return [intlit]


    # literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
    # this function return a literal
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        child = ctx.getChild(0).getText()
        if(ctx.INTLIT()):
            return IntLiteral(int(child, 0)) 
    
        if(ctx.FLOATLIT()):
            return FloatLiteral(float(child)) 
            # return FloatLiteral(float(ctx.FLOATLIT().getText())) 

        if(ctx.BOOLLIT()):
            return BooleanLiteral(child == 'True') 
            # return BooleanLiteral(ctx.BOOLLIT().getText() == 'True') 

        return StringLiteral(child)
        # return StringLiteral(ctx.STRINGLIT())
    

    # funcdeclara: KEY_FUNCTION CL ID KEY_PARAMETER CL listparam funcbody | KEY_FUNCTION CL ID funcbody;
    # this function return a FuncDecl object
    def visitFuncdeclara(self, ctx:BKITParser.FuncdeclaraContext):
        if(ctx.listparam()):
            return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.listparam()), self.visit(ctx.funcbody()))
    
        return FuncDecl(Id(ctx.ID().getText()), [], self.visit(ctx.funcbody()))


    # listparam: param CM listparam | param;
    # this function return a list of VarDecl object
    def visitListparam(self, ctx:BKITParser.ListparamContext):
        param = self.visit(ctx.param())

        if(ctx.listparam()):
            return [param] + self.visit(ctx.listparam())

        return [param]

    # param: ID | varArrayIdentifier;
    # this function return a VarDecl object
    def visitParam(self, ctx:BKITParser.ParamContext):
        if(ctx.ID()):
            return VarDecl(Id(ctx.ID().getText()), [], None)

        identifier, listIndex = self.visit(ctx.varArrayIdentifier())
        return VarDecl(identifier, listIndex, None)

    # funcbody
    #  : KEY_BODY CL listStatement KEY_ENDBODY DOT
    #  ;
    def visitFuncbody(self, ctx:BKITParser.FuncbodyContext):
        return self.visit(ctx.listStatement())

    # listStatement
    #  : listVarDeclar listOtherStatements
    #  ;
    def visitListStatement(self, ctx:BKITParser.ListStatementContext):
        return (self.visit(ctx.listVarDeclar()), self.visit(ctx.listOtherStatements()))

    # listOtherStatements
    # : noNullListOtherStatements
    # | 
    # ;
    def visitListOtherStatements(self, ctx:BKITParser.ListOtherStatementsContext):
        if(ctx.noNullListOtherStatements()):
            return self.visit(ctx.noNullListOtherStatements())

        return []


    # noNullListOtherStatements
    #  : statement noNullListOtherStatements
    #  | statement
    #  ;
    def visitNoNullListOtherStatements(self, ctx:BKITParser.NoNullListOtherStatementsContext):
        statement = self.visit(ctx.statement())

        if(ctx.noNullListOtherStatements()):
            return [statement] + self.visit(ctx.noNullListOtherStatements())

        return [statement]


    # variable
    #  : ID
    #  | element_exp
    #  ;
    # this function return a Id or a ArrayCell
    def visitVariable(self, ctx:BKITParser.VariableContext):
        if(ctx.ID()):
            return Id(ctx.ID().getText())

        return self.visit(ctx.element_exp())


    # statement
    #  : assigment
    #  | if_statement
    #  | for_statement
    #  | while_statement
    #  | do_while_statement
    #  | break_statement
    #  | continue_statement
    #  | call_statement
    #  | return_statement
    #  ;
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # assigment
    # : variable ASSIGN exp SM
    # ;
    # this function return a Assign object
    def visitAssigment(self, ctx:BKITParser.AssigmentContext):
        return Assign(self.visit(ctx.variable()), self.visit(ctx.exp()))


    # if_statement
    #  : KEY_IF exp KEY_THEN listStatement (KEY_ELSEIF exp KEY_THEN listStatement)* (KEY_ELSE listStatement)? KEY_ENDIF DOT
    #  ;
    # this function return a If object
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        exp = ctx.exp(); # list exp
        listStatement = ctx.listStatement(); # list listStatement

        if(ctx.KEY_ELSE()):
            listExpStatements = list(zip(exp,listStatement[:-1]))
            ifthenStmt = [(self.visit(i[0]), *self.visit(i[1])) for i in listExpStatements]
            elseStmt = self.visit(listStatement[-1])
            return If(ifthenStmt, elseStmt)

        listExpStatements = list(zip(exp,listStatement))
        ifthenStmt = [(self.visit(i[0]), *self.visit(i[1])) for i in listExpStatements]
        elseStmt = ([],[]) 

        return If(ifthenStmt, elseStmt)


    # for_statement
    #  : KEY_FOR LP ID ASSIGN exp CM exp CM ID ASSIGN exp RP KEY_DO listStatement KEY_ENDFOR DOT
    #  ;
    # this function return a For object
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return For(
            Id(ctx.ID(0).getText()),
            self.visit(ctx.exp(0)),
            self.visit(ctx.exp(1)),
            Id(ctx.ID(1).getText()),
            self.visit(ctx.exp(2)),
            self.visit(ctx.listStatement())
        )


    # while_statement
    #  : KEY_WHILE exp KEY_DO listStatement KEY_ENDWHILE DOT
    #  ;
    # this function return a While object
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return While(self.visit(ctx.exp()), self.visit(ctx.listStatement()))


    # do_while_statement
    #  : KEY_DO listStatement KEY_WHILE exp SM
    #  ;
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return Dowhile(self.visit(ctx.listStatement()), self.visit(ctx.exp()))


    # break_statement
    #  : KEY_BREAK SM
    #  ;
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return Break()


    # continue_statement
    #  : KEY_CONTINUE SM
    #  ;
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return Continue()


    # call_statement
    # : func_call SM
    # ;
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        func_call = self.visit(ctx.func_call())
        return CallStmt(*func_call)


    # return_statement
    #  : KEY_RETURN exp SM
    #  | KEY_RETURN SM
    #  ;
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        if(ctx.exp()):
            return Return(self.visit(ctx.exp()))

        return Return(None)



    # exp
    #  : exp EQUAL exp1
    #  | exp NOTEQUAL exp1
    #  | exp LESS exp1
    #  | exp GREATER exp1
    #  | exp LESSEQUAL exp1
    #  | exp GREATEREQUAL exp1
    #  | exp FNOTEQUAL exp1
    #  | exp FLESS exp1
    #  | exp FGREATER exp1
    #  | exp FLESSEQUAL exp1
    #  | exp FGREATEREQUAL exp1
    #  | exp1
    #  ;
    def visitExp(self, ctx:BKITParser.ExpContext):
        if(ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp()), self.visit(ctx.exp1()))

        return self.visit(ctx.exp1())


    # exp1
    #  : exp1 AND exp2
    #  | exp1 OR exp2
    #  | exp2
    #  ;
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        if(ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp1()), self.visit(ctx.exp2()))

        return self.visit(ctx.exp2())


    # exp2
    #  : exp2 ADD exp3
    #  | exp2 FADD exp3
    #  | exp2 SUB exp3
    #  | exp2 FSUB exp3
    #  | exp3
    #  ;
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if(ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))

        return self.visit(ctx.exp3())


    # exp3
    #  : exp3 MUL exp4
    #  | exp3 FMUL exp4
    #  | exp3 DIV exp4
    #  | exp3 FDIV exp4
    #  | exp3 MOD exp4
    #  | exp4
    #  ;
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        if(ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))

        return self.visit(ctx.exp4())


    # exp4
    #  : NOT exp5
    #  | exp5
    #  ;
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if(ctx.NOT()):
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))

        return self.visit(ctx.exp5())


    # exp5
    #  : SUB exp6
    #  | FSUB exp6
    #  | exp6
    #  ;
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if(ctx.getChildCount() == 2):
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))

        return self.visit(ctx.exp6())


    # exp6
    #  : literal
    #  | LP exp RP
    #  | ID
    #  | element_exp
    #  | func_call
    #  ;
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        if(ctx.literal()):
            return self.visit(ctx.literal())

        if(ctx.exp()):
            return self.visit(ctx.exp())

        if(ctx.ID()):
            return Id(ctx.ID().getText())

        if(ctx.element_exp()):
            return self.visit(ctx.element_exp())

        if(ctx.func_call()):
            func_call = self.visit(ctx.func_call())
            return CallExpr(*func_call)


    # element_exp
    #  :  ID index_operators
    #  ;
    # this function return a ArrayCell
    def visitElement_exp(self, ctx:BKITParser.Element_expContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))


    # index_operators
    #  : LSB exp RSB
    #  | LSB exp RSB index_operators
    #  ;
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        exp = self.visit(ctx.exp())
        if(ctx.index_operators()):
            return [exp] + self.visit(ctx.index_operators())

        return [exp]


    # func_call
    #  : ID LP listExp RP
    #  ;
    # this function return a CallStmt object
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.listExp()))


    # listExp
    #  : noNullListExp
    #  |
    #  ;
    def visitListExp(self, ctx:BKITParser.ListExpContext):
        if(ctx.noNullListExp()):
            return self.visit(ctx.noNullListExp())

        return []

    # noNullListExp
    #  : exp CM noNullListExp
    #  | exp
    #  ;
    def visitNoNullListExp(self, ctx:BKITParser.NoNullListExpContext):
        exp = self.visit(ctx.exp())

        if(ctx.noNullListExp()):
            return [exp] + self.visit(ctx.noNullListExp())

        return [exp]

    


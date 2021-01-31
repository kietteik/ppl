from abc import ABC, abstractmethod, ABCMeta

# program: vardecls EOF;

# vardecls: vardecl vardecltail;

# vardecltail: vardecl vardecltail | ;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID ',' ids | ID;

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;


# class Program():  # decl:list(VarDecl)
#     def __init__(self, decl: list):
#         self.decl = decl

#     def __str__(self):
#         result = ''
#         for i in self.decl:
#             result += str(i)
#         return result


class Type(ABC):
    pass


class IntType(Type):

    def __str__(self):
        return 'IntType'


class FloatType(Type):
    def __str__(self):
        return 'FloatType'


class Id:  # name:str
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return 'Id(' + self.name+')'


class VarDecl:  # variable:Id; varType: Type
    def __init__(self, variable: Id, varType: Type):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return 'VarDecl('+str(self.variable) + ',' + str(self.varType) + ')'
    # Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if (ctx.vardecl()):
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return []

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        mptype = self.visit(ctx.mptype())
        return [VarDecl(x, mptype) for x in self.visit(ctx.ids())]

    def visitMptype(self, ctx: MPParser.MptypeContext):

        if (ctx.INTTYPE()):
            return IntType()
        else:
            return FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        if (ctx.ids()):
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        return [Id(ctx.ID().getText())]


b = [VarDecl(Id('a'), IntType()), VarDecl(Id('a'), IntType())]
# a = Program(b)
print(b)

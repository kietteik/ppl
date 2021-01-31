from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        #return Program([self.visit(x) for x in ctx.decl()])                # đổi node x trên parse trên thành node trên cây ast, câu lệnh có nghĩa là cho mỗi node x trên cây parse tree, ta sẽ đổi thành node ast
        return Program(list(map(self.visit,ctx.decl())))                    # for x in cxt.decl() -> trả về danh sách các node trên cây parse tree
                                                                            # Nhiệm vụ 1: đổi thành map
                                                                            # Nhiệm vụ 2: chuyển list của list thành list trên python, chỉ dùng 1 dòng lệnh. Ví dụ: [[1,2,3],[4,5]] sẽ trả về [1,2,3,4,5](flatten in python)
                                                                            # chú ý: map() duyệt từng phần tử trong list, còn nếu list(map) thì chạy hết các phần tử              
    def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt,
                        self.visit(ctx.mtype()))

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt)

    def visitBody(self,ctx:MPParser.BodyContext):
        return [],[self.visit(x) for x in ctx.stmt()]
  
    def visitStmt(self,ctx:MPParser.StmtContext):
        return self.visit(ctx.funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MPParser.ExpContext):
        return IntLiteral(int(ctx.INTLIT().getText()))

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return IntType()


class Count(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return reduce(lambda x,y: x + self.visit(y),ctx.decl(),2)

    def visitDecl(self,ctx:MPParser.DeclContext):
        if (ctx.funcdecl() is None):
            return 1 + self.visit(ctx.procdecl())
        else:
            return 1 + self.visit(ctx.funcdecl())

    def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
        return 7 + self.visit(ctx.mtype()) + self.visit(ctx.body())

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        return 6 + self.visit(ctx.body())

    def visitStmt(self,ctx:MPParser.StmtContext):
        return 2 + self.visit(ctx.funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        if  (ctx.getChildCount()==4):
            return 4 + self.visit(ctx.exp())
        else:
            return 4

    def visitBody(self,ctx:MPParser.BodyContext):
        if  (ctx.getChildCount()==3):
            return 3 + self.visit(ctx.stmt())
        else:
            return 3

    def visitExp(self,ctx:MPParser.ExpContext):
        return 2

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return 2
 

from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):
    
    def visit(self,ast,param):
        return ast.accept(self,param)

    @abstractmethod
    def visitAddOp(self, param):
        pass

    @abstractmethod
    def visitMinusOp(self, param):
        pass

    @abstractmethod
    def visitMulOp(self, param):
        pass

    @abstractmethod
    def visitDivOp(self, param):
        pass




    @abstractmethod
    def visitId(self, param):
        pass

    @abstractmethod
    def visitIntLiteral(self, param):
        pass

    @abstractmethod
    def visitBooleanLiteral(self, param):
        pass

        
class BaseVisitor(Visitor):
    

    def visitAddOp(self, param):
        return None

    def visitMinusOp(self, param):
        return None

    def visitMulOp(self, param):
        return None

    def visitDivOp(self, param):
        return None





    def visitId(self, param):
        return None

    def visitIntLiteral(self, param):
        return None

    def visitBooleanLiteral(self, param):
        return None
 
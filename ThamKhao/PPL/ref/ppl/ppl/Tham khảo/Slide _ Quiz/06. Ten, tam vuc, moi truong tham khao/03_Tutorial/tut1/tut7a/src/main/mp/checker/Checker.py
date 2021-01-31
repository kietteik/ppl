from AST import * 
from Visitor import BaseVisitor
from Utils import Utils
from collections import Counter

class RedeclaredVariable(Exception):
    def __init__(self,lst,message):
        self.lst =lst
        self.message =  message

class Checker(BaseVisitor):

    # #..................Question 1..................
    # def visitProgram(self,ast,param):
    #     return [x for x in ast.decl if isinstance(x,VarDecl)]

    #..................Question 2..................
    def visitProgram(self,ast,param):
        lstVar =  [str(x) for x in ast.decl if isinstance(x,VarDecl)]
        counter_lstVar=Counter(lstVar)
        duplicateVar =  list(filter(lambda elemLst:counter_lstVar[elemLst] > 1,lstVar))
        if duplicateVar != []:
            raise RedeclaredVariable(lstVar,duplicateVar )
        return lstVar 

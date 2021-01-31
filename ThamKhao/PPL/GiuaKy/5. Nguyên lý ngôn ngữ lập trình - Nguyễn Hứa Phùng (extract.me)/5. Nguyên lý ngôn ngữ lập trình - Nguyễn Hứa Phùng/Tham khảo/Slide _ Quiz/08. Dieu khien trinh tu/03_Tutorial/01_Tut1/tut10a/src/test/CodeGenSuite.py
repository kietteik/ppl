import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([],[
    			CallExpr(Id("putFloat"),[FloatLiteral(5.0)])]))])
    	expect = "5.0"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_int_int(self):
        """Simple program: int main() {} """
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([],[
                CallExpr(Id("putInt"),[BinaryOp('+',IntLiteral(5),IntLiteral(5))])]))])
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_int_int(self):
        """Simple program: int main() {} """
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([],[
                CallExpr(Id("putFloat"),[BinaryOp('+',FloatLiteral(5.0),FloatLiteral(5.0))])]))])
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """void main() {putFloat(10.0);}"""
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

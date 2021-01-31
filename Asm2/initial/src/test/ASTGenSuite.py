import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int x;float y;"""
    #     expect = Program([VarDecl(Id("x"), IntType()),
    #                       VarDecl(Id("y"), FloatType())])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 300))
    def test_simple_program_1(self):
        """Simple program: int main() {} """
        input = """a := b := 4"""
        expect = Binary(':=', Id('a'), Binary(':=', Id('b'), IntLiteral(4)))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))
    def test_simple_program_1(self):
        """Simple program: int main() {} """
        input = """a and b or 4"""
        expect = Binary(':=', Id('a'), Binary(':=', Id('b'), IntLiteral(4)))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

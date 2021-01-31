import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_check_type1(self):
        """Simple program: int main() {} """
        input = Program(
            [
                VarDecl(Id("b"), ArrayType(1,3,IntType())),
                VarDecl(Id("b"), ArrayType(-1,3,IntType()))
            ])
        expect = "False"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_check_type2(self):
        """Simple program: int main() {} """
        input = Program(
            [
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])
            ])
        expect = "False"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_check_type3(self):
        """Simple program: int main() {} """
        input = Program(
            [
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType())], [], []),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])
            ])
        expect = "False"
        self.assertTrue(TestChecker.test(input,expect,402))    

    def test_check_type4(self):
        """Simple program: int main() {} """
        input = Program(
            [
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])
            ])
        expect = "True"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_check_type5(self):
        """Simple program: int main() {} """
        input = Program(
            [
                FuncDecl(Id("main"), [VarDecl(Id("m"), IntType()),VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])
            ])
        expect = "False"
        self.assertTrue(TestChecker.test(input,expect,404))
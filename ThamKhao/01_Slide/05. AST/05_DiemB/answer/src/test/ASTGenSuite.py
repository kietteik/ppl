import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """a - b + 4 + 6"""
        expect = str(
            Add( 
                Add(
                    Minus(
                        Id("a"),
                        Id("b")
                        ), 
                    IntLiteral(4) 
                    ),
                IntLiteral(6)
                )
        )
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
        """Simple program: int main() {} """
        input = """a - b"""
        expect = str(
                    Minus(
                        Id("a"),
                        Id("b")
                        )
                )
        self.assertTrue(TestAST.test(input,expect,301))

    def test_3(self):
        """Simple program: int main() {} """
        input = """a * b"""
        expect = str(
                    Mul(
                        Id("a"),
                        Id("b")
                        )
                )
        self.assertTrue(TestAST.test(input,expect,302))

    def test_4(self):
        """Simple program: int main() {} """
        input = """a * b * c / 5"""
        expect = str(
                    Div(
                        Mul(
                            Mul(
                                Id("a"),
                                Id("b")
                                ),
                            Id("c")
                            ),
                        IntLiteral(5)
                        )
                )
        self.assertTrue(TestAST.test(input,expect,303))


    def test_5(self):
        """Simple program: int main() {} """
        input = """a * 2 - b * 3 + 2 - c / 5 + 34 - 123"""
        expect = str(
                    Minus(
                        Add(
                            Minus(
                                Add(
                                    Minus(
                                        Mul(
                                            Id("a"),
                                            IntLiteral(2)
                                            ),
                                        Mul(
                                            Id("b"),
                                            IntLiteral(3)
                                            )
                                        ),
                                    IntLiteral(2)
                                    ),
                                Div(
                                    Id("c"),
                                    IntLiteral(5)
                                    )
                                ),
                            IntLiteral(34)
                            ),
                        IntLiteral(123)
                        )
                )
        self.assertTrue(TestAST.test(input,expect,304))
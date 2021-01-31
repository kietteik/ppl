import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_global_var1(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                VarDecl(Id("b"), IntType()),
                VarDecl(Id("z"), StringType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])# procedure

            ])
        expect = '[Symbol(a,FloatType),Symbol(b,IntType),Symbol(z,StringType),Symbol(main,MType([StringType,IntType],VoidType()))]'
        self.assertTrue(TestChecker.test(input, expect, 300))

    def test_redecl_vardecl(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),# procedure
                VarDecl(Id("a"), IntType()),
            ])
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 301))

    def test_redecl_func(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])

            ])
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 302))

    def test_redecl_proce(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main"), [VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main1s"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
            ])
        expect = 'Redeclared Procedure: main'
        self.assertTrue(TestChecker.test(input, expect, 303))
import unittest
from TestUtils import TestChecker
from StaticCheck import *
from AST import *


class CheckerSuite(unittest.TestCase):


    def test_redecl_vardecl(self):
        input = Program(
            [
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),# procedure
                VarDecl(Id("main"), IntType())
            ])
        expect = 'Redeclared Variable: main'
        self.assertTrue(TestChecker.test(input, expect, 301))

    def test_redecl_vardecl(self):
        input = Program(
            [
                VarDecl(Id("main"), IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])

            ])
        expect = 'Redeclared Procedure: main'
        self.assertTrue(TestChecker.test(input, expect, 302))

    def test_redecl_func(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])

            ])
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 303))

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
        self.assertTrue(TestChecker.test(input, expect, 304))

    def test_redecl_vardecl2(self):
        input = Program(
            [
                VarDecl(Id("x"), FloatType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),# procedure
                VarDecl(Id("a"), IntType()),
                VarDecl(Id("x"), IntType())
            ])
        expect = 'Redeclared Variable: x'
        self.assertTrue(TestChecker.test(input, expect, 305))

    def test_redecl_func2(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                FuncDecl(Id("a"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [])

            ])
        expect = 'Redeclared Function: a'
        self.assertTrue(TestChecker.test(input, expect, 306))

    def test_redecl_proce2(self):
        input = Program(
            [
                VarDecl(Id("afoo"), FloatType()),
                FuncDecl(Id("afoo"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main"), [VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main1s"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
            ])
        expect = 'Redeclared Procedure: afoo'
        self.assertTrue(TestChecker.test(input, expect, 307))

    def test_redecl_vardecl3(self):
        input = Program(
            [
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),
                VarDecl(Id("main"), FloatType()),                
                VarDecl(Id("a"), IntType()),
                VarDecl(Id("a"), IntType())
            ])
        expect = 'Redeclared Variable: main'
        self.assertTrue(TestChecker.test(input, expect, 308))

    def test_redecl_func3(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("a"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
                FuncDecl(Id("main"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType())
                

            ])
        expect = 'Redeclared Function: a'
        self.assertTrue(TestChecker.test(input, expect, 309))

    def test_redecl_builtinfunc(self):
        input = Program(
            [
                VarDecl(Id("putIntLn"), FloatType()),
                FuncDecl(Id("afoo"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main"), [VarDecl(Id("h"), IntType())], [], []),
                FuncDecl(Id("main1s"), [VarDecl(Id("m"), StringType()),VarDecl(Id("h"), IntType())], [], [],IntType()),
            ])
        expect = 'Redeclared Variable: putIntLn'
        self.assertTrue(TestChecker.test(input, expect, 310))
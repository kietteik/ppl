import unittest
from TestUtils import TestChecker
from StaticCheck import *
from AST import *


class CheckerSuite(unittest.TestCase):

    def test_redecl_vardecl(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                VarDecl(Id("b"), FloatType())
            ])
        expect = [Symbol('b',FloatType()),Symbol('a',FloatType())]
        self.assertTrue(TestChecker.test(input, expect, 301))

    def test_redecl_vardecl2(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                VarDecl(Id("b"), FloatType()),
                FuncDecl(Id('main'),[],[],[],VoidType())
            ])
        expect = [Symbol('main',MType([],VoidType())) ,Symbol('b',FloatType()),Symbol('a',FloatType())]
        self.assertTrue(TestChecker.test(input, expect, 302))

    def test_redecl_vardecl3(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                VarDecl(Id("b"), FloatType()),
                FuncDecl(Id('main'),[],[],[],VoidType()),
                FuncDecl(Id('foo'),[VarDecl(Id("a"), FloatType())],[],[],IntType())
            ])
        expect = [Symbol('foo',MType([FloatType()],IntType())), Symbol('main',MType([],VoidType())) ,Symbol('b',FloatType()),Symbol('a',FloatType())]
        self.assertTrue(TestChecker.test(input, expect, 303))

    def test_redecl_vardecl4(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                VarDecl(Id("b"), IntType()),
                FuncDecl(Id('main'),[],[],[],VoidType()),
                FuncDecl(Id('foo'),[VarDecl(Id("a"), FloatType()),VarDecl(Id("b"), IntType())],[],[],IntType())
            ])
        expect = [Symbol('foo',MType([FloatType(),IntType()],IntType())), Symbol('main',MType([],VoidType())) ,Symbol('b',IntType()),Symbol('a',FloatType())]
        self.assertTrue(TestChecker.test(input, expect, 304))

    def test_redecl_funcdecl1(self):
        input = Program(
            [
                VarDecl(Id("abc"), FloatType()),
                VarDecl(Id("xya"), FloatType()),
                FuncDecl(Id('main'),[],[],[],VoidType())
            ])
        expect = [Symbol('main',MType([],VoidType())) ,Symbol('xya',FloatType()),Symbol('abc',FloatType())]
        self.assertTrue(TestChecker.test(input, expect, 305))

    def test_redecl_funcdecl2(self):
        input = Program(
            [
                VarDecl(Id("id1"), StringType()),
                VarDecl(Id("id2"), IntType()),
                FuncDecl(Id('main'),[],[],[],VoidType()),
                FuncDecl(Id('foo'),[VarDecl(Id("a"), FloatType())],[],[],IntType())
            ])
        expect = [Symbol('foo',MType([FloatType()],IntType())), Symbol('main',MType([],VoidType())) ,Symbol('id2',IntType()),Symbol('id1',StringType())]
        self.assertTrue(TestChecker.test(input, expect, 306))

    def test_redecl_funcdecl3(self):
        input = Program(
            [
                VarDecl(Id("a"), FloatType()),
                VarDecl(Id("b"), IntType()),
                FuncDecl(Id('main'),[],[],[],VoidType()),
                FuncDecl(Id('foo'),[VarDecl(Id("a"), FloatType()),VarDecl(Id("b"), IntType())],[],[],IntType())
            ])
        expect = [Symbol('foo',MType([FloatType(),IntType()],IntType())), Symbol('main',MType([],VoidType())) ,Symbol('b',IntType()),Symbol('a',FloatType())]
        self.assertTrue(TestChecker.test(input, expect, 303))


import unittest
from TestUtils import TestChecker
from AST import *

class ExerciseSuite(unittest.TestCase):
	def test_cau1(self):
		input = Program([VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),IntType()),FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())])
		expect = """[VarDecl(Id(x),FloatType),VarDecl(Id(y),IntType)]"""
		self.assertTrue(TestChecker.test(input,expect,300))

	def test_cau2(self):
		input = Program([VarDecl(Id("x"),IntType()),VarDecl(Id("x"),IntType()),VarDecl(Id("z"),IntType()),FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())])
		expect = """[VarDecl(Id(x),IntType),VarDecl(Id(x),IntType),VarDecl(Id(z),IntType)] Redeclared Variable: VarDecl(Id(x),IntType),VarDecl(Id(x),IntType)"""
		self.assertTrue(TestChecker.test(input,expect,301))
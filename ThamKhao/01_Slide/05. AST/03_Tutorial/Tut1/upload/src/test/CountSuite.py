import unittest
from TestUtils import TestCount
from AST import *

class CountSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """function a(): INTTYPE ;
        		   BEGIN
        		   END 
        		"""
        expect = "15"
        self.assertTrue(TestCount.test(input,expect,300))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """procedure b();
        		   BEGIN
        		   		aaaaa();
        		   END 
        		"""
        expect = "18"
        self.assertTrue(TestCount.test(input,expect,301))    

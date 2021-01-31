import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Var: x;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,201))

    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """Var: ;"""
    #     expect = "Error on line 1 col 5: ;"
    #     self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_program_1(self):
        """Success"""
        input = """int a,b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_program_2(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_program_3(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e
            e = a + 4;
            c = a * d / 2.0;
            return c + 1;
        }
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "Error on line 4 col 12: e"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_program_4(self):
        """Success"""
        input = """int a,b,c;
        float f + 4;
            c = a * d / 2.0;
            return c + 1;
        }
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "Error on line 2 col 16: +"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_program_5(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
            e = a + 4;
            c = a * d / 2.0;
            return c + 1;
        }
        float goo(float){
            return foo(1,a,b);
        }
        """
        expect = "Error on line 8 col 23: )"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_program_6(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
            e = a + 4;
            c = a * d / 2.0 * goo(a,b+1);
            return c + 1;
        }
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_program_7(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
            e = a + 4;
            c = a * d / 2.0 * goo(a,b+1);
            return;
        }
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "Error on line 6 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_program_8(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
            e = a + 4;
            c = a * d / 2.0 * goo(a,b+1);
            return c++;
        }
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "Error on line 6 col 21: +"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_program_9(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
            e = a + 4;
            c = a * d / 2.0 * goo(a,b+1);
            return c+1;
        
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "Error on line 8 col 17: ("
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_program_10(self):
        """Success"""
        input = """int a,b,c;
        float foo(int a; float c,d){
            int e;
            e = a + 4;
            c = a * d / 2e+0 * goo(a,b+1);
            return c + 1;
        }
        float goo(float a,b){
            return foo(1,a,b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

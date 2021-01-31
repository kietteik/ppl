import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """int a, b, c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
        
    def test_2(self):
        """Simple program: int main() {} """
        input = """float test(int a)
        {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_3(self):
        """Simple program: int main() {} """
        input = """int a, b, c;
        float main(int a;b){}"""
        expect = "Error on line 2 col 25: b"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_4(self):
        """Simple program: int main() {} """
        input = """ float test(int a, b )
        {
            fooa(2+ 2, 4 * 7);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_5(self):
        """Simple program: int main() {} """
        input = """float f()
        {
            int c = 2;
            return c;
        }"""
        expect = "Error on line 3 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_6(self):
        """Miss variable"""
        input = """float f(int a)
        {
            int e;
            e = a + 4;
            c = a * d / 2.0;
            return;
        }
        """
        expect = "Error on line 6 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_7(self):
        """Simple program: int main() {} """
        input = """int main()
        {
            int k;
            c = f(;

        }"""
        expect = "Error on line 4 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_8(self):
        """Simple program: int main() {} """
        input = """int a, b, c;
        float main()
        {
            int e;
            e = foo() * 2.2 + 4;
            return +;
        }"""
        expect = "Error on line 6 col 19: +"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_9(self):
        """Simple program: int main() {} """
        input = """int main()
        {
            float f = 2.0;
            f = f * 10;

        """
        expect = "Error on line 3 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_10(self):
        """Simple program: int main() {} """
        input = """int a, b, c"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,210))

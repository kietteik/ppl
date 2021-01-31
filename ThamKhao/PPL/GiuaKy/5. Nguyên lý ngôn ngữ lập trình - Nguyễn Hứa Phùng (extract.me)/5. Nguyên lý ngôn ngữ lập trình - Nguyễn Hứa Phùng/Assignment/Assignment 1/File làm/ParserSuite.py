import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    """variable declaration"""
    def test_vardecl_201(self):
        input = """float b[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_vardecl_202(self):
        input = """
            int a;
            float b, c[2];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_vardecl_203(self):
        input = """int ; float b;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_vardecl_204(self):
        input = """
            int a;
            float ;
        """
        expect = "Error on line 3 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_vardecl_205(self):
        input = """int a int b int c"""
        expect = "Error on line 1 col 6: int"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_vardecl_206(self):
        input = "in i; float b;"
        expect = "Error on line 1 col 0: in"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_vardecl_207(self):
        input = "int i; float a[2;"
        expect = "Error on line 1 col 16: ;"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_vardecl_208(self):
        input = "int i; float a2];"
        expect = "Error on line 1 col 15: ]"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_vardecl_209(self):
        input = "int a, b[2]; float c;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_vardecl_210(self):
        input = "int a[2], b;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_vardecl_211(self):
        input = """int i;
int b[5]"""
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    """function variable"""
    def test_funcvar_212(self):
        input = "void foo() { }"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_funcvar_213(self):
        input = "int[] foo() { }"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))  

    def test_funcvar_214(self):
        input = """
            void a()
            {
                b();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_funcvar_215(self):
        input = "void foo () { "
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_funcvar_216(self):
        input = """
            in foo(){
                foo();
            }
        """
        expect = "Error on line 2 col 12: in"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_funcvar_217(self):
        input = "int[5] foo() { }"
        expect = "Error on line 1 col 4: 5"
        self.assertTrue(TestParser.checkParser(input,expect,217))  

    def test_funcvar_218(self):
        input = "int foo(int a) { }"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_funcvar_219(self):
        input = "void foo(int a, float b[]) { }"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_funcvar_220(self):
        input = "int main(boolean b) { }"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))


    """block statement"""
    def test_blockstmt_221(self):
        input = """int main() {
            int a;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test_blockstmt_222(self):
        input = """void main() {
            string str
         }"""
        expect = "Error on line 3 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test_blockstmt_223(self):
        input = """int main() {
            string str; int a[1];
            float b;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_blockstmt_224(self):
        input = """void main() {
            string str; int n[];
         }"""
        expect = "Error on line 2 col 30: ]"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_blockstmt_225(self):
        input = """void foo(int a) {
            STRING b;
         }"""
        expect = "Error on line 2 col 19: b"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_blockstmt_226(self):
        input = """void main() {
            string str; int 2];
         }"""
        expect = "Error on line 2 col 28: 2"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_blockstmt_227(self):
        input = """int main() {
            string str; int a[2;
         }"""
        expect = "Error on line 2 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_blockstmt_228(self):
        input = """void foo() {
            float int b[2];
         }"""
        expect = "Error on line 2 col 18: int"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    """if statement"""
    def test_ifstmt_229(self):
        input = """void main() {
            int a, b;
            if (a != 1) b = a;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_ifstmt_230(self):
        input = """int main() {
            int a, b;
            if (a != 1) {b = a;}
            else
            {
                a = 3;
                b = a + 3;
            }
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_ifstmt_231(self):
        input = """int main() {
            int a, b, c;
            a = 3; b = 4; c = 5;
            if (a != 2) {b = 3}
            else {c = 4};
         }"""
        expect = "Error on line 4 col 30: }"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_ifstmt_232(self):
        input = """void main() {
            int a, b;
            if (a != 1) {b = a;}
            else if (a < 1)
                {
                    b = a - 1;
                }
            else b = a + 1;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_ifstmt_233(self):
        input = """int main() {
            int a, b;
            if (a != 1) {b = a;}
            else if (a > 2)
                {
                    b = a - 1
                }
         }"""
        expect = "Error on line 7 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_ifstmt_234(self):
        input = """int main() {
            int a, b;
            if (a != 1 b = a;
         }"""
        expect = "Error on line 3 col 23: b"
        self.assertTrue(TestParser.checkParser(input,expect,234))    

    def test_ifstmt_235(self):
        input = """
            int main()
            {
                if(foo(1, 2) == 3) a = a + 1;
                else a = a - 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_ifstmt_236(self):
        input = """int main() {
            int a, b;
            if (a != 1) {b = a;}
            else 
            {
                b = 2;           
            };
         }"""
        expect = "Error on line 7 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_ifstmt_237(self):
        input = """int main() {
            int a, b;
            if (a != 1); {b = a;}
            else 
            {
                b = 2;           
            }
         }"""
        expect = "Error on line 3 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    """do while statement"""
    def test_dowhile_238(self):
        input = """void main() {
            a = 1;
            do a = a + 1; while (a < 5);
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_dowhile_239(self):
        input = """int main() {
            int a, b;
            a = 1;
            do {
                if (a != 1) b = a;
                a = a + 1;
                b = b - 1;
            } while (a < 5);
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_dowhile_240(self):
        input = """void main() { 
            int a;
            a = 1;
            do a = a + 1 while (a < 5);
         }"""
        expect = "Error on line 4 col 25: while"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_dowhile_241(self):
        input = """int main() {
            int a;
            a = 1;
            while (a < 5) do {
                a = a + 1;
            }
         }"""
        expect = "Error on line 4 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_dowhile_242(self):
        input = """
            int main()
            {
                do a = a + 1;
                while (1);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_dowhile_243(self):
        input = """int main() {
            int a;
            a = 0;
            do a = a + 1; while (a < 5 & a > 0);
         }"""
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    """for statement"""
    def test_forstmt_244(self):
        input = """int main() {
            int a, i;
            for (i = 0; i <= 5; i = i + 1) a = a + 1;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    
    def test_forstmt_245(self):
        input = """
            void main(){
                for (;;)
            }
        """
        expect = "Error on line 3 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_forstmt_246(self):
        input = """int main() {
            int a, i;
            for (; i <= 5; i = i + 1) a = a + i;
         }"""
        expect = "Error on line 3 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    
    def test_forstmt_247(self):
        input = """void main() {
            int a, i;
            for (i , i <= 5; i = i + 1) a = a + i;
         }"""
        expect = "Error on line 3 col 19: ,"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_forstmt_248(self):
        input = """void main() {
            int a, i;
            i = 1;
            for (i;; i = i + 1) a = a + i;
         }"""
        expect = "Error on line 4 col 19: ;"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_forstmt_249(self):
        input = """void main() {
            int i, a;
            i = 1;
            for (i; i < 5;) a = a + i;
         }"""
        expect = "Error on line 4 col 26: )"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    """return, continue, break"""
    def test_return_continue_break_250(self):
        input = """void main() {
            int a;
            a = 0;
            do {
                a = a + 1;
                if (a == 3) break; 
            } while (a > 0);
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_return_continue_break_251(self):
        input = """int main() {
            int a, b;
            a = 0;
            do {
                a = a + 1;
                if (a == 3) b = a + 3; 
            } while (a < 5);
            return a b;
         }"""
        expect = "Error on line 8 col 21: b"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_return_continue_break_252(self):
        input = """int main() {
            int a;
            a = 0;
            do {
                a = a + 1;
                if (a == 3) break a; 
            } while (a < 5 && a > 0);
            return a;
         }"""
        expect = "Error on line 6 col 34: a"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_return_continue_break_253(self):
        input = """int main() {
            int a, b;
            a = 0;
            b = 0;
            do {
                a = a + 1;
                if (a > 3) continue; 
                b = b + a;
            } while (a < 5);
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_return_continue_break_254(self):
        input = """void main() {
            int a, b;
            a = 0;
            b = 0;
            do {
                a = a + 1;
                if (a > 3) continue: 
                b = b + a;
            } while (a < 5);
         }"""
        expect = ":"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_return_continue_break_255(self):
        input = """int main() {
            int a, i;
            for (i = 0; i <= 5; i = i + 1) 
                {
                    if (i == 3) continue;
                    a = a + i;
                }
            return a / 3;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_return_continue_break_256(self):
        input = """int main() {
            int a, i;
            for (i = 0; i <= 5; i = i + 1) 
                {
                    if (i == 3) break;
                    a = a + i;
                }
            return i * a * 2;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    
    def test_return_continue_break_257(self):
        input = """int main() {
            int a, i;
            a = 10;
            for (i = 0; i <= 5; i = i + 1) 
                {
                    if (a < 5) continue;
                    a = a - 1;
                }
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_return_continue_break_258(self):
        input = """int main() {
            int a, i;
            a = 9;
            for (i = 0; i <= 10; i = i + 2) 
                {
                    if (a != 3) break;
                    a = a - 2;
                }
            return i;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_return_continue_break_259(self):
        input = """int main() {
            int a, i;
            a = 1;
            for (i = 0; i <= 20; i = i + 1) 
                {
                    if (@ < 10) break;
                    a = a + 1;
                }
            return i;
         }"""
        expect = "@"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    
    def test_return_continue_break_260(self):
        input = """int main() {
            int a, i;
            for (i = 0; i <= 10; i = i + 1) 
                {
                    if (a[) break;
                    a = a / 10;
                }
            return a * a;
        }"""
        expect = "Error on line 5 col 26: )"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_return_continue_break_261(self):
        input = """int main() 
        {
            int a, i;
            a = 10;
            for (i = 0; i <= 3; i = i + 1) 
                {
                    if (a < 3) continue;
                    a = a | 3;
                }
            return a * a;
        }"""
        expect = "|"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_return_continue_break_262(self):
        input = """int main() {
            int a, i;
            a = 3;
            for (i = 0; i <= 10; i = i + 2) 
                {
                    if (a & i) continue;
                    a = a / 2;
                }
            return a * a;
        }"""
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,262)) 


    """call function"""
    def test_funccall_263(self):
        input = """
        int foo(int a){
            return a + 3; }
        int main() {
            int x, y;
            x = 4;
            y = foo(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_funccall_264(self):
        input = """
        int foo(int a, int b){
            return a * b; }
        int main() {
            int a, b, x;
            a = 5; b = 6;
            if (a != b) x = foo(a b);
            else x = 7;
        }"""
        expect = "Error on line 7 col 34: b"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_funccall_265(self):
        input = """
        int foo(int a, int b){
            return a * b; }
        int main() {
            int a, b, x;
            a = 5; b = 6;
            if (a != b) x = foo(a b);
            else x = 7;
        }"""
        expect = "Error on line 7 col 34: b"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_funccall_266(self):
        input = """
        int foo(int a, int b){
            return a * b; }
        int main() {
            int a, b, x;
            a = 5; b = 6;
            if (a != b) x = foo(a; b);
            else x = 7;
        }"""
        expect = "Error on line 7 col 33: ;"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_funccall_267(self):
        input = """
        int foo(int a, int b){
            return a * b; }
        int main() {
            int a, b, x;
            a = 5; b = 6;
            if (a != b) x = foo(-a, b);
            else x = 7;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_funccall_268(self):
        input = """
        int foo(int a, int b){
            return a * b; }
        int main() {
            int a, x;
            a = 5;
            do {
            x = foo(-a, a);
            ) while (a != x)
        }"""
        expect = "Error on line 9 col 12: )"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_funccall_269(self):
        input = """int foo(int a, int b){
            return a * b; }
        void main() {
            int a;
            a = 2;
            do {
                a = foo(a, 2);
            } while (a < 30);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_funccall_270(self):
        input = """int foo(int a, int b){
            return a * b; }
        void main() {
            int a, b;
            a = 0;
            do 
            {
                a = sum(a, b);
            } while (a < 100);
            return a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    """test the other"""    
    def test_other_271(self):
        input = """
        void main() {
            int a, b;
            a = 1; b = 0;
            do1 {b = b + a} while (a != 3);
         }"""
        expect = "Error on line 5 col 16: {"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_other_272(self):
        input = """
        int main()
        {
            int x;
            float[] foo()
            {
                int s;
                float[] x;
        }"""
        expect = "Error on line 5 col 17: ["
        self.assertTrue(TestParser.checkParser(input,expect,272))
    
    def test_other_273(self):
        input = """         
        float foo()
        {
            int a;
            a = 10;
            {
            do a = a + 1;
            while(true);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_other_274(self):
        input = """         
        float foo()
        {
            int a;
            a = 10;
            {
            do a = a + 1;
            while(TRUE);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_other_275(self):
        input = """         
        float foo()
        {
            int a;
            a = 10;
            {
            do a = a + 1;
            while(FALSE + 1);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_other_276(self):
        input = """int foo(int a, int b){
            return a * b;
        }
        int main() {
            int i, a;
            for (i = 0; i <= 10; i = i + 1) 
                {
                    if (a < 10) break;
                    a = foo(a, 10);
                }
            return a * a;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_other_277(self):
        input = """int main() {
            int a, i;
            for (i = 30; i > 1; i = i * 2) 
                {
                    if (a) break;
                    a = a + 1;
                }
            return a;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_other_278(self):
        input = """
        float[] foo(){
        int a;
           for (i = 0; i < 5; i = i + 1)
                do a = a + 1;
                while (i > 1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_other_279(self):
        input = """
        int s;
        int foo(int a, int b, int c){
            return a + b + c;
        }
        void main() {
            int x, y, z;
            for (x = 0; x <= 20; y = y + 1) 
            {
                z = foo(x, y, z);
                x = z - 1;
            }
            return y;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_other_280(self):
        input = """int div(int a, int b){
            return a b;
        }
        int main() {
            int i, a;
            for (i = 0; i <= 10; i = i + 1) 
                {
                    if (a < 10) continue;
                    a = div(a,10);
                }
            return a * a;
         }"""
        expect = "Error on line 2 col 21: b"
        self.assertTrue(TestParser.checkParser(input,expect,280))
   
    def test_other_281(self):
        input = """int foo() {
                float a;
                a = 1e2;
                return a + 5;
              }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_other_282(self):
        input = """
        int foo()
        {
        int a,b;
        a()
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_other_283(self):
        input = """int foo(){
        // A line comment
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_other_284(self):
        input = """void foo(){
        /* 
        A block comment
        */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_other_285(self):
        input = """int foo(){
        int a;
        a = 3;
        if (3a == 9) return a;
      }"""
        expect = "Error on line 4 col 13: a"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_other_286(self):
        input = """
        int main () 
        {
             return void;   
        }
        """
        expect = "Error on line 4 col 20: void"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_other_287(self):
        input = """
        int main () {
             return foo(2, 3 + 4);   
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_other_288(self):
        input = """
        int main () {
            foo();
            boo();
            return noo();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_other_289(self):
        input = """
        int main () {
             1.2e-3;
             c;
             a = b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    # def test_program_9(self):
    #     input = """int main(){
    #       a(b(c(d())));
    #      }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_other_291(self):
        input = """int main(){
            for(i;k;j) printf();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_other_292(self):
        input = """int main(){
        // abc
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_other_293(self):
        input = """int main(a){
        {}
        }"""
        expect = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_other_294(self):
        input = """int main(){
        {};
        }"""
        expect = "Error on line 2 col 10: ;"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_other_295(self):
        input = """int main(){
        {
        abc; foo(); a = b;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    
    def test_other_296(self):
        input = """int main(){
        // abc\nc=;
        }"""
        expect = "Error on line 3 col 2: ;"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    
    def test_other_297(self):
        input = """int main(){
        // abc
        c=;
        }"""
        expect = "Error on line 3 col 10: ;"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_other_298(self):
        input = """int main(){
        // abc\nc=
        ;
        }"""
        expect = "Error on line 4 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_other_299(self):
        input = """int main(){
        ;
        }"""
        expect = "Error on line 2 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_other_300(self):
        input = """int main(){
        int a[-2];
        }"""
        expect = "Error on line 2 col 14: -"
        self.assertTrue(TestParser.checkParser(input,expect,300))
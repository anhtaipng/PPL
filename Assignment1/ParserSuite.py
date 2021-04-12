import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_simple_program_with(self):
        """Simple program: int main() {}"""
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_simple_program_with_expession(self):
        """Simple program: int main() {}"""
        input = """Function: anhtaideptrai
        Body: 
        Var: x,y,z,t=0;
        x= t&&2 -4*3\\6;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_simple_program_with_simple_var(self):
        """simple_program_with_simple_var"""
        input = """Function: main
                Body:
                    Var: r = 10., v;
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_while_not_do(self):
        """test_while_not_do"""
        input = """Function: main
                Body:
                    While True print(abc); EndWhile.
                EndBody. """
        expect = "Error on line 3 col 31: print"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_function1(self):
        input = """Var: a[5] = {12,4,5}; 
        Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_function6(self):
        input = """Function: main
                Body:
                    Return foo(2+x,4.\\.y);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_function2(self):
        input = """
        Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "Error on line 2 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_function3(self):
        input = """Var: x;
        Function: fact
        Parameter: n,s,dBody:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_function4(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    Do statement-list While expression EndDo.
                EndBody."""
        expect = "Error on line 4 col 32: -"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_function5(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_function7(self):
        input = """Function: main
                Body:
                    Continue;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_function8(self):
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_function9(self):
        input = """Function: main
                Body:
                    a=b&&c\nd;
                EndBody."""
        expect = "Error on line 4 col 0: d"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_function10(self):
        input = """Function: main
                Body:
                    Continue;
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_function11(self):
        input = """Function: main
                Body:
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_function12(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_function13(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "Error on line 6 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_function14(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1)
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.."""
        expect = "Error on line 9 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test_wrong_miss_close1(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_simple_program_with1(self):
        """Simple program: int main() {}"""
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    
    def test_simple_program_with_expession1(self):
        """Simple program: int main() {}"""
        input = """Function: anhtaideptrai
        Body: 
        Var: x,y,z,t=0;
        x= t&&2 -4*3\\6;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_simple_program_with_simple_var1(self):
        """simple_program_with_simple_var"""
        input = """Function: main
                Body:
                    Var: r = 10., v;
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_while_not_do1(self):
        """test_while_not_do"""
        input = """Function: main
                Body:
                    While True print(abc); EndWhile.
                EndBody. """
        expect = "Error on line 3 col 31: print"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_function20(self):
        input = """Var: a[5] = {12,4,5}; 
        Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_function21(self):
        input = """Function: main
                Body:
                    Return foo(2+x,4.\\.y);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_function22(self):
        input = """
        Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "Error on line 2 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_function23(self):
        input = """Var: x;
        Function: fact
        Parameter: n,s,dBody:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_function24(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    Do statement-list While expression EndDo.
                EndBody."""
        expect = "Error on line 4 col 32: -"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_function25(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_function27(self):
        input = """Function: main
                Body:
                    Continue;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_function28(self):
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_function29(self):
        input = """Function: main
                Body:
                    a=b&&c\nd;
                EndBody."""
        expect = "Error on line 4 col 0: d"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_function30(self):
        input = """Function: main
                Body:
                    Continue;
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_function31(self):
        input = """Function: main
                Body:
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_function32(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_function33(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "Error on line 6 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_function34(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1)
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.."""
        expect = "Error on line 9 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    
    def test_wrong_miss_close2(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_simple_program_with2(self):
        """Simple program: int main() {}"""
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    
    def test_simple_program_with_expession2(self):
        """Simple program: int main() {}"""
        input = """Function: anhtaideptrai
        Body: 
        Var: x,y,z,t=0;
        x= t&&2 -4*3\\6;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_simple_program_with_simple_var2(self):
        """simple_program_with_simple_var"""
        input = """Function: main
                Body:
                    Var: r = 10., v;
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_while_not_do2(self):
        """test_while_not_do"""
        input = """Function: main
                Body:
                    While True print(abc); EndWhile.
                EndBody. """
        expect = "Error on line 3 col 31: print"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_funcction1(self):
        input = """Var: a[5] = {12,4,5}; 
        Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_funcction6(self):
        input = """Function: main
                Body:
                    Return foo(2+x,4.\\.y);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_funcction2(self):
        input = """
        Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "Error on line 2 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_funcction3(self):
        input = """Var: x;
        Function: fact
        Parameter: n,s,dBody:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_funcction4(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    Do statement-list While expression EndDo.
                EndBody."""
        expect = "Error on line 4 col 32: -"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_funcction5(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_funcction7(self):
        input = """Function: main
                Body:
                    Continue;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_funcction8(self):
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_funcction9(self):
        input = """Function: main
                Body:
                    a=b&&c\nd;
                EndBody."""
        expect = "Error on line 4 col 0: d"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_funcction10(self):
        input = """Function: main
                Body:
                    Continue;
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_funcction11(self):
        input = """Function: main
                Body:
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_funcction12(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_funcction13(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "Error on line 6 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_funcction14(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1)
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.."""
        expect = "Error on line 9 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    
    def test_wrong_miss_close3(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_simple_program_with3(self):
        """Simple program: int main() {}"""
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    
    def test_simple_program_with_expession3(self):
        """Simple program: int main() {}"""
        input = """Function: anhtaideptrai
        Body: 
        Var: x,y,z,t=0;
        x= t&&2 -4*3\\6;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_simple_program_with_simple_var3(self):
        """simple_program_with_simple_var"""
        input = """Function: main
                Body:
                    Var: r = 10., v;
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_while_not_do3(self):
        """test_while_not_do"""
        input = """Function: main
                Body:
                    While True print(abc); EndWhile.
                EndBody. """
        expect = "Error on line 3 col 31: print"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_funccction1(self):
        input = """Var: a[5] = {12,4,5}; 
        Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_funccction6(self):
        input = """Function: main
                Body:
                    Return foo(2+x,4.\\.y);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_funccction2(self):
        input = """
        Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "Error on line 2 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_funccction3(self):
        input = """Var: x;
        Function: fact
        Parameter: n,s,dBody:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_funccction4(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    Do statement-list While expression EndDo.
                EndBody."""
        expect = "Error on line 4 col 32: -"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_funccction5(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_funccction7(self):
        input = """Function: main
                Body:
                    Continue;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_funccction8(self):
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_funccction9(self):
        input = """Function: main
                Body:
                    a=b&&c\nd;
                EndBody."""
        expect = "Error on line 4 col 0: d"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_funccction10(self):
        input = """Function: main
                Body:
                    Continue;
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_funccction11(self):
        input = """Function: main
                Body:
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_funccction12(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_funccction13(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "Error on line 6 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_funccction14(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1)
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.."""
        expect = "Error on line 9 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    
    def test_wrong_miss_close5(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_simple_program_with5(self):
        """Simple program: int main() {}"""
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    
    def test_simple_program_with_expession5(self):
        """Simple program: int main() {}"""
        input = """Function: anhtaideptrai
        Body: 
        Var: x,y,z,t=0;
        x= t&&2 -4*3\\6;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_simple_program_with_simple_var5(self):
        """simple_program_with_simple_var"""
        input = """Function: main
                Body:
                    Var: r = 10., v;
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_while_not_do5(self):
        """test_while_not_do"""
        input = """Function: main
                Body:
                    While True print(abc); EndWhile.
                EndBody. """
        expect = "Error on line 3 col 31: print"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_funcccction1(self):
        input = """Var: a[5] = {12,4,5}; 
        Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_funcccction6(self):
        input = """Function: main
                Body:
                    Return foo(2+x,4.\\.y);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_funcccction2(self):
        input = """
        Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = "Error on line 2 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_funccctcion3(self):
        input = """Var: x;
        Function: fact
        Parameter: n,s,dBody:
        EndBody.
        Function: main
        Body:
        EndBody."""
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_funccctcion4(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    Do statement-list While expression EndDo.
                EndBody."""
        expect = "Error on line 4 col 32: -"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_funcccction5(self):
        input = """Function: main
                Body:
                    Var: r = 10., v;
                    For (i = 0, i < 10, 2) Do
                    writeln(i);
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_funcccction7(self):
        input = """Function: main
                Body:
                    Continue;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_funcccction8(self):
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_funcccction9(self):
        input = """Function: main
                Body:
                    a=b&&c\nd;
                EndBody."""
        expect = "Error on line 4 col 0: d"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_funcccction10(self):
        input = """Function: main
                Body:
                    Continue;
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_funcccction11(self):
        input = """Function: main
                Body:
                    Break;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_funcccction12(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_funccctcion13(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody."""
        expect = "Error on line 6 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_funcccction14(self):
        input = """Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1)
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.."""
        expect = "Error on line 9 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,300))
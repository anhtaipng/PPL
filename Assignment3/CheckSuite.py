import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

# Pham Nguyen Anh Tai
# 1813897

class CheckSuite(unittest.TestCase):


    def test_undeclared_function1(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: z
        Body:
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Function(),"z"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_function2(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Body:
        EndBody.
        Function: m
        Body: 
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function3(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Var: int_of_float = 2;
        Function: a
        Body:
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Variable(), 'int_of_float'))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_undeclared_function4(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z,y
        Body:
        Var: a;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Parameter(), 'y'))
        self.assertTrue(TestChecker.test(input,expect,404))
        

    def test_undeclared_function5(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a,x;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_undeclared_function6(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        b = 6;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_undeclared_function7(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        a = x;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_undeclared_function8(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        a = 5;
        a = 9.6;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'),FloatLiteral(9.6))))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_undeclared_function9(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        a = {4,5,6};
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))))
        self.assertTrue(TestChecker.test(input,expect,409))


    def test_undeclared_function10(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a[2];
        a = {4,5,6};
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_function11(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a[2], x[3][4];
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Variable(),'x'))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_function12(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: b;
        EndBody.
        Function: main
        Body: 
        x = {2,3,4};
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('x'),ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]))))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_function13(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: x,y
        Body:
        x = 6.5;
        Return 1;
        x = 2.3;
        Return 1.0;
        EndBody.
        Function: main
        Body: 
        x = 3;
        EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_function14(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: x
        Body:
	    Return x;
        EndBody.
        Function: main
        Body: 
        x = 3;
        EndBody."""
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_function15(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: x,y
        Body:
        Var: a[2][3], b[2][3];
        a = b;
        EndBody.
        Function: main
        Body: 
        x = 3;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_function16(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: x
        Body:
	    Return 1;
        EndBody.
        Function: main
        Body:
	    Var: y = 2, a;
	    y = a();
        EndBody.
        """
        expect = str(Undeclared(Function(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_function17(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: x,y
        Body:
	    Return 1;
        EndBody.
        Function: main
        Body:
	    Var: y = 2;
	    y = a(1);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('a'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_function18(self):
        """Simple program: main"""
        input = """
        Function: a
        Parameter: x, y, z
        Body:
        x = 1.9;
        y = True;
        Return 1.0;
        EndBody.
        Function: main
        Body:
        Var: z, t;
        z = a(1.3, True, t);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('z'),CallExpr(Id('a'),[FloatLiteral(1.3),BooleanLiteral(True),Id('t')]))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_function19(self):
        """Simple program: main"""
        input = """
        Function: a
        Parameter: x, y, z
        Body:
        x = 1.9;
        y = True;
        z = "anhtaideptrai";
        Return 1.0;
        EndBody.
        Function: main
        Body:
        Var: z, t, m, n;
        z = a(m, n, t);
        m = 34e-10;
        n = False;
        t = 2;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('t'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_function20(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
        Var: y = 2, z = 0.5;
        z = a(y);
        EndBody.
        Function: a
        Parameter: x
        Body:
        Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_function21(self):
        """Simple program: main"""
        input = """
        Function: foo
        Body:
        Var: a[3][4];
        a[2][3] = 2;
        Return a;
        EndBody.
        Function: main
        Body:
        foo()[0] = 2;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_function22(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
        foo()[0][2] = True;
        foo()[1][2] = True;
        EndBody.
        Function: foo
        Body:
        Var: a[3][4];
        Return a;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(0),IntLiteral(2)]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_function23(self):
        """Simple program: main"""
        input = """
        
        Function: foo
        Body:
        Var: a[3][4];
        Return a;
        EndBody.
        Function: main
        Body:
        foo()[0][2] = True;
        foo()[1][2] = True;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_function24(self):
        """Simple program: main"""
        input = """      
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
        Var: a[3][4], b[3][4];
        a[0][2] = 3.4;
        a = b;
        b[1][2] = True;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(1),IntLiteral(2)]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_function25(self):
        """Simple program: main"""
        input = """
        Function: main
        Parameter: a,b,c
        Body:
        Var: d, e;
        e = main(b, main(d, c, a),d); 
        Return 3;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('e'),CallExpr(Id('main'),[Id('b'),CallExpr(Id('main'),[Id('d'),Id('c'),Id('a')]),Id('d')]))))
        self.assertTrue(TestChecker.test(input,expect,425))

    

    def test_undeclared_function26(self):
        """Simple program: main"""
        input = """
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
        Var: a[1][3][3] = {{{1,2,3},{4,5,6},{7,8,9}}}, b[3];
        b[0] = a[0][1][2];
        b[1] = 4;
        b[2] = 5.4;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(2)]),FloatLiteral(5.4))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_function27(self):
        """Simple program: main"""
        input = """
        Var: a[1][3][3] = {{{1,2,3},{4,5,6},{7,8,9}}}, b[3];
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
        Var: a;
        a = 3 -. 2;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('-.',IntLiteral(3),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_function28(self):
        """Simple program: main"""
        input = """
        Var: a[1][3][3] = {{{1,2,3},{4,5,6},{7,8,9}}}, b[3];
        Function: foo
        Body:
        EndBody.
        Function: main
        Body:
        b[0] = a[0][1][2];
        b[1] = 4;
        b[2] = 53.0 -. 2.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('b'),[IntLiteral(2)]),BinaryOp('-.',FloatLiteral(53.0),FloatLiteral(2.1)))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_function29(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a + b + c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y, z, t;
        x = foo(y,z,t);
        y = 3.0;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('y'),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_function30(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
        Var: y;
        y = 2.0 +. foo(2);
        EndBody.
        Function: foo
        Parameter: a
        Body:
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undeclared_function31(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
        Var: y;
        y = 2.0 +. foo(2) <= 5;
        EndBody.
        Function: foo
        Parameter: a
        Body:
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('<=',BinaryOp('+.',FloatLiteral(2.0),CallExpr(Id('foo'),[IntLiteral(2)])),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,431))
    

    def test_undeclared_function32(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a + b + c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        y[z][t] = 2;
        z = 3;
        t = 2.3;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('t'),FloatLiteral(2.3))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undeclared_function33(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a + b + c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        y[z][t] = 4 || 5;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('||',IntLiteral(4),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_undeclared_function34(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a + b + c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        y[z][t] = 4 == 5;
        y[z][t] = 4.3;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('y'),[Id('z'),Id('t')]),FloatLiteral(4.3))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_undeclared_function35(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a + b + c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        t = 2.0 +. 1.2;
        y[z][t] = 4;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('y'),[Id('z'),Id('t')])))
        self.assertTrue(TestChecker.test(input,expect,435))
    

    def test_undeclared_function36(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        z = 2 + foo(t);
        EndBody.
        Function: foo
        Parameter: a
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('z'),BinaryOp('+',IntLiteral(2),CallExpr(Id('foo'),[Id('t')])))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_undeclared_function37(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a +. b +. c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        y[2 + foo(0.2,0.3,0.4)][2] = 2;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+',IntLiteral(2),CallExpr(Id('foo'),[FloatLiteral(0.2),FloatLiteral(0.3),FloatLiteral(0.4)]))))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_undeclared_function38(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return a +. b +. c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        z = !t;
        t = 2.3;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('t'),FloatLiteral(2.3))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_undeclared_function39(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return ;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        foo(2,3,4);
        foo(2,3,4.5);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(2),IntLiteral(3),FloatLiteral(4.5)])))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_undeclared_function40(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return  a +. b +. c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        If z Then
        Var: a;
        ElseIf z Then
        a = 5.2;
        ElseIf z Then
        Var: b;
        b = 9.0;
        Else
        EndIf.
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_undeclared_function41(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return  a +. b +. c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        If z Then
        Var: a;
        ElseIf z Then
        z = 5.2;
        ElseIf z Then
        Var: b;
        b = 9.0;
        Else
        Var: c;
        c =True;
        EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('z'),FloatLiteral(5.2))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_undeclared_function42(self):
        """Simple program: main"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return  a +. b +. c;
        EndBody.
        Function: main
        Body:
        Var: x = 2, y[5][6], z, t;
        If z Then
        Var: a;
        ElseIf z Then
        t = 5.2;
        ElseIf z Then
        Var: t;
        t = True;
        Else
        t = "anhtai";
        EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('t'),StringLiteral('anhtai'))))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_undeclared_function43(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    If main(main(5)) Then EndIf. 
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_function44(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = ! main(main(5));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_undeclared_function45(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = 5.0 -. main(main(5));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_undeclared_function46(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = 5 - main(main(5.2));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[FloatLiteral(5.2)])))
        self.assertTrue(TestChecker.test(input,expect,446))


    def test_undeclared_function47(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = True && main(main(5.2));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[FloatLiteral(5.2)])))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_undeclared_function48(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return ;
        EndBody.
        Function: main
        Body:
        Var: z;
        If z Then
        foo(foo(real(),3,3),3,3);
        EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[CallExpr(Id('real'),[]),IntLiteral(3),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_undeclared_function49(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return  ;
        EndBody.
        Function: main
        Body:
        Var: z;
        If z Then
        foo(3,3,3) = real();
        EndIf.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id('foo'),[IntLiteral(3),IntLiteral(3),IntLiteral(3)]),CallExpr(Id('real'),[]))))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_undeclared_function50(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return  ;
        EndBody.
        Function: main
        Body:
        Var: x, y , z, t;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        t = 10.2;
        EndFor.   
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('t'),FloatLiteral(10.2))))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_undeclared_function51(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return  ;
        EndBody.
        Function: main
        Body:
        Var: x, y , z, t;
        z =True;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        EndFor.   
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('z'),IntLiteral(0),BinaryOp('<=',Id('z'),IntLiteral(10)),Id('t'),[[VarDecl(Id('z'),[],None)],\
        [Assign(Id('z'),BooleanLiteral(True))]])))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_undeclared_function52(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return  ;
        EndBody.
        Function: main
        Body:
        Var: x, y , z, t;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        printStr(i);
        EndFor.   
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_undeclared_function53(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return  real();
        EndBody.
        Function: main
        Body:
        Var: x, y , z, t;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        EndFor.   
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('real'),[]))))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_undeclared_function54(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return ;
        EndBody.
        Function: main
        Body:
        Var: x, y , z, t;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        While z >= 10 Do
        EndWhile.
        EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('>=',Id('z'),IntLiteral(10))))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_undeclared_function55(self):
        """Simple program: main"""
        input = """
        Function: real
        Body:
        Return ;
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        Return ;
        EndBody.
        Function: main
        Body:
        Var: x, y , z, t;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        While x >= 10 Do
        x = True;
        EndWhile.
        EndFor.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_undeclared_function56(self):
        """Simple program: main"""
        input = """
        Function: main
        Body:
        Var: x, y , z, t;
        For (z = 0 , z <= 10, t) Do
        Var: z;
        z = True;
        While x >= 10 Do
        x = 8;
        Do Var: x;
        x = True;
        While x >= 10
        EndDo.
        EndWhile.
        EndFor.
        x = True;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_undeclared_function57(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_diff_numofparam_stmt58(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_diff_numofparam_expr59(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_undeclared_function_use_ast60(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_diff_numofparam_expr_use_ast61(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_diff_numofparam_stmt_use_ast62(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_diff_numofparam_stmt_use_ast63(self):
        """Complex program"""
        input = """
        Var: x;
            Function: main
            Body:
                Var: y;
                For (x = 1, x && y, 1+2) Do
                    y = 2.1;
                EndFor.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('&&',Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_diff_numofparam_stmt_use_ast64(self):
        """Complex program"""
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a[2][3],b,c 
        Body:
            Var: y = True;
            a = {{1,2,3},{4,5,6}};
            b = "string";
            For (x = 1, True,2) Do
                a = call(2,1,True);
            EndFor.            
        EndBody.

        Function: call
        Parameter: a,b,c
        Body:
            Var: x[3] = {1.3,2.1,4.3};
            Var: y[2][3];
            y[1][1] = x[1];
            Return y;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_diff_numofparam_stmt_use_ast65(self):
        """Complex program"""
        input = """
        Var:x = 25;
        Function: man 
        Parameter: a[2][3],b,c 
        Body:
            Var: y = True;
            a = {{1,2,3},{4,5,6}};
            b = "string";
            For (x = 1, True,2) Do
                a = call(2,1,True);
            EndFor.            
        EndBody.

        Function: call
        Parameter: a,b,c
        Body:
            Var: x[3] = {1,2,3};
            Var: y[2][3];
            y[1][1] = x[1];
            Return y;
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,465))


    def test_diff_numofparam_stmt_use_ast66(self):
        """Complex program"""
        input = """
        Var:x = 5;
        Function:foo
        Parameter:m,n
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 1.2 >.n;
            Return 0.2;
        EndBody.

        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 3, True, 12) Do
                a = foo(a,b) +. 2.9;
            EndFor.            
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),BinaryOp('+.',CallExpr(Id('foo'),[Id('a'),Id('b')]),FloatLiteral(2.9)))))
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_diff_numofparam_stmt_use_ast67(self):
        """Complex program"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        EndBody.
        Function: real
        Body:
        EndBody.
        Function: main
        Body:
        Var: x,y,z,t;
        Do
        x = 1.5;
        y = 2;
        z = True;
        t = "anhtai";
        While x || y 
        EndDo.
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('||',Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_diff_numofparam_stmt_use_ast68(self):
        """Complex program"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return;
        EndBody.
        Function: real
        Body:
        Return foo(1,2,3);
        EndBody.
        Function: main
        Body:
        Var: x,y,z,t;
        Do
        x = 1.5;
        y = 2;
        z = True;
        t = "anhtai";
        While z
        EndDo.
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id('foo'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_diff_numofparam_stmt_use_ast69(self):
        """Complex program"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return;
        EndBody.
        Function: real
        Body:
        Return;
        EndBody.
        Function: main
        Body:
        Var: x,y,t;
        Do
        x = 1.5;
        y = 2;
        t = "anhtai";
        While z
        EndDo.
        EndBody.
        """
        expect = str(Undeclared(Identifier(),'z'))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_diff_numofparam_stmt_use_ast70(self):
        """Complex program"""
        input = """
        Function: foo
        Parameter: a,b,c
        Body:
        Return;
        EndBody.
        Function: real
        Body:
        Return;
        EndBody.
        Function: main
        Body:
        Var: x,y,t, foo;
        Do
        x = 1.5;
        y = 2;
        t = "anhtai";
        foo(1,2,3);
        While z
        EndDo.
        EndBody.
        """
        expect = str(Undeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_diff_numofparam_stmt_use_ast71(self):
        """Complex program"""
        input = """
        Function: main
        Body:
        Var: x,y,t, foo;
        Do
        x = 1.5;
        y = 2;
        t = "anhtai";
        foo = foo() - foo;
        While z
        EndDo.
        EndBody.
        """
        expect = str(Undeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_diff_numofparam_stmt_use_ast71(self):
        """Complex program"""
        input = """
        Function: main
        Body:
        Var: x,y,t, foo;
        Do
        x = 1.5;
        y = 2;
        t = "anhtai";
        foo = foo() - foo;
        While z
        EndDo.
        EndBody.
        """
        expect = str(Undeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_diff_numofparam_stmt_use_ast72(self):
        """Complex program"""
        input = """
        Function: main
        Body:
        Var: x,y,t;
        Do
        x = 1.5;
        y = 2;
        t = "anhtai";
        foo = foo - foo;
        While z
        EndDo.
        EndBody.
        """
        expect = str(Undeclared(Identifier(),'foo'))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_undeclared_function73(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_diff_numofparam_stmt74(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStr();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStr"),[])))
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test_diff_numofparam_expr75(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(printLn(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("printLn"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_undeclared_function76(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    If main(main(1)) Then EndIf. 
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_undeclared_function77(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = ! main(main(1));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_undeclared_function78(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = 5.0 -. main(main(1));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_undeclared_function79(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = 5 - main(main(1.2));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[FloatLiteral(1.2)])))
        self.assertTrue(TestChecker.test(input,expect,479))


    def test_undeclared_function80(self):
        """Simple program: main"""
        input = """
        Function: main
                Parameter: x
                Body:
                    Var: a;
                    a = True && main(main(1.2));
                EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[FloatLiteral(1.2)])))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_undeclared_function81(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x, y
            Body:
                Return x;
            EndBody.

            Function: main
            Body:
                Var: x;
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_undeclared_function82(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,xy = True;
        Function: xy
        Body:
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Function(),"xy"))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_undeclared_function83(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Var: int_of_string = 2;
        Function: a
        Body:
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Variable(), 'int_of_string'))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_undeclared_function84(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z,z
        Body:
        Var: a;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Parameter(), 'z'))
        self.assertTrue(TestChecker.test(input,expect,484))
        

    def test_undeclared_function85(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a,y;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Variable(), 'y'))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_undeclared_function86(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        c = 6;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Undeclared(Identifier(), 'c'))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_undeclared_function87(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        a = z;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('z'))))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_undeclared_function88(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        a = 5;
        a = 2.1;
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'),FloatLiteral(2.1))))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_undeclared_function89(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: b;
        b = {4,5,6};
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('b'),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))))
        self.assertTrue(TestChecker.test(input,expect,489))


    def test_undeclared_function90(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: b[2];
        b = {4,5,6};
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('b'),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_undeclared_function91(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a[2], y[3][4];
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(Redeclared(Variable(),'y'))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_undeclared_function92(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z ;
        Function: a
        Parameter: x,y,z
        Body:
        Var: b;
        EndBody.
        Function: main
        Body: 
        z = {2,3,4};
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('z'),ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]))))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_undeclared_function93(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: x,y
        Body:
        x = 6.5;
        Return 1;
        x = 2.3;
        Return 3.0;
        EndBody.
        Function: main
        Body: 
        x = 3;
        EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_undeclared_function94(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Parameter: a
        Body:
	    Return a;
        EndBody.
        Function: main
        Body: 
        x = 3;
        EndBody."""
        expect = str(TypeCannotBeInferred(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_undeclared_function95(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: a
        Body:
        Var: x[2][3], y[2][3];
        x = y;
        EndBody.
        Function: main
        Body: 
        x = 3;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_undeclared_function96(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: foo
        Parameter: x
        Body:
	    Return 1;
        EndBody.
        Function: main
        Body:
	    Var: y = 2, foo;
	    y = foo(1);
        EndBody.
        """
        expect = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_undeclared_function97(self):
        """Simple program: main"""
        input = """
        Var: x,y =7.5,z;
        Function: b
        Parameter: x,y
        Body:
	    Return 1;
        EndBody.
        Function: main
        Body:
	    Var: y = 2;
	    y = b(1);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('b'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_undeclared_function98(self):
        """Simple program: main"""
        input = """
        Function: b
        Parameter: x, y, z
        Body:
        x = 1.9;
        y = True;
        Return 1.0;
        EndBody.
        Function: main
        Body:
        Var: z, t;
        z = b(1.3, True, t);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('z'),CallExpr(Id('b'),[FloatLiteral(1.3),BooleanLiteral(True),Id('t')]))))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_undeclared_function99(self):
        """Simple program: main"""
        input = """
        Function: a
        Parameter: x, y, z
        Body:
        x = 1.9;
        y = True;
        z = "anhtaideptrai";
        Return 1.0;
        EndBody.
        Function: main
        Body:
        Var: z, tt, m, n;
        z = a(m, n, tt);
        m = 34e-10;
        n = False;
        tt = 2;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('tt'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_undeclared_function100(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Body:
        EndBody.
        Function: masd
        Body: 
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,500))
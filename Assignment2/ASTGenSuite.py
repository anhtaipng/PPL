import unittest
from TestUtils import TestAST
from AST import *

# MSSV: 1813897
# Ho ten: Pham Nguyen Anh Tai

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x=10; Var: b[3];"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id('b'),[3],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Var: a,b;"""
        expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Var: a = "anhtaideptrai",b;"""
        expect = Program([VarDecl(Id('a'),[],StringLiteral('anhtaideptrai')),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """Var: a[3][5][8],b;"""
        expect = Program([VarDecl(Id('a'),[3,5,8],None),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """Var: a[3]={4,3,"taideptrai"},b;"""
        expect = Program([VarDecl(Id('a'),[3],ArrayLiteral([IntLiteral(4),IntLiteral(3),StringLiteral('taideptrai')])),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """Var: x; Var: y =19.01e8; Var:z;"""
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=None),VarDecl(variable=Id(name='y'), varDimen=[], varInit=\
        FloatLiteral(19.01e8)),VarDecl(variable=Id(name='z'), varDimen=[], varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_simple_program7(self):
        """Simple program: int main() {} """
        input = """Var: x; Var: y ="anhtaideptrai"; Var:z=12.0000;"""
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=None),VarDecl(variable=Id(name='y'), varDimen=[], varInit=\
        StringLiteral('anhtaideptrai')),VarDecl(variable=Id(name='z'), varDimen=[], varInit=FloatLiteral(12.0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_simple_program8(self):
        """Simple program: int main() {} """
        input = """Var: x = 0xFF;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(255))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_simple_program9(self):
        """Simple program: int main() {} """
        input = """Var: x = 0XFC;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(252))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_simple_program10(self):
        """Simple program: int main() {} """
        input = """Var: x = 0;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_simple_program11(self):
        """Simple program: int main() {} """
        input = """Var: x = 0o76;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(62))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_simple_program12(self):
        """Simple program: int main() {} """
        input = """Var: x = 0O66;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(54))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
 
    def test_simple_program13(self):
        """Simple program: int main() {} """
        input = """Var: x = 22.1e-4;"""
        expect = Program([VarDecl(Id('x'),[],FloatLiteral(22.1e-4))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))


    def test_simple_program14(self):
        input="""
        Function: fact
        Parameter: n,x,y
        Body:
        Var:x=10; 
        Var: b[3];
        EndBody."""
        expect = Program([FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None),VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None)],\
        ([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id('b'),[3],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_simple_program15(self):
        input="""
        Function: fact
        Parameter: n,x,y
        Body:
        Var:x=10; 
        Var: b[3];
        a = 10;
        b = 11;
        EndBody."""
        expect = Program([FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None),VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None)],\
        ([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id('b'),[3],None)],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))


    
    def test_simple_program16(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_simple_program117(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10;
        b = 11;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_simple_program18(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 == 5;
        b = 11 != 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('==',IntLiteral(10),IntLiteral(5))),Assign(Id('b'),BinaryOp('!=',IntLiteral(11),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_simple_program19(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 <=. 5;
        b = 11 >=. 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('<=.',IntLiteral(10),IntLiteral(5))),Assign(Id('b'),BinaryOp('>=.',IntLiteral(11),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_simple_program20(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 <= 5 && b;
        b = 11 =/= 4 || fact();
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('<=',IntLiteral(10),BinaryOp('&&',IntLiteral(5),Id('b')))),Assign(Id('b'),BinaryOp('=/=',IntLiteral(11),\
        BinaryOp('||',IntLiteral(4),CallExpr(Id('fact'),[]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_simple_program21(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 <=. -.5;
        b = 11 +- 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('<=.',IntLiteral(10),UnaryOp('-.',IntLiteral(5)))),Assign(Id('b'),BinaryOp('+',IntLiteral(11),\
        UnaryOp('-',IntLiteral(4))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_simple_program22(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a[5][foo()-1] = 10;
        b = 11;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(5),\
        BinaryOp('-',CallExpr(Id('foo'),[]),IntLiteral(1))]),IntLiteral(10)),\
        Assign(Id('b'),IntLiteral(11))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_simple_program23(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = 3;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_simple_program24(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_simple_program25(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_simple_program26(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        Else

        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_simple_program27(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        Else
        Var: y=9; Var: z;
        a = 9; b = 6;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],\
        ([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_simple_program28(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        ElseIf a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        ElseIf a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        Else
        Var: y=9; Var: z;
        a = 9; b = 6;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]),\
        (BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]),
        (BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],\
        ([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    
    def test_simple_program29(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a[5][foo()-1] = 10;
        b = 11;
        For (x = 2, 10, 1) Do
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        EndIf.
        EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(5),\
        BinaryOp('-',CallExpr(Id('foo'),[]),IntLiteral(1))]),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        For(Id('x'),IntLiteral(2),IntLiteral(10),IntLiteral(1),([],[If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_simple_program30(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        While a Do
        a = 10;
        b = 11;
        EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        While(Id('a'),([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_simple_program31(self):
        """Simple program: int main() {} """
        input = """
        Var: x=8.009;
        """
        expect = Program([VarDecl(Id('x'),[],FloatLiteral(8.009))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_simple_program32(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_simple_program33(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_simple_program34(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_simple_program35(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        foo(x,y);
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),CallStmt(Id('foo'),[Id('x'),Id('y')]),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_simple_program36(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        foo(x,y);
        Return foo();
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),CallStmt(Id('foo'),[Id('x'),Id('y')]),Return(CallExpr(Id('foo'),[]))\
        ,Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_simple_program37(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m <= n*.t;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('<=',Id('m'),BinaryOp('*.',Id('n'),Id('t'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_simple_program38(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m >= n*.t - 3;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('>=',Id('m'),BinaryOp('-',BinaryOp('*.',Id('n'),Id('t')),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_simple_program39(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m =/= n\.t - 3;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('=/=',Id('m'),BinaryOp('-',BinaryOp('\.',Id('n'),Id('t')),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_simple_program40(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -3;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',IntLiteral(3)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_simple_program41(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -foo();
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',CallExpr(Id('foo'),[])))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_simple_program42(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -foo();
        foo(m)[2][3] = 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',CallExpr(Id('foo'),[]))))),\
        Assign(ArrayCell(CallExpr(Id('foo'),[Id('m')]),[IntLiteral(2),IntLiteral(3)]), IntLiteral(4))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_simple_program43(self):
        """Simple program: int main() {} """
        input = """Var: x =10,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -foo();
        foo(m)[2][3] = 4 || foo(a[2][b-2],1);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',CallExpr(Id('foo'),[]))))),\
        Assign(ArrayCell(CallExpr(Id('foo'),[Id('m')]),[IntLiteral(2),IntLiteral(3)]), BinaryOp('||',IntLiteral(4),\
        CallExpr(Id('foo'),[ArrayCell(Id('a'),[IntLiteral(2),BinaryOp('-',Id('b'),IntLiteral(2))]),IntLiteral(1)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_simple_program44(self):
        """Simple program: int main() {} """
        input = """Var: a[1][3][3][0o7777][0xFF]=0;"""
        expect = Program([VarDecl(Id('a'),[1,3,3,4095,255],IntLiteral(0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_simple_program45(self):
        """Simple program: int main() {} """
        input = """Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    If True Then
                        Break;
                    EndIf.
                    Continue;
                    
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),\
        BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([],[If([(BooleanLiteral(True),[],[Break()])],([],[])),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_simple_program46(self):
        """Simple program: int main() {} """
        input = """Function: function
            Parameter: i, arr[101]
            Body:
                While (True != !False) Do
                    WhileFalseDoWhileTrueDoEndWhile.
                EndWhile.EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[101],None)],([],[While(BinaryOp('!=',BooleanLiteral(True),\
        UnaryOp('!',BooleanLiteral(False))),([],[While(BooleanLiteral(False),([],[While(BooleanLiteral(True),([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_simple_program47(self):
        """Simple program: int main() {} """
        input = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Do
                Var: j = 0;
                    Do
                        j = i;
                    While 0. \. j
                    EndDo.
                While 0 == 0x1-0X1
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Dowhile(([VarDecl(Id('j'),[],\
        IntLiteral(0))],[Dowhile(([],[Assign(Id('j'),Id('i'))]),BinaryOp('\\.',FloatLiteral(0.0),Id('j')))]),BinaryOp('==',IntLiteral(0),\
        BinaryOp('-',IntLiteral(1),IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_simple_program48(self):
        """Simple program: int main() {} """
        input = """Function: function
            Body:
                If (21 == 4 || 18) 
                Then
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[],([],[If([(BinaryOp('==',IntLiteral(21),BinaryOp('||',IntLiteral(4),IntLiteral(18))),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_simple_program49(self):
        """Simple program: int main() {} """
        input = """Function: function
            Parameter: i
            Body:
                DoWhileTrueDoDoWhileFalseEndDo.EndWhile.WhileTrue=/=TrueEndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None)],([],[Dowhile(([],[While(BooleanLiteral(True),\
        ([],[Dowhile(([],[]),BooleanLiteral(False))]))]),BinaryOp('=/=',BooleanLiteral(True),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_simple_program50(self):
        """Simple program: int main() {} """
        input = """Var:x=3; Var: b[0xFF];"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id('b'),[255],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_simple_program51(self):
        """Simple program: int main() {} """
        input = """Var: t,q;"""
        expect = Program([VarDecl(Id('t'),[],None),VarDecl(Id('q'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_simple_program52(self):
        """Simple program: int main() {} """
        input = """Var: a = {"anhtaicuckydeptrai"};"""
        expect = Program([VarDecl(Id('a'),[],ArrayLiteral([StringLiteral('anhtaicuckydeptrai')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_simple_program53(self):
        """Simple program: int main() {} """
        input = """Var: a[100][25][81],b;"""
        expect = Program([VarDecl(Id('a'),[100,25,81],None),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_simple_program54(self):
        """Simple program: int main() {} """
        input = """Var: a[3]={44,33,"taideptrai"},b;"""
        expect = Program([VarDecl(Id('a'),[3],ArrayLiteral([IntLiteral(44),IntLiteral(33),StringLiteral('taideptrai')])),VarDecl(Id('b'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_simple_program55(self):
        """Simple program: int main() {} """
        input = """Var: z;"""
        expect = Program([VarDecl(variable=Id(name='z'), varDimen=[], varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_simple_program56(self):
        """Simple program: int main() {} """
        input = """Var: a; Var: b =19.01e-98; Var:c;"""
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[], varInit=None),VarDecl(variable=Id(name='b'), varDimen=[], varInit=\
        FloatLiteral(19.01e-98)),VarDecl(variable=Id(name='c'), varDimen=[], varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_simple_program57(self):
        """Simple program: int main() {} """
        input = """Var: x; Var: y ="taideptrai"; Var:z=12.0000;"""
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=None),VarDecl(variable=Id(name='y'), varDimen=[], varInit=\
        StringLiteral('taideptrai')),VarDecl(variable=Id(name='z'), varDimen=[], varInit=FloatLiteral(12.0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_simple_program58(self):
        """Simple program: int main() {} """
        input = """Var: x = 0xABC;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(2748))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_simple_program59(self):
        """Simple program: int main() {} """
        input = """Var: x = 0XFCEA;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(64746))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_simple_program60(self):
        """Simple program: int main() {} """
        input = """Var: x = 87;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(87))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_simple_program61(self):
        """Simple program: int main() {} """
        input = """Var: x = 0o75;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(61))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_simple_program62(self):
        """Simple program: int main() {} """
        input = """Var: x = 0O76;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(62))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
 
    def test_simple_program63(self):
        """Simple program: int main() {} """
        input = """Var: x = 22.e-4;"""
        expect = Program([VarDecl(Id('x'),[],FloatLiteral(22.e-4))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))


    def test_simple_program64(self):
        input="""
        Function: fact
        Parameter: n,x,y
        Body:
        Var:x=3; 
        Var: b[10];
        EndBody."""
        expect = Program([FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None),VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None)],\
        ([VarDecl(Id("x"),[],IntLiteral(3)),VarDecl(Id('b'),[10],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_simple_program65(self):
        input="""
        Function: fact
        Parameter: n,x,y
        Body:
        Var:x=10; 
        Var: b[3];
        a = 101;
        b = 111;
        EndBody."""
        expect = Program([FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None),VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None)],\
        ([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id('b'),[3],None)],[Assign(Id('a'),IntLiteral(101)),Assign(Id('b'),IntLiteral(111))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))


    
    def test_simple_program66(self):
        """Simple program: int main() {} """
        input = """Var: x = 101;
        Function: main
        Body:
        a = 101;
        b = 111;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(101)),Assign(Id('b'),IntLiteral(111))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_simple_program67(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 99, z;
        a = 101;
        b = 111;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(99)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),IntLiteral(101)),Assign(Id('b'),IntLiteral(111))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_simple_program68(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9999, z;
        a = 10 == 5;
        b = 11 != 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9999)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('==',IntLiteral(10),IntLiteral(5))),Assign(Id('b'),BinaryOp('!=',IntLiteral(11),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_simple_program69(self):
        """Simple program: int main() {} """
        input = """Var: x = 101;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 <=. 5;
        b = 11 >=. 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('<=.',IntLiteral(10),IntLiteral(5))),Assign(Id('b'),BinaryOp('>=.',IntLiteral(11),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_simple_program70(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 <= 5 && b;
        b = 11 =/= 4 || fact(a,b);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('<=',IntLiteral(10),BinaryOp('&&',IntLiteral(5),Id('b')))),Assign(Id('b'),BinaryOp('=/=',IntLiteral(11),\
        BinaryOp('||',IntLiteral(4),CallExpr(Id('fact'),[Id('a'),Id('b')]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_simple_program71(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        Var: y = 9, z;
        a = 10 <=. -.5;
        b = 11 +- 24;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],\
        [Assign(Id('a'),BinaryOp('<=.',IntLiteral(10),UnaryOp('-.',IntLiteral(5)))),Assign(Id('b'),BinaryOp('+',IntLiteral(11),\
        UnaryOp('-',IntLiteral(24))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_simple_program72(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a[5][foo()*1] = 10;
        b = 11;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(5),\
        BinaryOp('*',CallExpr(Id('foo'),[]),IntLiteral(1))]),IntLiteral(10)),\
        Assign(Id('b'),IntLiteral(11))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_simple_program73(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[22][0x3] = 3;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(22), IntLiteral(3)]),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_simple_program74(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][300] = b -c[2][4];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(300)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_simple_program75(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 69;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(69))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_simple_program76(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 999; b = 6;
        Else

        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(999)),Assign(Id('b'),IntLiteral(6))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_simple_program77(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[22][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        Else
        Var: y=9; Var: z;
        a = 9; b = 6;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(22),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],\
        ([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_simple_program78(self):
        """Simple program: int main() {} """
        input = """Function: main
        Body:
        a[2][3] = b -c[2][4];
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        ElseIf a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        ElseIf a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        Else
        Var: y=9; Var: z;
        a = 9; b = 69;
        EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(2), IntLiteral(3)]),BinaryOp('-',\
        Id('b'),ArrayCell(Id('c'),[IntLiteral(2),IntLiteral(4)]))),If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]),\
        (BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))]),
        (BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],\
        ([VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(69))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    
    def test_simple_program79(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a[5][foo()-1] = 10;
        b = 11;
        For (x = 2, 1000, 1) Do
        If a>c Then Var: y=9; Var: z;
        a = 9; b = 6;
        EndIf.
        EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(5),\
        BinaryOp('-',CallExpr(Id('foo'),[]),IntLiteral(1))]),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        For(Id('x'),IntLiteral(2),IntLiteral(1000),IntLiteral(1),([],[If([(BinaryOp('>',Id('a'),Id('c')),\
        [VarDecl(Id('y'),[],IntLiteral(9)),VarDecl(Id('z'),[],None)],[Assign(Id('a'),IntLiteral(9)),Assign(Id('b'),IntLiteral(6))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_simple_program80(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        While a Do
        a = 10;
        b = 119;
        EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        While(Id('a'),([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(119))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_simple_program81(self):
        """Simple program: int main() {} """
        input = """
        Var: x=82.009;
        """
        expect = Program([VarDecl(Id('x'),[],FloatLiteral(82.009))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_simple_program82(self):
        """Simple program: int main() {} """
        input = """Var: x = 10;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        b = 111;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(10)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(111))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_simple_program83(self):
        """Simple program: int main() {} """
        input = """Var: x = 101;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_simple_program84(self):
        """Simple program: int main() {} """
        input = """Var: x = 101;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_simple_program85(self):
        """Simple program: int main() {} """
        input = """Var: x = 101;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        foo(x,y);
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),CallStmt(Id('foo'),[Id('x'),Id('y')]),Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_simple_program86(self):
        """Simple program: int main() {} """
        input = """Var: x = 101;
        Function: main
        Body:
        a = 10;
        b = 11;
        Do
        a = 10;
        Break;
        Continue;
        foo(x,y);
        Return foo();
        b = 11;
        While a
        EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10)),Assign(Id('b'),IntLiteral(11)),\
        Dowhile(([],[Assign(Id('a'),IntLiteral(10)),Break(),Continue(),CallStmt(Id('foo'),[Id('x'),Id('y')]),Return(CallExpr(Id('foo'),[]))\
        ,Assign(Id('b'),IntLiteral(11))]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_simple_program87(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m <= n*.t;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('<=',Id('m'),BinaryOp('*.',Id('n'),Id('t'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_simple_program88(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m >= n*.t - 3;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('>=',Id('m'),BinaryOp('-',BinaryOp('*.',Id('n'),Id('t')),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_simple_program89(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m =/= n\.t - 3;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('=/=',Id('m'),BinaryOp('-',BinaryOp('\.',Id('n'),Id('t')),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_simple_program90(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -3;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',IntLiteral(3)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_simple_program91(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -foo();
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',CallExpr(Id('foo'),[])))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_simple_program92(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -foo();
        foo(m)[2][3] = 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',CallExpr(Id('foo'),[]))))),\
        Assign(ArrayCell(CallExpr(Id('foo'),[Id('m')]),[IntLiteral(2),IntLiteral(3)]), IntLiteral(4))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_simple_program93(self):
        """Simple program: int main() {} """
        input = """Var: x =101,z;
        Function: main
        Parameter: m,n,t
        Body:
        Return m && n%t + -foo();
        foo(m)[2][3] = 4 || foo(a[2][b-2],1);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(101)),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),\
        VarDecl(Id('t'),[],None)],([],[Return(BinaryOp('&&',Id('m'),BinaryOp('+',BinaryOp('%',Id('n'),Id('t')),UnaryOp('-',CallExpr(Id('foo'),[]))))),\
        Assign(ArrayCell(CallExpr(Id('foo'),[Id('m')]),[IntLiteral(2),IntLiteral(3)]), BinaryOp('||',IntLiteral(4),\
        CallExpr(Id('foo'),[ArrayCell(Id('a'),[IntLiteral(2),BinaryOp('-',Id('b'),IntLiteral(2))]),IntLiteral(1)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    
    def test_simple_program94(self):
        """Simple program: int main() {} """
        input = """Var: a[1][3][3][0o77][0xFF]=0;"""
        expect = Program([VarDecl(Id('a'),[1,3,3,63,255],IntLiteral(0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    
    def test_simple_program95(self):
        """Simple program: int main() {} """
        input = """Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 99, 0O1) Do
                    If True Then
                        Break;
                    EndIf.
                    Continue;
                    
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),\
        BinaryOp('<',Id('i'),IntLiteral(99)),IntLiteral(1),([],[If([(BooleanLiteral(True),[],[Break()])],([],[])),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_simple_program96(self):
        """Simple program: int main() {} """
        input = """Function: function
            Parameter: i, arr[1021]
            Body:
                While (True != !False) Do
                    WhileFalseDoWhileTrueDoEndWhile.
                EndWhile.EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1021],None)],([],[While(BinaryOp('!=',BooleanLiteral(True),\
        UnaryOp('!',BooleanLiteral(False))),([],[While(BooleanLiteral(False),([],[While(BooleanLiteral(True),([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_simple_program97(self):
        """Simple program: int main() {} """
        input = r"""Function: function
            Parameter: i, arr[1100]
            Body:
                Do
                Var: j = 0;
                    Do
                        j = i;
                    While 0. \. j
                    EndDo.
                While 0 == 0x1-0X1
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1100],None)],([],[Dowhile(([VarDecl(Id('j'),[],\
        IntLiteral(0))],[Dowhile(([],[Assign(Id('j'),Id('i'))]),BinaryOp('\\.',FloatLiteral(0.0),Id('j')))]),BinaryOp('==',IntLiteral(0),\
        BinaryOp('-',IntLiteral(1),IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_simple_program98(self):
        """Simple program: int main() {} """
        input = """Function: function
            Body:
                If (21 == 4 || 181) 
                Then
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[],([],[If([(BinaryOp('==',IntLiteral(21),BinaryOp('||',IntLiteral(4),IntLiteral(181))),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_simple_program99(self):
        """Simple program: int main() {} """
        input = """Function: function
            Parameter: z
            Body:
                DoWhileTrueDoDoWhileFalseEndDo.EndWhile.WhileTrue=/=TrueEndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('z'),[],None)],([],[Dowhile(([],[While(BooleanLiteral(True),\
        ([],[Dowhile(([],[]),BooleanLiteral(False))]))]),BinaryOp('=/=',BooleanLiteral(True),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))




 
   
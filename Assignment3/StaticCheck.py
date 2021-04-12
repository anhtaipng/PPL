
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

# Pham Nguyen Anh Tai
# 1813897

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)


    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def find_id(self, name, lst_lst_sym):
        for x in lst_lst_sym:
            for y in x:
                if name.lower() == y.name.lower():
                    return y
        return None

    def checkArrayType(self, mtype1, mtype2):
        if type(mtype1) is ArrayType and type(mtype2) is ArrayType:
            if mtype1.dimen != mtype2.dimen or type(mtype1.eletype) != type(mtype2.eletype):
                return False
        return True



    def toArrayType(self, decl):
        if decl.varInit:
            return Symbol(decl.variable.name, self.visit(decl.varInit, None))
        else:
            return Symbol(decl.variable.name, ArrayType(decl.varDimen, Unknown()))


    def toSymbol(self, decl):
        if type(decl) == VarDecl:
            if decl.varDimen == [] :
                if decl.varInit :
                    return Symbol(decl.variable.name, self.visit(decl.varInit, None))
                else:
                    return Symbol(decl.variable.name, Unknown())
            else:
                return self.toArrayType(decl)
        elif type(decl) == FuncDecl:
            return Symbol(decl.name.name, MType([Unknown() for i in decl.param], Unknown()))

    def toLstSymbol(self, listDecl, listSym, kind, listGlobal=None):
        for x in listDecl:
            sym = self.toSymbol(x)
            res = self.lookup(sym.name.lower(), listSym, lambda y: y.name.lower())
            res1 = None
            if listGlobal:
                res1 = self.lookup(sym.name.lower(), listGlobal, lambda y: y.name.lower())
            if res is None and res1 is None:
                listSym.insert(len(listSym), sym)
            elif type(sym.mtype) is MType:
                raise Redeclared(Function(), sym.name)
            elif kind == Parameter:
                raise Redeclared(Parameter(), sym.name)
            else:
                raise Redeclared(Variable(), sym.name)






    def visitProgram(self,ast, o):
        list_global = []
        self.toLstSymbol(ast.decl, list_global, None, o)

        if  list(filter(lambda x: x.name.lower() == 'main', list_global)) == []:
            raise NoEntryPoint()
        
        for x in ast.decl:
            self.visit(x, list_global + o)

    
    def visitVarDecl(self, ast, o):
        return
    
    def visitFuncDecl(self, ast, o):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]
        sym = self.lookup(ast.name.name.lower(), o, lambda y: y.name.lower())
        local_var = []
        self.toLstSymbol(ast.param, local_var, Parameter)
        lenParams = len(local_var)
        for i in range(len(local_var)): #cap nhat type cua param neu da duoc suy dien kieu
            if not type(sym.mtype.intype[i]) is Unknown:
                local_var[i].mtype = sym.mtype.intype[i]

        self.toLstSymbol(ast.body[0], local_var, None)
        
        varr = [local_var] + [o]

        for x in ast.body[1]:
            self.visit(x, (varr, sym))

        for i in range(lenParams): #cap nhat lai type cua param
            sym.mtype.intype[i] = local_var[i].mtype

    #c[0] : list sym [[local], [non_local],..]
    #c[1] : symbol cua function trong list global

    def visitDowhile(self, ast, c):
        # sl:Tuple[List[VarDecl],List[Stmt]]
        # exp: Expr
        local_var = []
        self.toLstSymbol(ast.sl[0], local_var, None)
        varr = [local_var] + c[0]
        for x in ast.sl[1]:
            self.visit(x, (varr, c[1]))

        typ_exp = self.visit(ast.exp, (c[0], BoolType(), ast))
        if not type(typ_exp) is BoolType:
            raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        # exp: Expr
        # sl:Tuple[List[VarDecl],List[Stmt]]
        typ_exp = self.visit(ast.exp, (c[0], BoolType(), ast))
        if not type(typ_exp) is BoolType:
            raise TypeMismatchInStatement(ast)

        local_var = []
        self.toLstSymbol(ast.sl[0], local_var, None)
        varr = [local_var] + c[0]
        for x in ast.sl[1]:
            self.visit(x, (varr, c[1]))

    def visitFor(self, ast, c):
        # idx1: Id
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop: Tuple[List[VarDecl],List[Stmt]]
        typ_idx = self.visit(ast.idx1, (c[0], IntType(), ast))
        if not type(typ_idx) is IntType:
            raise TypeMismatchInStatement(ast)
        typ1 = self.visit(ast.expr1, (c[0], IntType(), ast))
        if not type(typ1) is IntType:
            raise TypeMismatchInStatement(ast)
        typ2 = self.visit(ast.expr2, (c[0], BoolType(), ast))
        if not type(typ2) is BoolType:
            raise TypeMismatchInStatement(ast)
        typ3 = self.visit(ast.expr3, (c[0], IntType(), ast))
        if not type(typ3) is IntType:
            raise TypeMismatchInStatement(ast)

        local_var = []
        self.toLstSymbol(ast.loop[0], local_var, None)
        varr = [local_var] + c[0]
        for x in ast.loop[1]:
            self.visit(x, (varr, c[1]))

    def visitIf(self, ast, c):
        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        for x in ast.ifthenStmt:
            # x[0] = Expr
            # x[1] = List[VarDecl]
            # x[2] = List[Stmt]
            typ = self.visit(x[0], (c[0], BoolType(), ast))
            if not type(typ) is BoolType:
                raise TypeMismatchInStatement(ast)

            local_var = []
            self.toLstSymbol(x[1], local_var, None)
            varr = [local_var] + c[0]
            for y in x[2]:
                self.visit(y, (varr, c[1]))
        
        if ast.elseStmt != []:
            local_var = []
            self.toLstSymbol(ast.elseStmt[0], local_var, None)
            varr = [local_var] + c[0]

            for y in ast.elseStmt[1]:
                self.visit(y, (varr, c[1]))

    def visitCallStmt(self, ast, c):
        # method:Id
        # param:List[Expr]
        sym = self.find_id(ast.method.name.lower(), c[0])
        
        if sym is None or not type(sym.mtype) is MType:
            raise Undeclared(Function(), ast.method.name)
        elif len(sym.mtype.intype) != len(ast.param) and not type(sym.mtype.restype) is VoidType():
            raise TypeMismatchInStatement(ast)
        else:
            sym.mtype.restype = VoidType()
            for i in range(len(ast.param)):
                if type(ast.param[i]) is CallExpr:
                    if type(self.visit(ast.param[i], (c[0], Unknown(), ast))) is VoidType:
                        raise TypeMismatchInStatement(ast)
                    if ast.param[i].method.name.lower() == ast.method.name.lower():
                        sym.mtype.intype[i] = sym.mtype.restype
                if type(sym.mtype.intype[i]) is Unknown:
                    type_param_i = self.visit(ast.param[i], (c[0], Unknown(), ast))
                    if type(type_param_i) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                            sym.mtype.intype[i] = type_param_i
                else:
                    type_param_i = self.visit(ast.param[i], (c[0], sym.mtype.intype[i], ast))
                    if type(sym.mtype.intype[i]) != type(type_param_i) or not self.checkArrayType(sym.mtype.intype[i], type_param_i):
                        raise TypeMismatchInStatement(ast)
        
    
    def visitReturn(self, ast, c):
        #expr:Expr # None if no expression
        if ast.expr is None:
            if type(c[1].mtype.restype) is Unknown:
                c[1].mtype.restype = VoidType()
            elif type(c[1].mtype.restype) != VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            if type(c[1].mtype.restype) is Unknown: 
                typ = self.visit(ast.expr, (c[0], Unknown(), ast))
                if type(typ) is ArrayType:
                    if type(typ.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                if type(typ) is Unknown:
                    raise TypeCannotBeInferred(ast)
                if type(typ) is VoidType:
                    raise TypeMismatchInStatement(ast)
                c[1].mtype.restype = typ
            else:
                typ = self.visit(ast.expr, (c[0], c[1].mtype.restype, ast))
                
                if type(typ) != type(c[1].mtype.restype) or type(typ) is VoidType or not self.checkArrayType(typ, c[1].mtype.restype):
                    raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, c):
        # lhs: LHS
        # rhs: Expr
        
        lhs = self.visit(ast.lhs, (c[0], Unknown(), ast))
        rhs = self.visit(ast.rhs, (c[0], Unknown(), ast))
        
        if type(rhs) is ArrayType and not type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs) == Unknown and type(rhs) == Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) == Unknown or type(rhs) == Unknown:# ep kieu
                if type(lhs) == Unknown:
                    if type(rhs) is ArrayType:
                        if type(rhs.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                    lhs = self.visit(ast.lhs, (c[0], rhs, ast))
                if type(rhs) == Unknown:
                    if type(lhs) is ArrayType:
                        if type(lhs.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                    rhs = self.visit(ast.rhs, (c[0], lhs, ast))
                if type(lhs) != type(rhs) or type(lhs) == VoidType:
                    raise TypeMismatchInStatement(ast)
                
        elif type(lhs) != type(rhs) or type(lhs) == VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs) == ArrayType and type(rhs) == ArrayType: #xu ly arraytype
            if type(lhs.eletype) == Unknown and type(rhs.eletype) == Unknown:
                raise TypeCannotBeInferred(ast)
            elif lhs.dimen == rhs.dimen and (type(lhs.eletype) == Unknown or type(rhs.eletype) == Unknown):
                if type(lhs.eletype) == Unknown:
                    self.visit(ast.lhs, (c[0], rhs.eletype, ast))
                if type(rhs.eletype) == Unknown:
                    self.visit(ast.rhs, (c[0], lhs.eletype, ast))
            elif lhs.dimen != rhs.dimen or type(lhs.eletype) != type(rhs.eletype):
                raise TypeMismatchInStatement(ast)
        


    def visitContinue(self, ast, c):
        return

    def visitBreak(self, ast, c):
        return


    #expr_param gom
    #expr_param[0] : c[0] -> list sym [[local], [non_local],..]
    #expr_param[1] : type de infer, neu ko ep kieu thi truyen vao Unknown()
    #expr_param[2] : stmt dang xet


    def visitUnaryOp(self, ast, expr_param):
        # op:str
        # body:Expr
        op = ast.op
        if op == '!':
            typ = self.visit(ast.body, (expr_param[0], BoolType(), expr_param[2]))
            if not type(typ) in [BoolType]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op == '-':
            typ =self.visit(ast.body, (expr_param[0], IntType(), expr_param[2]))
            if not type(typ) in [IntType]:
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif op == '-.':
            typ = self.visit(ast.body, (expr_param[0], FloatType(), expr_param[2]))
            if not type(typ) in [FloatType]:
                raise TypeMismatchInExpression(ast)
            return FloatType()

    def visitBinaryOp(self, ast, expr_param):
        # op:str
        # left:Expr
        # right:Expr
        op = ast.op
        if op in ['-','+','*','\\','%']: #5
            left_type = self.visit(ast.left, (expr_param[0], IntType(), expr_param[2]))
            right_type = self.visit(ast.right, (expr_param[0], IntType(), expr_param[2]))
            if not (type(left_type) in [IntType] and type(right_type) in [IntType]):
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif op in ['-.','+.','*.','\\.']: #4
            left_type = self.visit(ast.left, (expr_param[0], FloatType(), expr_param[2]))
            right_type = self.visit(ast.right, (expr_param[0], FloatType(), expr_param[2]))
            if not (type(left_type) in [FloatType] or type(right_type) in [FloatType]):
                raise TypeMismatchInExpression(ast)
            return FloatType()
        elif op in ['==','!=','<','>','<=','>=']: #6
            left_type = self.visit(ast.left, (expr_param[0], IntType(), expr_param[2]))
            right_type = self.visit(ast.right, (expr_param[0], IntType(), expr_param[2]))
            if not (type(left_type) in [IntType] and type(right_type) in [IntType]):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['=/=','<.','>.','<=.','>=.']: #5
            left_type = self.visit(ast.left, (expr_param[0], FloatType(), expr_param[2]))
            right_type = self.visit(ast.right, (expr_param[0], FloatType(), expr_param[2]))
            if not (type(left_type) in [FloatType] and type(right_type) in [FloatType]):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['&&','||']: #2
            left_type = self.visit(ast.left, (expr_param[0], BoolType(), expr_param[2]))
            right_type = self.visit(ast.right, (expr_param[0], BoolType(), expr_param[2]))
            if not (type(left_type) in [BoolType] and type(right_type) in [BoolType]):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        


    def visitArrayCell(self, ast, expr_param):
        # arr:Expr
        # idx:List[Expr]
        
        if type(expr_param[1]) is Unknown:
            arr_type = self.visit(ast.arr, expr_param)
            if type(ast.arr) is CallExpr:
                if type(arr_type) is Unknown:
                    raise TypeCannotBeInferred(expr_param[2])
            if not type(arr_type) is ArrayType or len(arr_type.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
            for x in ast.idx:
                typ = self.visit(x, (expr_param[0], IntType(), expr_param[2]))
                if not type(typ) is IntType:
                    raise TypeMismatchInExpression(ast)
            return arr_type.eletype
        else:
            arr_type = self.visit(ast.arr, expr_param)
            if type(ast.arr) is CallExpr:
                if type(arr_type) is Unknown:
                    raise TypeCannotBeInferred(expr_param[2])
            if not type(arr_type) is ArrayType or len(arr_type.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
            for x in ast.idx:
                typ = self.visit(x, (expr_param[0], IntType(), expr_param[2]))
                if not type(typ) is IntType:
                    raise TypeMismatchInExpression(ast)
            arr_type.eletype = expr_param[1]
            return arr_type.eletype

    def visitCallExpr(self, ast, expr_param):
        # method:Id
        # param:List[Expr]
        sym = self.find_id(ast.method.name.lower(), expr_param[0])
        if type(expr_param[1]) is Unknown:
            if sym is None or not type(sym.mtype) is MType:
                raise Undeclared(Function(), ast.method.name)
            elif len(sym.mtype.intype) != len(ast.param):
                raise TypeMismatchInExpression(ast)
            else:
                for i in range(len(ast.param)):
                    if type(ast.param[i]) is CallExpr:
                        if ast.param[i].method.name.lower() == ast.method.name.lower():
                            sym.mtype.intype[i] = sym.mtype.restype
                    if type(sym.mtype.intype[i]) is Unknown:
                        type_param_i = self.visit(ast.param[i], (expr_param[0], Unknown(), expr_param[2]))
                        if type(type_param_i) is Unknown:
                            raise TypeCannotBeInferred(expr_param[2])
                        elif type(type_param_i) is VoidType:
                            raise TypeMismatchInExpression(ast)
                        else:
                            sym.mtype.intype[i] = type_param_i
                    else:
                        type_param_i = self.visit(ast.param[i], (expr_param[0], sym.mtype.intype[i], expr_param[2]))
                        if type(sym.mtype.intype[i]) != type(type_param_i) or type(type_param_i) is VoidType \
                        or not self.checkArrayType(sym.mtype.intype[i], type_param_i):
                            raise TypeMismatchInExpression(ast)
        else:
            if sym is None or not type(sym.mtype) is MType:
                raise Undeclared(Function(), ast.method.name)
            elif len(sym.mtype.intype) != len(ast.param):
                raise TypeMismatchInExpression(ast)
            if type(sym.mtype.restype) is Unknown:
                sym.mtype.restype = expr_param[1]
            for i in range(len(ast.param)):
                if type(ast.param[i]) is CallExpr:
                    if ast.param[i].method.name.lower() == ast.method.name.lower():
                        sym.mtype.intype[i] = sym.mtype.restype
                if type(sym.mtype.intype[i]) is Unknown:
                    type_param_i = self.visit(ast.param[i], (expr_param[0], Unknown(), expr_param[2]))
                    if type(type_param_i) is Unknown:
                        raise TypeCannotBeInferred(expr_param[2])
                    elif type(type_param_i) is VoidType:
                        raise TypeMismatchInExpression(ast)
                    else:
                        sym.mtype.intype[i] = type_param_i
                else:
                    type_param_i = self.visit(ast.param[i], (expr_param[0], sym.mtype.intype[i], expr_param[2]))
                    if type(sym.mtype.intype[i]) != type(type_param_i) or type(type_param_i) is VoidType\
                    or not self.checkArrayType(sym.mtype.intype[i], type_param_i):
                        raise TypeMismatchInExpression(ast)
        return sym.mtype.restype
        
    def visitId(self, ast, expr_param):
        #name: str
        if type(expr_param[1]) is Unknown :
            sym = self.find_id(ast.name, expr_param[0])
            if sym is None:
                raise Undeclared(Identifier(), ast.name)
            elif type(sym.mtype) is MType:
                raise Undeclared(Identifier(), ast.name)
            return sym.mtype
        else:
            sym = self.find_id(ast.name, expr_param[0])
            if sym is None:
                raise Undeclared(Identifier(), ast.name)
            elif type(sym.mtype) is MType:
                raise Undeclared(Identifier(), ast.name)
            if type(sym.mtype) is Unknown:
                sym.mtype = expr_param[1]
            if type(sym.mtype) is ArrayType:
                if type(sym.mtype.eletype) is Unknown:
                    sym.mtype.eletype = expr_param[1]
            return sym.mtype

    def visitIntLiteral(self, ast, c):
        # value: int
        return IntType()

    def visitFloatLiteral(self, ast, c):
        # value: float
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        # value: boolean
        return BoolType()

    def visitStringLiteral(self, ast, c):
        # value: string
        return StringType()

    def visitArrayLiteral(self, ast, c):
        #value: List[Literal]
        dimen = []
        if type(ast.value[0]) is ArrayLiteral:
            temp = ast.value
            while True:
                dimen += [len(temp)]
                if not type(temp[0]) is ArrayLiteral:
                    break
                temp = temp[0].value
            return ArrayType(dimen, self.visit(temp[0], None))
        else:
            return ArrayType([len(ast.value)], self.visit(ast.value[0], None))
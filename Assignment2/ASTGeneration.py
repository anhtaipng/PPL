from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

# MSSV: 1813897
# Ho ten: Pham Nguyen Anh Tai

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        lstdecl = []
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstdecl = lstdecl + decl
                else:
                    lstdecl.append(decl)
        if ctx.funcdecl():
            for x in ctx.funcdecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstdecl = lstdecl + decl
                else:
                    lstdecl.append(decl)
        return Program(lstdecl)

    def visitVardecl(self, ctx:BKITParser.VardeclContext):
        return self.visit(ctx.varlist())

    def visitVarlist(self, ctx:BKITParser.VarlistContext):
        varlst = list(self.visit(x) for x in ctx.variable())
        return varlst

    def visitVariable(self, ctx:BKITParser.VariableContext):
        initValue = None
        if ctx.literal():
            initValue = self.visit(ctx.literal())
        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],initValue)
        else:
            dimenArray = []
            dimenArray = self.visit(ctx.compositevar())
            return VarDecl(Id(dimenArray[0].getText()),dimenArray[1:],initValue)

    def visitCompositevar(self, ctx: BKITParser.CompositevarContext):
        dimenArray = [0]
        dimenArray[0] = ctx.ID()
        for x in ctx.INTLIT():
            a = x.getText()
            if a[0]=='0' and len(a)==1:
                dimenArray.append(0)
            elif a[0]=='0' and (a[1]=='x' or a[1]=='X'):
                result = int(a, 16)
                dimenArray.append(result)
            elif a[0]=='0' and (a[1]=='o' or a[1]=='O'):
                result = int(a, 8)
                dimenArray.append(result)
            else:
                dimenArray.append(int(x.getText()))
        return dimenArray
        
    def visitArray(self, ctx:BKITParser.ArrayContext):
        array = []
        for x in ctx.literal():
            lit = self.visit(x)
            if type(lit) == type([]):
                array = array + lit
            else:
                array.append(lit)
        return ArrayLiteral(array)

    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.INTLIT():
            a = ctx.INTLIT().getText()
            if a[0]=='0' and len(a)==1:
                return IntLiteral(0)
            elif a[0]=='0' and (a[1]=='x' or a[1]=='X'):
                result = int(a, 16)
                return IntLiteral(result)
            elif a[0]=='0' and (a[1]=='o' or a[1]=='O'):
                result = int(a, 8)
                return IntLiteral(result)
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.boollit():
            return self.visit(ctx.boollit())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.array():
            return self.visit(ctx.array())

    def visitBoollit(self, ctx: BKITParser.BoollitContext):
        str1 = ctx.getText()
        if len(str1) == 4:
            return BooleanLiteral(True)
        elif len(str1) == 5:
            return BooleanLiteral(False)
    
    def visitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        param = []
        lstVarDecl = []
        lstStmt = []
        if ctx.paramlist():
            param = self.visit(ctx.paramlist())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        return FuncDecl(Id(ctx.ID().getText()),param,(lstVarDecl, lstStmt))
    
    def visitParamlist(self, ctx:BKITParser.ParamlistContext):
        paramlist = list( self.visit(x) for x in ctx.param())
        return paramlist

    def visitParam(self, ctx: BKITParser.ParamContext):
        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],None)
        else:
            dimenArray = []
            dimenArray = self.visit(ctx.compositevar())
            return VarDecl(Id(dimenArray[0].getText()),dimenArray[1:],None)
            
    
    def visitStmt(self, ctx: BKITParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssignstmt(self, ctx:BKITParser.AssignstmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return Assign(lhs, rhs)

    def visitLhs(self, ctx: BKITParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.eleexpr():
            return self.visit(ctx.eleexpr())
    
    def visitEleexpr( self, ctx:BKITParser.EleexprContext):
        arr = Id(ctx.ID().getText()) if (ctx.ID()) else self.visit(ctx.callexpr())
        idx = self.visit(ctx.afterexpr())
        return ArrayCell(arr,idx)

    def visitAfterexpr(self, ctx:BKITParser.AfterexprContext):
        return list(self.visit(x) for x in ctx.expr())
    
    
    def visitExpr(self, ctx: BKITParser.ExprContext):
        op =''
        if ctx.EQEQ():
            op = ctx.EQEQ().getText()
        elif ctx.NOTEQ():
            op = ctx.NOTEQ().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GTE():
            op = ctx.GTE().getText()
        elif ctx.NOTEQF():
            op = ctx.NOTEQF().getText()
        elif ctx.LTF():
            op = ctx.LTF().getText()
        elif ctx.GTF():
            op = ctx.GTF().getText()
        elif ctx.LTEF():
            op = ctx.LTEF().getText()
        elif ctx.GTEF():
            op = ctx.GTEF().getText()
        else:
            return self.visit(ctx.expr1(0))
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)

    def visitExpr1(self, ctx: BKITParser.Expr1Context):
        op=''
        if ctx.CNJ():
            op = ctx.CNJ().getText()
        elif ctx.DSJ():
            op = ctx.DSJ().getText()
        else:
            return self.visit(ctx.expr2())
        left = self.visit(ctx.expr1())
        right = self.visit(ctx.expr2())
        return BinaryOp(op, left, right)

    def visitExpr2(self, ctx: BKITParser.Expr2Context):
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.ADDF():
            op = ctx.ADDF().getText()
        elif ctx.SUB() and ctx.expr2() and ctx.expr3():
            op = ctx.SUB().getText()
        elif ctx.SUBF() and ctx.expr2() and ctx.expr3():
            op = ctx.SUBF().getText()
        else:
            return self.visit(ctx.expr3())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)

    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.MULF():
            op = ctx.MULF().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.DIVF():
            op = ctx.DIVF().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        else:
            return self.visit(ctx.expr4())
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)

    def visitExpr4(self, ctx: BKITParser.Expr4Context):
        op = ''
        if ctx.NEG():
            op = ctx.NEG().getText()
        else:
            return self.visit(ctx.expr5())
        body = self.visit(ctx.expr4())
        return UnaryOp(op, body)

    def visitExpr5(self, ctx: BKITParser.Expr5Context):
        op = ''
        if ctx.SUB():
            op = ctx.SUB().getText()
        elif ctx.SUBF():
            op = ctx.SUBF().getText()
        else: 
            return self.visit(ctx.expr6())
        body = self.visit(ctx.expr5())
        return UnaryOp(op, body)

    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        if ctx.LSB() and ctx.RSB():
            arr = self.visit(ctx.expr6())
            idx = list(self.visit(x) for x in ctx.expr())
            return ArrayCell(arr, idx)
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.callexpr():
            return self.visit(ctx.callexpr())
        elif ctx.expr() and ctx.LB() and ctx.RB():
            return self.visit(ctx.expr())

    def visitCallexpr(self, ctx:BKITParser.CallexprContext):
        id = Id(ctx.ID().getText())
        if ctx.lstcallexpr():
            param = self.visit(ctx.lstcallexpr())
            return CallExpr(id, param)
        else:
            return CallExpr(id, [])
    
    def visitLstcallexpr(self, ctx:BKITParser.LstcallexprContext):
        return list(self.visit(x) for x in ctx.expr())
    
    def visitIfstmt(self, ctx:BKITParser.IfstmtContext):
        ifthenStmt = []
        elseStmt = ([],[])

        lstVarDecl = []
        lstStmt = []
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        expr = self.visit(ctx.expr())
        ifthenStmt.append((expr,lstVarDecl,lstStmt))

        if ctx.elifstmt():
            for x in ctx.elifstmt():
                newelifstmt = self.visit(x)
                ifthenStmt.append(newelifstmt)
      
        if ctx.elsestmt():
            elseStmt = self.visit(ctx.elsestmt())

        return If(ifthenStmt, elseStmt)

    def visitElifstmt(self, ctx:BKITParser.ElifstmtContext):
        lstVarDecl = []
        lstStmt = []
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        expr = self.visit(ctx.expr())
        return (expr,lstVarDecl,lstStmt)

    def visitElsestmt(self, ctx: BKITParser.ElsestmtContext):
        lstVarDecl = []
        lstStmt = []
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        return (lstVarDecl, lstStmt)

    def visitForstmt(self, ctx: BKITParser.ForstmtContext):
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        expr3 = self.visit(ctx.expr(2))
        lstVarDecl = []
        lstStmt = []
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        return For(Id(ctx.ID().getText()), expr1, expr2, expr3, (lstVarDecl, lstStmt))

    def visitWhilestmt(self, ctx: BKITParser.WhilestmtContext):
        expr = self.visit(ctx.expr())
        lstVarDecl = []
        lstStmt = []
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        return While(expr, (lstVarDecl, lstStmt))

    def visitDostmt(self, ctx: BKITParser.DostmtContext):
        expr = self.visit(ctx.expr())
        lstVarDecl = []
        lstStmt = []
        if ctx.stmt():
            lstStmt = list(self.visit(x) for x in ctx.stmt())
        if ctx.vardecl():
            for x in ctx.vardecl():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstVarDecl = lstVarDecl + decl
                else:
                    lstVarDecl.append(decl)
        return Dowhile((lstVarDecl, lstStmt),expr)

    def visitBreakstmt(self, ctx: BKITParser.BreakstmtContext):
        return Break()
    
    def visitContinuestmt(self, ctx: BKITParser.ContinuestmtContext):
        return Continue()

    def visitCallstmt( self, ctx:BKITParser.CallstmtContext):
        param = []
        if ctx.expr():
            param = list(self.visit(x) for x in ctx.expr())
        return CallStmt(Id(ctx.ID().getText()),param)

    def visitReturnstmt(self, ctx: BKITParser.ReturnstmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return Return(expr)
    
    

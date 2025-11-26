from antlr4 import TerminalNode
from GramaticaPortugolVisitor import GramaticaPortugolVisitor


class CodeGenerator(GramaticaPortugolVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.indent = 0
        self.lines = []
        self.symbols = {}

    # --------------------------
    # Funções utilitárias
    # --------------------------

    def emit(self, line=""):
        self.lines.append(("    " * self.indent) + line)

    def increase(self):
        self.indent += 1

    def decrease(self):
        if self.indent > 0:
            self.indent -= 1

    def get_code(self):
        return "\n".join(self.lines)

    # --------------------------
    # Conversão de expressões
    # --------------------------

    def expr_to_str(self, ctx):
        """Converte expressões Portugol → Python corretamente."""
        if ctx is None:
            return ""
        parts = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                text = child.getText()
                if text == "e":
                    parts.append("and")
                elif text == "ou":
                    parts.append("or")
                else:
                    parts.append(text)
            else:
                parts.append(self.expr_to_str(child))
        expr = " ".join(parts)
        expr = expr.replace("( ", "(").replace(" )", ")")
        return expr

    # --------------------------
    # Visitantes da gramática
    # --------------------------

    def visitPrograma(self, ctx):
        self.emit("# Código Python gerado automaticamente do Portugol")
        self.emit()
        self.visitChildren(ctx)
        return self.get_code()

    def visitInicio(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclara(self, ctx):
        tipo = ctx.tipo().getText()
        for dado in ctx.dado_declara():
            var = dado.VARIAVEL().getText()
            self.symbols[var] = tipo
            if dado.dado():  
                valor = self.expr_to_str(dado.dado())
            else:
                if tipo == "inteiro":
                    valor = "0"
                elif tipo == "real":
                    valor = "0.0"
                elif tipo == "caracter":
                    valor = "''"
                else:
                    valor = "''" 
            self.emit(f"{var} = {valor}")
        return None

    def visitAtribui(self, ctx):
        var = ctx.VARIAVEL().getText()
        expr = self.expr_to_str(ctx.dado())
        self.emit(f"{var} = {expr}")
        return None

    def visitLeia(self, ctx):
        vars = ctx.VARIAVEL()
        for v in vars:
            nome = v.getText()
            tipo = self.symbols.get(nome, "cadeia")
            if tipo == "inteiro":
                self.emit(f"{nome} = int(input())")
            elif tipo == "real":
                self.emit(f"{nome} = float(input().replace(',', '.'))")
            elif tipo == "caracter":
                self.emit(f"{nome} = input()[0]")
            else:
                self.emit(f"{nome} = input()")
        return None

    def visitEscreva(self, ctx):
        args = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                expr = self.expr_to_str(child)
                args.append(expr)
        if len(args) == 1:
            self.emit(f"print({args[0]}, end='')")
        else:
            self.emit(f"print({', '.join(args)}, end='')")
        return None

    def visitSe(self, ctx):
        cond = self.expr_to_str(ctx.expressao_logica())
        self.emit(f"if {cond}:")
        self.increase()
        self.visit(ctx.comandos())
        self.decrease()
        if ctx.senao():
            self.emit("else:")
            self.increase()
            self.visit(ctx.senao())
            self.decrease()
        return None

    def visitSenao(self, ctx):
        return self.visitChildren(ctx)

    def visitEnquanto(self, ctx):
        cond = self.expr_to_str(ctx.expressao_logica())
        self.emit(f"while {cond}:")
        self.increase()
        self.visit(ctx.comandos())
        self.decrease()
        return None

    def visitComandos(self, ctx):
        return self.visitChildren(ctx)
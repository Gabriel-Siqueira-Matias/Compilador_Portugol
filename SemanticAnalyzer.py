from antlr4 import *
from GramaticaPortugolVisitor import GramaticaPortugolVisitor
from GramaticaPortugolParser import GramaticaPortugolParser

class SemanticError(Exception):
    pass


class SemanticAnalyzer(GramaticaPortugolVisitor):
    def __init__(self):
        self.symbols = {}

    def visitDeclara(self, ctx: GramaticaPortugolParser.DeclaraContext):
        tipo = ctx.tipo().getText()
        for dado in ctx.dado_declara():
            nome = dado.VARIAVEL().getText()
            if nome in self.symbols:
                raise SemanticError(f"Variável '{nome}' já declarada")
            self.symbols[nome] = tipo
            if dado.dado():
                tipo_expr = self.visit(dado.dado())
                if tipo_expr is None:
                    raise SemanticError(f"Inicialização inválida para '{nome}'")
                if tipo != tipo_expr:
                    raise SemanticError(
                        f"Tipo incompatível na declaração de '{nome}': "
                        f"esperado {tipo}, encontrado {tipo_expr}"
                    )
        return None

    def visitAtribui(self, ctx: GramaticaPortugolParser.AtribuiContext):
        nome = ctx.VARIAVEL().getText()
        if nome not in self.symbols:
            raise SemanticError(f"Variável '{nome}' usada antes de ser declarada")
        tipo_var = self.symbols[nome]
        tipo_exp = self.visit(ctx.dado())
        if tipo_var != tipo_exp:
            raise SemanticError(
                f"Tipo incompatível na atribuição de '{nome}': "
                f"esperado {tipo_var}, recebido {tipo_exp}"
            )
        
    def visitEscreva(self, ctx):
        for dado in ctx.dado():
            if dado.textos():
                self.visit(dado.textos())
            elif dado.expressao_aritmetica():
                self.visit(dado.expressao_aritmetica())
            elif dado.VARIAVEL():
                nome = dado.VARIAVEL().getText()
                if nome not in self.symbols:
                    raise SemanticError(f"Variável '{nome}' usada antes de ser declarada")
            else:
                raise SemanticError("Elemento inválido em escreva()")
        return None

    def visitDado(self, ctx):
        if ctx.textos():
            return self.visit(ctx.textos())
        if ctx.expressao_aritmetica():
            return self.visit(ctx.expressao_aritmetica())
        raise SemanticError("Dado inválido")

    def visitTextos(self, ctx):
        if ctx.CARACTER():
            return "caracter"
        if ctx.CADEIA():
            return "cadeia"

    def visitExpressao_aritmetica(self, ctx):
        tipos = []
        for termo in ctx.termo_aritmetico():
            tipos.append(self.visit(termo))
        for t in tipos:
            if t not in ("inteiro", "real"):
                raise SemanticError("Expressão aritmética contendo tipos não numéricos")
        if "real" in tipos:
            return "real"
        return "inteiro"

    def visitTermo_aritmetico(self, ctx):
        tipos = []
        for fator in ctx.fator_aritmetico():
            tipos.append(self.visit(fator))
        for t in tipos:
            if t not in ("inteiro", "real"):
                raise SemanticError("Termo aritmético contendo tipos não numéricos")
        if "real" in tipos:
            return "real"
        return "inteiro"

    def visitFator_aritmetico(self, ctx):
        if ctx.VARIAVEL():
            nome = ctx.VARIAVEL().getText()
            if nome not in self.symbols:
                raise SemanticError(f"Variável '{nome}' usada antes de ser declarada")
            return self.symbols[nome]
        if ctx.numerais():
            return self.visit(ctx.numerais())
        if ctx.expressao_aritmetica():
            return self.visit(ctx.expressao_aritmetica())

    def visitNumerais(self, ctx):
        if ctx.REAL():
            return "real"
        return "inteiro"

    def visitExpressao_relacional(self, ctx):
        tipo_esq = self.visit(ctx.expressao_aritmetica(0))
        tipo_dir = self.visit(ctx.expressao_aritmetica(1))
        if tipo_esq not in ("inteiro", "real") or tipo_dir not in ("inteiro", "real"):
            raise SemanticError("Operação relacional com operandos não numéricos")
        return "logico"
    
    def visitExpressao_logica(self, ctx):
        tipos = []
        for rel in ctx.expressao_relacional():
            tipos.append(self.visit(rel))
        for t in tipos:
            if t != "logico":
                raise SemanticError("Expressão lógica possui elementos não booleanos")
        return "logico"
# Generated from GramaticaPortugol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaPortugolParser import GramaticaPortugolParser
else:
    from GramaticaPortugolParser import GramaticaPortugolParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaPortugolParser.

class GramaticaPortugolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaPortugolParser#programa.
    def visitPrograma(self, ctx:GramaticaPortugolParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#inicio.
    def visitInicio(self, ctx:GramaticaPortugolParser.InicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#declaracoes.
    def visitDeclaracoes(self, ctx:GramaticaPortugolParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#declara.
    def visitDeclara(self, ctx:GramaticaPortugolParser.DeclaraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#dado_declara.
    def visitDado_declara(self, ctx:GramaticaPortugolParser.Dado_declaraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#tipo.
    def visitTipo(self, ctx:GramaticaPortugolParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#comandos.
    def visitComandos(self, ctx:GramaticaPortugolParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#comando.
    def visitComando(self, ctx:GramaticaPortugolParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#atribui.
    def visitAtribui(self, ctx:GramaticaPortugolParser.AtribuiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#escreva.
    def visitEscreva(self, ctx:GramaticaPortugolParser.EscrevaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#leia.
    def visitLeia(self, ctx:GramaticaPortugolParser.LeiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#se.
    def visitSe(self, ctx:GramaticaPortugolParser.SeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#senao.
    def visitSenao(self, ctx:GramaticaPortugolParser.SenaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#enquanto.
    def visitEnquanto(self, ctx:GramaticaPortugolParser.EnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#dado.
    def visitDado(self, ctx:GramaticaPortugolParser.DadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#expressao_aritmetica.
    def visitExpressao_aritmetica(self, ctx:GramaticaPortugolParser.Expressao_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#termo_aritmetico.
    def visitTermo_aritmetico(self, ctx:GramaticaPortugolParser.Termo_aritmeticoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#fator_aritmetico.
    def visitFator_aritmetico(self, ctx:GramaticaPortugolParser.Fator_aritmeticoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#expressao_logica.
    def visitExpressao_logica(self, ctx:GramaticaPortugolParser.Expressao_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#expressao_relacional.
    def visitExpressao_relacional(self, ctx:GramaticaPortugolParser.Expressao_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#operador_relacional.
    def visitOperador_relacional(self, ctx:GramaticaPortugolParser.Operador_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#numerais.
    def visitNumerais(self, ctx:GramaticaPortugolParser.NumeraisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaPortugolParser#textos.
    def visitTextos(self, ctx:GramaticaPortugolParser.TextosContext):
        return self.visitChildren(ctx)



del GramaticaPortugolParser
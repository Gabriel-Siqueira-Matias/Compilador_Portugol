import sys
from antlr4 import *

from GramaticaPortugolLexer import GramaticaPortugolLexer
from GramaticaPortugolParser import GramaticaPortugolParser
from antlr4.error.ErrorListener import ErrorListener
from graphviz import Digraph
from SemanticAnalyzer import SemanticAnalyzer
from CodeGenerator import CodeGenerator

# ==========================================
# LOG
# ==========================================
LOG_FILE = "gerados/analisador.log"

def log(msg: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)


# ==========================================
# ERROS PERSONALIZADOS
# ==========================================
class ErroLexicoListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "token recognition error at:" in msg:
            simbolo = msg.split(":")[-1].strip().strip("'")
        else:
            simbolo = offendingSymbol.text if offendingSymbol else "???"

        log(f"ERRO LÉXICO [Linha {line}, Coluna {column}]: Símbolo '{simbolo}' inválido")
        sys.exit(1)


class ErroSintaticoListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token_text = offendingSymbol.text if offendingSymbol else "EOF"
        log(f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: Problema próximo de '{token_text}'")
        sys.exit(1)


# ==========================================
# AST (Parse Tree) para Graphviz
# ==========================================
class ASTGenerator(ParseTreeVisitor):
    def __init__(self):
        self.dot = Digraph("AST_Portugol")
        self.node_count = 0

    def criar_no(self, label):
        self.node_count += 1
        node_name = f"n{self.node_count}"
        self.dot.node(node_name, label)
        return node_name

    def visit(self, tree):
        label = type(tree).__name__.replace("Context", "")
        node = self.criar_no(label)

        for i in range(tree.getChildCount()):
            child = tree.getChild(i)

            if isinstance(child, TerminalNode):
                leaf = self.criar_no(child.getText())
                self.dot.edge(node, leaf)
            else:
                child_node = self.visit(child)
                self.dot.edge(node, child_node)

        return node


# ==========================================
# MAIN
# ==========================================
def main(input_file):
    # Limpa log anterior
    open(LOG_FILE, "w").close()

    log("=== INICIANDO ANÁLISE ===")
    log(f"Arquivo de entrada: {input_file}")

    # -------------------------
    # LÉXICO
    # -------------------------
    log("\n=== ANÁLISE LÉXICA ===")
    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = GramaticaPortugolLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ErroLexicoListener())

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else str(token.type)
            log(f"<{token_name}, '{token.text}', Linha {token.line}, Coluna {token.column}>")

    # -------------------------
    # SINTÁTICO
    # -------------------------
    log("\n=== ANÁLISE SINTÁTICA ===")

    parser = GramaticaPortugolParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ErroSintaticoListener())

    tree = parser.programa()

    log("Código sintaticamente correto ✅")

    # -------------------------
    # AST
    # -------------------------
    log("\nGerando AST visual...")

    ast = ASTGenerator()
    ast.visit(tree)
    ast.dot.render("gerados/ast_portugol", format="png", cleanup=True)

    log("AST gerada → gerados/ast_portugol.png ✅")

    # -------------------------
    # SEMÂNTICA
    # -------------------------
    log("\n=== ANÁLISE SEMÂNTICA ===")

    sema = SemanticAnalyzer()
    try:
        sema.visit(tree)
        log("Análise semântica concluída sem erros ✅")
    except Exception as e:
        log(f"ERRO SEMÂNTICO: {e}")
        sys.exit(1)

    # -------------------------
    # GERAÇÃO DE CÓDIGO
    # -------------------------
    log("\n=== GERANDO CÓDIGO PYTHON ===")

    generator = CodeGenerator(sema.symbols)
    codigo_python = generator.visit(tree)

    with open("gerados/output.py", "w", encoding="utf-8") as f:
        f.write(codigo_python)

    log("Código Python gerado → gerados/output.py ✅")
    log("\nProcesso concluído com sucesso! 🎉")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python run_portugol.py <arquivo.ptg>")
        sys.exit(1)

    main(sys.argv[1])
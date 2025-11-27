# 🧩 Compilador Portugol – Análise Léxica, Sintática, Semântica e Geração de Código Python

Este projeto implementa um **compilador completo** para uma linguagem inspirada no **Portugol**, utilizando **ANTLR 4** e **Python 3**, incluindo as etapas:
* ✔ Análise Léxica
* ✔ Análise Sintática
* ✔ Geração da AST (Árvore Sintática Abstrata)
* ✔ Análise Semântica
* ✔ Geração de Código Python

Ele foi desenvolvido como parte da disciplina de Compiladores, com base na especificação fornecida pelo professor.

---

## 📘 Estrutura do Projeto

```
Compilador_Portugol/
├── GramaticaPortugol.g4            # Gramática ANTLR da linguagem
├── run_portugol.py                 # Pipeline principal (Léxico → Sintático → AST → Semântica → Python)
├── SemanticAnalyzer.py             # Analisador semântico
├── CodeGenerator.py                # Gerador de código Python
│
├── gerados/
│   ├── analisador.log              # Log de erros e etapas
│   ├── ast_portugol.png            # AST gerada via Graphviz
│   └── output.py                   # Código Python traduzido do Portugol
│
├── exemplos/
│   ├── pascal.ptg                  # Teste: Triângulo de Pascal
│   ├── triangulo.ptg               # Teste: Classificação de triângulos
│   ├── simples.ptg                 # Exemplo simples funcional
│   ├── erroLexico.ptg              # Exemplo de erro léxico
│   ├── erroSintatico.ptg           # Exemplo de erro sintático
│   └── erroSemantico.ptg           # Exemplo de erro semântico
│
├── requirements.txt                # Dependências do ambiente
└── README.md                       # Documentação do projeto
```

---

## 🧠 Funcionalidades

O compilador executa todo o pipeline clássico:

| Etapa                 | Descrição                                                              | Implementação                       |
| --------------------- | ---------------------------------------------------------------------- | ----------------------------------- |
| **Análise Léxica**    | Identifica tokens: variáveis, palavras-chave, números, operadores etc. | `GramaticaPortugolLexer.py`         |
| **Análise Sintática** | Verifica se o código segue as regras da gramática                      | `GramaticaPortugolParser.py`        |
| **Geração da AST**    | Cria e exporta uma árvore sintática em `.png`                          | `ASTGenerator` no `run_portugol.py` |
| **Análise Semântica** | Verifica tipos, declarações, uso de variáveis, expressões válidas etc. | `SemanticAnalyzer.py`               |
| **Geração de Python** | Converte o programa Portugol para um programa Python executável        | `CodeGenerator.py`                  |

---

## 🧩 Tecnologias Utilizadas

* [Python 3.10+](https://www.python.org/)
* [ANTLR 4.13.2](https://www.antlr.org/)
* [Graphviz](https://graphviz.org/)
* Biblioteca `antlr4-python3-runtime`

---

## ⚙️ Instalação e Execução

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Gabriel-Siqueira-Matias/Compilador_Portugol.git
cd Compilador_Portugol
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Gere o lexer e parser (caso altere a gramática)

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor GramaticaPortugol.g4
```

### 4️⃣ Execute o compilador

```bash
python run_portugol.py exemplos/pascal.ptg
```

A saída será salva automaticamente dentro da pasta:

```bash
gerados/output.py
```

---

---

## 🧪 Casos de Teste

| Caso                            | Descrição                                  | Resultado Esperado |
| ------------------------------- | ------------------------------------------ | ------------------ |
| **Triângulo de Pascal**         | Teste com laços aninhados                  | ✅ Código correto   |
| **Classificação de Triângulos** | Teste com operadores lógicos e relacionais | ✅ Código correto   |
| **Simples**                     | Teste com operadores de leitura e escrita  | ✅ Código correto   |
| **Erro Léxico**                 | Variável inválida (`a$`)                   | ❌ ERRO LÉXICO      |
| **Erro Sintático**              | Palavra incorreta (`ento`)                 | ❌ ERRO SINTÁTICO   |
| **Erro Semântico**              | Tipos incompatíveis                        | ❌ ERRO SEMÂNTICO   |


---

## 📜 Exemplo de Execução

```bash
python run_portugol.py exemplos/triangulo.ptg
```

Saída esperada:

```
=== ANÁLISE LÉXICA ===
Todos os tokens

=== ANÁLISE SINTÁTICA ===
Código sintaticamente correto ✅

Gerando AST visual...
AST gerada → gerados/ast_portugol.png ✅

=== ANÁLISE SEMÂNTICA ===
Análise semântica concluída sem erros ✅

=== GERANDO CÓDIGO PYTHON ===
Código Python gerado → gerados/output.py ✅

Processo concluído com sucesso! 🎉
```

---

## 🧩 Estrutura da AST

A árvore sintática é gerada automaticamente como imagem na pasta gerados:

```
gerados/ast_portugol.png
```

Exemplo simplificado:

```
programa
 └── funcaoInicio
      ├── declaracoes
      └── comandos
```

---

## ⚠️ Tratamento de Erros

* **Erro Léxico:** detectado durante o reconhecimento de tokens.
  Exemplo: símbolo `$` ou número inválido.
* **Erro Sintático:** detectado durante a análise da estrutura do código.
  Exemplo: `se (a>1) ento { ... }`.
* **Erro Sintático:** detectado pelo analisador semântico.
  Exemplo: `inteiro a="bola"`.

Os erros são registrados em:

```
gerados/analisador.log
```

---

## 👥 Autores

Projeto desenvolvido por:

* Gabriel Siqueira Matias
* Krystyan Douglas Santos Costa

Disciplina: **Compiladores – Professor Ed Wilson Tavares Ferreira**

Instituição: **Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso – Campus Cuiabá – Coronel Octayde Jorge da Silva**
Ano: **2025**

---
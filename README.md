# 🧩 Compilador Portugol – Analisador Léxico e Sintático

Este projeto implementa um **compilador funcional até as etapas léxica e sintática** para uma linguagem inspirada no **Portugol**, utilizando **ANTLR 4** e **Python 3**.
Ele foi desenvolvido como parte da disciplina de Compiladores, com base na especificação fornecida pelo professor.

---

## 📘 Estrutura do Projeto

```
Compilador_Portugol/
├── GramaticaPortugol.g4         # Gramática ANTLR da linguagem Portugol
├── run_portugol.py              # Programa principal (lexer + parser + AST)
├── analisador.log               # Log gerado automaticamente com os erros
├── exemplos/
│   ├── pascal.ptg               # Caso de teste: Triângulo de Pascal
│   ├── triangulo.ptg            # Caso de teste: Classificação de Triângulos
│   ├── erroLexico.ptg           # Exemplo de erro léxico
│   └── erroSintatico.ptg        # Exemplo de erro sintático
├── requirements.txt             # Dependências do ambiente
└── README.md                    # Documentação do projeto
```

---

## 🧠 Funcionalidades

O compilador é composto por três partes principais:

| Etapa                 | Descrição                                                                                                               | Implementação                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Análise Léxica**    | Identifica e classifica os tokens do código-fonte, como palavras-chave, variáveis, números, operadores e delimitadores. | `GramaticaPortugolLexer.py`         |
| **Análise Sintática** | Verifica se a estrutura do código segue as regras da gramática Portugol.                                                | `GramaticaPortugolParser.py`        |
| **Geração de AST**    | Cria a Árvore Sintática Abstrata (AST) e exporta uma imagem em `.png` via Graphviz.                                     | `ASTGenerator` no `run_portugol.py` |

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
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 GramaticaPortugol.g4
```

### 4️⃣ Execute o compilador

```bash
python run_portugol.py exemplos/pascal.ptg
```

---

## 🧪 Casos de Teste

| Caso                            | Descrição                                            | Resultado Esperado                              |
| ------------------------------- | ---------------------------------------------------- | ----------------------------------------------- |
| **Triângulo de Pascal**         | Testa repetição (`enquanto`) e comandos aninhados    | ✅ Código sintaticamente correto                 |
| **Classificação de Triângulos** | Testa operadores `e`, `ou`, relacionais e `se/senao` | ✅ Código sintaticamente correto                 |
| **Erro Léxico**                 | Código com variável `a$`                             | ❌ ERRO LÉXICO — símbolo `$` inválido            |
| **Erro Sintático**              | Palavra incorreta `ento` no lugar de `entao`         | ❌ ERRO SINTÁTICO — problema próximo de `'ento'` |

---

## 📜 Exemplo de Execução

```bash
python run_portugol.py exemplos/triangulo.ptg
```

Saída esperada:

```
=== TOKENS ===
<PROGRAMA, 'programa', Linha 1, Coluna 0>
<FUNCAO, 'funcao', Linha 2, Coluna 4>
...
=== ANÁLISE SINTÁTICA ===
Código sintaticamente correto ✅
AST gerada → ast_portugol.png ✅
```

---

## 🧩 Estrutura da AST

A árvore sintática é gerada automaticamente como imagem:

```
ast_portugol.png
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

Os erros são registrados no arquivo:

```
analisador.log
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
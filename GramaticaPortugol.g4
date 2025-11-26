// GramaticaPortugol.g4
grammar GramaticaPortugol;

programa
    : 'programa' '{' inicio '}' EOF
    ;

inicio
    : 'funcao' 'inicio' '(' ')' '{' declaracoes comandos '}'
    ;

// ------------------- DECLARAÇÕES -------------------

declaracoes
    : (declara)*
    ;

declara
    : tipo dado_declara (',' dado_declara)*
    ;

dado_declara
    : VARIAVEL ('=' dado)?
    ;

tipo
    : 'inteiro' 
    | 'real' 
    | 'caracter' 
    | 'cadeia'
    ;

// ------------------- COMANDOS -------------------

comandos
    : (comando)*
    ;

comando
    : atribui
    | escreva
    | leia
    | se
    | enquanto
    ;

// ------------------- ATRIBUIÇÃO E E/S -------------------

atribui
    : VARIAVEL '=' dado
    ;

escreva
    : 'escreva' '(' dado (',' dado)* ')'
    ;

leia
    : 'leia' '(' VARIAVEL (',' VARIAVEL)* ')'
    ;

// ------------------- ESTRUTURAS DE CONTROLE -------------------

se
    : 'se' '(' expressao_logica ')' 'entao' '{' comandos '}' senao?
    ;

senao
    : 'senao' ('{' comandos '}' | se)
    ;

enquanto
    : 'enquanto' '(' expressao_logica ')' 'faca' '{' comandos '}'
    ;

// ------------------- EXPRESSÕES -------------------

dado
    : textos
    | VARIAVEL
    | expressao_aritmetica
    ;

expressao_aritmetica
    : termo_aritmetico (('+' | '-') termo_aritmetico)*
    ;

termo_aritmetico
    : fator_aritmetico (('*' | '/') fator_aritmetico)*
    ;

fator_aritmetico
    : '(' expressao_aritmetica ')'
    | numerais
    | VARIAVEL
    ;

expressao_logica
    : expressao_relacional (('e' | 'ou') expressao_relacional)*
    ;

expressao_relacional
    : expressao_aritmetica operador_relacional expressao_aritmetica
    ;

operador_relacional
    : '==' 
    | '!=' 
    | '>' 
    | '<' 
    | '<=' 
    | '>='
    ;

// ------------------- TOKENS -------------------

numerais : '-'? (INTEIRO | REAL) ;
textos   : CARACTER | CADEIA ;

INTEIRO : [0-9]+ ;
REAL    : [0-9]+ ',' [0-9]+ ;
CARACTER: '\'' (~['\r\n\\]) '\'' ;
CADEIA  : '"' ( '\\' . | ~["\\\r\n] )* '"' ;
VARIAVEL: [A-Za-z] [A-Za-z0-9]* ;

WS      : [ \t\r\n]+ -> skip ;
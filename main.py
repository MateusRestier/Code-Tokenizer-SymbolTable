import re

# Definir as regras de token usando expressões regulares
token_patterns = [
    (r'\{', 'L_BRACE'),
    (r'\}', 'R_BRACE'),
    (r'\(', 'L_PAREN'),
    (r'\)', 'R_PAREN'),
    (r'\;', 'SEMICOLON'),
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'\/', 'DIVIDE'),
    (r'=', 'ASSIGN'), # Adicionando o operador de atribuição
    (r'int|float|char', 'TYPE'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    (r'\d+', 'NUM'),
]

# Função para tokenizar o código-fonte
def tokenize(code):
    tokens = []
    code = code.strip()
    
    while code:
        matched = False
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                code = code[len(value):]
                code = code.strip()
                matched = True
                break
        
        if not matched:
            raise Exception(f"Erro de análise léxica: Caractere inesperado em '{code}'")
    
    return tokens

# Exemplo de código-fonte
source_code = "{ int x; float y; x = 10; y = x + 5; }"

# Tokenização do código
tokens = tokenize(source_code)

# Imprimir os tokens
for token in tokens:
    print(f"Token: {token[0]}, Tipo: {token[1]}")

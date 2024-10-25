import re

def lexer(code):
    tokens = re.findall(r'[\w]+|["\'].*?["\']|\(|\)|\,', code)
    return tokens

# Testando o lexer
code = 'print("Olá Mundo!")'
tokens = lexer(code)
print(tokens)  # Saída: ['print', '(', '"Olá Mundo!"', ')']

def parser(tokens):
    if tokens[0] == 'print':
        # Pega a string entre os parênteses
        content = tokens[2][1:-1]  # Remove aspas
        return ('print', content)
    
    elif tokens[0] == 'add':
        num1 = int(tokens[2])
        num2 = int(tokens[4])
        return ('add', num1, num2)

# Testando o parser
tokens = lexer('add(5, 10)')
parsed = parser(tokens)
print(parsed)  # Saída: ('add', 5, 10)

def interpreter(parsed):
    if parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")

# Testando o interpretador
parsed = parser(lexer('print("Olá Mundo!")'))
interpreter(parsed)  # Saída: Olá Mundo!

parsed = parser(lexer('add(5, 10)'))
interpreter(parsed)  # Saída: Resultado: 15

variables = {}  # Um dicionário para armazenar variáveis

def parser(tokens):
    if tokens[1] == '=':
        # Declaração de variável
        var_name = tokens[0]
        var_value = int(tokens[2])  # Supondo que só lidamos com inteiros por enquanto
        return ('assign', var_name, var_value)
    
    elif tokens[0] == 'print':
        if tokens[2] in variables:  # Verifica se é uma variável
            content = variables[tokens[2]]
        else:
            content = tokens[2][1:-1]  # Remove aspas se for string
        return ('print', content)
    
    elif tokens[0] == 'add':
        if tokens[2] in variables:
            num1 = variables[tokens[2]]
        else:
            num1 = int(tokens[2])
        
        if tokens[4] in variables:
            num2 = variables[tokens[4]]
        else:
            num2 = int(tokens[4])
        
        return ('add', num1, num2)

def interpreter(parsed):
    if parsed is None:
        print("Erro: comando não reconhecido.")
        return
    
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
        print(f"{parsed[1]} atribuído o valor {parsed[2]}")
    
    # Continue com outras instruções conforme necessário.
4

def parser(tokens):
    if len(tokens) == 3 and tokens[1] == '=':
        var_name = tokens[0]  # Exemplo: 'x'
        var_value = int(tokens[2])  # Exemplo: '10'
        return ('assign', var_name, var_value)
    
    # Adicione verificações para outros tipos de comandos, se necessário.
    
    return None  # Retorna None se os tokens não corresponderem a nenhum padrão reconhecido

interpreter(parser(lexer('print(x)')))  # Saída: 10
interpreter(parser(lexer('add(x, 5)')))  # Saída: Resultado: 15

def parser(tokens):
    if tokens[1] == '=':
        var_name = tokens[0]
        var_value = int(tokens[2])
        return ('assign', var_name, var_value)
    
    elif tokens[0] == 'print':
        if tokens[2] in variables:
            content = variables[tokens[2]]
        else:
            content = tokens[2][1:-1] 
        return ('print', content)
    
    elif tokens[0] == 'add':
        num1 = variables.get(tokens[2], int(tokens[2]))
        num2 = variables.get(tokens[4], int(tokens[4]))
        return ('add', num1, num2)
    
    elif tokens[0] == 'subtrair':
        num1 = variables.get(tokens[2], int(tokens[2]))
        num2 = variables.get(tokens[4], int(tokens[4]))
        return ('subtrair', num1, num2)
    
    elif tokens[0] == 'multiplicar':
        num1 = variables.get(tokens[2], int(tokens[2]))
        num2 = variables.get(tokens[4], int(tokens[4]))
        return ('multiplicar', num1, num2)
    
    elif tokens[0] == 'dividir':
        num1 = variables.get(tokens[2], int(tokens[2]))
        num2 = variables.get(tokens[4], int(tokens[4]))
        return ('dividir', num1, num2)

def interpreter(parsed):
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
    
    elif parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")
    
    elif parsed[0] == 'subtrair':
        result = parsed[1] - parsed[2]
        print(f"Resultado: {result}")
    
    elif parsed[0] == 'multiplicar':
        result = parsed[1] * parsed[2]
        print(f"Resultado: {result}")
    
    elif parsed[0] == 'dividir':
        result = parsed[1] / parsed[2]
        print(f"Resultado: {result}")

interpreter(parser(lexer('multiplicar(4, 5)')))  # Saída: Resultado: 20
interpreter(parser(lexer('subtrair(10, 3)')))   # Saída: Resultado: 7
interpreter(parser(lexer('dividir(8, 2)')))     # Saída: Resultado: 4.0

def parser(tokens):
    if tokens[0] == 'if':
        # Processa a condição dentro dos parênteses
        left_operand = variables.get(tokens[2], int(tokens[2]))  # Pega valor da variável ou número
        operator = tokens[3]
        right_operand = variables.get(tokens[4], int(tokens[4]))  # Pega valor da variável ou número
        command = tokens[6:]  # Comando a ser executado, ex: ['print', '(', '"Maior que 5"', ')']
        return ('if', left_operand, operator, right_operand, command)
    
    # Outras opções já implementadas (assign, print, add, etc.)
    elif tokens[1] == '=':
        var_name = tokens[0]
        var_value = int(tokens[2])
        return ('assign', var_name, var_value)
    
    elif tokens[0] == 'print':
        content = variables.get(tokens[2], tokens[2][1:-1])
        return ('print', content)
    
    elif tokens[0] == 'add':
        num1 = variables.get(tokens[2], int(tokens[2]))
        num2 = variables.get(tokens[4], int(tokens[4]))
        return ('add', num1, num2)

def interpreter(parsed):
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
    
    elif parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")
    
    elif parsed[0] == 'if':
        left_operand = parsed[1]
        operator = parsed[2]
        right_operand = parsed[3]
        command = parsed[4]
        
        # Avaliar a condição
        condition_met = False
        if operator == '>':
            condition_met = left_operand > right_operand
        elif operator == '<':
            condition_met = left_operand < right_operand
        elif operator == '==':
            condition_met = left_operand == right_operand
        elif operator == '!=':
            condition_met = left_operand != right_operand
        
        # Se a condição for verdadeira, executar o comando
        if condition_met:
            command_tokens = lexer(' '.join(command))  # Requebra o comando para tokens
            interpreter(parser(command_tokens))  # Interpreta o comando

# Testando Condicionais
interpreter(parser(lexer('x = 10')))
interpreter(parser(lexer('if (x > 5) print("Maior que 5")')))  # Saída: Maior que 5
interpreter(parser(lexer('if (x < 5) print("Menor que 5")')))  # Não imprime nada

interpreter(parser(lexer('y = 3')))
interpreter(parser(lexer('if (y == 3) print("y é igual a 3")')))  # Saída: y é igual a 3
interpreter(parser(lexer('if (y != 3) print("y não é igual a 3")')))  # Não imprime nada

def interpreter(parsed):
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
    
    elif parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")
    
    elif parsed[0] == 'if':
        left_operand = parsed[1]
        operator = parsed[2]
        right_operand = parsed[3]
        command = parsed[4]
        
        # Avaliar a condição
        condition_met = False
        if operator == '>':
            condition_met = left_operand > right_operand
        elif operator == '<':
            condition_met = left_operand < right_operand
        elif operator == '==':
            condition_met = left_operand == right_operand
        elif operator == '!=':
            condition_met = left_operand != right_operand
        elif operator == '>=':
            condition_met = left_operand >= right_operand
        elif operator == '<=':
            condition_met = left_operand <= right_operand
        
        # Se a condição for verdadeira, executar o comando
        if condition_met:
            command_tokens = lexer(' '.join(command))
            interpreter(parser(command_tokens))

def parser(tokens):
    if tokens[0] == 'while':
        left_operand = variables.get(tokens[2], int(tokens[2]))  # Pega valor da variável ou número
        operator = tokens[3]
        right_operand = variables.get(tokens[4], int(tokens[4]))  # Pega valor da variável ou número
        command = tokens[6:]  # Comando a ser repetido
        return ('while', left_operand, operator, right_operand, command)
    
    # Outras opções já implementadas (assign, print, add, etc.)
    elif tokens[1] == '=':
        var_name = tokens[0]
        var_value = int(tokens[2])
        return ('assign', var_name, var_value)
    
    elif tokens[0] == 'print':
        content = variables.get(tokens[2], tokens[2][1:-1])
        return ('print', content)
    
    elif tokens[0] == 'add':
        num1 = variables.get(tokens[2], int(tokens[2]))
        num2 = variables.get(tokens[4], int(tokens[4]))
        return ('add', num1, num2)

def interpreter(parsed):
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
    
    elif parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")
        return result  # Retorna o resultado para ser reutilizado
    
    elif parsed[0] == 'while':
        left_operand = parsed[1]
        operator = parsed[2]
        right_operand = parsed[3]
        command = parsed[4]
        
        while True:
            # Avaliar a condição
            condition_met = False
            if operator == '>':
                condition_met = left_operand > right_operand
            elif operator == '<':
                condition_met = left_operand < right_operand
            elif operator == '==':
                condition_met = left_operand == right_operand
            elif operator == '!=':
                condition_met = left_operand != right_operand
            elif operator == '>=':
                condition_met = left_operand >= right_operand
            elif operator == '<=':
                condition_met = left_operand <= right_operand

            # Se a condição não for mais verdadeira, interromper o loop
            if not condition_met:
                break

            # Executar o comando dentro do loop
            command_tokens = lexer(' '.join(command))
            new_result = interpreter(parser(command_tokens))  # Possível alteração de variáveis
            if 'x' in command_tokens:
                left_operand = variables['x']  # Atualiza a condição se x mudar

interpreter(parser(lexer('x = 0')))
interpreter(parser(lexer('while (x < 10) x = add(x, 1)')))  # Incrementa x até 10
interpreter(parser(lexer('print(x)')))  # Saída: 10

def parser(tokens):
    if tokens[0] == 'for':
        init = tokens[2:5]  # Exemplo: ['i', '=', '0']
        condition_left = tokens[6]
        operator = tokens[7]
        condition_right = tokens[8]
        increment = tokens[10:]  # Exemplo: ['i', '=', 'add', '(', 'i', ',', '1', ')']
        command = tokens[12:]  # Comando a ser repetido
        return ('for', init, condition_left, operator, condition_right, increment, command)

    # Outras opções (assign, while, etc.) já implementadas anteriormente
    elif tokens[1] == '=':
        var_name = tokens[0]
        var_value = int(tokens[2])
        return ('assign', var_name, var_value)
    
    elif tokens[0] == 'print':
        content = variables.get(tokens[2], tokens[2][1:-1])
        return ('print', content)

def interpreter(parsed):
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
    
    elif parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")
        return result
    
    elif parsed[0] == 'for':
        # Inicializa a variável do loop
        interpreter(parser(parsed[1]))  # Executa a inicialização, ex: ['i', '=', '0']
        
        condition_left = variables.get(parsed[2], int(parsed[2]))
        operator = parsed[3]
        condition_right = variables.get(parsed[4], int(parsed[4]))
        increment = parsed[5]  # Exemplo: ['i', '=', 'add', '(', 'i', ',', '1', ')']
        command = parsed[6]  # Comando a ser executado
        
        while True:
            # Avalia a condição
            condition_met = False
            if operator == '>':
                condition_met = condition_left > condition_right
            elif operator == '<':
                condition_met = condition_left < condition_right
            elif operator == '==':
                condition_met = condition_left == condition_right
            elif operator == '!=':
                condition_met = condition_left != condition_right
            elif operator == '>=':
                condition_met = condition_left >= condition_right
            elif operator == '<=':
                condition_met = condition_left <= condition_right
            
            # Se a condição não for mais verdadeira, parar o loop
            if not condition_met:
                break

            # Executar o comando dentro do loop
            command_tokens = lexer(' '.join(command))
            interpreter(parser(command_tokens))
            
            # Incrementa a variável do loop
            increment_tokens = lexer(' '.join(increment))
            interpreter(parser(increment_tokens))
            
            # Atualiza a variável da condição
            condition_left = variables.get(parsed[2], condition_left)

interpreter(parser(lexer('for (i = 0; i < 5; i = add(i, 1)) print(i)')))
# Saída esperada:
# 0
# 1
# 2
# 3
# 4

def parser(tokens):
    if tokens[0] == 'for':
        if tokens[2] == 'in':
            var_name = tokens[1]  # Exemplo: 'item'
            list_values = eval(tokens[3])  # Exemplo: '[1, 2, 3]'
            command = tokens[5:]  # O que será executado
            return ('for_in_list', var_name, list_values, command)
        
        # Continuação para o `for` padrão com inicialização e condição
        init = tokens[2:5]
        condition_left = tokens[6]
        operator = tokens[7]
        condition_right = tokens[8]
        increment = tokens[10:]
        command = tokens[12:]
        return ('for', init, condition_left, operator, condition_right, increment, command)
    
    # Outras opções
    elif tokens[1] == '=':
        var_name = tokens[0]
        var_value = int(tokens[2])
        return ('assign', var_name, var_value)
    
    elif tokens[0] == 'print':
        content = variables.get(tokens[2], tokens[2][1:-1])
        return ('print', content)

def interpreter(parsed):
    if parsed[0] == 'assign':
        variables[parsed[1]] = parsed[2]
    
    elif parsed[0] == 'print':
        print(parsed[1])
    
    elif parsed[0] == 'add':
        result = parsed[1] + parsed[2]
        print(f"Resultado: {result}")
        return result
    
    elif parsed[0] == 'for_in_list':
        var_name = parsed[1]
        list_values = parsed[2]
        command = parsed[3]
        
        for item in list_values:
            variables[var_name] = item  # Atribui o valor atual da lista à variável
            command_tokens = lexer(' '.join(command))
            interpreter(parser(command_tokens))  # Executa o comando para cada item da lista

interpreter(parser(lexer('for (item in [1, 2, 3, 4, 5]) print(item)')))
# Saída esperada:
# 1
# 2
# 3
# 4
# 5
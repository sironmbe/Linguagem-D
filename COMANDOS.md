
                                        == EXEMPLOS DE CODIGOS PARA A LINGUAGEM D ==

1- Declaração de Variáveis:
x = 10            # Atribuição de um inteiro
y = 3.14          # Atribuição de um float
nome = "Ariano"   # Atribuição de uma string
----------------------------------
2- Operações Aritméticas:
soma = x + y      # Adição
subtracao = x - y # Subtração
multiplicacao = x * y # Multiplicação
divisao = x / y   # Divisão
----------------------------------
3- Estruturas de Controle;
* Condicionais:
if x > y:
    print("x é maior que y")
elif x < y:
    print("x é menor que y")
else:
    print("x é igual a y")

* Loops:
# Loop While
while x < 10:
    x = x + 1

# Loop For
for i in range(10):
    print(i)
----------------------------------
4- Funções:
def soma(a, b):
    return a + b

resultado = soma(5, 3)  # Chamada da função
----------------------------------
5- Listas e Estruturas de Dados:
lista = [1, 2, 3, 4, 5]        # Declaração de uma lista
lista.append(6)                # Adiciona um elemento à lista
elemento = lista[0]            # Acessa o primeiro elemento
----------------------------------
6- Manipulação de Strings:
saudacao = "Olá, " + nome      # Concatenando strings
tamanho = len(saudacao)        # Obtendo o tamanho da string
----------------------------------
7- Entrada e Saída:
# Entrada do Usuário
entrada = input("Digite seu nome: ")

# Saída
print("Bem-vindo, " + entrada)
----------------------------------
8- Tratamento de Erros:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
----------------------------------
9- Módulos e Importações:
import modulo_exemplo  # Importando um módulo
----------------------------------
10- Comentários:
# Este é um comentário de linha única

"""
Este é um comentário
de múltiplas linhas.
"""



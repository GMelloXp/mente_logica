# 1. Verificando Se um Número é Positivo, Negativo ou Zero
# Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo
# ou zero.

# RESOLUÇÃO

# numero = int(input("Digite um número: "))
# if numero > 0:
#   print("O número é positivo ")
# elif numero == 0:
#   print("O número é zero ")
# else:
#   print("O número é negativo")

# 2. Calculadora Simples
# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza
# o cálculo correspondente.

#RESOLUÇÃO

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma das quatro operações (+)(-)(*)(/): ")

if operacao == "+":
  resultado = numero1 + numero2
  print("O resultado da soma é: ", resultado)
elif operacao == "-":
  resultado = numero1 - numero2
  print("O resultado da diferença é: ", resultado)
elif operacao == "*":
  resultado = numero1 * numero2
  print("O resultado do produto é: ", resultado)
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado da divisão é: ", resultado)
    else:
        print("Erro: divisão por 0!!!")
else:
  print("Operação não reconhecida!")

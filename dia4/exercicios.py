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

# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))
# operacao = input("Escolha uma das quatro operações (+)(-)(*)(/): ")

# if operacao == "+":
#   resultado = numero1 + numero2
#   print("O resultado da soma é: ", resultado)
# elif operacao == "-":
#   resultado = numero1 - numero2
#   print("O resultado da diferença é: ", resultado)
# elif operacao == "*":
#   resultado = numero1 * numero2
#   print("O resultado do produto é: ", resultado)
# elif operacao == "/":
#     if numero2 != 0:
#         resultado = numero1 / numero2
#         print("O resultado da divisão é: ", resultado)
#     else:
#         print("Erro: divisão por 0!!!")
# else:
#   print("Operação não reconhecida!")


# Classificação de Idade
# Crie um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

# idade = int(input("Digite sua idade: "))

# if idade >= 0 and idade <= 12:
#     print("Você é uma criança")
# elif idade <= 17:
#     print("Você é um Adolescente")
# elif idade < 60:
#     print("Você é um adulto")
# elif idade >= 60:
#     print("Você é um idoso")
# else:
#   print("Idade iválida!")

# 4. Verificando Ano Bissexto
# Crie um programa que verifica se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Mas não é bissexto se for divisível por 100, exceto se for divisível por 400

# ano = int(input("Digite um ano: "))

# if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#     print("O ano é bissexto")
# else:
#     print("O ano não é bissexto")


# Simulador de Caixa Eletrônico
# Crie um programa que simula um caixa eletrônico. O usuário deve informar o valor do saque
# (apenas valores inteiros) e o programa deve informar quantas cédulas de cada valor serão
# fornecidas.
# ● Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.

# valor_saque = int(input("Digite o valor a ser sacado: R$"))

# if valor_saque <= 0:
#     print("Valor indisponível!")
# else:
#     qtd_cedulas_100 = valor_saque // 100
#     valor_saque %= 100

#     qtd_cedulas_50 = valor_saque // 50
#     valor_saque %= 50

#     qtd_cedulas_20 = valor_saque // 20
#     valor_saque %= 20

#     qtd_cedulas_10 = valor_saque // 10
#     valor_saque %= 10

#     qtd_cedulas_5 = valor_saque // 5
#     valor_saque %= 5

#     qtd_cedulas_2 = valor_saque // 2
#     valor_saque %= 2

#     if valor_saque != 0:
#         print("Esse valo não pode ser sacado com as cédulas disponíveis!")
#     else:
#         print("Cédulas entregues: ")
#         if qtd_cedulas_100 > 0:
#             print(f"{qtd_cedulas_100} x R$100,00")
#         if qtd_cedulas_50 > 0:
#             print(f"{qtd_cedulas_50} x R$50,00")
#         if qtd_cedulas_20 >0:
#             print(f"{qtd_cedulas_20} x R$20,00")
#         if qtd_cedulas_10 > 0:
#             print(f"{qtd_cedulas_10} x R$10,00")
#         if qtd_cedulas_5 > 0:
#             print(f"{qtd_cedulas_5} x R$5,00")
#         if qtd_cedulas_2 > 0:
#             print(f"{qtd_cedulas_2} x R$2,00")

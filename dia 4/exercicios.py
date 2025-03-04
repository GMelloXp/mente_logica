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


# Classificação de Idade
# Crie um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança")
elif idade <= 17:
    print("Você é um Adolescente")
elif idade < 60:
    print("Você é um adulto")
elif idade >= 60:
    print("Você é um idoso")
else:
  print("Idade iválida!")

# 4. Verificando Ano Bissexto
# Crie um programa que verifica se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Mas não é bissexto se for divisível por 100, exceto se for divisível por 400

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
    



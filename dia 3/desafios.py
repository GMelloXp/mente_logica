
#Desafio 1

# Classificação Etária
# Crie um programa que verifica se uma pessoa pode assistir a um filme classificado como
# "maiores de 16 anos".
# Dados:
# ● Idade da pessoa: Pergunte ao usuário

#RESOLUÇÃO

#solicitar idade
# idade = int(input("Qual a sua idade?"))

# pode_assistir = idade >=16



# print("A pessoa pode assistir o filme? ", pode_assistir)

#DESAFIO 2

# Calculadora de IMC
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em
# metros) elevada ao quadrado.
# Crie um programa que calcula o IMC e verifica se a pessoa está dentro do peso ideal (IMC
# entre 18.5 e 24.9).

peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))

imc = float(peso / (altura ** 2))
peso_ideal = imc >= 18.5 and imc <= 24.9
print("O seu IMC é: ", imc)
print("Você está no peso ideal? ", peso_ideal)

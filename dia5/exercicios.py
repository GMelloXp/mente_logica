# 1. Imprimindo Números de 1 a 10
# Use um loop for para imprimir os números de 1 a 10

for i in range(10):
    print ("Número", i + 1)


#outra forma de fazer
for i in range(1, 11):
    print("Número", i)

# o parâmetro (1, 11) gera números de 1 a 10

# 2. Calculando a Soma dos Números de 1 a N
# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 a
# N
  
numero = int(input("Digite um número inteiro positivo"))
soma = 0

for i in range(1, numero+1):
    soma += i 
print("A soma dos números é: ", soma)

# 3. Tabuada de um Número
# Peça ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um número inteiro positivo"))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# 4. Contando Números Pares e Ímpares
# Gere uma lista de números de 1 a 20 e conte quantos são pares e quantos são ímpares.

pares = 0 
impares = 0 

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1 
    else:
        impares += 1 
print("O número de pares é: ", pares)
print("O número de ímpares é: ", impares)

# 5. Adivinhe o Número
# Crie um jogo em que o programa escolhe um número aleatório entre 1 e 100, e o usuário
# tenta adivinhar. O programa deve dar dicas se o número é maior ou menor do que o palpite.
# O jogo continua até o usuário acertar.

import random

numero_secreto = random.randint(1, 100)
tentativas = 0 

while True: 
    palpite = int(input("Adivinhe o número (entre 1 e 100)"))
    tentativas += 1 
    
    if palpite == numero_secreto:
        print(f"Você acertou o número {numero_secreto} em {tentativas} tentativas")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior")
    else:
        print("O número secreto é menor")


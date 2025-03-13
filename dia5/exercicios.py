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

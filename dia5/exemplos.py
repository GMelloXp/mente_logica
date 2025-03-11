#O loop for é usado para iterar sobre uma sequência
# Sintaxe Básica:
# for variável in sequência:
# # bloco de código a ser executado

frutas = ["maçã", "banana", "melancia"]

for fruta in frutas:
    print("Eu gosto de ", fruta)

#iteração utilizando a função range()

for i in range(5):
    print("Número ", i)

#o número 5 indica a quantidade de índices. [0] = 0 ... [4] = 4. Ou seja, temos 5 números indo do 0 ao 4.

#O loop while repete um bloco de código enquanto uma condição for verdadeira. 
# Sintaxe Básica:
# while condição:
# # bloco de código a ser executado

contador = 0

while contador < 5:
    print("Contagem ", contador)
    contador += 1 #contador += 1 --> contador = contador + 1


# Comando break
# O comando break é usado para interromper o loop imediatamente, mesmo que a condição
# do loop ainda seja verdadeira.
# Exemplo com break:


for numero in range(10):
    if numero == 5:
        break
    print("Numero", numero)

# Comando continue
# O comando continue é usado para pular a iteração atual e continuar com a próxima
# iteração do loop.
# Exemplo com continue:

for numero in range(5):
    if numero == 2:
        continue
    print("Numero", numero)


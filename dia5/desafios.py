
# 1. Calculando Fatorial de um Número
# Peça ao usuário um número inteiro positivo e calcule o fatorial desse número.
# ● Fatorial de N (N!) é o produto de todos os números inteiros positivos de 1 até N.
# ● Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120]

numero = int(input("Digite um número inteiro positivo"))

fatorial = 1 

if numero < 0:
    print("Não existe fatorial de número negativo")
elif numero == 0 or numero == 1:
    print(f"O fatorial de {numero} é {fatorial}")
else: 
    for i in range (1, numero+1):
        fatorial *= i 
    print(f"O fatorial de {numero} é {fatorial}")


# 2. Série Fibonacci
# Exiba os primeiros N termos da série de Fibonacci.
# ● A série de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos
# dois anteriores.
# ● Exemplo: 0, 1, 1, 2, 3, 5, 8, 13...

n = int(input("Quantos números da série que Fibonacci você quer ver?"))

termo1 = 0
termo2 = 1 
contador = 0 

if n < 0: 
    print("Insira um número positivo")
elif n == 1:
    print("Série de Fibonacci até ", n, "termo: ")
    print(termo1)
else:
    print("Série de Fibonacci: ")
    while contador < n:
        print(termo1)
        proximo_termo = termo1 + termo2 
        termo1 = termo2
        termo2 = proximo_termo 
        contador += 1


# 3. Jogo da Forca Simples
# Crie um jogo da forca simples em que o usuário deve adivinhar uma palavra letra por letra

palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    print("Palavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()
    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")
        
if "_" not in letras_descobertas:
    print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
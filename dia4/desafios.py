# 1. Aprovando Empréstimo Bancário
# Crie um programa para uma instituição bancária que analisa o pedido de empréstimo.
# ● O cliente deve informar o valor do empréstimo, a renda mensal e o número de
# parcelas.
# ● O empréstimo será aprovado se o valor da parcela não exceder 30% da renda
# mensal.

  #RESOLUÇÃO

# valor_emprestimo = float(input("Digite o valor desejado de empréstimo: R$"))
# renda_mensal = float(input("Informe sua renda mensal em reais: R$"))
# parcelas = int(input("Informe o número de parcelas do empréstimo: "))

# valor_parcela = valor_emprestimo / parcelas

# if valor_parcela <= (renda_mensal * 0.3):
#   print("O empréstimo está aprovado!")
#   print("Seu empréstimo será no valor de " f"{parcelas: .2f} x R$ {valor_parcela: .2f}")
# else:
#   print("O Empréstimo não foi aprovado!")
#   print(f"O valor da parcela R$ {valor_parcela: .2f} excede o limite de 30% da renda mensal ")


# 2. Jogo Pedra, Papel ou Tesoura
# Crie um programa que simula o jogo "Pedra, Papel ou Tesoura" entre o usuário e o
# computador.

#RESOLUÇÃO

# import random #o método random gera um número aleatório

# opcoes = ["pedra", "papel", "tesoura"] #array de opções

# usuario = input("Escolha pedra, papel ou tesoura: ").lower() #a função lower() deixa todas as letras em minúsculo

# computador = random.choice(opcoes) # o choice retorna um elemento da lista opcoes

# print(f"Você escolheu {usuario}")
# print(f"O computador escolheu {computador}")

# if usuario == computador:
#   print("Empate!")

# elif (usuario == "pedra" and computador == "tesoura") or \
#      (usuario == "papel" and computador == "pedra") or \
#      (usuario == "tesoura" and computador == "papel"):
#   print("Você venceu!")
# elif usuario in opcoes:
#   print("Você perdeu!") #se a opção que o usuario escolher estiver dentro da lista de opções mas não atender as condições de vitória
# else:
#   print("Escolha inválida!") #se o usuário digitar algo que não esteja na lista de opções


# 3. Calculadora de Tarifas de Táxi
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro
# rodado. Crie um programa que calcula o valor total da corrida com base na distância
# percorrida.

#RESOLUÇÃO

tarifa_basica = 4.00
adicional_por_km = 0.25

distancia_percorrida = float(input("Digite a distância percorrida na corrida (KM): "))

if distancia_percorrida > 0 and distancia_percorrida < 1:
  valor_corrida = tarifa_basica
  print(f"O valor total da corrida foi R$ {valor_corrida}")
elif distancia_percorrida > 1:
  valor_corrida = tarifa_basica + (distancia_percorrida * adicional_por_km)
  print(f"O valor total da corrida foi R$ {valor_corrida}")
else:
  print("Os dados informados não estão corretos!")

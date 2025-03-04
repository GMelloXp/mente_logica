
idade = 19

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


#condição aprovado/recuperação/reprovado

nota = 8

if nota >= 7.0:
    print("Você está aprovado")
elif nota >= 3 and nota < 7.0:
    print("Você está de recuperação")
else:
    print("Você está reprovado")


#calculando desconto em compras

#calculando desconto em compras
#Condições:
#se o preço for igual ou acima de 1000, o desconto é de 10%;
#se o preço for entre 500 e 999, o desconto é de 5%;
#se o preço for abaixo de 500, não terá desconto

preco = 499

if preco >= 1000:
  desconto = preco * 0.1
  print("Você recebeu um desconto de: R$", desconto)
  novo_valor = preco - desconto
  print("O novo valor é: R$", novo_valor)
elif preco >= 500 and preco < 1000:
  desconto = preco * 0.05
  print("Você recebeu um desconto de: R$", desconto)
  novo_valor = preco - desconto
  print("O novo valor é: R$", novo_valor)
else:
  print("Você não tem direito a desconto!!!")


#dia para ir a praia
#condições: ser sábado ou domingo e não estar chovendo

dia = "segunda"
esta_chovendo = False

if(dia == "sabado" or dia == "domingo") and not esta_chovendo:
  print("Hoje vamos para a praia!!!")
else:
  print("Hoje não vai rolar praia!")

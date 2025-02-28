
#Calculando o Troco.
# Você foi a uma padaria e comprou alguns itens:
# Pão: R$3.50
# Leite: R$4.20
# Café: R$2.80
# Você pagou com uma nota de R$20.
# Calcule quanto de troco você deve receber

#Resolução

# pao = 3.50
# leite = 4.20
# cafe = 2.80
# total = pao + leite + cafe
# valor_pago = 20
# troco = valor_pago - total
# print("Valor da conta: R$", total)
# print("Valor recebido: R$", valor_pago)
# print("O troco deve ser de R$", troco)

#Exercício 2
#Verificando Aprovação em um Exame
#Para ser aprovado em um exame, um estudante precisa ter uma nota média maior ou igual
# a 7.0 e uma frequência maior ou igual a 75%.
# Dados:
# Nota média: 8.5
# Frequência: 80%
# Verifique se o estudante foi aprovado.

#Resolução

# nota_media = 8.5
# frequencia_aluno = 80/100

# aprovado = (nota_media >= 7.0) and (frequencia_aluno >= (75/100))

# print("O aluno está aprovado? ", aprovado)

#Exercício 3
#Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o valor total da
# compra for superior a R$100.
# Dados:
# ● Quantidade de itens: 8
# ● Valor total: R$120
# Verifique se o cliente tem direito ao desconto.

#Resolução

# #dados da compra
# quantidade_itens = 8
# valor_total = 120

# #verificacao
# tem_desconto = (quantidade_itens > 10) or (valor_total > 100)
# print("O cliente tem direito a desconto? ", tem_desconto)


#Exercício 4
#Para acessar uma área restrita, o usuário deve inserir a senha correta e não pode estar bloqueado.
# Dados:
# ● Senha inserida: "abcd1234"
# ● Senha correta: "abcd1234"
# ● Usuário bloqueado: False
# Verifique se o acesso deve ser concedido.

#Resolução

#dados do usuário
# senha_inserida = "abcd1234"

# #dados do sistema
# senha_correta = "abcd1234"

# #situação
# usuario_bloqueado = False

# tem_acesso = (senha_inserida == senha_correta) and not usuario_bloqueado

# print("O usuário está liberado? ", tem_acesso)

#Exercício 5
#Três amigos vão dividir igualmente uma conta de R$150. Verifique quanto cada um deve
#pagar e se a divisão é exata (sem centavos restantes).

#Resolução
qtd_amigos = 3
valor_conta = 150
valor_individual = valor_conta / qtd_amigos
divisao_exata =  (valor_conta % qtd_amigos) == 0

print("Cada amigo deve pagar: R$", valor_individual)
print("A divisão é exata? ", divisao_exata)

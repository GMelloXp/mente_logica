
idade = 30
possui_carteira = True

#verificar se pode alugar um carro
pode_alugar = (idade > 21) and possui_carteira
print("Pode alugar o carro? ", pode_alugar)

#verificar se tem direito a meia-entrada
estudante = False
idoso = idade >= 60
meia_entrada = estudante or idoso
print("Tem direito a meia-entrada? ", meia_entrada)

#Inverter uma condição
chovendo = False
nao_chovendo = not chovendo
print("Está chovendo? ", chovendo)
print("Não está chovendo? ", nao_chovendo)

#analisando se um número é par

numero = int(input("Digite um número inteiro: "))
resto_divisão = numero % 2 
verificacao = resto_divisão == 0

print("O número digitado é par? ", verificacao)

#declaração de variáveis em python

nome = "Gabriel"
idade = 30
altura = 1.62
estudante = True

#exibindo as informações das variáveis

print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Estudante: ", estudante)

#calcular idade

ano_nascimento = 2025 - idade
print("Ano de nascimento: ", ano_nascimento)

#verificar se é maior de idade

maior_idade = idade >= 18
print("Maior de idade: ", maior_idade)

#manipulação de strings

frase = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos de idade."
print(frase)

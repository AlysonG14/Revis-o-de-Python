# Exercise 02

# MÉTODO - COM INPUT

ano = int(input("Digite o ano de nascimento: "))
nome = input("Digite o nome da pessoa: ")

idade = 2025 - ano

print("Olá, {} seja bem-vindo, você tem: {}".format(nome,idade))

# OUTRO MÉTODO - SEM O INPUT

ano_de_nascimento = 2002
primeiro_nome = 'David'

print(f'Olá, {primeiro_nome} seja-bem vindo, você tem {2025 - ano_de_nascimento}')


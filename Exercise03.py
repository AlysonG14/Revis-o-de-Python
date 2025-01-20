# Exercise 03 - IF, ELIF, ELSE

# - Primeiro Exercício do If e Else

num = int(input("Digite o número para verificar se é par ou ímpar: "))

if num % 2 == 0:
    print("{} Ele é Par".format(num))
else:
    print(f"{num} Ele é Ímpar")

# - Segundo Exercício do If e Else

nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a nota do aluno: "))
nota3 = float(input("Digite a nota do aluno: "))
nota4 = float(input("Digite a nota do aluno: "))
nota5 = float(input("Digite a nota do aluno: "))

todas_as_notas = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if todas_as_notas >= 5:
    print("APROVADO")
elif todas_as_notas <= 5 and todas_as_notas >= 2.5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

print("A média em geral fica na classficação de: {}".format(todas_as_notas))



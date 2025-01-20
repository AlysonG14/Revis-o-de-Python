# Exercise FOR & WHILE

# - Primeiro Exercício do FOR & WHILE

count = 0
while count <= 10:
    print(count)
    count += 1
else:
    print("Fim While")

# - Segundo Exercício do FOR & WHILE

solicite = int(input("Digite o número solicitado: "))
count = 0

while solicite >= count:
    if solicite <= 0:
        input('Digite o número solicitado: ')
        solicite += 1
    elif solicite <= 0:
        print("Acabou, você digitou negativo")
        break
else:
    print("Fim While")

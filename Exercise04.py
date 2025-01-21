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
    print('Numero atual {}'.format(solicite))
    solicite = int(input("Digite o número solicitado: "))

else:
    print('Acabou, você digitou o número negativo: {}'.format(solicite))

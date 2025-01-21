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
        print("Número atual: {}".format(solicite)) 
        solicite = int(input("Digite o número solicitado: "))

else:
     print('Acabou, você digitou negativo!')

# Exercicse 05 - Funções DEF

 # - Primeiro Exercício da Função DEF
 
def inverter_string(s):
     for i in s:
         print(i)
 
frase = input("Digite a frase: ")
 
resultado = (f'{inverter_string(reversed(frase))}')
print(resultado)

# - Segundo Exercício da Função DEF

def contar_caracters(string) -> str:
     dicionario = {}
     for i in string:
          if i in dicionario:
               dicionario[i] += 1
          else:
               dicionario[i] = 1
     return dicionario

resultado = contar_caracters('Banana')
print(resultado)
    

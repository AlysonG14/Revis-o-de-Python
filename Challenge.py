# Desafios

# Primeiro Desafio - O Merge Sort (Implementação sem utilização de funções e sem bibliotecas prontas)

def MergeSortPython(lista_de_alunos):
    if len(lista_de_alunos) <= 1:
        return lista_de_alunos
    
    meio = len(lista_de_alunos) // 2
    esquerda = lista_de_alunos[:meio] 
    direita = lista_de_alunos[meio:]
    
    Esquerda_classificado = MergeSortPython(esquerda)
    Direita_classificado = MergeSortPython(direita)

    return ordenação(Esquerda_classificado, Direita_classificado)

def ordenação(esquerda, direita):
    resultado = []
    ordena_para_esquerda = ordena_para_direita = 0

    while ordena_para_esquerda < len(esquerda) and ordena_para_direita < len(direita):
        if esquerda[ordena_para_esquerda] < direita[ordena_para_direita]:
            resultado += [esquerda[ordena_para_esquerda]]
            ordena_para_esquerda += 1
        else:
            resultado += [direita[ordena_para_direita]]
            ordena_para_direita += 1

    resultado += esquerda[ordena_para_esquerda:]
    resultado += direita[ordena_para_direita:]

    return resultado
 

lista_de_varios_alunos = ['Gabriel', 'Alyson', 'Leonardo', 'Renan', 'Daniel', 'Gustavo', 'Davi', 'Henrique', 'Emily']
resultado_da_ordenação = MergeSortPython(lista_de_varios_alunos)
print("Lista de Alunos:", (resultado_da_ordenação))


# Segundo Desafio - Insertion Sort e Bubble Sort

# - Implementando o Insertion Sort:

def InsertSort(lista):
    matriz = len(lista)          # Obtenha o comprimento da matriz
    
    if matriz <= 1:
        return                   # Se a matriz tiver 0 ou 1 elemento, ela já está classificada, então retorne
    
    for i in range(1, matriz):   # Interaja sobre a matriz começando pelo segundo elemento
        chave = lista[i]         # Guarda o elemento atual como a chave para ser inserido na posição certa
        j = i-1
        while j >= 0 and chave <= lista[j]: # Move os elementos maior do que a chave em uma posição à frente
            lista[j+1] = lista[j]           # Desloca os elementos para a direita
            j -= 1
        lista[j+1] = chave                  # Insere a chave na posição correta

# Classificando as listas númericas:
lista_numérica = [1, 5, 6, 8, 10, 3, 4]
InsertSort(lista_numérica)
print(lista_numérica)

# - Implementando o Bubble Sort



# Terceiro Desafio - Busca Linear e Busca Binária 


# Quarto Desafio - Pesquisar sobre complexidade de algoritmo e calcule a complexidade dos algoritmos anteriores


# Esse código faz a ordenação de um array do menor para o maior elemento

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# Em seguida é escrita a função de ordenação por seleção
def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print (ordenacaoporSelecao([5, 3, 6, 2, 10]))
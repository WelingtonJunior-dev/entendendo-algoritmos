def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9, 73, 80, 100]

print(f"O número 73 está na posição: {pesquisa_binaria(minha_lista, 73)}")
print(f"O número -1 está na posição: {pesquisa_binaria(minha_lista, -1)}")
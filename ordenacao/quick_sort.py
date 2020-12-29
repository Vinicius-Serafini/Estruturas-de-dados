def quick_sort(array, inicio=0, fim=None):

    assert isinstance(array, list), "O argumento deve ser do tipo list"

    fim = fim if fim is not None else len(array)

    if inicio < fim:
        pp = __particao(array, inicio, fim)
        quick_sort(array, inicio, pp)
        quick_sort(array, pp + 1, fim)
    return array

def __particao(array, inicio, fim):

    pivot = array[fim - 1]

    for index in range(inicio, fim):
        if array[index] > pivot:
            fim += 1
        else:
            fim += 1
            inicio += 1
            array[index], array[inicio - 1] = array[inicio - 1], array[index]
    
    return inicio - 1

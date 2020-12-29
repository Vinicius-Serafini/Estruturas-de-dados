def merge_sort(array, inicio=0, fim=None):

    assert isinstance(array, list), "O argumento deve ser do tipo list"

    fim = fim if fim is not None else len(array)

    if inicio < fim:
        meio = (inicio + fim) // 2

        merge_sort(array, inicio, meio)
        merge_sort(array, meio + 1, fim)

        __mescla(array, inicio, meio, fim)
    
    return array 

def __mescla(array, inicio, meio, fim):

    primeira_metade = array[inicio : meio+1]
    segunda_metade = array[meio+1 : fim+1] 

    i = inicio 
    posP = 0
    posS = 0

    while posP < len(primeira_metade) and posS < len(segunda_metade):
        if primeira_metade[posP] < segunda_metade[posS]:
            array[i] = primeira_metade[posP]
            posP += 1
        else:
            array[i] = segunda_metade[posS]
            posS += 1
        
        i += 1
    
    while posP < len(primeira_metade):
        array[i] = primeira_metade[posP]
        posP += 1
        i += 1
    
    while posS < len(segunda_metade):
        array[i] = segunda_metade[posS]
        posS += 1
        i += 1

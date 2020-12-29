def selection_sort(array):

    assert isinstance(array, list), "O argumento deve ser do tipo list"

    for index in range(len(array)):

        posicao_menor = index 

        for i in range(posicao_menor, len(array)):

            if array[i] < array[posicao_menor]:
                posicao_menor = i 
        
        array[index], array[posicao_menor] = array[posicao_menor], array[index]
    
    return array


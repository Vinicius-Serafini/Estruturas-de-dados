def bubble_sort(array):

    assert isinstance(array, list), "O argumento deve ser do tipo list"

    desordenado = True 

    while desordenado:
        desordenado = False 
        
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                desordenado = True

    return array 

def insertion_sort(array):

    assert isinstance(array, list), "O argumento deve ser do tipo list"

    for index in range(len(array)):
        copia = array[index]
        j = index - 1

        while j >= 0 and array[j] > copia:

            if array[j] > copia:
                array[j+1] = array[j]
            
            j -= 1
        
        array[j+1] = copia
    
    return array




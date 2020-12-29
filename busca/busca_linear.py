#  Retorna None caso não enconte o valor na lista

def busca_linear(array, chave):
    
    assert isinstance(array, list), "Argumento array deve ser do tipo list"
    
    for index in range(len(array)):
        if chave == array[index]:
            return index 
    return None

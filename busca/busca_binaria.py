# Retorna None se não encontrar o valor na lista

def busca_binaria(array, chave, posicao_inicial, posicao_final):

    assert isinstance(array, list), "Argumento array deve ser do tipo list"

    posicao_meio = (posicao_inicial + posicao_final) // 2
    
    if (chave == array[posicao_meio]):
        return posicao_meio
    elif (posicao_inicial >= posicao_final):
        return None
    else:
        if (array[posicao_meio] < chave):
            return busca_binaria(array, chave, posicao_meio+1 , posicao_final)
        else:
            return busca_binaria(array, chave, posicao_inicial , posicao_meio-1)

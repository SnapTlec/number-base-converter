def conversorBinToDec(binary):
    soma = 0
    # obter o  valor a ser convertido
    # multiplicar cada casa unitária por sua potênciação correspondente.
    # Example: 10110 -> seguindo da esquerda para a direita
    # 1 * 2^4
    # 0 * 2^3
    # 1 * 2^2
    # 1 * 2^1
    # 0 * 2^0
    aux = len(binary) # obter o tamanho do binário inserido
    for i in range(aux):
        if binary[i] == "1" or binary[i] == "0": # validação dos caracteres inseridos
            soma += int(binary[i])*2**((aux-1) - i)
        else:
            return False # caracteres digitados não corresponde a um binário valido.
    return soma

def div(number, list):
    # obter o valor a ser convertido
    # submeter esse valor a uma sequência de divições se o valor for diferente de 1
    quotient = number // 2 # obter o coeficiênte inteiro da divisão
    if number == 0:
        return False # caso o número  a ser convertido seja o zero(0), retorna Falso1
    elif(number == 1):
        list.append(number) 
    else:
        div(quotient, list)
        remainder = number - quotient * 2
        list.append(remainder) 
    
    return list

    # quando o coeficiênte for igual a 1 retornar o último coeficiênte
    # da divisão e os restos das divisões

def conversorDecToBin(number):
    binary = []
    # chamar uma função recursiva para dividi
    # e obter o coefiente da diviçã
    x =  div(number, binary)

    return x


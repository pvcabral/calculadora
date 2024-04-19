def converte_base(numero,saida):
    dic = {'10': 'A', '11': 'B', '12': 'c', '13': 'D', '14': 'E', '15': 'F'}
    resultado = []
    while numero >= saida:
        resultado.append(str(numero%saida))
        numero = int(numero/saida)
    
    resultado.append(str(numero))
    resultado.reverse()
    aux = ''

    for index in range(len(resultado)):
        if resultado[index] in dic:
            resultado[index] = dic[resultado[index]]
        aux += str(resultado[index])
    return aux

def solicita_usuario(numero,entrada,saida):
    numero = numero.upper()
    cont = 0
    for index in range(len(numero)):
        dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        if numero[index] in dic:
            cont = cont*entrada + dic[numero[index]]
        else: 
            cont = cont*entrada + int(numero[index])

    return converte_base(cont,saida)


    

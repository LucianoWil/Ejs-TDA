import pprint

def operaciones(k):
    #optimos = obtener_optimos(k)
    resultado = []
    indice = k
    while indice != 0:
        if indice % 2 == 0:
                resultado.append('por2')
                indice = indice / 2
        else:
            resultado.append('mas1')
            indice -= 1

    resultado.reverse()
    return resultado
def obtener_optimos(k):
    optimos = []

    for i in range(k + 1):
        if i == 0:
            optimos.append(0)
        elif i%2 == 0:
            optimos.append(min(optimos[i-1]+1, optimos[int(i/2)]+1))
        else:
            optimos.append(optimos[i-1]+1)

    return optimos

print(operaciones(13))
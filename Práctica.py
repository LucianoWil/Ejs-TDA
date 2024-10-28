def obtener_optimo(monedas):
    matriz = [[0 for j in range(len(monedas))] for  i in range(len(monedas))]    #O(n * n)

    elección_mateo_primera = 0 #elección de mateo si yo elijo la primera moneda
    elección_mateo_ultima = 0 #elección de mateo si yo elijo la última moneda
    optimo_primera_inicio = 0
    optimo_primera_fin = 0
    optimo_ultima_inicio = 0
    optimo_ultima_fin = 0
    indice_inicio = 0
    indice_fin = len(monedas) - 1

    for i in range(len(monedas)):
        for j in range(len(monedas)):
            if j > i:
                matriz[i][j] = 0
            elif i == j == 1:
                matriz[i][j] = monedas[indice_inicio]
                indice_inicio += 1
            elif i - j == 1:
                if monedas[indice_inicio] >= monedas[indice_fin]:
                    matriz[i][j] = monedas[indice_inicio]
                    indice_inicio += 1
                else:
                    matriz[i][j] = monedas[indice_fin]
                    indice_fin -= 1
            else:
                elección_mateo_primera = max(monedas[indice_inicio + 1], monedas[indice_fin])
                elección_mateo_ultima = max(monedas[indice_inicio], monedas[indice_fin - 1])
                if elección_mateo_primera == monedas[indice_inicio + 1]:
                    optimo_primera_inicio = 2
                    optimo_primera_fin = indice_fin
                else:
                    optimo_primera_inicio = indice_inicio + 1
                    optimo_primera_fin = indice_fin - 1
                if elección_mateo_ultima == monedas[indice_inicio]:
                    optimo_ultima_inicio = indice_inicio + 1
                    optimo_ultima_fin = indice_fin - 1
                else:
                    optimo_ultima_inicio = 0
                    optimo_ultima_fin = indice_fin - 2

                if monedas[indice_inicio] + matriz[optimo_primera_inicio][optimo_primera_fin] >= monedas[indice_fin] + matriz[optimo_ultima_inicio][optimo_ultima_fin]:
                    matriz[i][j] = monedas[indice_inicio] + matriz[optimo_primera_inicio][optimo_primera_fin]
                    indice_inicio = optimo_primera_inicio
                    indice_fin = optimo_primera_fin
                else:
                    matriz[i][j] = monedas[indice_fin] + matriz[optimo_ultima_inicio][optimo_ultima_fin]
                    indice_inicio = optimo_primera_inicio
                    indice_fin = optimo_primera_fin
    return matriz

def obtener_optimo(monedas):
    matriz = [[0 for j in range(len(monedas))] for  i in range(len(monedas))]    #O(n * n)

    elección_mateo_primera = 0 #elección de mateo si yo elijo la primera moneda
    elección_mateo_ultima = 0 #elección de mateo si yo elijo la última moneda
    optimo_primera_inicio = 0
    optimo_primera_fin = 0
    optimo_ultima_inicio = 0
    optimo_ultima_fin = 0
    indice_inicio = 0
    indice_fin = len(monedas) - 1

    for i in range(len(monedas)):
        for j in range(len(monedas)):
            if j > i:
                matriz[i][j] = 0
            elif i == j == 1:
                matriz[i][j] = monedas[indice_inicio]
                indice_inicio += 1
            elif i - j == 1:
                if monedas[indice_inicio] >= monedas[indice_fin]:
                    matriz[i][j] = monedas[indice_inicio]
                    indice_inicio += 1
                else:
                    matriz[i][j] = monedas[indice_fin]
                    indice_fin -= 1
            else:
                elección_mateo_primera = max(monedas[indice_inicio + 1], monedas[indice_fin])
                elección_mateo_ultima = max(monedas[indice_inicio], monedas[indice_fin - 1])
                if elección_mateo_primera == monedas[indice_inicio + 1]:
                    optimo_primera_inicio = 2
                    optimo_primera_fin = indice_fin
                else:
                    optimo_primera_inicio = indice_inicio + 1
                    optimo_primera_fin = indice_fin - 1
                if elección_mateo_ultima == monedas[indice_inicio]:
                    optimo_ultima_inicio = indice_inicio + 1
                    optimo_ultima_fin = indice_fin - 1
                else:
                    optimo_ultima_inicio = 0
                    optimo_ultima_fin = indice_fin - 2

                if monedas[indice_inicio] + matriz[optimo_primera_inicio][optimo_primera_fin] >= monedas[indice_fin] + matriz[optimo_ultima_inicio][optimo_ultima_fin]:
                    matriz[i][j] = monedas[indice_inicio] + matriz[optimo_primera_inicio][optimo_primera_fin]
                    indice_inicio = optimo_primera_inicio
                    indice_fin = optimo_primera_fin
                else:
                    matriz[i][j] = monedas[indice_fin] + matriz[optimo_ultima_inicio][optimo_ultima_fin]
                    indice_inicio = optimo_primera_inicio
                    indice_fin = optimo_primera_fin
    return matriz

monedas = [96,594,437,674,950]

matriz = obtener_optimo(monedas)
for fila in matriz:
    print(fila)

#print(obtener_optimo(monedas))
import sys

def dijkstra(grafo, nodo_inicial):
    etiquetas = {}
    visitados = []
    pendientes = [nodo_inicial]
    nodo_actual = nodo_inicial

    # Nodo inicial
    etiquetas[nodo_actual] = [0, '']

    # Seleccionar el siguiente nodo de menor peso acumulado
    while len(pendientes) > 0:
        nodo_actual = nodo_menor_peso(etiquetas, visitados)
        visitados.append(nodo_actual)

        # Obtener nodos adyacentes
        for adyacente, peso in grafo[nodo_actual].items():
            if adyacente not in pendientes and adyacente not in visitados:
                pendientes.append(adyacente)
            nuevo_peso = etiquetas[nodo_actual][0] + grafo[nodo_actual][adyacente]
            # Etiquetar
            if adyacente not in visitados:
                if adyacente not in etiquetas:
                    etiquetas[adyacente] = [nuevo_peso, nodo_actual]
                else:
                    if etiquetas[adyacente][0] > nuevo_peso:
                        etiquetas[adyacente] = [nuevo_peso, nodo_actual]
        del pendientes[pendientes.index(nodo_actual)]
    return etiquetas

def nodo_menor_peso(etiquetas, visitados):
    menor = sys.maxsize
    for nodo, etiqueta in etiquetas.items():
        if etiqueta[0] < menor and nodo not in visitados:
            menor = etiqueta[0]
            nodo_menor = nodo
    return nodo_menor

if __name__ == '__main__':
    grafo = {}
    num_nodos = int(input("Ingrese la cantidad de nodos en el grafo: "))
    for _ in range(num_nodos):
        nodo = input("Ingrese el nombre del nodo: ")
        conexiones = int(input("Ingrese la cantidad de conexiones para el nodo {}: ".format(nodo)))
        grafo[nodo] = {}
        for _ in range(conexiones):
            adyacente = input("Ingrese el nombre del nodo adyacente: ")
            peso = int(input("Ingrese el peso de la conexión: "))
            grafo[nodo][adyacente] = peso

    nodo_inicial = input("Ingrese el nodo inicial: ")
    etiquetas = dijkstra(grafo, nodo_inicial)
    print(etiquetas)



    '''
cómo ingresar los valores para crear un grafo utilizando el código modificado:

Ingrese la cantidad de nodos en el grafo: 3

Ingrese el nombre del nodo: A
Ingrese la cantidad de conexiones para el nodo A: 2
Ingrese el nombre del nodo adyacente: B
Ingrese el peso de la conexión: 4
Ingrese el nombre del nodo adyacente: C
Ingrese el peso de la conexión: 2

Ingrese el nombre del nodo: B
Ingrese la cantidad de conexiones para el nodo B: 1
Ingrese el nombre del nodo adyacente: C
Ingrese el peso de la conexión: 1

Ingrese el nombre del nodo: C
Ingrese la cantidad de conexiones para el nodo C: 1
Ingrese el nombre del nodo adyacente: A
Ingrese el peso de la conexión: 3

Ingrese el nodo inicial: A

En este ejemplo, estamos creando un grafo con 3 nodos: A, B y C. Luego, solicitamos las conexiones y los pesos para cada nodo. Finalmente, solicitamos el nodo inicial para ejecutar el algoritmo de Dijkstra.

Después de ingresar todos los valores, el programa calculará las etiquetas utilizando el algoritmo de Dijkstra y las imprimirá en la consola.

Recuerda que puedes ajustar el número de nodos y las conexiones según tus necesidades.¿
'''

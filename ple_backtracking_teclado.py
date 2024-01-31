def backtracking(variables, rango_variables, optimo, profundidad):
    min = rango_variables[profundidad][0]
    max = rango_variables[profundidad][1]
    for v in range(min, max):
        variables[profundidad] = v
        if profundidad < len(variables) - 1:
            if es_completable(variables):
                optimo = backtracking(variables[:], rango_variables, optimo, profundidad + 1)
        else:
            sol = evalua_solucion(variables)
            if sol > evalua_solucion(optimo) and es_completable(variables):
                optimo = variables[:]
    return optimo

def evalua_solucion(variables):
    x1 = variables[0]
    x2 = variables[1]
    val = (12 - 6) * x1 + (8 - 4) * x2
    return val

def es_completable(variables):
    x1 = variables[0]
    x2 = variables[1]
    val1 = 7 * x1 + 4 * x2
    val2 = 6 * x1 + 5 * x2
    if val1 <= 150 and val2 <= 160:
        return True
    else:
        return False

if __name__ == '__main__':
    num_variables = int(input("Ingrese la cantidad de variables en el PLE: "))
    variables = [0] * num_variables
    rango_variables = []
    for i in range(num_variables):
        min_val = int(input(f"Ingrese el valor mínimo para la variable x{i+1}: "))
        max_val = int(input(f"Ingrese el valor máximo para la variable x{i+1}: "))
        rango_variables.append((min_val, max_val))

    optimo = [0] * num_variables
    sol = backtracking(variables[:], rango_variables, optimo, 0)

    print('Mejor Solución:')
    for i, val in enumerate(sol):
        print(f'x{i+1} = {val}')
    print('Beneficio: ' + str(evalua_solucion(sol)))


'''
cómo ingresar los valores al programa modificado:

Ingrese la cantidad de variables en el PLE: 2
Ingrese el valor mínimo para la variable x1: 02
Ingrese el valor máximo para la variable x1: 51
Ingrese el valor mínimo para la variable x2: 0
Ingrese el valor máximo para la variable x2: 76

En este ejemplo, estamos ingresando que el PLE tiene 2 variables (x1 y x2) y los rangos de valores permitidos para cada variable. Para x1, el rango es de 0 a 51, y para x2, el rango es de 0 a 76.

Luego de ingresar estos valores, el programa calculará la mejor solución utilizando el algoritmo de Backtracking y mostrará la solución y el beneficio asociado en la consola.

Recuerda ajustar el número de variables y los rangos según tus necesidades y las restricciones de tu problema PLE.


'''
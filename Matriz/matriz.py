import numpy as np

# Funcion para detectar si hay una secuencia de manera horizontal
def detectHorizontalNumber(matriz):
    # Creamos un for que se repita la cantidad de veces depediendo de el largo de la matriz
     for i in range(len(matriz)):
         for j in range(2):             
            # Verificamos si los numeros de las columnas son iguales
            if ((matriz[i][j] == matriz[i][j+1]) and (matriz[i][j] == matriz[i][j+2]) and (matriz[i][j] == matriz[i][j+3])):
                """ Si encontramos que las columnas de la fila contiene numeros consecutivos mostramos en la consola
                    un mensaje que indique la posicion tanto de la columna como la fila
                    se muestra de una manera intuitiva evitando brindar posiciones que den 0
                    Y una vez encontrado se corta el ciclo
                """
                print(f'Se encontro una coincidencia horizontal en la posicion {j+1} a {j+4} de la fila {i+1} ')
                break
            
# Funcion para detectar si hay una secuencia de manera vertical
def detectVerticalNumber(matriz):
    # Creamos un for que se repita la cantidad de veces depediendo de el largo de la matriz
    for i in range(len(matriz)):
        for j in range(2):
            # Verificamos si los numeros de las filas son iguales en la misma columna
            if ((matriz[j][i]==matriz[j+1][i]) and (matriz[j][i]==matriz[j+2][i]) and (matriz[j][i]==matriz[j+3][i])):
                """ Si encontramos que las columnas contiene numeros consecutivos mostramos en la consola
                    un mensaje que indique la posicion tanto de la fila como la columna
                    se muestra de una manera intuitiva evitando brindar posiciones que den 0
                    Y una vez encontrado se corta el ciclo
                """
                print(f'Se encontro una coincidencia vertical desde la fila {j+1} hasta la {j+3} en la columna {i+1} ')
                break
            
def main():
    """ Creamos una matriz randomizada utilizando la funcion randint del modulo random de numpy
        como primer parametro le pasamos el numero maximo a generar aleatoriamente
        y como segundo parametro el tamaño de lista a generar.
    """
    matriz = np.random.randint(3, size=(5, 5))
    # Mostramos la matriz en la consola
    print(matriz)
    # Llamamos a las funciones para detectar numeros consecutivos tanto horizontalmente como verticalmente
    detectHorizontalNumber(matriz)
    detectVerticalNumber(matriz)

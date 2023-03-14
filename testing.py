import unittest
import sys
from io import StringIO
from Simple.simple import *
from Matriz.matriz import detectHorizontalNumber,detectVerticalNumber
from Clases.clases import Circulo


""" Inicializamos clase TesteExercise para probar los resultados que retorna los ejercicios.
    Se utilizo el modulo unittest que permite realizar los test de una manera facil y entendible
"""

class TestExercises(unittest.TestCase):
    
    _PRUEBAMATRIZ = [[1,1,1,1,1],[1,2,3,4,5,6],[1,4,5,6,7],[1,4,7,8,9],[4,2,3,4,6]]
    
    # Test para el modulo del ejercicio Simple
    def test_simple(self):
        # Verificamos si la funcion main devuelve una lista con 10 usuarios
        self.assertEqual(len(main()),10)
        prueba = [{id:1,'edad':80},{id:2,'edad':81},{id:3,'edad':82},{id:4,'edad':83},{id:5,'edad':84}]
        result = [{id:5,'edad':84},{id:4,'edad':83},{id:3,'edad':82},{id:2,'edad':81},{id:1,'edad':80}]
        # Verificamos si la funcion sortList ordena la lista correctamente
        self.assertEqual(sortList(prueba),result)
    
    # Test para el modulo del ejercicio Matriz funcion Horizontal
    def test_matriz_horizontal(self):
        out = StringIO()
        sys.stdout = out
        detectHorizontalNumber(self._PRUEBAMATRIZ)
        output = out.getvalue().strip()
        # Verificamos si el print es el correcto
        self.assertEqual(output,'Se encontro una coincidencia horizontal en la posicion 1 a 4 de la fila 1')

    # Test para el modulo del ejercicio Matriz funcion Vertical
    def test_matriz_vertical(self):
        out = StringIO()
        sys.stdout = out
        detectVerticalNumber(self._PRUEBAMATRIZ)
        output = out.getvalue().strip()
        # Verificamos si el print es el correcto
        self.assertEqual(output,'Se encontro una coincidencia vertical desde la fila 1 hasta la 3 en la columna 1')
    
    # Test para el modulo del ejercicio Clases
    def test_clases(self):
        circulo = Circulo(10)
        nuevoCirculo = circulo * 10
        """ Verificamos si al muliplicar la clase de Circulo se le asigna un radio diferente
            y retorna el Area y el Perimetro correctamente
        """
        self.assertEqual(nuevoCirculo.calculationArea(),31415.93)
        self.assertEqual(nuevoCirculo.calculationPerimeter(),628.32)
        
if __name__ == '__main__':
    test = TestExercises() 

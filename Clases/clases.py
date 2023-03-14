from math import pi

# Clase circulo
class Circulo():
    
    # Metodo inicializador de la clase Circulo
    def __init__(self,radio)->dict:
        # Verificamos si el radio ingresado es menor o igual a 0
        if (radio <= 0):
            # Retornamos un error en caso de recibir un radio incorrecto
            raise ValueError('Ups.. El radio ingresado es menor o igual a 0, tiene que ser mayor a 0. Vuelve a ingresar uno nuevamente!')
        self._radio = radio
        
    # Metodo property del atributo radio encapsulado    
    @property
    def radio(self)->int:
        return self._radio
    
    # Metodo setter de el atributo radio
    @radio.setter
    def radio(self,radio):
        # Verificamos si el radio es menor o igual a 0
        if radio <= 0:
            # Retornamos un error en caso de recibir un radio incorrecto
            raise ValueError('Ups.. Quisiste cambiar el radio por uno menor o igual a 0, tiene que ser mayor a 0. Vuelve a ingresar uno nuevamente!')
        # Asignamos un nuevo valor a el atributo radio de la clase
        self._radio = radio
    
    # Metodo que devuelve el area del circulo
    def calculationArea(self)->int:
        area = pi * self.radio ** 2
        return round(area,2)
    
    # Metodo que devuelve el parametro del circulo
    def calculationPerimeter(self)->int:
        perimeter = 2 * pi * self.radio
        return round(perimeter,2)
    
    # Metodo str de la clase que permite realizar representaciones mas amigables
    def __str__(self) -> str:
        return f'Circulo: Radio: {self.radio} Area: {self.calculationArea()} Perimetro: {self.calculationPerimeter()} '
    
    # Metodo que al multiplicar una instancia de la clase devuelve un objeto con el radio multiplicado
    def __mul__(self,num)->object:
        # Verificamos si el numero es menor o igual a 0
        if (num <= 0):
            # Retornamos un error en caso de recibir un numero incorrecto
            raise ValueError('Ups.. Has intentado multiplicar un radio por un numero menor o igual a 0. Eso no esta permitido, vuelve a ingresar uno nuevamente!')
        # Instanciamos un nuevo objeto con la multiplicacion del radio
        nuevoCirculo = Circulo(self.radio*num)
        return nuevoCirculo

import uuid
from random import randint as randomNumber
    
# Inicializamos la funcion principal        
def main() -> list:
    # Lista de usuarios
    users:list = []
    # Creamos un bucle que genere la cantidad de usuarios recibidos en el parametro quantity
    for i in range(10):
        # Obtenemos un numero aleaotorio entre 1 y 100 utilizando la funcion randint del modulo random
        age:int =  randomNumber(1,100)
        # Creamos el diccionario con las llaves id (Se genera un id unico utilizando la funcion uuid4 del modulo uuid) y edad
        user = {'id':str(uuid.uuid4()),'edad':age}
        # A continuacion comento otra forma de generar un id
        
        # user = {'id':i+1,'edad':age}

        # Pusheamos el usuario a la lista de usuarios
        users.append(user)

    # Retornamos los usuarios totales
    return users



import random

# Numeros rojos en una ruleta comun:
ROJOS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 }

class Ruleta:
    """Simula una ruleta de 37 números (0-36)"""
    def girar(self):
        """ 'Gira la ruleta' y devuelve un número entre 0 y 36"""
        return random.randint(0, 36)

    def es_rojo(self, num):
        """True si el número es rojo. (si el numero esta en la lista de numeros rojos)"""
        return num in ROJOS
 
    def es_negro(self, num):
        """True si el número es negro. (el numero es negro si no es rojo, el 0 nunca es negro)"""
        return num not in ROJOS and num != 0

    def es_par(self, num):
        """True si es par. El 0 no cuenta como par"""
        if num != 0:
            return num % 2 == 0
        return False

    def es_impar(self, num):
        """True si es impar """
        return num % 2 != 0 #no se excluimos explicitamente el 0 porque 0 % 2 == 0

    def es_bajo(self, num):
        """True si está entre 1 y 18"""
        return 1 <= num <= 18
   
    def es_alto(self, num):
        """True si está entre 19 y 36"""
        return 19 <= num <= 36

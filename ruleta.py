import random

ROJOS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 }

class Ruleta:
    def girar(self):
        return random.randint(0, 36)

    def es_rojo(self, num):
        return num in ROJOS
 
    def es_negro(self, num):
        return num not in ROJOS and num != 0

    def es_par(self, num):
        if num != 0:
            return num % 2 == 0
        return False

    def es_impar(self, num):
        return num % 2 != 0

    def es_bajo(self, num):
        return 1 <= num <= 18
   
    def es_alto(self, num):
        return 19 <= num <= 36

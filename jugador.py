class Jugador:
    INICIO = [1, 2, 3, 4]
    MIN_APUESTA = 5
    MAX_APUESTA = 4000

    def __init__(self, nombre, apuesta):
        self.nombre = nombre
        self.apuesta = apuesta
        self.cuaderno = list(self.INICIO)
        self.saldo = 0

    def calcular_apuesta(self):
        if len(self.cuaderno) == 1:
            return self.cuaderno[0]
        return self.cuaderno[0] + self.cuaderno[-1]

    def reiniciar_cuaderno(self):
        self.cuaderno = list(self.INICIO)

    def registrar_resultado(self, gano, monto):
        if gano: 
            self.saldo += monto
            self.cuaderno.append(monto)
        else:
            self.saldo -= monto
            if len(self.cuaderno) == 1:
                self.cuaderno.pop() 
            else:  
                self.cuaderno.pop() 
                self.cuaderno.pop(0)

        if len(self.cuaderno) == 0:
            self.reiniciar_cuaderno()

    def obtener_valida(self):
        apuesta = self.calcular_apuesta()
        if apuesta < self.MIN_APUESTA or apuesta > self.MAX_APUESTA:
            self.reiniciar_cuaderno()
            apuesta = self.calcular_apuesta()
        return apuesta


# cuaderno = [1, 2, 3, 4]

#cuaderno[0]      # primer elemento (no lo saca)
#cuaderno[-1]     # último elemento (no lo saca)
#cuaderno.append(x)   # agregar al final
#cuaderno.pop()        # sacar el último
#cuaderno.pop(0)       # sacar el primero (esto es lo "lento" que hablamos, pero no importa acá)
#len(cuaderno)         # cuántos elementos quedan
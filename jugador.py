class Jugador:
    """Un jugador con su propio cuaderno"""
    INICIO = [1, 2, 3, 4]
    MIN_APUESTA = 5
    MAX_APUESTA = 4000

    def __init__(self, nombre, tipo_apuesta):
        """
        nombre: identificador del jugador ("A", "B", "C"...)
        tipo_apuesta: función que con un número de la ruleta dice si ganó o no
                      (ej: ruleta.es_rojo)
        """
        self.nombre = nombre
        self.tipo_apuesta = tipo_apuesta
        self.cuaderno = list(self.INICIO)
        self.saldo = 0

    def calcular_apuesta(self):
        """Devuelve cuánto se va a apostar según el cuaderno actual"""
        if len(self.cuaderno) == 1:
            return self.cuaderno[0]
        return self.cuaderno[0] + self.cuaderno[-1]

    def reiniciar_cuaderno(self):
        """Vuelve a la secuencia inicial."""
        self.cuaderno = list(self.INICIO)

    def registrar_resultado(self, gano, monto):
        """Actualiza el cuaderno y el saldo según el resultado de la apuesta"""
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
        """Devuelve una apuesta válida según los límites de mesa, reiniciando el cuaderno si es necesario"""
        apuesta = self.calcular_apuesta()
        if apuesta < self.MIN_APUESTA or apuesta > self.MAX_APUESTA:
            self.reiniciar_cuaderno()
            apuesta = self.calcular_apuesta()
        return apuesta



from ruleta import Ruleta
from jugador import Jugador

RONDAS = 10000
CORRIDAS = 100

def simular_una():
    ruleta = Ruleta()

    jugadores = [
        Jugador("A", ruleta.es_rojo),
        Jugador("B", ruleta.es_negro),
        Jugador("C", ruleta.es_alto),
        Jugador("D", ruleta.es_bajo),
        Jugador("E", ruleta.es_impar),
        Jugador("F", ruleta.es_par),
    ]

    for _ in range(RONDAS):
        num = ruleta.girar()
        for jugador in jugadores:
            apuesta = jugador.obtener_valida()
            gano = jugador.tipo_apuesta(num)
            jugador.registrar_resultado(gano, apuesta)

    return sum(j.saldo for j in jugadores)


def main():
    res = []
    for _ in range(CORRIDAS): 
        res.append(simular_una())

    ganadas = sum(1 for r in res if r > 0)
    perdidas = sum(1 for r in res if r < 0)
    empatadas = sum(1 for r in res if r == 0)
    promedio = sum(res) / len(res)

    print(f"Corridas totales: {CORRIDAS}")
    print(f"El equipo ganó en:   {ganadas} corridas")
    print(f"El equipo perdió en: {perdidas} corridas")
    print(f"Empates:              {empatadas} corridas")
    print(f"Saldo promedio por corrida: {promedio:.2f}")
    print(f"Mejor corrida: {max(res)}")
    print(f"Peor corrida:  {min(res)}")
        
if __name__ == "__main__":
    main()
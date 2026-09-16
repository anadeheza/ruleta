from ruleta import Ruleta
from jugador import Jugador

RONDAS = 10000

def main():
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

    saldo_final = 0
    for j in jugadores:
        saldo_final += j.saldo
        print(f"jugador: {j.nombre}, saldo: {j.saldo}")

    print(f"\nSaldo final del equipo: {saldo_final}")
    if saldo_final > 0:
        print("ganaron")
    elif saldo_final < 0:
        print("perdieron")
    else:
        print("quedaron en cero")

if __name__ == "__main__":
    main()
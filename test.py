from ruleta import Ruleta
from jugador import Jugador

r = Ruleta()

# Giro y color 
for _ in range(10):
    n = r.girar()
    print(n, "rojo" if r.es_rojo(n) else "negro" if r.es_negro(n) else "cero")

print("\n")

# Ejemplos del enunciado: ganar y perder desde [1, 2, 3, 4] 
j = Jugador("A", None)
print(j.cuaderno)
print("apuesta: ", j.calcular_apuesta())

j.registrar_resultado(True, 5)
print(j.cuaderno)
print("ganó, su saldo es: ", j.saldo)

j.registrar_resultado(False, 5)
print(j.cuaderno)
print("perdió, su saldo es: ", j.saldo)

print("\n")

def chequear(ok, mensaje):
    """Imprime el resultado del chequeo y corta si falló."""
    print(("OK ;) -> " if ok else "FALLÓ :( -> ") + mensaje)
    assert ok, mensaje


# El 0 no entra en ninguna apuesta -> todos pierden.
chequear(not r.es_rojo(0), "0 no es rojo")
chequear(not r.es_negro(0), "0 no es negro")
chequear(not r.es_par(0), "0 no es par")
chequear(not r.es_impar(0), "0 no es impar")
chequear(not r.es_bajo(0), "0 no es bajo")
chequear(not r.es_alto(0), "0 no es alto")

# 18 números de cada tipo entre 1 y 36.
rojos = negros = pares = impares = bajos = altos = 0
for n in range(1, 37):
    rojos += r.es_rojo(n)
    negros += r.es_negro(n)
    pares += r.es_par(n)
    impares += r.es_impar(n)
    bajos += r.es_bajo(n)
    altos += r.es_alto(n)
chequear(rojos == negros == pares == impares == bajos == altos == 18,
         "18 números de cada tipo (rojo/negro, par/impar, bajo/alto)")

print("\ndesde el cuaderno inicial (1-2-3-4):\n")

# Si gana, agrega la apuesta al final del cuaderno (1-2-3-4 -> 1-2-3-4-5).
ganador = Jugador("ganador", None)
ganador.registrar_resultado(True, 5)
chequear(ganador.cuaderno == [1, 2, 3, 4, 5], "al ganar queda [1, 2, 3, 4, 5]")
chequear(ganador.calcular_apuesta() == 6, "siguiente apuesta es 1 + 5 = 6")
chequear(ganador.saldo == 5, "saldo neto al ganar es saldo + apuesta")

print("\n")
# Si pierde, tacha ambos extremos (1-2-3-4 -> 2-3).
perdedor = Jugador("perdedor", None)
perdedor.registrar_resultado(False, 5)
chequear(perdedor.cuaderno == [2, 3], "al perder queda [2, 3]")
chequear(perdedor.calcular_apuesta() == 5, "siguiente apuesta es 2 + 3 = 5")
chequear(perdedor.saldo == -5, "saldo neto al perder es saldo - apuesta")

print("\n")
# Un solo número en el cuaderno: esa es la apuesta, no se duplica.
uno = Jugador("uno", None)
uno.cuaderno = [7]
chequear(uno.calcular_apuesta() == 7, "con un solo número apuesta ese valor")

print("\n")
# Cuaderno vacío (se tacharon todos los números): vuelve a [1, 2, 3, 4].
vacio = Jugador("vacio", None)
vacio.registrar_resultado(False, 5)  # [2, 3]
vacio.registrar_resultado(False, 5)  # [] -> reinicia
chequear(vacio.cuaderno == [1, 2, 3, 4], "cuaderno vacío reinicia la secuencia inicial")


print("\n")
# Apuesta por debajo del mínimo (5) o por encima del máximo (4000): reinicia.
chica = Jugador("chica", None)
chica.cuaderno = [3]
chequear(chica.obtener_valida() == 5, "apuesta < 5: reinicia y apuesta 5")
chequear(chica.cuaderno == [1, 2, 3, 4], "después del mínimo el cuaderno es el inicial")

grande = Jugador("grande", None)
grande.cuaderno = [2000, 1, 2500]
chequear(grande.obtener_valida() == 5, "apuesta > 4000: reinicia y apuesta 5")
chequear(grande.cuaderno == [1, 2, 3, 4], "después del máximo el cuaderno es el inicial")

print("\n")
# Los límites de mesa sí se pueden apostar (5 y 4000 inclusive).
en_min = Jugador("en_min", None)
chequear(en_min.obtener_valida() == 5, "apuesta de 5 es válida")
en_max = Jugador("en_max", None)
en_max.cuaderno = [4000]
chequear(en_max.obtener_valida() == 4000, "apuesta de 4000 es válida")
chequear(en_max.cuaderno == [4000], "no reinicia si la apuesta está en el límite")

print("\n")
# Un jugador al rojo gana con un rojo y pierde con negro o con 0.
rojo = Jugador("rojo", r.es_rojo)
chequear(rojo.tipo_apuesta(1) is True, "n1 es rojo: gana quien apostó al rojo")
chequear(rojo.tipo_apuesta(2) is False, "2 es negro: pierde quien apostó al rojo")
chequear(rojo.tipo_apuesta(0) is False, "0: pierde quien apostó al rojo (o a cualquier cosa)")

print("\nTodo funciona :)")

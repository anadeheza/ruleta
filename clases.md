# CLASES
## Jugador

### Situacion inicial
At the beginning, the notebook looks like this (we'll call that the initial sequence): 1 - 2 - 3 - 4

- Maximum bet on the table is 4000.
- Minimum bet on the table is 5.

Para el notebook use una lista que empieza siendo [1, 2, 3, 4] y decalre el minimo y el maximo de apuestas como pedido

Cada jugador tiene su nombre (para definir quien gana), ademas de el tipo de apuesta que hace y su saldo inicial que es cero.

El saldo es cero al inicio ya que segun el problema los jugadores tienen dinero infinito, por lo que el saldo es el monto que ganaron/perdieron jugando y no sería su dinero total real, por lo que no importa realmente si es negativo, la comparación para buscar el ganador funciona igual.

### calcular_apuesta
"*In order to place their bets they add up both ends of the sequence*"
<br>
entonces cuando hay 2+ elementos, se suman el primero ( lista[0] ) y el ultimo ( lista[-1] )

"*If at some point he only has one number left, that's his bet (he doesn't have to double it as if he was adding both extremes).*"
<br>
Entonces cuando la longitud del cuaderno es 1 directamente devolvemos ese elemento como apuesta

### reiniciar_cuaderno
el cuaderno vuelve a ser la lista inicial ([1, 2, 3, 4])

### registrar_resultado
si gana se suma el monto duplicado 
In single bets, if you win, the table will pay you back twice as much: this means that if your bet was 10 you'll get 20 back. If you lose, the table takes the money from your bet.

### Por que un list?
pocos elem
mas facil de implementar

## Ruleta 
# Simulación de ruleta 

Simulación en Python de 6 jugadores apostando al mismo tiempo y en la misma mesa
de ruleta, cada uno con una apuesta simple distinta (rojo, negro, alto,
bajo, par, impar)

## Requisitos
- Python 3.x
- Sin dependencias externas: solo usa la librería estándar 'random'.

## Archivos

| Archivo                 | Contenido                                                                          
|-------------------------|------------------------------------------------------------------------------------
| ruleta.py               | Clase Ruleta: gira y clasifica números (rojo/negro/par/impar/alto/bajo).         
| jugador.py              | Clase Jugador: mantiene el cuaderno de cada jugador y calcula sus apuestas.      
| simulacion.py           | Corre una simulación de 10.000 tiradas con los 6 jugadores y muestra el resultado.
| test.py                 | Prueba manual: verifica el giro/clasificación de la ruleta y el comportamiento del cuaderno de un jugador (ganar, perder) contra los ejemplos del enunciado.                                        
| simulacion_multiple.py  | Corre la simulación completa 100 veces y reporta cuántas corridas ganó/perdió el equipo, el promedio, y los extremos — para evaluar el resultado con más de una muestra.                          

## Cómo correrlo

Simulación de 10.000 tiradas (consigna):

```bash
python simulacion.py
```

Simula 10.000 tiradas de ruleta, actualiza el cuaderno y saldo de cada uno
de los 6 jugadores según el resultado, y al final imprime el saldo de cada
jugador y el balance total del equipo.


Para validar reglas de la ruleta y el cuaderno con ejemplos puntuales:

```bash
python test.py
```

Para repetir la simulación 100 veces y ver la distribución de resultados
(para no sacar conclusiones, una sola corrida de 10.000 tiradas no nos dice mucho sobre la tendencia a ganar o perder del equipo, mas que nada para ver que los calculos se hagan bien incluso cuando se repite muchas veces):

```bash
python simulacion_multiple.py
```

## Estrategia 

Cada jugador arranca con el cuaderno [1, 2, 3, 4]. Para decidir cuánto
apostar, suma **el primer y el último número** del cuaderno (si solo queda un
número, apuesta ese). Si gana, agrega el monto apostado al final del cuaderno.
Si pierde, tacha (elimina) ambos extremos. Si el cuaderno queda vacío, o si la
próxima apuesta calculada se sale de los límites de mesa (mínimo 5, máximo
4000), reinicia con la secuencia inicial ([1, 2, 3, 4]).

## Resultados observados

Corriendo la simulación una vez, el resultado varía ya que los numeros de la ruleta son aleatorios. Para llegar a una conclusión hizo falta repetirlo muchas veces (100) y mirar la distribución de resultados.

Repitiendo la simulación 100 veces:

- El equipo perdió en casi todas las corridas (90-95 de 100).
- El saldo promedio por corrida fue negativo.
- Las pérdidas máximas superaron por bastante a las ganancias máximas.

Esto conincide con lo esperado: el 0 le da a la mesa una ventaja en cada apuesta y ningún sistema de apuestas puede cambiar esa tendencia a perder en el largo plazo. 

## Notas 

- El saldo representa la ganancia o pérdida neta acumulada (no el dinero total en la mesa ni el dinero que tenia el jugador): al ganar se suma solo el monto apostado (se recupera lo apostado + se gana lo mismo), y al perder se resta el monto apostado.
- Se asume dinero ilimitado para los 6 jugadores, nunca dejan de apostar por falta de fondos.
- Cada jugador tiene su propio cuaderno, los resultados de un jugador no afectan a los demás (solo comparten la misma ronda).
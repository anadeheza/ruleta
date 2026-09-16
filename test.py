from ruleta import Ruleta
from jugador import Jugador

r = Ruleta()

for _ in range(10):
    n = r.girar()
    print(n, "rojo" if r.es_rojo(n) else "negro" if r.es_negro(n) else "verde(0)")

print("\n")
j = Jugador("A", None)  
print(j.cuaderno) 
print("apuesta: ", j.calcular_apuesta())   

j.registrar_resultado(True, 5)  
print(j.cuaderno)          
print("ganó, su saldo es: ", j.saldo)    

j.registrar_resultado(False, 5)  
print(j.cuaderno)          
print("perdió, su saldo es: ", j.saldo)            
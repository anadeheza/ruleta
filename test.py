from ruleta import Ruleta
from jugador import Jugador

r = Ruleta()

for _ in range(10):
    n = r.girar()
    print(n, "rojo" if r.es_rojo(n) else "negro" if r.es_negro(n) else "verde(0)")

print("\n")
j = Jugador("A", None)  
print(j.cuaderno)          
print(j.calc_apuesta())   

j.regist_result(True, 5)  
print(j.cuaderno)          
print(j.saldo)    

j.regist_result(False, 5)  
print(j.cuaderno)          
print(j.saldo)            
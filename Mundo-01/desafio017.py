import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print (f'a hipotenusa vai medir {hi:.2f}')
import math
an = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(an))
print (f'O ângulo de {an} tem o seno de {seno:.2f} ')
cos = math.cos(math.radians(an))
print (f'O ângulo de {an} tem o cosseno de {cos:.2f}')
tan = math.tan(math.radians(an))
print (f'O ângulo de {an} tem a tangente de {tan:.2f}')
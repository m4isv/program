import math

angulo = float(input("digite o angulo\n"))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print(f"o angulo de {angulo} tem o seno de {seno:.2f} o cosseno e {cosseno:.2f} a tangente e {tangente:.2f}")

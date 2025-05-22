# Pedir al usuario que ingrese un número
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("=========Dibujo===========")
N = int(input("Ingresa un número entero positivo: "))

for i in range(N):
    print("*", end="")


print()

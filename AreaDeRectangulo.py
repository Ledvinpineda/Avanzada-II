#Calculando el area de un rectangulo
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("========Area de un rectangulo==========")

lado_A = int(input("Ingrese la base del rectangulo: "))
lado_b = int(input("Ingrese la altura del rectangulo: "))

area = lado_A * lado_b

print(f"{lado_A} * {lado_b} = ", area)
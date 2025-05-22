#Pidiendo al usuario que ingrese dos numeros para luego sumarlos
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("========Suma de dos Numeros========")
a = int(input("Ingrese el primer numero: "))
x = int(input("Inrese el segundo numero: "))

suma = a+x

print(f"{a} + {x} = ", suma)
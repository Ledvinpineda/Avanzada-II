#Tablas de multiplicar con ciclo for

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("========Tablas de multiplicar=========2")

num=int(input("Ingresa un numero: "))

for i in range(1,11):
    print(f"{num}*{i}= {num*i}")
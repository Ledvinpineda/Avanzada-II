#Sumando numeros hasta N con ciclo for 
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("========Suma de numros=======")
N = int(input("Ingrese un numero: "))
suma = 0

for i in range(1, N+1):
    suma =+ i
print(suma)

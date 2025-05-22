#Utilizando condicionales le pedimos al usuario que ingrese un numero y validamos si es mayor o menor que cero 
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("========Mayor o Menor Que 0==========")
a = int(input("Ingrese un numero: "))

if a > 0 :
    print(f"{a} es mayor que 0")  
else:
    if a == 0 :
        print(f"{a} es igual a 0 no es nayor ni menor")
    else:
        if a < 0 :
            print(f"{a} es menor que 0")
    
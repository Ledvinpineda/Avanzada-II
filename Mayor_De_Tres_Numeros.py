#Determinando numero mmayor de tres ingresados
import os
os.system('cls' if os.name == 'nt' else 'clear')


print("========Mayor de 3 numeros=========")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a > b and a > c:
    print(f"{a} es mayor que {b} y {a} es mayor que {c}, por lo tanto {a} es el numero mayor")
elif b > a and b > c:
        print(f"{b} es mayor que {a} y {b} es mayor que {c}, por lo tanto {b} es el numero mayor") 
else:
        if c > a and c > b:
            print(f"{c} es mayor que {a} y {c} es mayor que {b}, por lo tanto {c} es el numero mayor")
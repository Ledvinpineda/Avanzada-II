#Determinando si un numero es par o impar

import os
os.system('cls' if os.name == 'nt' else 'clear') 
print("=========Par o Impar=========")
a=int(input("a: "))

if a%2==0:
    if a==0:
        print("El cero no se puede tomar como par o impar")
    else:
        print(f"{a} es par")
else:
    print(f"{a} es impar")
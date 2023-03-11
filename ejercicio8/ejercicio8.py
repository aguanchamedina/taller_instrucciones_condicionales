print("-------------------------")
print("---------MULTIPLO--------")
print("-------------------------")

# INPUT
a = int(input ("Ingresa el primer numero: "))
b = int(input ("Ingresa el segundo numero: "))

# PROCESS 
def calcular (x, y):
    if x % y == 0:
        print(f"{x} es multiplo de {y}") #OUTPUT
    elif y % x == 0:
        print(f"{y} es multiplo de {x}") #OUTPUT
    else:
        print("Los numeros no son multiplos ") #OUTPUT

calcular(a,b)
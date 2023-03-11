print("---------------------------------")
print("---------MASA CORPORAL-----------")
print("---------------------------------")

# INPUT
a = float(input("Ingrese el peso en kilogramos: "))
b = float(input("Ingrese la altura en metros: "))

# PROCESS 

imc = a // (b ** 2)
if imc < 16:
    print("Critico se recomienda ingreso a un hospital") #OUTPUT
elif 16 < imc < 17:
    print("Infrapeso") #OUTPUT
elif 17 < imc < 18:
    print("Bajo peso") #OUTPUT
elif 18 < imc < 25:
    print("Peso normal (Saludable)") #OUTPUT
elif 25 < imc < 30:
    print("Sobrepeso (Obesidad grado I)") #OUTPUT
elif 30 < imc < 35:
    print("Sobrepeso cronico (Obesidad grado II)") #OUTPUT
elif 35 < imc < 40:
    print("Obesidad premorbida (obesidad grado III)") #OUTPUT
elif 40 < imc:
    print("Obesidad mórbida (obesidad de grado IV)") #OUTPUT
else:
    print("Hubo un error con los datos") #OUTPUT
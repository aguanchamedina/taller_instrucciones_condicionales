print("------------------------------------------------")
print("-----------GANANCIA DE LA PAPELERIA-------------")
print("------------------------------------------------")

# INPUT
a = int(input("Ingrese el valor del costo: "))

#  PROCESS 
if a < 3000:
    b = a * (15/100) 

elif 3000 < a < 6000:
    b = 500

elif a > 6000:
    b = a * 25/100

c = a + b 

# OUTPUT
print("El precio total del prodructo es : " + str(c))
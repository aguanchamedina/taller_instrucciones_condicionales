print("--------------------------------------------")
print("-----------PRESTAMO BANCARIO----------------")
print("--------------------------------------------")
print (" ")
print("REQUISITOS")
print(" *Para acceder a un prestamo con el banco debe de tener unos ingresos totales de $945.200")    
print(" *No tener deudas con el banco  ")
print (" ")

# INPUT
nombre = input("Digite nombre completo: ")
ingresos = int(input("Cantidad de ingresos totales: "))
deudas = int(input("Posee alguna de deudas?  \n1.SI \n2.NO \nrta:"))
prestamo = int(input ("Digite la cantidad del pretamo: "))

# PROCESS 
if ingresos > 945200 and deudas == 2:
    print("Señor@: " + str(nombre) + " no posee deudas " + "Su prestamo de: " + str(prestamo) + " a sido aprovado!") #OUTPUT

else:

    ingresos < 945200 and deudas == 1
    print("Señor@: " + str(nombre) +  " udted posee deudas, " + "Su prestamo de: " + str(prestamo) + " NO a sido aprovado!") #OUTPUT



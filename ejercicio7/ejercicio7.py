print("------------------------------------------")
print("---------SUMA DOS PRIMEROS DIGITOS--------")
print("------------------------------------------")

# INPUT

X = int(input("ingresa el primer valor:"))
Y = int(input("ingresa el segundo valor:"))
Z = int(input("ingresa el tercer valor:"))

# PROCESS 
if Z == X + Y:
    msj = print("La suma de los dos primeros digitos es igual al tercero "+ str(X)+ "+" + str(Y)+"="+str(Z) ) #OUTPUT
else :
    print("La suma de los dos primeros digitos no es igual al tercero "+ str(X)+ "+" + str(Y)+ " NO ES "+str(Z) ) #OUTPUT

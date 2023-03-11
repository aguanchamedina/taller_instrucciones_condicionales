print("---------------------------------------------------------")
print("-----------COORDENADAS DE PLANO CARTECIANO---------------")
print("---------------------------------------------------------")


x = float(input("Digite la coordenada de x: "))
y = float(input("Digite la coordenada de y: "))

if x > 0 and y > 0:
    print("-------------------------------------------------------------------")
    print("El punto se encuentra en el primer cuadrante del plano carteciano. ")
    print("-------------------------------------------------------------------")

if x < 0 and y > 0:
    print("-------------------------------------------------------------------")
    print("El punto se encuentra en el segundo cuadrante del plano carteciano. ")
    print("-------------------------------------------------------------------")

if x < 0 and y < 0:
    print("-------------------------------------------------------------------")
    print("El punto se encuentra en el tercer cuadrante del plano carteciano. ")
    print("-------------------------------------------------------------------")

if x > 0 and y < 0:
    print("-------------------------------------------------------------------")
    print("El punto se encuentra en el cuarto cuadrante del plano carteciano. ")
    print("-------------------------------------------------------------------")
from math import acos, degrees

# input
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# processing
alfa  = degrees(acos((c**2 - a**2 - b**2)/(-2*a*b)))
beta  = degrees(acos((b**2 - a**2 - c**2)/(-2*a*c)))
theta = degrees(acos((a**2 - b**2 - c**2)/(-2*b*c)))

if a+b>c and a+c>b and b+c>a:
    if alfa > 90 or beta > 90 or theta > 90:
        triangle = "Triángulo obtuso"
    elif alfa < 90 and beta < 90 and theta < 90:
        triangle = "Triángulo agudo"
    else:
        triangle = "Triángulo rectángulo"
else:
    triangle = "Triángulo no válido"

# outpu
print("Resultado: ", triangle)


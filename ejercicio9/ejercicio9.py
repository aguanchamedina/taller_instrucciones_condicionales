from math import acos, degrees

print("-----------------------")
print("-------TRIANGULO-------")
print("-----------------------")
  
#INPUT
a=float(input("Dijite el valor del Lado A: "))
b=float(input("Dijite el valor del Lado B: "))
c=float(input("Dijite el valor del Lado C: "))

#PROCESS
seno  = degrees(acos((c**2 - a**2 - b**2)/(-2*a*b)))
coseno  = degrees(acos((b**2 - a**2 - c**2)/(-2*a*c)))
tangente = degrees(acos((a**2 - b**2 - c**2)/(-2*b*c)))

if a+b>c and a+c>b and b+c>a:
    if seno > 90 or coseno > 90 or tangente > 90:
        triangulo = "Triángulo obtuso"
    elif seno < 90 and coseno < 90 and tangente < 90:
        triangulo = "Triángulo agudo"
    else:
        triangulo = "Triángulo rectángulo"
else:
    triangulo = "Triángulo no válido"

# OUTPUT
print("Los lados ingresados conforman un", triangulo)




import os
os.system("cls")

print("\n sentencia condicional ")


edad = 18 
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")


edad = 15 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")    




    print("\nelif condicional")

nota = 3
if nota >= 9:
    print("!Sobresaliente¡")
elif nota >=7:
    print("Notable")
elif nota >=5:
    print("Aprobado")
else: 
    print("!No esta calificado¡")    



print("\n&& -> and  ,  || -> or")
edad = 17
tiene_carnet = True


if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No tienes permitido conducir")

    
print("\nmismo caso pero en Venezuela")
edad = 17
tiene_carnet = False


if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Pagale al policia y sales ganando")

    

    
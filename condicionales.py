# Declaramos una variable 
calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)

# Preguntamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("Veees, por no estudiar") # Si es menor a 700 muestra esto
elif calificacion == 700 :
    print("PANZASOOOOO")
elif calificacion > 1000 :
    print("MIENTES!!!! No puedes sacar mas de mil")
else : # Si no se cumple el if anterior pasa a esta linea
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ningunos de los if se cumple

# Verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <=100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

# En Python no hay Switch Case
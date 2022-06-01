# Declarar variable
calificacion = input("Introduce tu calificaión de la certificación AZ-900: ")

# Casteo
calificacion = int(calificacion)

# Condicional
if calificacion < 700 :
    print("Reprobado")
elif calificacion > 1000 :
    print("Favor de introducir un valor maximo de 1000")
else :
    print("Felicidades as aprobado")

# Verificador de edad
edad = input("Introduce tu edad ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Eres mayor de edad")
elif edad > 100 : 
    print("Tienes mas de 100 años")
elif edad < 0 :
    print("Favor de ontroducir valores positivos")
else :
    print("Eres menor de edad")

# En Python no hay Switch case
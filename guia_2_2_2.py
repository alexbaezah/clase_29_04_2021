"""1) consulta de edad, en base a ello indicar si es mayor o menor de edad """

edad = 0

while type(edad) == int: 
    edad = int(input("ingrese su edad "))
    if edad >= 18: 
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
    opcion = input("¿deseas salir? \t escribe si o no ")
    if opcion == "si":
        edad = False 
    else:
        type(edad) == int



        
    
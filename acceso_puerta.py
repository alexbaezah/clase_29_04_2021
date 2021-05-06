acceso_puerta = False 
acumulador = 0

while acceso_puerta == False: 
    user = input("ingrese usuario ")
    contraseña = str(input("ingrese contraseña "))
    if (user == "pedro" and contraseña == "1234") or (user == "angel" and contraseña == "a4s1"):
        acceso_puerta = True
        print("accediendo... ")
    
    elif acumulador == 3: 
        acceso_puerta = True
        print("Excediste el número de cantidad de veces")
    
    else: 
        acumulador += 1
        print(f"tienes 3 intentos, llevas {acumulador} intento ")
        acceso_puerta = False
    


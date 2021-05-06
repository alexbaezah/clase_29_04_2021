def pregunta_1():
    print( "¿Cuál de los siguiente personajes dice la frase: yo soy tu padre?\n")
    print("1. Darth Vader \n2. Walter White\n3. Gokú\n4. Colo Colo")

def pregunta_2():
    print( "¿De quién es el ataque kame hame ha?\n")
    print("1. Vegeta \n2. Naruto\n3. Goku\n4. Luffy")

def pregunta_3():
    print( "¿De quién es la frase: nunca se le da la espalda a la familia?\n")
    print("1. Totoro \n2. del Toro\n3. Toreto\n4. Paul Walker")

def pregunta_4():
    print( "¿A quién parodia Kinnikuman?\n")
    print("1.Superman\n2. Ultraman\n3. Goku\n4. Godzilla")



puntaje = 0


while puntaje < 4:
    pregunta_1()
    alternativa = str(input("Ingrese la anternativa correcta ")) 
    if alternativa == "1":
        puntaje += 1
        print(f"llevas {puntaje} punto")
    else:
        puntaje += 0 
    pregunta_2()
    alternativa = str(input("Ingrese la anternativa correcta ")) 
    if alternativa == "3":
        puntaje += 1 
        print(f"llevas {puntaje} puntos")
    else:
        puntaje += 0 
    pregunta_3()
    alternativa = str(input("Ingrese la anternativa correcta ")) 
    if alternativa == "3":
        puntaje += 1 
        print(f"llevas {puntaje} puntos")
    else:
        puntaje += 0 
    pregunta_4()
    alternativa = str(input("Ingrese la anternativa correcta ")) 
    if alternativa == "2":
        puntaje +=1 
        print(f"llevas {puntaje} puntos, finalizaste la trivia")
    else:
        print(f"llevas {puntaje} puntos")
        print("intenta nuevamente...")


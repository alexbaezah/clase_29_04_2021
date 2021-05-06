puntaje = 0
parte_1 = "Cuál de los siguientes animales vive en el agua\n"
parte_2 = "1. Perro \n2. Cocodrilo\n3. Conejo\n4. Tiburón"


print(parte_1 + parte_2)
alternativa = str(input("Ingrese la anternativa correcta "))
if alternativa == "2":
    puntaje += 0.5
    print(f"tu puntaje es de {puntaje}")
elif alternativa == "4":
    puntaje += 1
    print(f"tu puntaje es de {puntaje}")
else:
    print("fallaste")


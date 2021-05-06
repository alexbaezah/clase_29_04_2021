nota_1 = float(input("ingrese primera nota "))
nota_2  = float(input("ingrese segunda nota "))
nota_3  = float(input("ingrese tercera nota "))

notas = [nota_1, nota_2, nota_3]
prom = 0
indice = len(notas)


for i in notas:
    prom += i 

prom = prom / indice
print(f"{prom:,.2f}")

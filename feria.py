acumulador = 0 

bebida = input("¿Desea llevar una bebida. si/no ")
if bebida == "si": 
    acumulador = acumulador + 300 
else:
    print("no hay bebida, no lleva nada")
    acumulador = acumulador

print(f"compraste por un monto de: {acumulador}")

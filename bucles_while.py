cantNotas = 5
sumatoriadenotas = 0

while cantNotas > 0:
    nota = int(input("Por favor ingrese la nota Numero {}: ".format(cantNotas)))
    sumatoriadenotas = sumatoriadenotas + nota
    cantNotas = cantNotas-1

promedio = sumatoriadenotas / 5

if promedio >= 7:
    print("Usted ha aprobado con un promedio de {}. Felicitaciones!!!".format(promedio))
else:
    print("Usted ha desaprobado con un promedio de {} .".format(promedio))

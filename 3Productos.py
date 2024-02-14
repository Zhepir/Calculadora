cantProductos = 3
EjemploLista = []
Costo_total=0

for _ in range(cantProductos):
    print("Ingresando informacion informacion del producto #{} " .format(cantProductos))
    Nombre = input("Ingrese el nombre del producto: ")
    Cantidad = int(input("Ingrese la cantidad a llevar de este: "))
    PrecioU = float(input("Ingrese el precio de este ítem: "))
    EjemploLista.append({"nombre": Nombre, "cantidad": Cantidad, "precio": PrecioU})
    total= PrecioU * Cantidad
    Costo_total = Costo_total+total
    cantProductos=cantProductos-1
    print("-----------------------------------------------")


for producto in EjemploLista:
    print(producto)

print()

print("Costo total de los productos: ${}" .format(Costo_total))

if Costo_total>3000:
    print("Felicidades! usted ha ganado una bonificacion del 10%")
    bonificacion= Costo_total*0.10
    total_bonificado=Costo_total-bonificacion
    print("Monto total con bonificacion: ${}" .format(total_bonificado))
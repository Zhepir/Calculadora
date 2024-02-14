# buscar tutorial como subir a un repositorio github

def suma (numero1 ,numero2):
    resultado = numero1+numero2
    return resultado

def resta (numero1 ,numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicacion (numero1 ,numero2):
    resultado = numero1 * numero2
    return resultado

def division(numero1, numero2):
    if numero2 == 0:
        print("No es posible dividir por cero")
        return None
    resultado = numero1 / numero2
    return resultado

continuar = True

while continuar:
    primer_numero = int(input("Ingrese el primer valor, por favor: "))
    operacion = input("Ingrese el tipo de operacion que quiere hacer (+, -, *, /): ")
    segundo_numero = int(input("Ingrese el segundo valor, por favor: "))

    while operacion not in ["+", "-", "*", "/"]:
        print("Operación ingresada incorrecta. Por favor elija una de las siguientes opciones: +, -, *, /")
        operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

    if operacion == "+":
        print(suma(primer_numero, segundo_numero))
    elif operacion == "-":
        print(resta(primer_numero, segundo_numero))
    elif operacion == "*":
        print(multiplicacion(primer_numero, segundo_numero))
    elif operacion == "/":
        print(division(primer_numero, segundo_numero))

    continuar_respuesta = input("Desea hacer otra operacion matematica? (si/no): ").lower()
    while continuar_respuesta not in ["si", "no"]:
        print("Opción ingresada incorrecta.")
        continuar_respuesta = input("Por favor, ingrese 'si' o 'no': ").lower()

    if continuar_respuesta != "si":
        continuar = False

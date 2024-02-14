
# Tarea no hacer que no descuente cuando el caracter no es valido

import random

def contadorletras(palabra):
    return len(palabra)

def imprimirAhorcado():
    if intentos == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif intentos == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif intentos == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 5:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)

def descubrir(palabra, letras_acertadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_acertadas:
            resultado = resultado + letra
        else:
            resultado = resultado + "-"
    return resultado


palabras = ["Tomate", "Python", "Auto", "Libro", "Sol"]

palabras = [palabra.lower() for palabra in palabras]

palabraAleatoria = random.choice(palabras)

palabraConcatenada=set(palabraAleatoria)


letrasAcertadas=[]

intentos=6;

print(palabraAleatoria)

print("Tiene {} intentos".format(intentos))
adivinanza =input("Ingrese una letra: ")

while intentos != 0:
    if adivinanza.isalpha():
        if adivinanza in palabraAleatoria:
            print("¡Correcto! La letra introducida es correcta.")
            letrasAcertadas.append(adivinanza)

        else:
            intentos = intentos - 1
            imprimirAhorcado()
            print("Palabra incorrecta. Te quedan {} intentos.".format(intentos))
    else:
        print("Por favor ingrese una letra valida.")
    if intentos == 0:
        print("¡Te quedaste sin intentos! La palabra correcta era '{}'.".format(palabraAleatoria))
        break
    if set(palabraAleatoria)==set(letrasAcertadas):
        print("Haz adivinado correctamente la palabra es {}".format(palabraAleatoria))
        break

    print(descubrir(palabraAleatoria,letrasAcertadas))


    adivinanza = input("Ingrese una letra: ")
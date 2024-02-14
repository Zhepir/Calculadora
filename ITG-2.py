
def descubrir(palabra , letras_acertadas):
    resultado=""
    for letra in palabra:
        if letra in letras_acertadas:
            resultado=resultado+letra+""
        else:
            resultado=resultado+"-"
    return resultado

adivinanza = input("Ingrese una letra, por favor: ")

descubrir(adivinanza, )
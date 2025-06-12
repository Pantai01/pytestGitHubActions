def calcularAreaTriangulo(base, altura):
    #Si la base o la altura son menores o iguales a cero, retorna -1
    if base <= 0 or altura <= 0:
        return -1
    return (base * altura) / 2


def calcularAreaCuadrado(lado):
    #Si el lado es menor o igual a cero, retorna -1
    if lado <= 0:
        return -1
    return lado * lado

def calcularArea(figura, **kwargs):
    if figura == "triangulo":
        return calcularAreaTriangulo(kwargs.get("base"), kwargs.get("altura"))
    elif figura == "cuadrado":
        return calcularAreaCuadrado(kwargs.get("lado"))
    else:
        raise ValueError("Figura no reconocida")
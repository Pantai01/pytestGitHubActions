def calcularAreaTriangulo(base, altura):
    if base < 0 or altura < 0:
        return -1
    return (base * altura) / 2


def calcularAreaCuadrado(lado):
    if lado < 0:
        return -1
    return lado * lado

def calcularArea(figura, **kwargs):
    if figura == "triangulo":
        return calcularAreaTriangulo(kwargs.get("base"), kwargs.get("altura"))
    elif figura == "cuadrado":
        return calcularAreaCuadrado(kwargs.get("lado"))
    else:
        raise ValueError("Figura no reconocida")
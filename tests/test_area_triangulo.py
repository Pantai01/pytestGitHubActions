from app import calcularArea
def test_area_triangulo():
    assert calcularArea("triangulo", base=4, altura=3) == 6

def test_area_triangulo_cero():
    assert calcularArea("triangulo", base=0, altura=3) == 0

def test_area_triangulo_negativo():
    assert calcularArea("triangulo", base=-4, altura=3) == -1
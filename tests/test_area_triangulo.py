from app import calcularArea
def test_area_triangulo():
    assert calcularArea("triangulo", base=5, altura=7) == 17.5

def test_area_triangulo_cero():
    assert calcularArea("triangulo", base=0, altura=3) == -1

def test_area_triangulo_negativo():
    assert calcularArea("triangulo", base=-4, altura=3) == -1
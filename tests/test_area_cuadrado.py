from app import calcularArea

def test_area_cuadrado():
    assert calcularArea("cuadrado", lado=4) == 16

def test_area_cuadrado_cero():
    assert calcularArea("cuadrado", lado=0) == 0

def test_area_cuadrado_negativo():
    assert calcularArea("cuadrado", lado=-4) == -1
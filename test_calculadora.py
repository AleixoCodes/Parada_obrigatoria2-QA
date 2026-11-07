import pytest

from Calculadora import adicao

@pytest.mark.parametrize(
    "x, y, esperado",
    [
        (2, 3, 5),
        (50, 10, 60),
        (-3, -7, -10),
        (1.5, 2.5, 4.0),
    ],
)
def test_adicao(x, y, esperado):
    assert adicao(x, y) == pytest.approx(esperado)
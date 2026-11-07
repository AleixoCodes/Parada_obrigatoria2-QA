import itertools
import math

import pytest

import Calculadora as calc

def eh_erro(resultado):
    return isinstance(resultado, str) and resultado.startswith("Erro")

def bug(numero, descricao):
    return pytest.mark.xfail(strict=True, reason=f"BUG-{numero:02d}: {descricao}")

def simular_entradas(monkeypatch, respostas):
    iterador = iter(respostas)
    monkeypatch.setattr("builtins.input", lambda *_: next(iterador))

# BUG-02 --------------------------------------------------------------------
@bug(2, "fatorial retorna sempre 0")
@pytest.mark.parametrize("n", [0, 1, 5, 9, 50])
def test_fatorial_de_numero_nao_negativo(n):
    assert calc.fatorial(n) == math.factorial(n)

# BUG-03 --------------------------------------------------------------------
@bug(3, "fatorial aceita número negativo")
@pytest.mark.parametrize("n", [-1, -10, -50])
def test_fatorial_de_numero_negativo_retorna_erro(n):
    assert eh_erro(calc.fatorial(n))

# BUG-04 --------------------------------------------------------------------
@bug(4, "logaritmo natural usa np.ln, que não existe")
@pytest.mark.parametrize("x", [1, 22, 100])
def test_logaritmo_natural(x):
    assert calc.logaritmo_natural(x) == pytest.approx(math.log(x))

# BUG-05 --------------------------------------------------------------------
@bug(5, "logaritmo base 10 calcula o logaritmo natural")
@pytest.mark.parametrize("x, esperado", [(10, 1), (20, math.log10(20)), (100, 2)])
def test_logaritmo_base10(x, esperado):
    assert calc.logaritmo_base10(x) == pytest.approx(esperado)

# BUG-06 --------------------------------------------------------------------
@bug(6, "logaritmo base 10 aceita zero e retorna -inf")
def test_logaritmo_base10_de_zero_retorna_erro():
    assert eh_erro(calc.logaritmo_base10(0))

# BUG-07 --------------------------------------------------------------------
@bug(7, "divisão por zero levanta ZeroDivisionError")
@pytest.mark.parametrize("x, y", [(10, 0), (10.0, 0.0), (-3, 0)])
def test_divisao_por_zero_retorna_erro(x, y):
    assert eh_erro(calc.divisao(x, y))

# BUG-08 --------------------------------------------------------------------
@bug(8, "potência de base negativa com expoente fracionário retorna nan")
@pytest.mark.parametrize("x, y", [(-5, 0.5), (-8, 1 / 3)])
def test_potencia_de_resultado_nao_real_retorna_erro(x, y):
    assert eh_erro(calc.potencia(x, y))

# BUG-09 --------------------------------------------------------------------
@bug(9, "seno listado no menu, mas não implementado")
@pytest.mark.parametrize("graus, esperado", [(0, 0), (30, 0.5), (90, 1)])
def test_seno_em_graus(graus, esperado):
    assert calc.seno(graus) == pytest.approx(esperado, abs=1e-9)

@bug(9, "seno listado no menu, mas não implementado")
def test_menu_opcao_10_executa_o_seno(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["10", "30", "n"])
    calc.calculadora_cientifica()
    assert "Operação inválida" not in capsys.readouterr().out

# BUG-10 --------------------------------------------------------------------
@bug(10, "cosseno chama função inexistente")
@pytest.mark.parametrize(
    "graus, esperado", [(0, 1), (45, math.sqrt(2) / 2), (60, 0.5), (90, 0)]
)
def test_cosseno_em_graus(graus, esperado):
    assert calc.cosseno(graus) == pytest.approx(esperado, abs=1e-9)

# BUG-11 --------------------------------------------------------------------
@bug(11, "tangente chama função inexistente")
@pytest.mark.parametrize("graus, esperado", [(0, 0), (45, 1)])
def test_tangente_em_graus(graus, esperado):
    assert calc.tangente(graus, radianos=False) == pytest.approx(esperado, abs=1e-9)

@bug(11, "tangente chama função inexistente")
def test_tangente_em_radianos():
    assert calc.tangente(math.pi / 4, radianos=True) == pytest.approx(1)

@bug(11, "tangente chama função inexistente")
@pytest.mark.parametrize("graus", [90, 270, -90])
def test_tangente_de_angulo_indefinido_retorna_erro(graus):
    assert eh_erro(calc.tangente(graus, radianos=False))

# BUG-12 --------------------------------------------------------------------
@bug(12, "entrada não numérica encerra o programa com ValueError")
@pytest.mark.parametrize(
    "opcao, entrada_invalida",
    [("1", "abc"), ("2", "abc"), ("3", "abc"), ("6", "numero"), ("7", "3.5"), ("8", "x"), ("9", "x")],
)
def test_entrada_nao_numerica_nao_encerra_o_programa(
    monkeypatch, opcao, entrada_invalida
):
    # Depois da entrada inválida, qualquer pergunta recebe "0" (um número válido
    # e também uma resposta que encerra o "deseja continuar?").
    simular_entradas(
        monkeypatch,
        itertools.chain([opcao, entrada_invalida], itertools.repeat("0")),
    )
    try:
        calc.calculadora_cientifica()
    except ValueError as erro:
        pytest.fail(f"Entrada inválida causou ValueError: {erro}")
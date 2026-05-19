import pytest
from calculadora import Calculadora

def test_soma():
    calc = Calculadora()
    assert calc.soma(2, 3) == 5
    assert calc.soma(-1, 1) == 0

def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(10, 5) == 5

def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(3, 4) == 12

def test_divisao():
    calc = Calculadora()
    assert calc.divisao(10, 2) == 5

def test_varias_operacoes():
    """Teste de integração: simulando uma cadeia de cálculos."""
    calc = Calculadora()
    res = calc.soma(10, 10)          # 20
    res = calc.multiplicacao(res, 2) # 40
    res = calc.subtracao(res, 10)    # 30
    res = calc.divisao(res, 3)       # 10
    assert res == 10

def test_divisao_por_zero():
    """Parte 2: Ciclo TDD - Esperando ValueError."""
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.divisao(10, 0)


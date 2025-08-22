import pytest
from calculadora import Calculadora


def test_adicao():
    calc = Calculadora()
    assert calc.adicao(5, 3) == 8
    assert calc.adicao(-1, 1) == 0
    assert calc.adicao(-1, -1) == -2
    assert calc.adicao(0, 0) == 0


def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(5, 3) == 2
    assert calc.subtracao(3, 5) == -2
    assert calc.subtracao(-1, 1) == -2
    assert calc.subtracao(-1, -1) == 0
    assert calc.subtracao(0, 0) == 0


def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(5, 3) == 15
    assert calc.multiplicacao(-1, 5) == -5
    assert calc.multiplicacao(-1, -1) == 1
    assert calc.multiplicacao(0, 5) == 0
    assert calc.multiplicacao(5, 0) == 0


def test_divisao():
    calc = Calculadora()
    assert calc.divisao(10, 2) == 5
    assert calc.divisao(5, 2) == 2.5
    assert calc.divisao(-10, 2) == -5
    assert calc.divisao(-10, -2) == 5
    assert calc.divisao(0, 5) == 0
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        calc.divisao(10, 0)


def test_potenciacao():
    calc = Calculadora()
    assert calc.potenciacao(2, 3) == 8
    assert calc.potenciacao(5, 0) == 1
    assert calc.potenciacao(2, 1) == 2
    assert calc.potenciacao(4, 0.5) == 2  # Raiz quadrada
    assert calc.potenciacao(9, 0.5) == 3  # Raiz quadrada
    
    # Teste com expoente negativo inteiro
    assert calc.potenciacao(2, -2) == 0.25
    assert calc.potenciacao(5, -1) == 0.2


def test_raiz_quadrada():
    calc = Calculadora()
    assert calc.raiz_quadrada(9) == 3
    assert calc.raiz_quadrada(4) == 2
    assert calc.raiz_quadrada(0) == 0
    assert calc.raiz_quadrada(2.25) == 1.5
    with pytest.raises(ValueError, match="Não é possível calcular a raiz quadrada de um número negativo."):
        calc.raiz_quadrada(-1)


def test_validacao_tipos():
    calc = Calculadora()
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calc.adicao("5", 3)
    
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calc.subtracao(5, "3")
    
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calc.multiplicacao("2", 3)
    
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calc.divisao(10, "2")
    
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calc.potenciacao("2", 3)
    
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calc.raiz_quadrada("9")


def test_expoente_decimal_nao_suportado():
    calc = Calculadora()
    with pytest.raises(ValueError, match="Expoente decimal não suportado"):
        calc.potenciacao(2, 0.3)
    
    with pytest.raises(ValueError, match="Expoente decimal não suportado"):
        calc.potenciacao(3, 1.2)
class Calculadora:
    
    def _validar_numerico(self, *valores):
        for valor in valores:
            if not isinstance(valor, (int, float)):
                raise TypeError("Os valores devem ser numéricos")
    
    def adicao(self, a, b):
        self._validar_numerico(a, b)
        return a + b

    def subtracao(self, a, b):
        self._validar_numerico(a, b)
        return a - b

    def multiplicacao(self, a, b):
        self._validar_numerico(a, b)
        return a * b

    def divisao(self, a, b):
        self._validar_numerico(a, b)
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def potenciacao(self, base, expoente):
        self._validar_numerico(base, expoente)
        
        if expoente == 0:
            return 1
        if expoente == 1:
            return base
        
        if expoente == 0.5:
            return self.raiz_quadrada(base)
        
        if expoente > 0 and expoente == int(expoente):
            resultado = 1
            for _ in range(int(expoente)):
                resultado *= base
            return resultado
        
        if expoente < 0 and expoente == int(expoente):
            resultado = 1
            for _ in range(int(-expoente)):
                resultado *= base
            return 1 / resultado
        
        raise ValueError("Expoente decimal não suportado para valores diferentes de 0.5")

    def raiz_quadrada(self, numero):
        self._validar_numerico(numero)
        
        if numero < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        if numero == 0:
            return 0
        
        x = numero
        for _ in range(10):
            x = (x + numero / x) / 2
        return x
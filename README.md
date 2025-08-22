# Calculadora em Python com TDD

Uma calculadora robusta desenvolvida usando Test-Driven Development (TDD) com pytest, implementando operações matemáticas básicas e avançadas.

## 📋 Funcionalidades

### Operações 
- **Adição**: Soma de dois ou mais números
- **Subtração**: Diferença entre dois números
- **Multiplicação**: Produto de dois ou mais números
- **Divisão**: Quociente entre dois números (com tratamento para divisão por zero)
- **Potenciação**: Cálculo de potências (base ^ expoente)
- **Raiz Quadrada**: Cálculo de raízes quadradas



## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd calculadora-tdd
```

2. **Instale as dependências**:
```bash
pip install pytest
```

### Executando os Testes

```bash
# Executar todos os testes com verbose
pytest test_calculadora.py -v

# Executar testes com cobertura
pytest test_calculadora.py --cov=calculadora

# Executar testes específicos
pytest test_calculadora.py::TestCalculadora::test_adicao_numeros_positivos -v

# Executar testes com relatório detalhado
pytest test_calculadora.py --cov=calculadora --cov-report=html
```

### Estrutura do Projeto

```
calculadora-tdd/
├── calculadora.py          # Implementação da classe Calculadora
├── test_calculadora.py     # Testes unitários com pytest
└── README.md              # Este arquivo
```

## 🧪 Testes Implementados

A suite de testes cobre:

- **Operações com números positivos e negativos**
- **Operações com zero**
- **Números decimais**
- **Tratamento de erros e exceções**
- **Validação de tipos de dados**
- **Casos especiais e edge cases**
- **Múltiplos argumentos**

### Categorias de Testes

1. **Testes de Adição**: Somas variadas com diferentes tipos de números
2. **Testes de Subtração**: Diferenças em diversos cenários
3. **Testes de Multiplicação**: Produtos e casos especiais
4. **Testes de Divisão**: Quocientes e tratamento de divisão por zero
5. **Testes de Potenciação**: Potências com bases e expoentes variados
6. **Testes de Raiz Quadrada**: Raízes e tratamento de números negativos
7. **Testes de Validação**: Verificação de tipos de dados

## 🔧 Métodos da Classe Calculadora

### Métodos Públicos
- `adicionar(*valores)`: Soma dois ou mais números
- `subtrair(a, b)`: Subtrai b de a
- `multiplicar(*valores)`: Multiplica dois ou mais números
- `dividir(a, b)`: Divide a por b
- `potenciar(base, expoente)`: Calcula base elevada ao expoente
- `raiz_quadrada(numero)`: Calcula a raiz quadrada




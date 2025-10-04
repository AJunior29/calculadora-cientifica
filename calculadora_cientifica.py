import math

# --- FUNÇÕES MATEMÁTICAS ---

def soma(valores):
    return sum(valores)

def subtrai(valores):
    if not valores: return 0
    resultado = valores[0]
    for v in valores[1:]:
        resultado -= v
    return resultado

def multiplica(valores):
    resultado = 1
    for v in valores:
        resultado *= v
    return resultado

def divide(valores):
    if not valores: return 0
    resultado = valores[0]
    for v in valores[1:]:
        if v == 0:
            raise ValueError("divisão por zero é inválida.")
        resultado /= v
    return resultado

def raiz_quadrada(valor):
    if valor < 0:
        raise ValueError("raiz de número negativo é inválida.")
    return math.sqrt(valor)

def potencia(base, expoente):
    return math.pow(base, expoente)

def logaritimo(valor, base=10):
    if valor <= 0:
        raise ValueError("logaritmo de número não positivo é inválido.")
    return math.log(valor, base)

def fatorial(valor):
    if valor < 0 or int(valor) != valor:
        raise ValueError("fatorial de número negativo ou não inteiro é inválido.")
    return math.factorial(int(valor))

def seno(graus):
    return math.sin(math.radians(graus))

def cosseno(graus):
    return math.cos(math.radians(graus))

def tangente(graus):
    if abs(graus) % 180 == 90:
        raise ValueError("tangente de 90° e seus múltiplos (indefinida).")
    return math.tan(math.radians(graus))


# --- FUNÇÕES DE SUPORTE ---

def obter_numero(mensagem, tipo=float):
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


# --- EXECUÇÃO PRINCIPAL ---

MAPA_OPERACAO = {
    "1": (soma, "Digite os Números separados por um espaço:"),
    "2": (subtrai, "Digite os Números separados por um espaço:"),
    "3": (multiplica, "Digite os Números separados por um espaço:"),
    "4": (divide, "Digite os Números separados por um espaço:"),
    "5": (raiz_quadrada, "Digite o número:"),
    "8": (fatorial, "Digite o número (inteiro):"),
    "10": (seno, "Digite o ângulo em graus:"),
    "11": (cosseno, "Digite o ângulo em graus:"),
    "12": (tangente, "Digite o ângulo em graus:"),
}


def main():
    print("-" * 30)
    print("      CALCULADORA CIENTÍFICA       ")
    print("-" * 30)
    print("1 - Soma          5 - Raiz Quadrada  9 - Pi")
    print("2 - Subtração     6 - Potência      10 - Seno")
    print("3 - Multiplicação 7 - Logaritmo     11 - Cosseno")
    print("4 - Divisão       8 - Fatorial      12 - Tangente")
    print("-" * 30)

    op = input("Digite o número da operação: ")
    print("-" * 30)

    try:
        if op in ["1", "2", "3", "4"]:
            _, mensagem = MAPA_OPERACAO[op]
            entrada_str = input(mensagem)
            valores = list(map(float, entrada_str.split()))
            funcao, _ = MAPA_OPERACAO[op]
            resultado = funcao(valores)

        elif op in ["5", "8", "10", "11", "12"]:
            funcao, mensagem = MAPA_OPERACAO[op]
            tipo_conversao = int if op == "8" else float
            valor = obter_numero(mensagem, tipo=tipo_conversao)

            resultado = funcao(valor)

        elif op == "6":
            base = obter_numero("Digite a base: ")
            expoente = obter_numero("Digite o expoente: ")
            resultado = potencia(base, expoente)

        elif op == "7":
            valor = obter_numero("Digite o Número: ")
            base_str = input("Digite a base (Enter para base 10): ")
            base = float(base_str) if base_str else 10.0
            resultado = logaritimo(valor, base)

        elif op == "9":
            resultado = math.pi

        else:
            print("Operação inválida.")
            return

        print(f"Resultado: {resultado}")

    except ValueError as e:
        if 'invalid literal' in str(e) or 'could not convert' in str(e):
             print("Erro de entrada: A entrada contém caracteres não numéricos. Tente novamente.")
        else:
            print(f"Erro na operação: {e}")

    except KeyError:
        print("Erro: Opção inválida.")

if __name__ == "__main__":
    main()

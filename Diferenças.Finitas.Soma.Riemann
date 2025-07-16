import numpy as np

# Derivada por Diferenças Finitas (centrada)
def diferencas_finitas(f, x, ordem=1, h=1e-5):
    try:
        if ordem == 1:
            return (f(x + h) - f(x - h)) / (2 * h)
        elif ordem == 2:
            return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
        else:
            raise ValueError("Ordem inválida. Use 1 ou 2.")
    except Exception as e:
        print("Erro no cálculo da derivada:", e)
        return None

# Integral por Soma de Riemann
def soma_riemann(f, a, b, n=1000, tipo='meio'):
    h = (b - a) / n
    if tipo == 'esquerda':
        x = np.linspace(a, b - h, n)
    elif tipo == 'direita':
        x = np.linspace(a + h, b, n)
    elif tipo == 'meio':
        x = np.linspace(a + h / 2, b - h / 2, n)
    else:
        raise ValueError("Tipo inválido. Use: 'esquerda', 'direita', 'meio' ou 'todas'.")

    y = []
    for xi in x:
        try:
            val = f(xi)
            if np.isnan(val) or np.isinf(val):
                val = 0
        except Exception:
            val = 0
        y.append(val)
    return np.sum(y) * h

# Função principal
def main():
    print("Você deseja calcular:")
    print("1 - Derivada por Diferenças Finitas")
    print("2 - Integral por Soma de Riemann")
    escolha = input("Escolha a opção (1 ou 2): ").strip()
    print("\nDigite a função f(x), por exemplo: x^2 + sin (x)")
    print("Você pode usar: sin, cos, tan, exp, log, sqrt, e, pi, abs")
    func_str = input("f(x) = ").replace("^", "**")
    safe_dict = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'log': np.log,
        'sqrt': np.sqrt,
        'abs': np.abs,
        'pi': np.pi,
        'e': np.e,
        'x': 0
    }
    def f(x):
        safe_dict['x'] = x
        return eval(func_str, {"__builtins__": None}, safe_dict)

    # Intervalo fixo para a integral
    a = 0.1
    b = 3
    n = 1000

    if escolha == '1':
        try:
            x = float(input("Digite o ponto x para derivar: "))
            ordem = int(input("Ordem da derivada (1 ou 2): "))
            resultado = diferencas_finitas(f, x, ordem)
            if resultado is not None:
                print(f"\nResultado: Derivada de ordem {ordem} em x = {x} ≈ {resultado:.6f}")
        except Exception as e:
            print("\nErro ao calcular a derivada:", e)
    elif escolha == '2':
        try:
            tipo = input("Tipo de soma (esquerda, direita, meio ou todas): ").lower()
            if ('log' in func_str or 'sqrt' in func_str) and a <= 0:
                print("Erro: o limite inferior deve ser > 0 para log ou sqrt.")
                return
            if tipo == 'todas':
                for t in ['esquerda', 'direita', 'meio']:
                    resultado = soma_riemann(f, a, b, n, t)
                    print(f"Soma de Riemann ({t}): {resultado:.6f}")
            else:
                resultado = soma_riemann(f, a, b, n, tipo)
                print(f"Resultado: Integral de f(x) de {a} a {b} ({tipo}) ≈ {resultado:.6f}")
        except Exception as e:
            print("\nErro ao calcular a integral:", e)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

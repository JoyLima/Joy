import numpy as np

def soma_riemann(f, a, b, n=1000, tipo='meio'):
    h = (b - a) / n
    if tipo == 'esquerda':
        x = np.linspace(a, b - h, n)
    elif tipo == 'direita':
        x = np.linspace(a + h, b, n)
    elif tipo == 'meio':
        x = np.linspace(a + h/2, b - h/2, n)
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
    y = np.array(y)
    return np.sum(y) * h

def main():
    print("== Cálculo da Integral por Soma de Riemann ==")
    print("Digite a função f(x), ex: x^2 + sin (x)")
    print("Você pode usar: sin, cos, tan, exp, log, sqrt, e, pi")
    func_str = input("f(x) = ").replace("^", "**")
    tipo = input("Tipo de soma (esquerda, direita, meio ou todas): ").lower()

    # Intervalo fixo
    a = 0.1   #evita zero para log e sqrt
    b = 3
    n = 1000

    if ('log' in func_str or 'sqrt' in func_str) and a <= 0:
        print("\nErro: para funções log ou sqrt, o limite inferior fixo deve ser > 0.")
        return
    if b <= a:
        print("\nErro: limite superior deve ser maior que o inferior.")
        return

    safe_dict = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'log': np.log,
        'sqrt': np.sqrt,
        'pi': np.pi,
        'e': np.e,
        'abs': np.abs,
        'x': 0
    }

    def f(x):
        safe_dict['x'] = x
        return eval(func_str, {"__builtins__": None}, safe_dict)
    try:
        tipos_validos = ['esquerda', 'direita', 'meio', 'todas']
        if tipo not in tipos_validos:
            print("\nTipo inválido! Escolha: esquerda, direita, meio ou todas.")
            return
        if tipo == 'todas':
            for t in ['esquerda', 'direita', 'meio']:
                resultado = soma_riemann(f, a, b, n, t)
                print(f"Soma de Riemann ({t}): {resultado:.6f}")
        else:
            resultado = soma_riemann(f, a, b, n, tipo)
            print(f"Soma de Riemann ({tipo}): {resultado:.6f}")
    except Exception as e:
        print("\nErro durante o cálculo:", e)

if __name__ == "__main__":
    main()

import numpy as np

def diferencas_finitas(f, x, ordem=1, h=1e-5):
    if ordem == 1:
        return (f(x + h) - f(x - h)) / (2 * h)
    elif ordem == 2:
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
    else:
        return None

def main():
    print("Digite a função f(x), ex: x^2 + sin(x)")
    print("Você pode usar: sin, cos, tan, exp, log, e, pi e sqrt")

#Converte ^ para ** e outras funções
    func_str = input("f(x) = ").replace("^", "**")
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
        x = float(input("Digite o ponto x para calcular a derivada: "))
        ordem = int(input("Digite a ordem da derivada (1 ou 2): "))
        if ordem not in [1, 2]:
            print("\nApenas derivadas de 1ª ou 2ª ordem são permitidas.")
            return
        resultado = diferencas_finitas(f, x, ordem)
        print(f"\nResultado: Derivada ordem {ordem} de f(x) em x = {x} é aproximadamente: {resultado}")
    except Exception as e:
        print("\nErro durante o cálculo:", e)

if __name__ == "__main__":
    main()

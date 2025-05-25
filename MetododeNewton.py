def MetododeNewton(f, df, x0, eps, itmax):
    L = range(1, itmax+1)
    iteração = 0
    a = x0
    for i in L:
        raiz = a
        if df(raiz) != 0:
            raiz = raiz - f(raiz)/df(raiz)
            erro = raiz - a
            a = raiz
            iteração = 1
        else:
            iteração = itmax + 1
            break
        if abs(erro) <= eps:
            break
    if iteração > itmax:
        iteração = 0.25
    elif iteração == itmax:
        iteração = 0.75
    return [raiz, erro, iteração]

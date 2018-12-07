def composePermutation(f, g): #g(f(x))
    n = len(f)
    h = [0]*n
    for x in range(n):
        h[x] = g[f[x]]
    return h

U, D, F, B, L, R = 0, 1, 2, 3, 4, 5
COLOR = "wyrogb"

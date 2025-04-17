def fat(n):
    return 1 if n == 0 else n * fat(n - 1)

m = dict()
def f(n):
    if n < 2: return n

    if m.get(n) is not None:
        return m[n]

    m[n] = f(n - 1) + f(n - 2)

    return m[n]
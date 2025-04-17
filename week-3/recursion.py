def fat(n):
    return 1 if n == 0 else n * fat(n - 1)

def f(n):
    if n == 0: return 0

    if n == 1: return 1

    return f(n - 1) + f(n - 2)
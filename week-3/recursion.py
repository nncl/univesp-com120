def fat(n):
    return 1 if n == 0 else n * fat(n - 1)

def f(n):
    if n < 2: return n

    return f(n - 1) + f(n - 2)
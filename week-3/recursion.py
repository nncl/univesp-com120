def fat(n):
    return 1 if n == 0 else n * fat(n - 1)

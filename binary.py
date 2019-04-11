
def bin(n):
    an = ""
    N = n
    while N > 0:
        a = N % 2
        N = N // 2
        an = str(a) + an
    return an
print(bin(3))


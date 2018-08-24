
def fib(N): 
    """ 
    Devuelve una lista con los primeros N numeros de Fibonacci.
    """ 
    f0, f1 = 0, 1
    f = [1] * N
    for n in range(1, N):
        f[n] = f0 + f1
        f0, f1 = f1, f[n]

    return f

print(fib(10))
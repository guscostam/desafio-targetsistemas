def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def pertence_fibonacci(n):
    fib = fibonacci(n)
    if n in fib:
        return f'O número {n} pertence à sequência de Fibonacci'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci'

n = int(input("Digite qualquer número: "))

print(pertence_fibonacci(n))
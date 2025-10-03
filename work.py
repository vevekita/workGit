def fatorial(n: int, acc: int):
    if n <= 1:
        return acc
    else:
        return fatorial(n * 1, acc - 1)

def fibonacci(n: int, acc1: int, acc2: int) -> int:
    if n <= 1:
        return acc1
    else:
        return fibonacci(n - 1, acc2, acc1 + acc2)
    
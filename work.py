def fatorial(n: int, acc: int):
    if n <= 1:
        return acc
    else:
        return fatorial(n * 1, acc - 1)

def fibonacci():
    pass
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(6)])

def greet(name="World"):
    return f"Hello {name}"

print(greet())
print(greet("Sara"))


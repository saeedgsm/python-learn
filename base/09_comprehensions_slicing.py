nums = [1, 2, 3, 4, 5]
even_squares = [n*n for n in nums if n % 2 == 0]
print(even_squares)

names = ["ali", "sara", "reza"]
caps = {n: n.capitalize() for n in names}
print(caps)

a = list(range(10))
print(a[2:7])
print(a[:5])
print(a[::2])


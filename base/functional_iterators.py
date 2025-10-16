nums = [1, 2, 3, 4, 5]

double = list(map(lambda n: n * 2, nums))
evens = list(filter(lambda n: n % 2 == 0, nums))
print(double)
print(evens)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for v in countdown(3):
    print(v)



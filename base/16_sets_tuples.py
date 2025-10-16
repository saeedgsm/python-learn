# مجموعه‌ها (set) و تاپل‌ها (tuple) در پایتون

# tuple: غیرقابل‌تغییر، مرتب، قابل ایندکس
person = ("Ali", 30, "Tehran")
print(person[0])
print(len(person))

# tuple unpacking
name, age, city = person
print(name, age, city)

# single item tuple
single = (42,)
print(type(single))

# تبدیل بین tuple و list برای ویرایش غیرمستقیم
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)

# set: بدون ترتیب، بدون عضو تکراری، عملیات مجموعه‌ای
nums = {1, 2, 2, 3}
print(nums)
nums.add(4)
nums.discard(2)
print(nums)

# عملیات مجموعه‌ای: اتحاد، اشتراک، تفاضل، تفاضل متقارن
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference
print(a ^ b)   # symmetric difference

# زیرمجموعه/ابر‌مجموعه
print({1, 2}.issubset(a))
print(a.issuperset({1}))

# set comprehension
squares = {n*n for n in range(6)}
print(squares)

# frozenset: نسخهٔ غیرقابل‌تغییر از set
fs = frozenset([1, 2, 3])
print(fs)


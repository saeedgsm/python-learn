# سبک‌های مختلف import

# import کامل ماژول
import math
print(math.sqrt(16))

# import یک نام مشخص
from math import ceil
print(ceil(3.2))

# import با نام مستعار
import datetime as dt
print(dt.date.today())

# import از ماژول خودمان
from _sample_module import hello
print(hello("World"))


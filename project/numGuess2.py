# بازه عدد حدس از کاربر گرفته بشه
# سیستم مابین بازه عددی کاربر عدد رو مشخص کنه
#بعد از کاربر عدد های حدسی را بگیره
#سیستم بررسی کنه عدد همون عدد سیستم هس یا کوچیک یا بزرگ بودنش 
#10 شانش برای کاربر بده عدد انتخاب شده رو پیدا کنه
import random
import funcs


a = funcs.get_int("Please enter a integer number for start: \n")

b = funcs.check_second_num(a)

print(f"very good you selected range is between: {a} and {b}")

sysNumber = random.randint(a,b)



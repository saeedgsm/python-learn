# step 1 بازه عددی گرفتن از کاربر 
# step 2 انتخاب یک عدد در بازه انتخاب شده
# step 3 گرفتن حدس از کاربر 
# بررسی عدد حدس زده  کاربر با عدد انتخابی سیستم
# نمایش فاصله عددی
# عدد درست نبود 5 بار شانس وارد کردن عدد برای کاربر
import random

renge_numbers = input('Please enter your range number with komo:\n')

ex_nums=str.split(renge_numbers,',')
x=int(ex_nums[0])
y=int(ex_nums[1])
num = random.randint(x,y)
try:
    user_num=int(input("Please eneter your guess number: \n"))
except ValueError:
    print('try again and enter valid number! \n')
    exit()
    
print(renge_numbers,ex_nums,num,user_num)
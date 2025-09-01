# بازه عدد حدس از کاربر گرفته بشه
# سیستم مابین بازه عددی کاربر عدد رو مشخص کنه
#بعد از کاربر عدد های حدسی را بگیره
#سیستم بررسی کنه عدد همون عدد سیستم هس یا کوچیک یا بزرگ بودنش 
#10 شانش برای کاربر بده عدد انتخاب شده رو پیدا کنه
import random
import funcs

a = funcs.get_int("Please enter a integer number for start: \n")
b = funcs.check_second_num(a)

print(f"✅ Very good! You selected range between: {a} and {b}")

sysNumber = random.randint(a, b)

chances = 5
for attempt in range(1, chances + 1):
    user_guess = funcs.get_int(f"Guess {attempt}/{chances}: ")

    if user_guess == sysNumber:
        print("🎉 You won!")
        break
    elif user_guess > sysNumber:
        print("⬇️ Your guess is bigger than the secret number. Try again.")
    else:
        print("⬆️ Your guess is smaller than the secret number. Try again.")
else:
    print(f"❌ Sorry, you lost! The secret number was {sysNumber}.")




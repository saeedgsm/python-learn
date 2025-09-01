def get_int(prompt: str) -> int:
    """دریافت عدد صحیح از کاربر با بررسی ورودی"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer number!")

def check_second_num(a: int) -> int:
    """دریافت عدد دوم که باید بزرگتر از a باشد"""
    while True:
        b = get_int(f"Ok, please enter a number bigger than {a}: ")
        if b > a:
            return b
        print(f"❌ The number must be bigger than {a}. Try again.")

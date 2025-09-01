def get_int(prompt):
    while True:
        try:
           # return int(input())
            return int(input(prompt))
        except ValueError:
            print("Please enter a number!")


def check_second_num(a):
    while True:
        b = get_int(f"ok Please enter num bigger than {a}: \n")
        if b > a:
            return b
        print("Your a number is bigger than b : \n")
import random
import funcs

def play_game():
    a = funcs.get_int("Please enter an integer number for start: \n")
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


# اجرای بازی در یک حلقه
while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").strip().lower()
    if again != "y":
        print("👋 Thanks for playing! Bye.")
        break

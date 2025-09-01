import random

names = ['saeed','ali','alisa','vahid','amin','amir','mahdi','reza','aysan','meysam']

selected_name = random.choice(names)

guess_count = len(selected_name)
guessed_list = ['-'] * len(selected_name)
current_guess = " ".join(guessed_list)
print(current_guess)

while guess_count > 0:
    guessed_char = input('Enter a char: \n')

    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("you have guessed before, try new character")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                    current_guess = " ".join(guessed_list)
                    print(f"Perfect => {current_guess}")

                    if not "_" in guessed_list:
                        print("You won!")
                        break
        else:
            guess_count -=1
            print(f"Wrong! => remined guesses: {guess_count}")            
    else:
        print("Please enter a valid character")        
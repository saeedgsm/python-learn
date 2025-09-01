import random
import time

def question_generator():
    a = random.randint(1,9)
    b = random.randint(1,9)

    operator_list = ["+","-","*"]
    selected_operator = random.choice(operator_list)

    print(f"{a} {selected_operator} {b} = ?")

    if selected_operator == "+":
        return a+b
    elif selected_operator == "-":
        return a-b
    else:
        return a*b
    
question_number_limit = 5
question_number = 0
score = 0
time_limit = 10


while question_number < question_number_limit:
    result = str(question_generator())
    start_time = time.time()

    user_answer = input("Enter your answer: ")
    end_time = time.time()

    time_diff = end_time - start_time

    if time_diff < time_limit:
        if result == user_answer:
            score += 1
            print(f"Perfect, score: P{score}")
        else:
            print("Sorry, your answe is wrong")
    else:
        print("You are to late!")

    question_number += 1

print(f"FINAL SCORE:{score} out of {question_number_limit}")    
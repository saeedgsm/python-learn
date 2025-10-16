# بازی سوال چندگزینه‌ای با امتیازدهی
# مباحث: لیست/دیکشنری، حلقه، شرط، ورودی کاربر

questions = [
    {
        "q": "خروجی 2**3 چیست؟",
        "choices": ["5", "6", "8", "9"],
        "answer": 2,
    },
    {
        "q": "کدام نوع داده قابل تغییر است؟",
        "choices": ["tuple", "list", "str", "frozenset"],
        "answer": 1,
    },
]

def ask(q):
    print(q["q"])
    for i, c in enumerate(q["choices"]):
        print(f"{i}) {c}")
    ans = input("your choice: ")
    return ans.isdigit() and int(ans) == q["answer"]

def main():
    score = 0
    for q in questions:
        if ask(q):
            score += 1
            print("correct")
        else:
            print("wrong")
    print(f"score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()


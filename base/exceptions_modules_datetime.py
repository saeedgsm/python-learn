from datetime import datetime, timedelta

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_div(10, 2))
print(safe_div(5, 0))

now = datetime.now()
tomorrow = now + timedelta(days=1)
print(now.strftime("%Y-%m-%d %H:%M"))
print(tomorrow.date())

def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    print(greet("World"))



from csv import DictWriter, DictReader

# نوشتن و خواندن فایل متنی ساده
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("سلام\n")
    f.write("Python File I/O\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# خواندن خط به خط
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# حالت‌های متداول: 'r' خواندن، 'w' بازنویسی، 'a' افزودن، 'x' ساخت اگر موجود نباشد

# CSV: نوشتن با DictWriter و خواندن با DictReader
rows = [
    {"name": "A", "price": 10},
    {"name": "B", "price": 20},
]

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = DictWriter(f, fieldnames=["name", "price"])
    writer.writeheader()
    writer.writerows(rows)

with open("products.csv", newline="", encoding="utf-8") as f:
    for row in DictReader(f):
        print(row["name"], row["price"])

# مدیریت خطا هنگام کار با فایل
try:
    with open("not_exists.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")


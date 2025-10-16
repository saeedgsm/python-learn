# ردیاب مخارج ساده با ذخیره CSV
# مباحث: dict، لیست، فایل CSV، جمع‌زدن، ورودی کاربر

import csv
from pathlib import Path

CSV_FILE = Path("expenses.csv")

def add_expense(title, amount, category):
    new_row = {"title": title, "amount": float(amount), "category": category}
    write_header = not CSV_FILE.exists()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "amount", "category"])
        if write_header:
            writer.writeheader()
        writer.writerow(new_row)

def total_amount():
    if not CSV_FILE.exists():
        return 0.0
    total = 0.0
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total += float(row["amount"])
    return total

def total_by_category(category):
    if not CSV_FILE.exists():
        return 0.0
    total = 0.0
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["category"].lower() == category.lower():
                total += float(row["amount"])
    return total

def main():
    while True:
        cmd = input("[a]dd [t]otal [c]ategory [q]uit: ").strip().lower()
        if cmd == "a":
            title = input("title: ")
            amount = input("amount: ")
            category = input("category: ")
            add_expense(title, amount, category)
        elif cmd == "t":
            print(total_amount())
        elif cmd == "c":
            cat = input("category: ")
            print(total_by_category(cat))
        elif cmd == "q":
            break
        else:
            print("unknown")

if __name__ == "__main__":
    main()


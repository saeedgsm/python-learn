# دفترچه مخاطبین با CSV و جستجو
# مباحث: dict، لیست، CSV، جستجو، ورودی کاربر

import csv
from pathlib import Path

CSV_FILE = Path("contacts.csv")
FIELDS = ["name", "phone", "email"]

def add_contact(name, phone, email):
    write_header = not CSV_FILE.exists()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow({"name": name, "phone": phone, "email": email})

def list_contacts():
    if not CSV_FILE.exists():
        return []
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def search_contacts(query):
    q = query.lower()
    return [c for c in list_contacts() if q in c["name"].lower() or q in c["phone"].lower() or q in c["email"].lower()]

def main():
    while True:
        cmd = input("[a]dd [l]ist [s]earch [q]uit: ").strip().lower()
        if cmd == "a":
            name = input("name: ")
            phone = input("phone: ")
            email = input("email: ")
            add_contact(name, phone, email)
        elif cmd == "l":
            for c in list_contacts():
                print(f"{c['name']} - {c['phone']} - {c['email']}")
        elif cmd == "s":
            q = input("query: ")
            for c in search_contacts(q):
                print(f"{c['name']} - {c['phone']} - {c['email']}")
        elif cmd == "q":
            break
        else:
            print("unknown")

if __name__ == "__main__":
    main()


import sqlite3

def add_contact(name,phone,email):
    conn = sqlite3.connect("./project/contact-manager/contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name,phone, email) VALUES(?,?,?)",(name,phone,email))
    conn.commit()
    conn.close()
    print(f"مخاطب {name} اضافه شد!")


# تست
add_contact("Ali", "09120000000", "ali@test.com")
add_contact("Sara", "09123334444", "sara@test.com")
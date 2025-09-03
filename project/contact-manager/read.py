import sqlite3

def get_contacts():
    conn = sqlite3.connect("./project/contact-manager/contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()

    print("Contact List:")
    for row in rows:
        print(row)


get_contacts()
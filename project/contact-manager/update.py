import sqlite3

def update_contact(contact_id,name,phone,email):
    conn = sqlite3.connect("./project/contact-manager/contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",(name,phone,email,contact_id))
    conn.commit()
    conn.close()
    print(f"the user {contact_id} updated!")


update_contact(1, "Ali Reza", "09121111111", "alireza@test.com")
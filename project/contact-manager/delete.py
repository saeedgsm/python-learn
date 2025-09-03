import sqlite3

def delete(id):
    conn = sqlite3.connect("./project/contact-manager/contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?",(id,))
    conn.commit()
    conn.close()
    print(f"user : {id} deleted!" )



delete(2)
import sqlite3

conn = sqlite3.connect("./project/contact-manager/contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               phone TEXT NOT NULL,
               email TEXT
               )
""")

conn.commit()
conn.close()

print("DATABASE & TABLE CREATED SUCCESSFULLY!")
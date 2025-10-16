import sqlite3

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               question text not null,
               answer text not null)
""")
conn.commit()
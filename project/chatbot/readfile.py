import sqlite3
import csv

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

with open("faq.csv",newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("insert into faq (question, answer) values (?,?)",
                       (row["question"], row["answer"]))
conn.commit()


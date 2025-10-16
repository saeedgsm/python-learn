import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer


user_question = input("Please ask you question: ")

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

cursor.execute("select * from faq")
rows = cursor.fetchall()

best_match = None
best_score = 0


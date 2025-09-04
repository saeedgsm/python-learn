
import sqlite3


DB_PATH = "./project/contact-manager/contacts.db"

def execute_query(query,params=(),fetch=False):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query,params)
            if fetch:
                return cursor.fetchall()
            else:
                return cursor.lastrowid
            
    except sqlite3.Error as e:
        print("❌ خطای دیتابیس:", e)
        return None


# ===============================
# CRUD Functions
# ===============================
def db():
    query = """
CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               phone TEXT NOT NULL,
               email TEXT
               )

"""
    rows = execute_query(query)

def add_contact(name,phone,email):
    query = "INSERT INTO contacts (name,phone, email) VALUES (?,?,?)"
    contact_id = execute_query(query,(name,phone,email))
    if contact_id:
        print(f"✅ مخاطب {name} اضافه شد. (ID = {contact_id})")
    return contact_id



def get_contacts():
    query = "SELECT * FROM contacts"
    rows =execute_query(query,fetch=True)
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
    print("-" * 40)
    return rows

def update_contact(contact_id,name,phone,email):
    query = "UPDATE contacts SET name=?, phone=?, email WHERE id=?"
    result = execute_query(query,(name,phone,email,contact_id))
    if result is not None:
        print(f"✏️ مخاطب {contact_id} بروزرسانی شد.")

def delete_contact(contact_id):
    query = "DELETE FROM contacts WHERE id=?"
    result = execute_query(query, (contact_id,))
    if result is not None:
        print(f"🗑️ مخاطب {contact_id} حذف شد.")


def main():
    db()
    while True:
        print("\n=== مدیریت مخاطبین ===")
        print("1. افزودن مخاطب")
        print("2. نمایش همه مخاطبین")
        print("3. ویرایش مخاطب")
        print("4. حذف مخاطب")
        print("0. خروج")
        
        choice = input("انتخاب شما: ")

        if choice =="1":
            name = input("نام: \n")
            phone = input("شماره تماس \n")
            email = input("ایمیل \n")
            add_contact(name,phone,email)

        elif choice == "2":
            get_contacts()

        elif choice == "3":
            contact_id = int(input("ID مخاطب برای ویرایش: "))
            name = input("نام جدید: ")
            phone = input("شماره جدید: ")
            email = input("ایمیل جدید: ")
            update_contact(contact_id, name, phone, email)

        elif choice == "4":
            contact_id = int(input("ID مخاطب برای حذف: "))
            delete_contact(contact_id)

        elif choice == "0":
            print("👋 خداحافظ!")
            break

        else:
            print("❌ گزینه نامعتبر. دوباره تلاش کنید.")

main()
if __name__ == "__name__":
    main()
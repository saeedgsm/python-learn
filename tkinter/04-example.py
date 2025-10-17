import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

# ساخت پنجره اصلی
root = tk.Tk()
root.title("فرم ورود کاربران")
root.geometry("400x250")
root.configure(bg="#f9f9f9")

# ساخت فونت سفارشی (در ویندوز فونت Tahoma و Vazir رایج هستند)
app_font = tkFont.Font(family="Tahoma", size=11)

# تابع بررسی ورود
def login():
    username_val = username_entry.get().strip()
    password_val = password_entry.get().strip()

    if username_val == "" or password_val == "":
        messagebox.showwarning("خطا", "لطفاً همه فیلدها را پر کنید.")
    elif username_val == "admin" and password_val == "1234":
        messagebox.showinfo("وضعیت", f"خوش آمدی {username_val} 🌸")
    else:
        messagebox.showerror("خطا", "نام کاربری یا رمز عبور اشتباه است.")

# چیدمان فرم درون یک فریم برای کنترل بهتر
form_frame = tk.Frame(root, bg="#f9f9f9")
form_frame.pack(expand=True)

# برچسب نام کاربری
username_label = tk.Label(form_frame, text="نام کاربری:", font=app_font, bg="#f9f9f9", anchor="e", justify="right")
username_label.grid(row=0, column=1, sticky="e", pady=8, padx=5)

# فیلد ورود نام کاربری
username_entry = tk.Entry(form_frame, font=app_font, justify="right")
username_entry.grid(row=0, column=0, padx=10)

# برچسب رمز عبور
password_label = tk.Label(form_frame, text="رمز عبور:", font=app_font, bg="#f9f9f9", anchor="e", justify="right")
password_label.grid(row=1, column=1, sticky="e", pady=8, padx=5)

# فیلد ورود رمز عبور
password_entry = tk.Entry(form_frame, show="*", font=app_font, justify="right")
password_entry.grid(row=1, column=0, padx=10)

# دکمه ورود
login_button = tk.Button(form_frame, text="ورود", font=app_font, bg="#0078D7", fg="white", width=15, command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()

import tkinter as tk
from tkinter import messagebox


# ساخت پنجره اصلی
root = tk.Tk()
# تنظیم عنوان پنجره
root.title("My First GUI")
# تعیین اندازه پنجره
root.geometry("400x400")
root.configure(bg="#E5E5E5")

# ساخت یک Label (متن ساده)
label = tk.Label(root, text="Hello, World!",font=("Arial",16))
label.pack(pady=10)
label.configure(bg="#EEF680",fg="#F23245",font=('Tahoma',14))

def say_hello():
    messagebox.showinfo("Hello", "Hello, World!")

button = tk.Button(root, text="Click me", command=say_hello)
button.pack(pady=10)


label_name = tk.Label(root, text="لطفاً نام خود را وارد کنید:",font=("Tahoma", 12), bg="#f8f8f8")
label_name.pack(pady=2)

name_entry = tk.Entry(root,width=30,font=('Tahoma',12))
name_entry.pack(pady=2)

def say_myName():
    name = name_entry.get()
    if name.strip() == "":
        messagebox.showwarning("Warning","لطفاً نام خود را وارد کنید")
    else:
        messagebox.showinfo("My Name is", f"سلام {name} خوش اومدی")

def clear_name():
    name_entry.delete(0,tk.END)

button_name = tk.Button(root, text="what's your name?",command=say_myName)
button_name.pack(pady=2)

btn_clr_name = tk.Button(root, text="clear name",command=clear_name)
btn_clr_name.pack(pady=2)
btn_clr_name.configure(bg="#4CAF50", fg="white")



# اجرای حلقه اصلی برنامه
root.mainloop()
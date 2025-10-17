import tkinter as tk

root = tk.Tk()
root.title('آموزش grid')
root.geometry("300x200")


tk.Label(root,text='نام کاربری:').grid(row=0,column=0,padx=10,pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0,column=1)


tk.Label(root,text='رمز عبور:').grid(row=1,column=0,padx=10,pady=10)
password_entry = tk.Entry(root,show='*')
password_entry.grid(row=1,column=1)

login_button = tk.Button(root,text='ورود')
login_button.grid(row=2,column=0,columnspan=1,pady=10)

root.mainloop()

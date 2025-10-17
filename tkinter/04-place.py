import tkinter as tk

root = tk.Tk()
root.title("آموزش place()")
root.geometry("300x200")

tk.Label(root, text="سلام دنیا!", bg="lightblue").place(x=100, y=80)

root.mainloop()

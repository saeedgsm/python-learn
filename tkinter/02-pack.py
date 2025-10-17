from logging import root
import tkinter as tk

root = tk.Tk()
root.title("آموزش Pack")
root.geometry("300x200")

tk.Label(root,text="بالا",bg="lightblue").pack(side="top",fill="x")
tk.Label(root,text="پایین",bg="lightgreen").pack(side="bottom",fill="x")
tk.Label(root,text="چپ",bg="orange").pack(side="left",fill="x")
tk.Label(root,text="راست",bg="pink").pack(side="right",fill="x")
root.mainloop()
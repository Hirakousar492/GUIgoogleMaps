import tkinter as tk
from tkinter import StringVar, Entry, Label

root=tk.Tk()
root.title("Login Window")
root.geometry("400x400")
user = Label(root, text="Username",padx=30, pady=23)
Password = Label(root, text="password", padx=30)
user.grid()
Password.grid(row=1)
username = StringVar()
password = StringVar()
userentry = Entry(root, text="username")
passentry = Entry(root, text="password")
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
b1 = tk.Button(root, text="Click me", fg="white", bg="blue")
b1.grid(row=4, column=1)
root.mainloop()

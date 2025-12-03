import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Thông tin cá nhân")


labels = ["Họ tên:", "Ngày sinh:", "MSSV:", "Ngành học:"]
entries = []

for i, text in enumerate(labels):
    lbl = ttk.Label(root, text=text)
    lbl.grid(row=i, column=0, padx=10, pady=5)

    entry = ttk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

root.mainloop()

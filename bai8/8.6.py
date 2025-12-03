from tkinter import *
from tkinter import messagebox, filedialog

def NewFile():
    messagebox.showinfo("New File", "This is a simple example of a menu!")

def OpenFile():
    filename = filedialog.askopenfilename(
        title="Open file",
        filetypes=[("All files", "*.*")]
    )
    if filename:
        messagebox.showinfo("Open File", f"You selected:\n{filename}")

def Exit():
    root.quit()

def InsText():
    messagebox.showinfo("Insert Text", "You chose: Text")

def InsPic():
    messagebox.showinfo("Insert Picture", "You chose: Picture")

def About():
    messagebox.showinfo("About", "This is the About dialog!")

root = Tk()
root.title("Menu Example")


menu = Menu(root)
root.config(menu=menu)


filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)


insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)


helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About...", command=About)

root.mainloop()

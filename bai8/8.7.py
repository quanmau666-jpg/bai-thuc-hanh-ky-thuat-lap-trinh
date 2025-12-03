from tkinter import *
from tkinter import filedialog, messagebox


def NewFile():
    messagebox.showinfo("New File", "This is a simple example of a menu!")

def OpenFile():
    filename = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("All files", "*.*")]
    )
    if filename:
        messagebox.showinfo("Open File", f"You selected:\n{filename}")

def ExitApp():
    root.quit()

def InsText():
    messagebox.showinfo("Insert", "You chose: Text")

def InsPic():
    messagebox.showinfo("Insert", "You chose: Picture")

def About():
    messagebox.showinfo("About", "This is the About dialog!")



root = Tk()
root.title("Menu Example")

menubar = Menu(root)
root.config(menu=menubar)


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ExitApp)


insertmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Insert", menu=insertmenu)

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About...", command=About)

root.mainloop()

from tkinter import *

window = Tk()
window.title("Major Subjects")
L = ["reading","writing","arithmetic","coding"]
content = StringVar()
list = Listbox(window, width=15, height = 4, listvariable = content)
list.grid(padx = 100, pady = 10)
content.set(tuple(L))
window.mainloop()

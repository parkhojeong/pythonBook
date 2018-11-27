from tkinter import *

window = Tk()
window.title("Presidents")
presList = [line.rstrip() for line in open("USPres.txt")]
listContent = StringVar()
listBox = Listbox(window, width = 15, height = 5 , listvariable = listContent)
listBox.grid(padx = 80 , pady = 5)
listContent.set(tuple(presList))
window.mainloop()
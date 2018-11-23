from tkinter import *

window = Tk()
window.title("Colors")
L = ["red", "yellow", "light blue", "orange", "blue", "white","green"]
conOFlstColors = StringVar()   # contents of the list box 
lstColors = Listbox(window, width=10, height=5, # width - char의 개수 지정 height - 줄 수 지정
                    listvariable=conOFlstColors)
lstColors.grid(padx=100, pady=15)
conOFlstColors.set(tuple(L))
window.mainloop()

 

from tkinter import *

window = Tk()
window.title("Readonly Entry")

conOFentOutput = StringVar()
conOutput = Entry(window, state="readonly", textvariable= conOFentOutput,width=2)
conOutput.grid(padx = 100, pady = 10)
conOFentOutput.set("Hi")
window.mainloop()

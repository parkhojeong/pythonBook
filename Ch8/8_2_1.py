from tkinter import *
window = Tk()
window.title("New England")
scroll = Scrollbar(window, orient = VERTICAL)
scroll.grid(row = 0, column= 2, rowspan = 4, padx= (0,100) ,pady =5 ,sticky = NS )
stateList = ["A","B","C","D","E","F"]
content = StringVar()
listBox = Listbox(window, width = 14 , height =4 , listvariable = content, yscrollcommand=scroll.set)
listBox.grid(row = 0 , column= 1, rowspan=4, padx= (100,0), pady =5 , sticky= E)
content.set(stateList)
scroll["command"]= listBox.yview()

window.mainloop()
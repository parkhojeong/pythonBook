from tkinter import *

def concatNamt(event):
    res = entry2.get()+" "+entry1.get()
    content.set(res)

window = Tk()
window.title("Full name")
label1 = Label(window, text = "Last name:")
label1.grid(row= 0 , column =0)
entry1 = Entry(window, fg="black", width =15)
entry1.grid(row = 0, column =1, padx = (0,30))

label2 = Label(window, text = "First name:")
label2.grid(row= 1 , column =0)
entry2 = Entry(window, fg="black", width =15)
entry2.grid(row = 1, column =1, padx = (0,30))

btn = Button(window, text ="Display Full Name")
btn.grid(row = 2, column= 0, rowspan=2, columnspan= 2,padx = 25, pady=5)
btn.bind("<Button-1>",concatNamt)

label3 = Label(window, text = "Full name:")
label3.grid(row= 4 , column =0)
content = StringVar()
entryOutput = Entry(window, state="readonly", width=15, textvariable=content)
entryOutput.grid(row= 4, column = 1,padx = (0,30))
window.mainloop()
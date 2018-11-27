from tkinter import *

window = Tk()
window.title("States")
stateDict = {line.split(',')[0]:{"shortState":line.split(',')[1], "alias": line.split(',')[2],
                                 "capital":line.split(',')[3].rstrip()} for line in open("StatesANC.txt")}
stateList = [key+" ("+stateDict[key]["alias"]+")" for key in stateDict.keys()]
print(stateList)
listContent = StringVar()
listBox = Listbox(window, width = 30, height = 10, listvariable = listContent)
listBox.grid(padx = 15,pady = 5)
listContent.set(tuple(stateList))
window.mainloop()
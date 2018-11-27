from tkinter import *
def viewShortState(event):
    selectedState = listBox.get(listBox.curselection())

    newStateList = []
    for key in stateDict.keys():
        if key == selectedState:
            newStateList.append(key+"("+stateDict[key]["shortState"]+")")
        else:
            newStateList.append(key)
    listContent.set(tuple(newStateList))

window = Tk()
window.title("States")
stateDict = {line.split(',')[0]:{"shortState":line.split(',')[1], "alias": line.split(',')[2],
                                 "capital":line.split(',')[3].rstrip()} for line in open("StatesANC.txt")}
stateList = [key for key in stateDict.keys()]
print(stateList)
listContent = StringVar()
listBox = Listbox(window, width = 30, height = 10, listvariable = listContent)
listBox.grid(padx = 15,pady = 5)
listContent.set(tuple(stateList))
listBox.bind("<<ListboxSelect>>",viewShortState)
window.mainloop()
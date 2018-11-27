from tkinter import *

class Statebirds:
    def __init__(self):
        window = Tk()
        window.title("Largest Number")

        Label(window, text="First number: ").grid(row=0, column=0, pady=5, sticky=E)
        self._conOFentNum1 = StringVar()
        Entry(window, width=8, textvariable=self._conOFentNum1).grid(row=0, column=1, sticky=W)

        Label(window, text="Second number: ").grid(row=1, column=0, pady=5, sticky=E)
        self._conOFentNum2 = StringVar()
        Entry(window, width=8, textvariable=self._conOFentNum2).grid(row=1, column=1, sticky=W)

        Label(window, text="Third number: ").grid(row=2, column=0, pady=5, sticky=E)
        self._conOFentNum3 = StringVar()
        Entry(window, width=8, textvariable=self._conOFentNum3).grid(row=2, column=1, sticky=W)

        btnFind = Button(window, text="Find the Largest Number", command=self.findLargest)
        btnFind.grid(row=3, column=0, columnspan=2, padx=75)

        Label(window, text="Largest number: ").grid(row=4, column=0, sticky=E)
        self._conOFentLargest = StringVar()
        Entry(window, state="readonly", width=8, textvariable=self._conOFentLargest).grid(row=4, column=1, pady=5, sticky=W)
        window.mainloop()

    def findLargest(self):
        L = []
        L.append(eval(self._conOFentNum1.get()))
        L.append(eval(self._conOFentNum2.get()))
        L.append(eval(self._conOFentNum3.get()))
        self._conOFentLargest.set(max(L))

Statebirds()





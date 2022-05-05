from functools import partial

import psutil
import wmi
from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("AppLocker GUI")
        self.minsize(1080, 720)


def initialize(data, settings, boolArr):
    with open("data.cnf", "r") as dataFile:
        tmpData = dataFile.readlines()
    for line in tmpData:
        splitLine = line.split(";")
        splitLine.pop(0)
        print(splitLine)
        data.append(splitLine)
        boolArr.append(False)

    with open("settings.cnf", "r") as settingsFile:
        settings = settingsFile.readline().split(",")


def checkValidity(program, pwd, notice, tries):
    tries.set(tries.get() + 1)
    print(tries.get())
    if tries.get() == 4:
        notice.grid(row=1)


def displayOverlay(app):
    root = Root()
    overlayFrame = Frame()
    programPassword = StringVar()
    numOfTries = IntVar()
    numOfTries.set(0)

    Label(overlayFrame, text="Password:").grid()
    Entry(overlayFrame, show="*", width=10, text=programPassword).grid(column=1, row=0)
    notice = Label(overlayFrame, text="One try left before shutdown!", fg="red")
    notice.grid(row=1)
    notice.grid_forget()
    Button(overlayFrame, text="Submit", command=partial(checkValidity, program=app, pwd=programPassword, notice=notice, tries=numOfTries)).grid(row=2)

    overlayFrame.pack()
    root.mainloop()
    print("Yes")
    """
    try:
        app.kill()
    except:
        print("Already closed!")"""


# variables
data = []
settings = []
boolArr = []
f = wmi.WMI()

# code
initialize(data=data, settings=settings, boolArr=boolArr)
print(data)

# start loop
while(True):
    i = 0
    for arr in data:
        # if the exe is running and it hasnt been open before
        for proc in psutil.process_iter():
            if arr[0] == proc.name():
                boolArr[i] = True
                displayOverlay(proc)
        else:
            print("no")
        i += 1

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


def checkValidity(program, pwd, notice, tries, conf):
    ppwd = data[i].split(";")[2]
    tries.set(tries.get() + 1)
    print(tries.get())
    if pwd == ppwd:
        #close window and continue to app
        pass
    else:
        if tries.get() == conf[1]:
            #sendEmail
            pass
        if tries.get() == conf[2]-1:
            notice.grid(row=1)
        if tries.get() == conf[2]:
            #close program

            #shutdown
            pass



def displayOverlay(app, settings, data, iterator):
    root = Root()
    overlayFrame = Frame()
    enteredPwd = StringVar()
    numOfTries = IntVar()
    numOfTries.set(0)

    Label(overlayFrame, text="Password:").grid()
    Entry(overlayFrame, show="*", width=10, text=enteredPwd).grid(column=1, row=0)
    notice = Label(overlayFrame, text="One try left before shutdown!", fg="red")
    notice.grid(row=1)
    notice.grid_forget()
    Button(overlayFrame, text="Submit", command=partial(checkValidity, program=app, pwd=enteredPwd, notice=notice, tries=numOfTries, conf=settings, strLine = data[iterator])).grid(row=2)

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
                displayOverlay(proc, settings, data, i)
        else:
            print("no")
        i += 1

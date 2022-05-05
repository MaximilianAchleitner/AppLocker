from functools import partial

import psutil
import wmi
from tkinter import *
from emailSend import createEmail
import os

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
        line = settingsFile.readline()
        for e in line.split(","):
            settings.append(e)
        settings[2].strip("\n")

def checkValidity(program, pwd, notice, tries, root, i):
    ppwd = data[i][1]
    ppwd = ppwd.strip("\n")
    print(ppwd)
    print(pwd.get())
    tries.set(tries.get() + 1)
    if pwd.get() == ppwd:
        #close window and continue to app
        root.destroy()
        boolArr[i] = True
    else:
        if tries.get() == int(settings[1]):
            createEmail()
        if tries.get() == int(settings[2])-1:
            notice.grid(row=1)
        if tries.get() == int(settings[2]):
            #close program
            try:
                program.kill()
            except:
                print("Already closed!")
            #shutdown
            os.system("shutdown /s /t 1")


def onMinimize(root):
    # root.state(newstate='normal')
    root.protocol()
    print("Hi")


def displayOverlay(app, data, iterator):
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
    Button(overlayFrame, text="Submit", command=partial(checkValidity, program=app, pwd=enteredPwd, notice=notice, tries=numOfTries, root=root, i=iterator)).grid(row=2)

    overlayFrame.pack()
    root.wm_attributes("-topmost", 1)
    root.wm_attributes("-fullscreen", True)
    root.overrideredirect(1)
    root.mainloop()
    print("Yes")


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
            if arr[0] == proc.name() and not boolArr[i]:
                displayOverlay(proc, data, i)
        else:
            print("no")
        i += 1

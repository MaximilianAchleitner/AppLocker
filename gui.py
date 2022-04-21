from tkinter import *
from tkinter.filedialog import askopenfilename
from functools import partial
import os

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("AppLocker GUI")
        self.minsize(1080, 720)


def openRemoveProgram(currentFrame):
    # create list of programs to display
    file = open("data.cnf", "r")
    lines = file.readlines()
    dataList = []
    names = []

    # list is now multidimensional array
    for line in lines:
        tmp = line.split(";")
        dataList.append(tmp)
        names.append(tmp[0])

    print(names)
    clearFrame(currentFrame)
    Label(currentFrame, text="Remove a program from your security list!").grid()
    Label(currentFrame, text="Choose Program: ").grid(column=0, row=1, sticky=W)
    listView = StringVar(currentFrame)
    listView.set(names[0])
    OptionMenu(currentFrame, listView, *names).grid(column=1, row=1)

    currentFrame.pack(fill="both", expand=TRUE)


def openEditProgram(currentFrame):
    clearFrame(currentFrame)
    file = open("data.cnf", "r")
    lines = file.readlines()
    dataList = []
    names = []
    programName = StringVar()
    programPath = StringVar()
    programPassword = StringVar()

    # dataList is now multidimensional array
    for line in lines:
        tmp = line.split(";")
        dataList.append(tmp)
        names.append(tmp[0])

    print(names)

    Label(currentFrame, text="Program: ").grid(sticky=W)
    listView = StringVar(currentFrame)
    listView.set(names[0])
    OptionMenu(currentFrame, listView, *names, command=partial(updateEditVariables, dataList=dataList, thisName=programName, path=programPath,
                                                               password=programPassword, choice=listView)).grid(column=1, row=0)
    Label(currentFrame, text="Name: ").grid(column=0, row=1, sticky=W)
    Entry(currentFrame, width=10, text=programName).grid(column=1, row=1)
    Label(currentFrame, text="Path: ").grid(column=0, row=2, sticky=W)
    Entry(currentFrame, width=10, text=programPath).grid(column=1, row=2)
    Label(currentFrame, text="Password: ").grid(column=0, row=3, sticky=W)
    Entry(currentFrame, show="*", width=10, text=programPassword).grid(column=1, row=3)

    Button(currentFrame, text="Submit", command=updateProgram).grid(column=0, row=4, sticky=W)

    currentFrame.pack(fill="both", expand=TRUE)


def updateEditVariables(self, dataList, thisName=StringVar, path=StringVar, password=StringVar, choice=StringVar):
    print(choice.get())
    thisName.set(choice.get())

    for entry in dataList:
        if entry[0] == thisName.get():
            path.set(value=entry[1])
            password.set(value=entry[2])
            return


def openAddProgram(currentFrame):
    isExe = bool
    programPath = StringVar()
    programName = StringVar()
    programPassword = StringVar()

    clearFrame(currentFrame)
    Label(currentFrame, text="Add a program to your security list!")
    Label(currentFrame, text="Program Name: ").grid(column=0, row=1, sticky=W)
    Entry(currentFrame, width=10, text=programName).grid(column=1, row=1)
    Label(currentFrame, text="Password: ").grid(column=0, row=2, sticky=W)
    Entry(currentFrame, show="*", width=10, text=programPassword).grid(column=1, row=2)
    Label(currentFrame, text="Find .exe: ").grid(column=0, row=3, sticky=W)
    Button(currentFrame, text="Browse", command=partial(findEXE, isExe=isExe, path=programPath)).grid(column=1, row=3, sticky=W)
    Button(currentFrame, text="Submit", command=partial(submitNewProgram, pName=programName, pPath=programPath, pPassword=programPassword, isExe=isExe)).grid(column=0, row=4, sticky=W)
    currentFrame.pack(fill="both", expand=TRUE)


def findEXE(isExe, path):
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    rootPath, ext = os.path.splitext(filename)
    if ext == ".exe":
        isExe = True
        path.set(filename)
        print(path.get())
    else:
        isExe = False


def submitNewProgram(pName, pPath, pPassword, isExe):
    if isExe:
        print(pPath)
        confLine = "\n" + pName.get() + ";" + pPath.get() + ";" + pPassword.get()
        confFile = open("data.cnf", "a")
        confFile.writelines(confLine)
    print("done")


def updateProgram():
    pass


def clearFrame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def dashboard(currentFrame):
    clearFrame(currentFrame)
    Label(currentFrame, text="Welcome to AppLocker").grid()
    currentFrame.pack(fill="both", expand=TRUE)


def browse():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    filenameLabel = Label(root, text=filename)
    filenameLabel.grid(column=1, row=2)


def btnSubmit(txtEmail, txtSecu, txtShut):
    print(txtEmail)


def openSettings(currentFrame):
    clearFrame(currentFrame)
    Label(currentFrame, text="Settings").grid()
    Label(currentFrame, text="Email:").grid(row=1)
    Label(currentFrame, text="Number of failed Tries to send Security-Email:").grid(row=2)
    Label(currentFrame, text="Number of failed Tries to Shut-Down:").grid(row=3)

    txtEmail = Entry(currentFrame, width=10).grid(row=1,column=1)
    txtSecu = Entry(currentFrame, width=3).grid(row=2,column=1)
    txtShut = Entry(currentFrame, width=3).grid(row=3,column=1)

    btn = Button(currentFrame, text="Click", fg="red", command=partial(btnSubmit, txtEmail, txtSecu, txtShut)).grid(column=1, row=4)
    currentFrame.pack(fill="both", expand=TRUE)


# START OF PROGRAM
root = Root()

dashboardFrame = Frame()
dashboard(dashboardFrame)

menu = Menu(root)
editDropdown = Menu(menu)
editDropdown.add_command(label="Add", command=partial(openAddProgram, dashboardFrame))
editDropdown.add_command(label="Remove", command=partial(openRemoveProgram, dashboardFrame))
editDropdown.add_command(label="Edit", command=partial(openEditProgram, dashboardFrame))
menu.add_command(label="Dashboard", command=partial(dashboard, dashboardFrame))
menu.add_cascade(label="Menu", menu=editDropdown)
menu.add_command(label="Settings", command=partial(openSettings, dashboardFrame))

root.config(menu=menu)

root.mainloop()

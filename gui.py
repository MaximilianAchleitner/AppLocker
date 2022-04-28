import os.path
from tkinter import *
from tkinter.filedialog import askopenfilename
from functools import partial
import os
import csv

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
    Button(currentFrame, text="Confirm", command=partial(removeProgram, originalName=listView, currentFrame=currentFrame)).grid(column=0, row=2)

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

    isExe = bool

    originalName = StringVar()

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
                                                               password=programPassword, choice=listView, originalName=originalName)).grid(column=1, row=0)
    Label(currentFrame, text="Name: ").grid(column=0, row=1, sticky=W)
    Entry(currentFrame, width=10, text=programName).grid(column=1, row=1)
    Label(currentFrame, text="Path: ").grid(column=0, row=2, sticky=W)
    Entry(currentFrame, width=10, text=programPath).grid(column=1, row=2)
    Button(currentFrame, text="Browse", command=partial(findEXE, path=programPath, isExe=isExe)).grid(column=2, row=2)
    Label(currentFrame, text="Password: ").grid(column=0, row=3, sticky=W)
    Entry(currentFrame, show="*", width=10, text=programPassword).grid(column=1, row=3)

    Button(currentFrame, text="Submit", command=partial(updateProgram, currentFrame=currentFrame, pName=programName, pPath=programPath, pPassword=programPassword, isExe=isExe, originalName=originalName)).grid(column=0, row=4, sticky=W)

    currentFrame.pack(fill="both", expand=TRUE)


def updateEditVariables(self, dataList, thisName=StringVar, path=StringVar, password=StringVar, choice=StringVar, originalName=StringVar):
    print(choice.get())
    thisName.set(choice.get())
    originalName.set(thisName.get())


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
    displayName = StringVar()

    clearFrame(currentFrame)
    Label(currentFrame, text="Add a program to your security list!")
    Label(currentFrame, text="Program Name: ").grid(column=0, row=1, sticky=W)
    Entry(currentFrame, width=10, text=programName).grid(column=1, row=1)
    Label(currentFrame, text="Password: ").grid(column=0, row=2, sticky=W)
    Entry(currentFrame, show="*", width=10, text=programPassword).grid(column=1, row=2)
    Label(currentFrame, text="Find .exe: ").grid(column=0, row=3, sticky=W)
    Button(currentFrame, text="Browse", command=partial(findEXE, isExe=isExe, path=programPath)).grid(column=1, row=3, sticky=W)
    Label(currentFrame, text=displayName).grid(column=2, row=3, sticky=W)
    Button(currentFrame, text="Submit", command=partial(submitNewProgram, update=False, pName=programName, pPath=programPath, pPassword=programPassword, isExe=isExe, currentFrame=currentFrame)).grid(column=0, row=4, sticky=W)
    currentFrame.pack(fill="both", expand=TRUE)


def findEXE(isExe, path):
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    rootPath, ext = os.path.splitext(filename)
    if ext == ".exe":
        isExe = True
        sections = filename.split("/")
        path.set(sections[len(sections)-1])
        print(path.get())
    else:
        isExe = False


def submitNewProgram(pName, pPath, pPassword, isExe, currentFrame, update):
    if isExe:
        print(pPath)
        if update:
            confLine = pName.get() + ";" + pPath.get() + ";" + pPassword.get()
        else:
            confLine = pName.get() + ";" + pPath.get() + ";" + pPassword.get() + "\n"
        confFile = open("data.cnf", "a")
        confFile.writelines(confLine)
    print("done")
    openAddProgram(currentFrame)


def updateProgram(pName, pPath, pPassword, isExe, originalName, currentFrame):
    removeProgram(originalName=originalName, currentFrame=currentFrame)
    submitNewProgram(pName=pName, pPath=pPath, pPassword=pPassword, isExe=isExe, currentFrame=currentFrame, update=True)


def removeProgram(originalName, currentFrame):
    try:
        with open("data.cnf", "r") as fr:
            lines = fr.readlines()

            with open("data.cnf", "w") as fw:
                for line in lines:
                    if line.find(originalName.get()) == -1:
                        fw.write(line)
        print("Deleted")
        openRemoveProgram(currentFrame)
    except:
        print("Oops! something error")


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


def openSettings(currentFrame):
    def getEntry():
        stringEmail = txtEmail.get()
        stringSecu = txtSecu.get()
        stringShut = txtShut.get()
        file = open("settings.cnf", "w")
        writer = csv.writer(file)
        writer.writerow([stringEmail, stringSecu, stringShut])
        file.close()

    if os.path.exists("settings.cnf"):
        file = open("settings.cnf", "r")
        line = file.readline()
        settings = line.split(",")
        email = StringVar()
        email.set(settings[0])
        secu = StringVar()
        secu.set(settings[1])
        shut = StringVar()
        shut.set(settings[2])
        file.close()
    else:
        email = StringVar()
        secu = StringVar()
        shut = StringVar()

    clearFrame(currentFrame)
    Label(currentFrame, text="Settings").grid()
    Label(currentFrame, text="Email:").grid(row=1)
    Label(currentFrame, text="Number of failed Tries to send Security-Email:").grid(row=2)
    Label(currentFrame, text="Number of failed Tries to Shut-Down:").grid(row=3)
    txtEmail = Entry(currentFrame, text=email, width=30)
    txtSecu = Entry(currentFrame, text=secu, width=3)
    txtShut = Entry(currentFrame, text=shut, width=3)
    txtEmail.grid(row=1, column=1)
    txtSecu.grid(row=2, column=1)
    txtShut.grid(row=3, column=1)
    Button(currentFrame, text="Save", command=getEntry).grid(column=1, row=4)
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

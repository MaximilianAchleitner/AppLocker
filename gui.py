from tkinter import *
from tkinter.filedialog import askopenfilename
from functools import partial

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


def openAddProgram(currentFrame):
    clearFrame(currentFrame)
    Label(currentFrame, text="Add a program to your security list!")
    Label(currentFrame, text="Program Name: ").grid(column=0, row=1, sticky=W)
    Entry(currentFrame, width=10).grid(column=1, row=1)
    Label(currentFrame, text="Password: ").grid(column=0, row=2, sticky=W)
    Entry(currentFrame, show="*", width=10).grid(column=1, row=2)
    Label(currentFrame, text="Find .exe: ").grid(column=0, row=3, sticky=W)
    Button(currentFrame, text="Browse", command=findEXE).grid(column=1, row=3, sticky=W)
    Button(currentFrame, text="Submit", command=submitNewProgram).grid(column=0, row=4, sticky=W)
    currentFrame.pack(fill="both", expand=TRUE)


def findEXE():
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)


def submitNewProgram():
    print("hello")



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
editDropdown.add_command(label="Edit")
menu.add_command(label="Dashboard", command=partial(dashboard, dashboardFrame))
menu.add_cascade(label="Menu", menu=editDropdown)
menu.add_command(label="Settings", command=partial(openSettings, dashboardFrame))

root.config(menu=menu)

root.mainloop()

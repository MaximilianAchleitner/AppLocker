from tkinter import *
from tkinter.filedialog import askopenfilename
from functools import partial
from os import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("AppLocker GUI")
        self.minsize(1080, 720)


def openRemoveProgram(currentFrame):
    clearFrame(currentFrame)
    Label(currentFrame, text="New Window REMOVE").grid()
    currentFrame.pack(fill="both", expand=TRUE)


def openAddProgram(currentFrame):
    clearFrame(currentFrame)
    Label(currentFrame, text="Program Name: ").grid()

    currentFrame.pack(fill="both", expand=TRUE)


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

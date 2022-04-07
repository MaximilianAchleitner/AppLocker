from tkinter import *
from tkinter.filedialog import askopenfilename
from functools import partial

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
    Label(currentFrame, text="New Window addProgram").grid()
    currentFrame.pack(fill="both", expand=TRUE)


def clearFrame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

def dashboard():
    frame = Frame(root)
    Label(frame, text="Welcome to AppLocker").grid()
    return frame


def browse():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    filenameLabel = Label(root, text=filename)
    filenameLabel.grid(column=1, row=2)


def setEmail():
    print("hi")


# START OF PROGRAM
root = Root()

dashboardFrame = dashboard()
dashboardFrame.pack(fill="both", expand=TRUE)

menu = Menu(root)
editDropdown = Menu(menu)
editDropdown.add_command(label="Add", command=partial(openAddProgram, dashboardFrame))
editDropdown.add_command(label="Remove", command=partial(openRemoveProgram, dashboardFrame))
editDropdown.add_command(label="Edit")
menu.add_cascade(label="Menu", menu=editDropdown)
menu.add_command(label="Settings", command=setEmail)
root.config(menu=menu)

root.mainloop()

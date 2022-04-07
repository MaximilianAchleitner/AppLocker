from tkinter import *
from tkinter.filedialog import askopenfilename

class Root(Tk):
    def init(self):
        super(Root, self).init()

        self.title("AppLocker GUI")
        self.minsize(1080, 720)


def onClick():
    result = "You Wrote: " + txtf.get()
    lbl.configure(text=result)


def onNew():
    print("Hi")


def browse():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    filenameLabel = Label(root, text=filename)
    filenameLabel.grid(column=1, row=2)


root = Root()

#1. Create Image --> 2. Label with image as parameter --> label.grid(col, row)
img = PhotoImage(file="D:\Schule\ITP\swoleGams1.png")
imgLabel = Label(root, image=img)
imgLabel.grid(column=3, row=0)

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New", command=onNew)
item.add_command(label="Print")
menu.add_cascade(label="File", menu=item)
menu.add_cascade(label="Menu")
root.config(menu=menu)

fileBtn = Button(root, text="Browse", command=browse)
fileBtn.grid(column=4, row=0)

lbl = Label(root, text="Hello World")
lbl.grid()

btn = Button(root, text="Click", fg="red", command=onClick)
btn.grid(column=2, row=0)

txtf = Entry(root, width=10)
txtf.grid(column=1, row=0)

root.mainloop()
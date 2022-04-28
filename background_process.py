import psutil
import wmi


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


def displayOverlay(app):
    print("Yes")
    try:
        app.kill()
    except:
        print("Already closed!")

    pass


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

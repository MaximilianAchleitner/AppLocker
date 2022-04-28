import psutil



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


def displayOverlay():
    print("Yes")
    pass


# variables
data = []
settings = []
boolArr = []

# code
initialize(data=data, settings=settings, boolArr=boolArr)
print(data)

# start loop
while(True):
    i = 0
    for arr in data:
        # if the exe is running and it hasnt been open before
        if arr[0] in (it.name() for it in psutil.process_iter()) and not boolArr[i]:
            boolArr[i] = True
            displayOverlay()
        else:
            print("no")
        i += 1

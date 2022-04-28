import psutil



def initialize(data, settings):
    with open("data.cnf", "r") as dataFile:
        tmpData = dataFile.readlines()
    for line in tmpData:
        splitLine = line.split(";").pop(0)
        data.append(splitLine)

    with open("settings.cnf", "r") as settingsFile:
        settings = settingsFile.readline().split(",")


def displayOverlay():
    pass


# variables
data = []
settings = []

# code
initialize(data=data, settings=settings)
print(data)

# start loop
while(True):
    for arr in data:
        if arr[0] in (i.name() for i in psutil.process_iter()):
            displayOverlay()
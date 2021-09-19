import pickle


class car_object:

    def __init__(self):
        self.direction = "N"
        self.speed = 0
        self.location = "38.8334N,77.2365W"
        self.moving = False

    def startMoving(self, speed=0):
        self.moving = True
        self.speed = speed

    def stopMoving(self):
        self.moving = False
        self.speed = 0

    def changeDirection(self, direction):
        self.direction = direction

    def changeLocation(self, location):
        self.location = location


def saveObject(obj, file):
    with open(file, "wb") as pickleFile:  # note write and binary mode#
        pickle.dump(obj, pickleFile)


def loadObject(file):
    pickleFile = open(file, 'rb')
    obj = pickle.load(pickleFile)
    pickleFile.close()
    return obj


HondaCivic = car_object()
HondaCivic.startMoving(80)
print("speed:" + str(HondaCivic.speed) + " moving:" + str(HondaCivic.moving))
saveObject(HondaCivic, "Hfile")
HondaCivic = None
print(type(HondaCivic))
HondaCivic = loadObject("Hfile")
print("speed:" + str(HondaCivic.speed) + " moving:" + str(HondaCivic.moving))

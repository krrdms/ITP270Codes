import json
from collections import namedtuple

class car_object:

    def __init__(self):
        self.direction = "N"
        self.speed = 0
        self.location = "38.8334N,77.2365W"
        self.moving = False

    def startMoving(self, speed=0):
        self.moving = True
        self.speed = speed

    def stopMoving (self):
        self.moving = False
        self.speed = 0

    def changeDirection(self,direction):
        self.direction = direction

    def changeLocation(self,location):
        self.location = location

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

def saveObject(obj,file):
    with open(file,"w") as pickleFile: # note write mode#
        pickleFile.write(obj.toJson())

def loadObject(file):
    with open(file, "r") as pickleFile: # note write mode#
        jsondata = pickleFile.read()
    pickleFile.close()
    return json.loads(jsondata)

HondaCivic = car_object()
HondaCivic.startMoving(80)
print("speed:" + str(HondaCivic.speed) + " moving:" + str(HondaCivic.moving))
saveObject(HondaCivic,"hfile")
HondaCivic = None
print(type(HondaCivic))
HondaCivic = loadObject("hfile")
print(type(HondaCivic))
print(str(HondaCivic))

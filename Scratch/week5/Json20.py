import json
from collections import namedtuple
import sys

sys.path.insert(0, '.')
import github.Scratch.week5.class7 as class8


class jCar(class8.car):

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def saveObject(cls, obj, file):
        with open(file, "w") as jsonFile:  # note write mode#
            jsonFile.write(obj.toJson())

    @classmethod
    def customCarDecoder(cls, carDict):
        return namedtuple('car', carDict.keys())(*carDict.values())

    @classmethod
    def loadObject(cls, file, obj_hook=None):
        with open(file, "r") as pickleFile:  # note write mode#
            JSONdata = pickleFile.read()
        pickleFile.close()
        if obj_hook == jCar.customCarDecoder:
            return json.loads(JSONdata, object_hook=obj_hook)
        else:
            return json.loads(JSONdata)


# Loads the pickle data then uses JSON loads to convert it to a dict
def classToDictJSON(fileName):
    return jCar.loadObject(fileName)


# Loads the pickle data then uses JSON loads to convert it to an object
def classToClassJSON(fileName):
    return jCar.loadObject(fileName, jCar.customCarDecoder)


def main():
    HondaCivic = jCar()
    HondaCivic.changeMovingDirection(80, "NE")
    print("speed:" + str(HondaCivic.speed) + " moving:" + str(HondaCivic.direction))
    print("-----")
    jCar.saveObject(HondaCivic, "Car_Pickle.json")
    HondaCivic = None
    print(type(HondaCivic))
    HondaCivic = classToClassJSON("Car_Pickle.json")
    HondaCivicDict = classToDictJSON("Car_Pickle.json")
    print("-----")
    print(type(HondaCivic))
    print("[Class]: %s %d" % (HondaCivic.direction, HondaCivic.speed))
    print(type(HondaCivicDict))
    print("[Dict]: " + HondaCivicDict['direction'], HondaCivicDict['speed'])


if __name__ == "__main__":
    # execute only if run as a script
    main()


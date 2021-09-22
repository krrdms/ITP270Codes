import pickle
import sys

sys.path.insert(0, '.')
import github.Scratch.week5.class8 as class8


class pCar(class8.car):

    # inherits from car class
    # adds methods to support pickling
    ########
    @classmethod
    def saveObject(cls, obj, file):
        with open(file, "wb") as pickleFile:  # note write and binary mode#
            pickle.dump(obj, pickleFile)

    @classmethod
    def loadObject(cls, file):
        pickleFile = open(file, 'rb')
        obj = pickle.load(pickleFile)
        pickleFile.close()
        return obj


def main():
    # initialize and instance of car and set attributes
    HondaCivic = pCar()
    HondaCivic.changeMovingDirection(80, "NE")
    # print values
    print("speed:%d moving:%s" % (
        HondaCivic.speed, HondaCivic.moving
    ))
    # pickle object and state
    pCar().saveObject(HondaCivic, "hondaPickle")
    # nuke the object
    HondaCivic = None
    print(type(HondaCivic))
    # load the object from the pickle
    HondaCivic = pCar().loadObject("hondaPickle")
    print("speed:%d moving:%s" % (
        HondaCivic.speed, HondaCivic.moving
    ))


if __name__ == "__main__":
    # execute only if run as a script
    main()

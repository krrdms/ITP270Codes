

class car:

    valid_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    # initialization function - initializes instance of car class
    # with direction, speed, and location values

    def __init__(self):
        self.direction = "N"
        self.speed = 0
        self.location = (38.8334, -77.2365)
        self.moving = False

    # These methods change class attributes
    # also known as setters
    def changeMovingDirection(self, speed, direction):
        if type(speed) is int or float:
            self.speed = speed
        if direction in self.valid_directions:
            self.direction = direction

    def stop(self):
        self.speed = 0

    def changeStaticDirection(self,direction):
        if not self.moving:
            self.direction = direction

    def setLocation(self, location):
        self.location = location

    # these methods return class attributes
    # also referred to as 'getters"
    @property
    def retLatorLong(self, choice):
        Lat, Long = self.location
        if choice == 1:
            return Lat
        elif choice == 2:
            return Long
        else:
            return Lat,Long

    @property
    def retSpeed(self):
        return self.speed

    @property
    def retIsMoving(self):
        return self.moving

    @property
    def getDirection(self):
        return self.direction


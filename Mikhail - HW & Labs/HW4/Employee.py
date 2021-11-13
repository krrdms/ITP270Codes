# create this sample class that uses encapsulation and class methods

class Employee:
    # Private variables and methods names should be preceded with __ (two underscores)
    __hourly_rate = None
    __weekly_hours = None
    __last_name = None
    __first_name = None

    def __init__(self, l, f, h, w):
        self.__hourly_rate = h
        self.__weekly_hours = w
        self.__last_name = l
        self.__first_name = f

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getLastName(self):
        return self.__last_name

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getFirstName(self):
        return self.__first_name

    def setHourlyRate(self, rate):
        self.__hourly_rate = rate

    def getHourlyRate(self):
        return self.__hourly_rate

    def setWeeklyHours(self, hrs):
        self.__weekly_hours = hrs

    def getWeeklyHours(self):
        return self.__weekly_hours

    def calcWeeklySalary(self):
        return self.__weekly_hours * self.__hourly_rate

    @classmethod
    def baseEmployeeFactory(cls, last_name, first_name):
        return cls(last_name, first_name, 15.00, 40)

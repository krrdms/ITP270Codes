class ipv4Address:

    __isInitialized = False

    def __init__(self, ipAddress):
        self.__ipAddress = ipAddress
        self.__octets = ipAddress.split(".")
        self.__isInitialized = True

    def getIpAddress(self):
        return self.__ipAddress

    def setIpAddress(self, ipAddress):
        self.__ipAddress = ipAddress
        self.__octets = ipAddress.split(".")
        self.__isInitialized = True

    def isInitialized(self):
        return self.__isInitialized

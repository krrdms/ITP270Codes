import requests


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


class ipLocation:

    def __init__(self, latitude, longitude, city, region, country):
        self.__latitude = latitude
        self.__longitude = longitude
        self.__city = city
        self.__region = region
        self.__country = country

    def setLatLong(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def getLatLong(self):
        return self.__latitude, self.__longitude

    def setLocation(self, city, region, country):
        self.__city = city
        self.__region = region
        self.__country = country

    def getLocation(self):
        return self.__city, self.__region, self.__country


class ipv4AddressClass(ipv4Address, ipLocation):

    def __init__(self, ipAddress):
        self.__ipAddress = ipAddress
        self.__octets = ipAddress.split(".")
        self.queryIPLocation()

    def getIpAddress(self):
        return self.__ipAddress

    def queryIPLocation(self):
        assert len(self.__ipAddress) > 0, "IP Address must be initialized"
        """  Function To Print GeoLocation Latitude & Longitude """
        try:
            geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' + self.__ipAddress + '.json')
            geo_data = geo_request.json()
            self.setLatLong(geo_data['latitude'], geo_data['longitude'])
            self.setLocation(geo_data['city'], geo_data['region'], geo_data['country'])
            rv = True
        except Exception:
            rv = False
        return rv

    @classmethod
    def myIP(cls):
        try:
            ip_request = requests.get('https://get.geojs.io/v1/ip.json')
            ipAddress = ip_request.json()['ip']
            return cls(ipAddress)
            rv = True
        except Exception:
            rv = False
        return rv


def main():
    # targetIPAddress = input("Enter IP Address: ")
    # someIP = ipv4AddressClass(targetIPAddress)
    # print("LatLong:", someIP.getLatLong())
    # print("Locality:", someIP.getLocation())

    myIP = ipv4AddressClass.myIP()
    print("MyIP:", myIP.getIpAddress())
    print("LatLong:", myIP.getLatLong())
    print("Locality:", myIP.getLocation())


if __name__ == "__main__":
    # execute only if run as a script
    main()
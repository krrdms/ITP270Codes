import abc
import requests


class restCaller(abc.ABC):

    @abc.abstractmethod
    def testService(self, param):
        pass


class openWeather(restCaller):
    def testService(self, param):
        with open("keys/apikey") as keyFile:
            kf = keyFile.read()

        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        units = "metric"

        querystring = {"q": param, "units": units}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': kf
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        weather = response.json()
        print(weather["weather"][0]["description"], "and", weather["main"]["temp"])


class covidData(restCaller):

    def testService(self, param):
        with open("keys/apikey") as keyFile:
            kf = keyFile.read()

        url = "https://covid-19-data.p.rapidapi.com/country/code"

        querystring = {"code": param}

        headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': kf
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)


gT = covidData()
gT.testService("it")

oW = openWeather()
oW.testService("Annandale, VA, US")
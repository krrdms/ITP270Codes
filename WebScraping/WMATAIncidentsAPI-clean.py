########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'api_key': '',
}

params = urllib.parse.urlencode({
    # Request parameters
    'Route': '{string}',
})

def getData(url):
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "%s%s" % (url,params), "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "[Errno {0}] {1}".format(e.errno, e.strerror)

    return data

busData = getData("/Incidents.svc/json/BusIncidents?")
elevatorData = getData("/Incidents.svc/json/ElevatorIncidents?")
railData = getData("/Incidents.svc/json/Incidents?")

busData = json.loads(busData)
elevatorData = json.loads(elevatorData)
railData = json.loads(railData)
print(busData)
print("-"*40)
print(elevatorData)
print("-"*40)
print(railData)
####################################
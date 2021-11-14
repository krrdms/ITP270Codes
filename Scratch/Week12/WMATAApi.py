import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

with open("apikey.txt") as f:
    apiKey = f.read()

headers = {
    'api_key': apiKey
}

params = urllib.parse.urlencode({
    'Route': '{string}',
})


def getData(url):
    data = ""
    try:
        conn = http.client.HTTPSConnection("api.wmata.com")
        conn.request("GET", "%s%s" % (url,params),"{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("Error: ", e.errno, e.strerror)

    return data


busData = getData("/Incidents.svc/json/BusIncidents?")
railData = getData("/Incidents.svc/json/Incidents?")
eleData = getData("/Incidents.svc/json/ElevatorIncidents?")

busData = json.loads(busData)
railData = json.loads(railData)
eleData = json.loads(eleData)

for incident in busData['BusIncidents']:
    print(incident)
print("-"*40)
for incident in railData['Incidents']:
    print(incident['LinesAffected'], incident['Description'], incident['IncidentType'], incident['DateUpdated'])
print("+"*40)
for incident in eleData['ElevatorIncidents']:
    print(incident['StationName'], incident['LocationDescription'], incident['DateOutOfServ'])



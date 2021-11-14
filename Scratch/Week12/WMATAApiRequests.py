import requests
import json


def getData(url, headers):
    data = ""
    url = "https://api.wmata.com"+url+"Route="
    try:
        data = requests.get(url, headers=headers)
    except Exception as e:
        print("Error: ", e.errno, e.strerror)

    return data.content


def convertData(*sources, headers):
    output = []
    for source in sources:
        output.append(json.loads(getData(source, headers)))

    return tuple(output)


def main():
    headers = {
        'api_key': '68d2e21415984e969645d8f1e0d31750'
    }

    busData, railData, eleData = convertData("/Incidents.svc/json/BusIncidents?",
                                             "/Incidents.svc/json/Incidents?",
                                             "/Incidents.svc/json/ElevatorIncidents?",
                                             headers=headers)

    for incident in busData['BusIncidents']:
        print(incident)
    print("-"*40)
    for incident in railData['Incidents']:
        print(incident['LinesAffected'], incident['Description'], incident['IncidentType'], incident['DateUpdated'])
    print("+"*40)
    for incident in eleData['ElevatorIncidents']:
        print(incident['StationName'], incident['LocationDescription'], incident['DateOutOfServ'])


if __name__ == '__main__':
    main()

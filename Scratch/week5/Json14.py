import json

# Example code to convert Dict object to JSON
# defines city dict
cities = { "DC": "District of Columbia","ARL": "Arlington",
           "ALX": "Alexandria","BTH": "Bethesda",
            "SilSp": "Silver Spring" }

cities_json = json.dumps(cities)

print("cities dict: ", cities)
print("cities type: ", type(cities))
print("cities JSON: ", cities_json)
print("cities type: ", type(cities_json))
print("-------------")

# vrfy loading JSON format back into dict
cities_load = json.loads(cities_json)
print("cities JSON: ", cities_load)
print("cities type: ", type(cities_load))


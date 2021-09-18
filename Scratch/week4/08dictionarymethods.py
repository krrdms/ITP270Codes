citycoords = {"NYC": (40.43,-73.56),
              "CHI": (41.88,-87.63),
              "KC": (39.5,-94.34)
              }

print (citycoords)

citycoords_ = citycoords.copy()
citycoords.clear()

print(citycoords)

citycoords = citycoords_.copy()

NYC = citycoords.get("NYC")
print("NYC:",NYC)

for city,coords in citycoords.items():
    print(city,coords)

cities = citycoords.keys()
print(cities)

coords = citycoords.values()
print(coords)

citycoords.pop("NYC")
print(citycoords)

citycoords.popitem()
print(citycoords)

citycoords = citycoords_.copy()
citycoords.update({"DC": (38.91,-77.04)})
print(citycoords)

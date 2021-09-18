citycoords = {"NYC": (40.43,-73.56),
              "CHI": (41.88,-87.63),
              "KC": (39.5,-94.34)
              }

keylist = list(citycoords)
print("Keys:",keylist)

keylist_sorted = sorted(citycoords)
print("Sorted Keys:",keylist_sorted)


print("Items",citycoords.items())


for k,v in citycoords.items():
    print(k,":",v)
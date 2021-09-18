citycoords = {"NYC": (40.43,-73.56),
              "CHI": (41.88,-87.63),
              "KC": (39.5,-94.34)
              }

#simple lookup

#print("NYC:",citycoords["NYC"])

##simple lookup fail
#print(citycoords["DC"])

#simple lookup a different way
#print("CHI:",citycoords.get("CHI"))
#print("DC:",citycoords.get("DC"))

##simple lookup a different way/fail
#print(citycoords["DC"])

if "DC" in citycoords:
    print("DC:",citycoords["DC"])
else:
    print("Cannot find key DC")

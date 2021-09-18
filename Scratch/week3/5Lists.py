campuses = ["AN","WO","AL"]
print("\n")
print("len:%d" % (len(campuses)))
for campus in campuses:
    print("x:%s" % (campus))

campuses.append("LO")
print("\n")
for campus in campuses:
    print("y:%s" % (campus))

campuses.insert(2,"MEC")
print("\n")
print("how many MEC:%d" % (campuses.count("MEC")))
for campus in campuses:
    print("z:%s" % (campus))

print("\n")
campuses.pop(2)
print("how many MEC:%d" % (campuses.count("MEC")))
for campus in campuses:
    print("x:%s" % (campus))

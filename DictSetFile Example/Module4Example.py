command = "n"
objects = []
while command != "e":
    command = input("Enter d to create a dict or s to create a set or f to write to file or e to exit: ")
    if command == "d":
        dname = input("enter name of dictionary: ")
        items = int(input("enter number of items: "))
        exec("%s = {}" % dname)
        while items > 0:
            items -= 1
            k = input("enter key: ")
            v = input("enter value: ")
            exec("%s.update(%s = %s)" % (dname, k, v))
        exec("objects.append(%s)" % dname)
    else:
        continue

for o in objects:
    print(o)

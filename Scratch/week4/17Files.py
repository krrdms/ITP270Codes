inputfile = "textfile.txt"
outputfile = "outfile.txt"

#write file example
f = open(outputfile,"w")
f.write("spent 101 got 81 car 3")
f.close()

#read file example
f = open(outputfile)
data = f.read()
numbers = data.split(" ")
sum=0
for number in numbers:
    if number.isdigit():
        sum += int(number)

f.close()
print(sum)

#with example
with open(outputfile) as f:
    data = f.read()
#print(data)

#readlines example
with open(inputfile) as f:
    in_data = f.readlines()

#for line in in_data:
#    print(line)

# writelines example
outlines = ["Think twice, code once.","Scientists build to learn; Engineers learn to build."]
f = open(inputfile,"a")
f.writelines(outlines)
f.close()
#
with open(inputfile) as f:
    in_data = f.readlines()
for line in in_data:
    print(line)
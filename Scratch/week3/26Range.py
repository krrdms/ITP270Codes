#how to use Range to generate characters
#ord function converts characters - to ascii numeric values
#chr function converts ascii numeric values to characters

a = ord("a")
z = ord("z") + 1
for char in range(a,z,1):
    char = chr(char)
    print(char)
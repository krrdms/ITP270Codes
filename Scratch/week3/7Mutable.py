import ctypes

string = "More code, More problems"
a = id(string)
print(a)
#append makes a new object
string += " 2021"
b = id(string)
print(b)

print (ctypes.cast(a,ctypes.py_object).value)
print (ctypes.cast(b,ctypes.py_object).value)

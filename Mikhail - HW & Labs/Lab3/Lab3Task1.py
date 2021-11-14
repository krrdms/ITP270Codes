#  TASK ONE:

e = (2, 123.4567, 10000, 12345.67)

#  print("file_00{} : {:.2f}, {:.2e}, {:.2e}".format(e[0], e[1], e[2], e[3]))
#  TASK ONE ^
y = "file{:0>3d}".format(e[0]), "{:.2f}".format(e[1]), "{:.2e}".format(e[2]), "{:.2e}".format(e[3])
print(y)

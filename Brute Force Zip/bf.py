
password = "cool1"
encoding = "utf-8"
zf = "Flag.brute.zip"

try:
    with ZipFile(zf) as z:
        z.extractall(pwd=bytes(password))
        with open("Flag.txt") as p:
            data = p.readlines()
            print(data)
except RuntimeError as e:
    print(e.message)

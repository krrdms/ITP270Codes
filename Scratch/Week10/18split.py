import re

pattern = '-+'
string = '2344------HELLO--WORLD'
result = re.split(pattern, string)
print(result)

pattern = '\s+'
string = 'Today   is a   present'
result = re.split(pattern, string)
print(result)

# same pattern
# same string
result = re.split(pattern, string, maxsplit=2)
print(result)

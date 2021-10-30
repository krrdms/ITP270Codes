import re

testString = "purple alice@google.com, blah money bob@abc.com blah dishwasher"

# matches alphanumeric characters (w is a class) surrounded by an @
emails = re.findall('[\w\.-]+@[\w\.-]+', testString)

for email in emails:
    print(email)

sentence4 = '<a href="https://www.nvcc.edu">'
print(sentence4)
sentence4 = re.findall("https://[\w|\.]+",sentence4)
print(sentence4)

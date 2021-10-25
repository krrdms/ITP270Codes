import re

testString = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"

# matches alphanumeric characters (w is a class) surrounded by an @
emails = re.findall('[\w\.-]+@[\w\.-]+', testString)

for email in emails:
    print(email)


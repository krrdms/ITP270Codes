import re

st = "purple alice@google.com, blah money bob@abc.com blah dishwasher"
# Change the email domain to yo-yo-dyne.com
print(st)
st = re.sub("(\w+)@(\w+\.\w+)", "\\1@nvcc.edu", st)
print(st)

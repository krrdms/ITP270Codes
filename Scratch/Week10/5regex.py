import re


titleHTML = "<HTML><HEAD><TITLE>Some Web Page</TITLE></HEAD></HTML>"

# + is a greedy match - as many chars as possible
results = re.findall("<.+>", titleHTML)
print("Greedy", results)

# adding the "?" makes the search non-greedy
# as a result find multiple small hits versus one big one
results = re.findall("<.+?>", titleHTML)
print("Non-Greedy", results)


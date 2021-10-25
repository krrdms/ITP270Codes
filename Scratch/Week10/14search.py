import re

textString = "an example word:cat!!!"

match = re.search("word:\w\w\w", textString)

if match:
    print("found", match.group())

# another way to get same outcome
match = re.search("word:\w{3}", textString)

if match:
    print("found", match.group())

# another way to get same outcome
match = re.search("word:[a-zA-Z0-9]{3}", textString)

if match:
    print("found", match.group())

# 'found word:cat’else: print(”not found")

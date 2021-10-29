import re


htmlText = "As you’ve just seen, the backslash character can " \
           "introduce special character classes like word, digit, and " \
           "whitespace. There are also <b>special</b> metacharacter sequences " \
           "called anchors that begin with a backslash, which you’ll learn about below. " \
           "When it’s not serving either of these purposes, the backslash " \
           "escapes metacharacters. <i>A metacharacter preceded by a backslash " \
           "loses its special meaning and matches the literal character " \
           "instead</i>. Consider the following examples"

matchX = re.findall(".+?\.", htmlText)

for match in matchX:
    print(match)
print("-------------")

matchY = re.search("backslash", htmlText)
print("searching for special - find")
if matchY:
    print("hit found")
else:
    print("no hits found")
print("-------------")
print("-------------")

matchZ = re.split("\. ", htmlText)
for match in matchZ:
    print(match)
print("-------------")
print("-------------")
print("-------------")

newHtmlText = re.sub("metacharacter\s","_metachar_ ",htmlText)
newHtmlText = re.sub("\. ",". \n",newHtmlText)
print(newHtmlText)

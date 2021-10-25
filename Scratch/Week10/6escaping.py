import re

htmlText = "As you’ve just seen, the backslash character can " \
           "introduce special character classes like word, digit, and " \
           "whitespace. There are also <b>special</b> metacharacter sequences " \
           "called anchors that begin with a backslash, which you’ll learn about below." \
           "When it’s not serving either of these purposes, the backslash " \
           "escapes metacharacters. <i>A metacharacter preceded by a backslash " \
           "loses its special meaning and matches the literal character " \
           "instead</i>. Consider the following examples"

hits = re.findall(".+?\.", htmlText)
# hits = re.findall(".+?.", htmlText)
for hit in hits:
    print("[+]",hit)

import re


sentence1 = "It is raining outside."
print(sentence1)
print(re.sub("raining", "sunny", sentence1))

# this example limits to one match
sentence2 = "Thank you very very much."
print(sentence2)
print(re.sub("very", "so", sentence2, 1))

# replace all vowels with underscore
sentence2 = "Thank you very very much."
print(sentence2)
print(re.sub("[aeiou]", "_", sentence2))

sentence3 = "the GALAXY and PIXEL are the best phones"
print(sentence3)
sentence3 = re.sub("[A-Z]{2,}","iPhone",sentence3,1)
print(re.sub("[A-Z]{2,}","OnePLus",sentence3,1))



text = "Airtificial Neural Networks are state of the art machine learning algorithm to solve complex problems."


print "Length of file %d" % len(text)

print text[0]
print text[1]
print text[-1]

every_word = text.split(".")
for e in every_word:
	print e

lowercase = text.lower()
print lowercase 


uppercase = text.upper()
print uppercase 


words = text.split()
for w in words:
	upper  = w.capitalize()
	print upper


print text.find("algorithm")

print text.count("art")

print text.replace("state", "stupid")


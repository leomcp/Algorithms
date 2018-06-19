import re 

with open('data.txt', 'r') as f :

	content = f.read()

	# pattern = re.compile(r'[a-z]')
	# pattern = re.compile(r'[a-zA-Z]')
	# pattern = re.compile(r'[^a-zA-Z]')
	# pattern = re.compile(r'[^b]at')

	pattern = re.compile(r'[^a-zA-Z]')

	#pattern = re.compile(r'Mr\.')

	matches = pattern.findall(content)

	for match in matches:
		print(match)
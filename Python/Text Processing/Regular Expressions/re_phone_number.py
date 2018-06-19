import re 

with open('data.txt', 'r') as f:

	content = f.read()

	# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
	# pattern = re.compile(r'[89]00.\d\d\d.\d\d\d\d')
	# pattern = re.compile(r'[1-4]00.\d\d\d.\d\d\d\d')
	# pattern = re.compile(r'[^1-8]\d\d.\d\d\d.\d\d\d\d')
	# pattern = re.compile(r'[^1-8]\d{2}.\d{3}.\d{4}')

	matches = pattern.finditer(content)

	for match in matches:
		print(match)
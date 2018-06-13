'''
Identifiers :

\d any number 
\D anythong but a number 
\s space
\S anything but a space 
\w any character 
\W anythong but a character 
.  \. any character, except for a newline
\b the whitespace around words 
\. a period 


Modifiers :

{1, 3} we're expecting 1-3  \d{1-3}
+ Match 1 or more 
? Match 0 or 1
* Match 0 or more 
$ Match the end of a string 
^ matching the beginning of a string 
| either or \d{1-3} | \w{5-6}
[] range or "variance" [A-Za-Z1-5]
{x}  expecting "x" amount



White Soace Characters :
\n new line 
\s space 
\t tab
\e escape 
\f form feed 
\r return 



DONT FORGET ! 

. + * ? [ ] $ ^ ( ) { } | \


'''

import re 

exampleString = '''
Jessica is 15 years old, and Daneil is 
27 years old.Edward is 97, and his 
grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)

ageDict = {}
x = 0 
for eachName in names:
	ageDict[eachName] = ages[x]
	x+=1

print(ageDict)


"""

Output :

['15', '27', '97', '102']
['Jessica', 'Daneil', 'Edward', 'Oscar']
{'Oscar': '102', 'Daneil': '27', 'Jessica': '15', 'Edward': '97'}

"""

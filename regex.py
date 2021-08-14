#regular expressions or regex 1.0
import re
pattern = r"spam"
pattern2 = r"wed"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")

if re.match(pattern2, "web_development"):
    print('True')

else:
    print('False')
    
#regex 2.0
import re
pattern = r"spam"
string = "spam and eggs are well known in python programming language."

if re.match(pattern, string):
    print("Match")
else:
    print("No match")

if re.search(r"python", string):
    print("Search Found.")
else:
    print("No Search Found.")

split = re.findall(r"[\w']+", string)
print(split)
split.reverse()
print(split)

#method in regex
import re
pattern = r"yth"

match = re.search(pattern, "spam and eggs are well known in python programming language.")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

#re.sub
import re
str = "My name is Andie. Everyone calls me Andie."
newstr = re.sub(r"Andie", "Anthony", str, count = 1)
print(newstr)

#(.) dot metacharacter
import re
pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match found.")
else: 
    print("Match not found.")

if re.match(pattern, "gray"):
    print("Another match found.")
else:
    print("Match not found.")

if re.match(pattern, "glue"):
    print("Third match found.")
else:
    print("Match not found.")

if re.match(pattern, "blue"):
    print("Fourth match found.")
else:
    print("Match not found.")

#(^) and ($) metacharacters
import re
pattern = r"^g..y$"

if re.match(pattern, "grey"):
    print("Match found.")
else: 
    print("Match not found.")

if re.match(pattern, "gray"):
    print("Another match found.")
else:
    print("Match not found.")

if re.match(pattern, "glue"):
    print("Third match found.")
else:
    print("Match not found.")

if re.match(pattern, "blue"):
    print("Fourth match found.")
else:
    print("Match not found.")

#Character class 1.0
import re
pattern = r"[aeiou]"

if re.search(pattern, "elephant"):
    print("Vowel found.")
else:
    print("All consonants.")

if re.search(pattern, "qwerty keypad"):
    print("Vowel found.")
else:
    print("All consonants.")

if re.search(pattern, "rhythm myths"):
    print("Vowel found.")
else:
    print("All consonants.")

#Character class 2.0
import re
pattern = r"[A-Z][a-z][0-9]"

if re.search(pattern, "ABC abc 123"):
    print("Match")
else:
    print('No match')

if re.search(pattern, "AAbb33"):
    print("Match2")
else:
    print('No match')

if re.search(pattern, "Sp3Kt4"):
    print("Match3")
else:
    print('No match')

#Character class 3.0
import re
pattern = r"[abc][def]"

if re.search(pattern, 'alemighty bedens'):
    print('matched')
else:
    print('not matched')
    
if re.search(pattern, 'alemighty den'):
    print('matched')
else:
    print('not matched')

#(^) before a class
import re
pattern = r"[^A-Z]"

if re.search(pattern, "this is all small. so accepted."):
    print("Match1")
else:
    print('No match')

if re.search(pattern, "AbCdEfG123"):
    print("Match2")
else:
    print('No match')

if re.search(pattern, "THISISALLCAPITAL"):
    print("Match3")
else:
    print('No match')

#Use of (*)
import re
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match1")
else:
    print('No match')

if re.match(pattern, "eggspamspamegg"):
    print("Match2")
else:
    print('No match')

if re.match(pattern, "spamegg"):
    print("Match3")
else:
    print('No match')

#Use of (+)
import re
pattern = r"(spam)+"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spamegg"):
    print("Match 3")

#Use of (?)
import re
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")

if re.search(pattern, "saice-creamusage"):
    print("Match 3")

if re.search(pattern, "ice-icecream"):
    print("Match 4")
    
if re.match(pattern, "ice-icecream"):
    print("Match 4")

#Use of {}
import re
pattern = r"9{2,4}[4$]"

if re.match(pattern, "9587412364"):
    print("Match 1")

if re.match(pattern, "9998465549"):
    print("Match 2")

if re.search(pattern, "9859999454"):
    print("Match 3")

#group
import re
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.search(pattern, "tomatoeggcheesespam"):
    print("Match 3")

list_name = ['egg', 'spam', 'tomatoegg', 'eggsausgespam']
new_list = []
for word in list_name:
    if re.search(pattern, word):
        new_list.append(word)
print(new_list)

#group functions
import re
pattern = r"c(de)(f(g)h)(ij)k"

match = re.search(pattern, "abcdefghijklmnopqrstuvwxyz")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.groups())


pattern2 = r"(c(de)(f(g)h)(ij)k)"

match = re.search(pattern2, "abcdefghijklmnopqrstuvwxyz")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.group(5))
    new = match.groups()
print(new)
print(list(new))

#Named and non-capturing groups
import re
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pattern2 = r"(?P<first>abc)(def)(ghi)"

match = re.match(pattern2, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pattern3 = r"(?P<first>abc)(?:def)(?:ghi)"

match = re.match(pattern3, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pattern4 = r"(?P<first>abc)(def)(?:ghi)"

match = re.match(pattern4, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pattern5 = r"(?P<first>abc)(?:ghi)"

match = re.match(pattern5, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

#non-capturing group
import re
pattern = r'(a)(b(?:c)(d)(?:e))'
string = re.search(pattern, 'wxyzabcdefghi')
if string:
    print(string.group())
    print(string.group(0))
    print(string.group(1))
    print(string.group(2))
    print(string.group(3))
    print(string.groups())
    print(len(string.groups()))
    print(list(string.groups()))

#(|) in group - or
import re
pattern = r"g(?:r)(a|e|i|o|u)y"
word = input('Enter a word: ')
string = re.match(pattern, word)

if string:
    print ("Match found")
else:
    print('No match found')

if string:
    items = list(string.groups())
    items.append(string.group())
print(items)
items.reverse()
new_items = items
print(new_items)

#\(1-99) special sequences
import re
pattern = r"(.+)(.?) \2"

match = re.match(pattern, "word word")
if match:
    print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")

#\d, \s, \w, \D,\S and \W special sequences
import re
pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
print('')
pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, " 1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?5")
if match:
    print("Match 3")

#\b, \A, \Z and \B special sequences
import re
pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")

match = re.search(pattern, "We s cattered.")
if match:
    print ("Match 3")

match = re.search(pattern, "We scat tered.")
if match:
    print ("Match 4")

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 5")

#regex - email extraction
import re
import random
pattern = r"([\w\.-]+)(@)([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com and it.hub1992@gmail.com for assistance."

email_list = re.findall(pattern, str)

i = 0
for i in range(len(email_list)):
    email_list[i] = list(email_list[i]) 

new_email_list = []

for j in range(len(email_list)):
    for i in range(len(email_list[0]) - 1):
        email_list[j][i+1] = email_list[j][i] + email_list[j][i+1]
    new_email_list.append(email_list[j][i+1])
print(new_email_list)

print(new_email_list[random.randint(0,len(new_email_list) - 1)])

#Indian phone number validator for jio
import re
phone_number = input('enter a jio sim number: ')
pattern = r"[\+91|0|6|7|9]([0-9]+)"
match = re.match(pattern,phone_number)

if match and (len(phone_number) == 10) and (phone_number[0] == '9' or '7' or '6'):
    print('Ten digt phone number is valid.')
elif match and (len(phone_number) == 11) and (phone_number[0] == '0') and (phone_number[1] == '9' or '7' or '6'):
    print('Ten digit phone number is valid with zero as country code.')
elif match and (len(phone_number) == 13) and (phone_number[0] == '+') and (phone_number[1] == '9') and (phone_number[2] == '1') and (phone_number[3] == '9' or '7' or '6'):
    print('Ten digit phone number is valid with country code.')
else:
    print('Invalid phone number')  




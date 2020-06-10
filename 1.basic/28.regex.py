# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

'''
RegEx

Use of regex:

1. filltering strings
2. validate string values
3. remove unused spaces, special charaters

hello@gmail.com
hello@gmail.com
hello@gmail.com
hello@gmail.com
hello@gmail.com
hello@gmail.com

'''

import re

val = 'Hello Python team how are you!'
print('\n\nSearch: ',re.search("^Hello.",val))

'''
RegEx Functions:

findall:	Returns a list containing all matches
search:	Returns a Match object if there is a match anywhere in the string
split: Returns a list where the string has been split at each match
sub: Replaces one or many matches with a string


Metacharacters
[a-zAZ0-9]

Character	Description	Example
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d" hello\'s	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group


Special Sequences

Character	Description	Example	Try it
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

Sets

Set	Description
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

# The findall() Function

txt = "The rain in Spain"
x = re.findall("ai", txt)
print('findall: ',x)


# The search() Function

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# The split() Function

txt = "The rain in Spain"
x = re.split("\s", txt)
print(type(x))


# The sub() Function

txt = "The rain in Spain"
x = re.sub("\s", "-", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

'''
Questions:

1. What is ASCII code and how many of them.

'''

'''
Excercise:

1. user input se ek string print karao aur usme se specific word ko find karo. Like as 'This is regex excercise and have lots to learn' isme se have ya lots ya to find karo.
2. pahle string me se single charatcer find karo using parameter and search method of regex.
3. function create karo jo user string ko recive kare aur funtion me ek welcome string ko user string ke sath concatenate karke usko return kare aur usko print karo iske baad us output me se jo user serch karna cahta hai useke liye ek new function create karo aur seraching word agar milta hai to usko thank you message ke sath use ko oupput show karao.
4. fuction create karo jsime user input se ek string ko enter kara ke use split method ka use karke list me modify karo aur fir again user se input lo ki kaonsa word list me se search karna hai agar wo milta hai to thank you message show karo.
'''
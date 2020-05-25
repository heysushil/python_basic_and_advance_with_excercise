# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP


strval = '''
# Python Strings
1. String Literals
String literals in python are surrounded by either single quotation marks, or double quotation marks.

2. Assign String to a Variable
3. Multiline Strings
4. Strings are Arrays - are arrays of bytes representing unicode characters.
5. Slicing - print(b[2:5])
6. Negative Indexing
7. String Length - len()
8. String Methods
    strip() method removes any whitespace from the beginning or the end:
    lower() method returns the string in lower case
    upper() method returns the string in upper case
    replace() method replaces a string with another string
    split() method splits the string into substrings if it finds instances of the separator
    etc....

9. Check String - x = "ain" in txt
10. String Concatenation - +
11. String Format - we cannot combine strings and numbers
                  - combine strings and numbers by using the format() method!
                  - The format() method takes unlimited number of arguments, and are placed into the respective placeholders
                  - use index numbers {0} to be sure the arguments are placed in the correct placeholders
12. Escape Character - insert characters that are illegal in a string use '/' rest by site
13. String Methods - Python has a set of built-in methods that you can use on strings. by site
'''
# print('\n\n',strval)

strval = 'hello'
str2 = "hi"
print(strval)

mullinestr = '''

No | Name |       Mobile Number
--------------------------------
1  |Hey   |      89798798798
2  |Suny  |      76876876879
'''

print('\n\n',mullinestr)


arrstr = 'hello how are you HEY '
print('\n\n',arrstr[0:3])  # n-1 

print('\n\n',arrstr[-4:-1])  # n-1
print(len(arrstr))

stripval = arrstr.strip()
print(len(stripval))
print(arrstr.lower())
print(arrstr.replace('hello','Youtube'))

print('hello' in arrstr)

# escape 
name = "Number\'s"
print(name)

name = input('Enter your name => ')
mobile = input('Enter you mobile number => ')
course = input('Enter your course => ')

detail = '''
Name = {}
Mobile = {}
Course = {}
'''.format(name,mobile,course)

print('\n\n',detail)
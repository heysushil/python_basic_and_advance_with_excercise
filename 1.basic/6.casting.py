# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP


'''
Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''

# int to str
intnum = 566576
int2str = str(intnum)
print('\nint2str type',type(int2str))

# float to str
flotnum = 7878.90980
f2s = str(flotnum)
print('\nf2s type',type(f2s))

# casting karte hai isme int2flaot, int2str, float2int, float2str
strval = '98878787'
print('\nstrval type ',type(strval))
str2int = int(strval)
print('\nstr2int tyepe ',type(str2int))

# user input
val1 = int(input('Enter first number = '))
val2 = int(input('Enter second number = '))
sumval = val1 + val2
print('\nsumval = ',sumval)
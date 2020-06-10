# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

'''
Librarys: ye multiple classes hain aur in classes me multiple methods hai

Qestions: 
    1. what is non-relation databse?
    2. 
'''
import json

# user details in dictonary 
user = {
'ankit': {'name':'Ankit','course':'python'},
'shubharm': {'name':'Ankit','course':'python'}
}
print('User Details: ',user['ankit'])

# dictornary to json conver = use dumps of json
ankit = {'name':'Ankit','course':'python'}
d2j = json.dumps(ankit)
print('\nd2j type: ',type(d2j))
print('\nd2j type: ',d2j)


# json to dictonary convertions = use loads method of json
x =  '{"name":"John", "age":30, "city":"New York"}'
print('Thpe of X: ',type(x))
# print('\n\nX:',x['age'])
# parse x:

# json ka loads method x arg ko recive kar raha hai aur isko json se dictonary me conver karke return kar raha hain.
# x = 87887
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


'''
Number of types which conver into json

You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''


'''
Excercise:
    1. use list tupel set and dictonary to convert on json and json 2 noraml fromate and then using string formatting print the output.
    2. take user input and stroe them into dictonary and then convert it into json also json 2 dictonaty using class and related method.
    3. what is api and work of api in python.
'''
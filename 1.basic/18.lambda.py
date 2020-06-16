# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

'''
Lambda function: 

normal func: def functionName

Syntax
lambda arguments : expression

Diff b/w normal function and lambda function

1. hum koi user define name nahi dete hai
2. yaha par lambda keyword use kiya jata hain
3. ye function single line hota hain.
4. yaha par bhi hum arguments pass karte hain.
5. yaha par bhi expression hote hain
6. yaha par direct call kiya jata hain
'''

# normal function
def user(name):
    print('Name: ',name)

# function call
user('Hey kya karu')

# lambda function
lamval = lambda name,course : 'Name: '+name + ' Course: ' + course
print('Lamval: ',lamval('Hey','Kya karu'))

# fuction craete

# sabse pahel normal funciton me 1 argument recive hua b = 40
def userdata(b):
    # newval lambda function ko store kiya hai jo ki next line me 100 value pass karene pe newval = 110
    newval = lambda a : a + 10
    # at last print me b = 40 pada hai aur newval = 110
    # to final value b(40) + newval(110) = 150
    print('\n\nA: ',b + newval(100))

userdata(40)

'''
Excercise:

1. ek program bano jisme ki normal function ko 2 value recive karoa aur function body ke andar lambada function create karo jisme normal function ke 2no argument ka sum pass karo aur last me lambada argument aur normal function ke result ka sum print karo.

2. lambada function create karn a hai aur user name ko print karan hain.
'''
# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# Contact for: College Project | Project Reporting | Documentation | Project Training | Website Development | SEO @ heykyakaru@gmail.com

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Development: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB

'''
Topics:

Python Classes/Objects
Create a Class
Create Object
The __init__() Function
Object Methods
The self Parameter
Modify Object Properties
Delete Object Properties
Delete Objects
The pass Statement
'''

'''
Class Example:

Car => Class
    Methods of Car:
        Start()
        Break()
        Exceleater()
        Off()

TV => Class => Parent Class
    Methos of Tv:
        On()
        CHannel()
        Volume()
        Off()

SmartTv => Class => Child Class
    Methos of SmartTv:
        YouTube()
        OnlineGame()
        Amazon()
'''

class Tv1:
    # constructer: automatic created
    '''
    Points of Constructor:
        1. isme define concepts or variables or values har ek method me accessable hote hain.
        2. python me constructor ko define karna jaruri hai
    '''
    x = 10
    # print(x)

# creat object of Tv class
tvobj = Tv1()
print(tvobj.x)


# creat new class
class Tv:
    # creat construct in class
    def __init__(self,name, email):
        self.n = name
        self.e = email
        self.a = 'India'
    # self current instanst object
    def user(self):
        print('''\nHello Mr. {}, welcome to class.
        \nYour Email id is {}
        \nYour address is {}
        '''.format(self.n,self.e,self.a))

name = input('Enter your name: ')
email = input('Enter your email id: ')
# create object of calss
newobj = Tv(name, email)
newobj.user()

del newobj
print(newobj)



'''
Questions:

What is constructer?
Inheritance ?
'''

'''
Excercise:

1. ek class banani hai aur useme ek user method banake usme user details ko recive karna hai. Jiase ki name,email,password,address. In sabhi details ko user method me recive kareke multiline string ke though outhput show karna hai.

2. ek add / subtract / multiplication / diviton ka alag alag method bana hain ek calculater class ke andar aur user se 2 number ka input lena hai 2 alag-alag variable ke andar. aur abshi method ke andar yahi 2no varable reice karke method ouput show karana hai. sath me output me sahi tairke se user input value aur method ka nama sath me outhput dikhana hai.
'''
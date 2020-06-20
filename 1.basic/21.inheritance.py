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
Topics
'''

# Python Inheritance
'''
Inheritance:

1. reuseablity
2. progamming ki complexity kam ho jati hain
3. memory save hoti hai
'''

# parent class create
class Tv:
    # create cusntructer
    def __init__(self, name):
        self.tn = name

    # tv name show karane ke liye method
    def tvname(self):
        print('\nHello this is your tv name {}'.format(self.tn))

# child class
class Subtv(Tv):
    # ye child class ka cunstructer hai. yaha se parent class ke construct ko value bhejne ke liye use call karna padega.
    def __init__(self, name, price):
        # name ko parent class tak beja gaya
        Tv.__init__(self, name)
        self.price = price
        
    def tvprice(self):
        print('Your tv price is ',self.price)
        
class Subsubtv(Tv):
    def __init__(self, name, channel):
        # super() method ka use ye direct parent class ko use karta hai
        super().__init__(name)
        self.cn = channel 

    # show numer of channel in tv
    def showChannels(self):
        print('\nApp ki tv me itne channel hain: ',self.cn)

# tv name by user
name = input('Enter your tv name: ')
price = int(input('Enter your tv price in numbers only: '))
cn = int(input('Enter number of channels: '))
# tv class ka object create kiya
tv1 = Subtv(name, price)
# tv1 object ke tvname method ko call kiya taki tv name ka output dekh sake
tv1.tvname()
# tvprice method ko price value dirct de diya aur ye dircet method ko recivve ho raha hai. isme constructer ka koi roll nahi hai
tv1.tvprice()

# subsubtv ka object aur uske method ko call karna
tv2 = Subsubtv(name, cn)
tv2.tvname()
tv2.showChannels()

# Create a Parent Class: Tv
# Create a Child Class: Subtv and Subsubtv
# Add the __init__() Function in child class: parent class ke init method ko override karna
# Use the super() Function
'''
1. Super(): super jab use kiya jata hai to ye hamesa child class me use ho raha hai
2. is case me child class me jo bhi parent class call ki gai hai use ko super() method fetch kar leta hai
3. jab super method ka use karte hain to init method me andar self pass karne ki jarurta nahi hoti hai
'''
# Python Multi-Level inheritance
'''
Is case me 
A => Parent class
B => Child class
C => CHild ka child class hai

A ko B ne inherit kiya C ne B ko inherit kiya jisse ki B aur A class dono ki properties ko C istemal kar sakta hain
'''
class Reffral_A:
    # ref1 yaha revice hoga aur isi class me method ke thorugh uska output show hoga
    def __init__(self, ref1):
        self.ref1 = ref1

    def ref1Name(self):
        print('\n\nRef 1 Name: ',self.ref1)

class Reffral_B(Reffral_A):
    # ref1 ki value A class ko pass ki jayegi aur ref2 ka output B class ke method ke thorught show hoga
    def __init__(self, ref1, ref2):
        super().__init__(ref1)
        self.ref2 = ref2
    
    def ref2Name(self):
        print('\n\nRef 2 Name: ',self.ref2)

class Reffral_C(Reffral_B):
    # yaha par ref1 pass hoga pahel B ko aur wo pass karega A ko
    # ref2 ye direct B ko pass hoga
    # ref3 ye yahi class ka method output show karayega
    def __init__(self, ref1, ref2, ref3):
        super().__init__(ref1, ref2)
        self.ref3 = ref3
    
    def ref3Name(self):
        print('\n\nRef 3 Name: ',self.ref3)
    
# yaha par hum last class ka object create karenge aur waht multilevel inheritance ka use karke baki B and A ke method ka use karke output show kara dega
a = input('Enter 1st ref name: ')
b = input('Enter 2nd ref name: ')
c = input('Enter 3rd ref name: ')
output = Reffral_C(a, b, c)
# ab A,B aur C ke method jo ki output ko show karenge unko call karna hain
output.ref1Name()
output.ref2Name()
output.ref3Name()


# Python Multiple inheritance
'''
1. iska matlab hai ki ek baar me 1 se jada parent class ki properites ko child class use karta hain

A = Parent
B = Parent
C = Chile(A,B)
'''
class A: #Ye Father ho gaya
    def __init__(self, name):
        self.n = name

    def userName(self):
        print('\nYour name is ',self.n)

class B: #Ye Mother class
    def __init__(self, relation):
        self.r = relation

    def userRelation(self):
        print('\nYour relation is ',self.r)

class C(A,B): #Ye hai baccha
    def __init__(self, name, relation, student):
        # super().__init__(name, relation)
        A.__init__(self,name)
        B.__init__(self,relation)
        self.s = student

    def studentName(self):
        print('\nStudent Name: ',self.s)

# creat object of C class
abc = C('Parent','Gaudian','Hitesh')
abc.userName()
abc.userRelation()
abc.studentName()
    

# The issubclass(sub,sup) method
print('\n\nCheck subclass: ',issubclass(C,A))

# The isinstance (obj, class) method
print('\n\nCHeck instance: ',isinstance(abc,A))

# Method Overriding
'''
App ne dekha ki kis tarike se humne har ek child class ke andar kaise construter ko override kiya
'''

# Data abstraction in python
'''
1. abstract ka use karke values ko limited kar diya jata hain class tak hi
2. is case ke liye agar kisi bhi varaibale ko define karte time double understore use kiya jaye to wo class ke bahar non-acceaable ho jata hain
'''
class Hi:
    val = 10
    __val = 100

newval = Hi()
print(newval.val)
print(newval.__val)

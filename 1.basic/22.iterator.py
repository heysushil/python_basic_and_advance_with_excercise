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
'''
for loop using iter and next at backgournd to run this loop
'''
listval = ['a','b','c','d']
for i in listval:
    print('i => ',i)

# Python Iterators: __iter__() and __next__()
iterval = iter(listval)
print('\n\nUsing iterval')
print(next(iterval))
print(next(iterval))
print(next(iterval))
print(next(iterval))
# print(next(iterval))

# Iterator vs Iterable

# Looping Through an Iterator
# Create an Iterator
class Number:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            n = self.a
            self.a += 1
            return n
        else:
            raise StopIteration

nextnum = Number()
mynum = iter(nextnum)

# print(next(mynum))
for i in mynum:
    print(i)

# StopIteration

'''
Exc:

1. aap ek loop creat karo useing iter and next.
'''










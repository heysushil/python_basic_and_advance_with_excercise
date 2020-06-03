# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

newlist = ['list','tuple','set','dictionay']
print('\nNew LIst => ',newlist)

'''
list
    new vale add kar sakete hai
    current value ko change 
    curernt value ko remove kar sakte hai    
'''

print('\nList 1st possition => ',newlist[1])
print('\nList 1st possition => ',newlist[-1])

# Range of Indexes
print('\nList 1st possition => ',newlist[1:3])
print('\nList 1st possition => ',newlist[-3:-1])
print('\nList 1st possition => ',newlist[1:])
print('\nList 1st possition => ',newlist[:3])

# Change Item Value
newlist[0] = 'new list'
print('\nNewlist value[0] => ',newlist[0])

# List Length
print('\nLen => ',len(newlist))
print('\nOld List => ',newlist)

# Add Items
newlist.append('Conditon')


# inset
newlist.insert(0,'list')

# Remove Item
newlist.remove('Conditon')

# pop()
newlist.pop()

# Copy a List
copylist = newlist.copy()

print('\nNew List Value => ',newlist)
# del
del newlist

# newlist = ['new list', 'tuple', 'set', 'dictionay']

# clear
secondlist = copylist.copy()
copylist.clear()

print('\nCopy List Value => ',copylist)

print('\nSecond List Value => ',secondlist)

# Join Two Lists
joinlist = ['join','new','list data']
secondlist.extend(joinlist)



print('\nJoin List => ',secondlist)
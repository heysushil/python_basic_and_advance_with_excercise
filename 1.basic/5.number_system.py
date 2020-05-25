# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

'''
1. int
2. float
3. compex
'''

# int number
intnum = 5 # int number
print('\n\n',intnum)
print(type(intnum))

# float numbr
floatnum = 4.4
print('\n\n',floatnum)
print(type(floatnum))

# complex number
complexnum = 4j
print('\n\nCompex number => ',complexnum)
print(type(complexnum))

# You can convert from one type to another with the int(), float(), and complex() methods:

int2float = float(intnum)
print('\n\int2float value => ',int2float)
print('Int 2 float => ',type(int2float))

float2int = int(floatnum)
print('\n\n float2int value => ',float2int)
print('float2int type => ',type(float2int))

# complex number ko int ya float me convert nahi kar sakte hai
# complex2int = float(complexnum)
# print('\n\n Complex2int value => ',complex2int)
# print('complex2int type => ',complex2int)

import random

randomnum = random.randrange(1,1000,3)
print('\n\n Random number => ',randomnum)
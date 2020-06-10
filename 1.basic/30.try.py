'''
Try.....Except
Finally


1. ye error find karne aur errors ke custome message dene ke liye use hota hai

'''

x = 10
try:
    print(x)
except:
    print('X ko koi value dedo')
else:
    print('Ye else message hai')
finally:
    print('Finally x ki probme solve ho gai')


# Raise an exception
number = '5'

if not type(number) is int:
    raise TypeError('Kewal int number accepted')






'''
Excercies:

1. user se input ko numbers ka jo ki input lene pe string type ka hota hai aur unka sum karna hai but sum karne se pahle ye check karna hai ki number int hai ya nahi. agar int nahi hai to message show karo ki numer ek strning hai otherwise sum kardo.

2. user se input lo agar user input me kuch likhe bina hi enter kar deta hai to empty ya null ka try excep case use karke check karo aur user ko message do.
'''
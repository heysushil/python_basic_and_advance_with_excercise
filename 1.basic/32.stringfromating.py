'''
String formatting

1. ye {} is bracket ka use kiya jata hai string ke andar
2. format method values ko list ya dictonary ke format me rakhta hai.
'''

details = ['ankit','yogesh','subham']

printdetail = '''
---------------------------------
Students details:
---------------------------------
First Student    ==>  {}      
Second Student   ==>  {}          
3rd Student      ==>  {}      
'''

print(printdetail.format(details[0],details[1],details[2]))


'''
Excersise:

1. user se 3 alag - alag number input karna hai aur user input number kya - kya user ne input kiya wo user ko batao aur iske baad function banake 3no nubers ka sum function aur multiplication ka function bana ke result bhi show karo.
'''
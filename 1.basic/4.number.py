# NUMBERS 

intval = '5'
print(type(intval))

floatval = float(intval)
print(type(floatval))

import random
# for(i=1;i < 10;i++)
print(random.randrange(100,999))

strval = 'hello team'
# range starting and ending point deta hai.
print(strval[-4:])
print(len(strval))
print(strval.replace('hello','Hi'))
print(strval)

str1 = 'hello'
str2 = '9999'
str3 = str1 +' '+ str2
print(str3)

name = 'Shubham'
age = str(25)
course = 'Python'

print(name +' '+ age+' ' +course)
outpt = 'Hi my name is {2}, my age is {1}. I\'m learing {0}.'.format(name,age,course)
print(outpt)

print(bool())
print(bool(15))



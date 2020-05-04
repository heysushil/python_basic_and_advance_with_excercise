x = 5
print('\n',type(x))

# string

singlQuote = 'hello'
doubleQuote = "hello doble"
multilineString = '''

Hello Class
    How are you
'''

print('\n,',singlQuote)
print('\n,',doubleQuote)
print('\n,',multilineString)

'''
This is a multi line comment
'''

# Number section

x = 48484 # this is a integer value
y = 88.343 # this is float

# complex number
complexvalue = 7j
print('\n',type(complexvalue))

# Sequence Types

# list
'''
list is changable add/modify/remove/delte
'''
# same as index array example=> value = array('a','b') => value['a']
listvalue = ['hello','hi','how','are','you']
print('\n',type(listvalue))
listvalue.append('Hello')
print('\n',listvalue)
listvalue[0] = 'Python'
print('\n',listvalue[0])
listvalue.remove('Python')
print('\n',listvalue)

# tuple
'''
tuple non-changeable => delte
'''
tuplevalue = ('hello','hi','how','are','you')
print('\n',type(tuplevalue))
print('\n',tuplevalue)
print('\n',tuplevalue[0])

rangevalue = range(0,10)
print('\n',type(rangevalue))
print('\n',rangevalue)

# Dictonary

dictonaryvalue = {"name" : "John", "age" : 36}
print('\n',type(dictonaryvalue))
print('\n',dictonaryvalue)

dictonaryvalue['name'] = 'Shubham'
print('\n',dictonaryvalue['name'])


# set

setvalue = {"apple", "banana", "cherry"}
print('\n',type(setvalue))
print('\n',setvalue)
# print('\n',setvalue[0])





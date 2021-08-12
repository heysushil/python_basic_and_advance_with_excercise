# datatypes
# a ek vairable hai jo ki 10 ko store kiye hai
# yaha par = (equal to) ek assignment operatore hai jo ki 10 ko a me store kar raha hai.
a = 10
print('a ka datatype: ', type(a))
print(a)

# hum 2 number addition karate hai
b = 20
c = a + b
print('C or a aur b ka sum: ', c)

# hum user se 2 number ka input lenge then uska sum karke resutl show karenge
# a = int(input('Enter first number: \n'))
# b = int(input('Etner second number: \n'))

print('check datatype of a: ', type(a), ' b: ', type(b))
d = a + b
print('My sum: ', d)

# ye function ka definition hai matlab yaha hamne ek function deifne kiya hai ki wo kya kaam karega.

def myFitstFunction(myname):    
    # print('My name is', myname)
    return 'My name is', myname

# ek function ka output dekhne ke liye kya jaruri hai.
# funciton define kerne ke bad usko call karna jaruri hai
a = input('\nEnter your name')
output = myFitstFunction(a)
print('\nMy output is: ', output)
print('\noutput type: ', type(output))
# function

'''
function
    argument = varaible
    retrung
'''

# Creating a Function: function defining
# Arguments
# Arbitrary Arguments, *args
# def user(*num):
#     # print(type(num)); exit()
#     print('\nWelcome to function')
#     print('\nAddintion: ',num[0] + num[1] + num[2])

# # function call
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# num3 = int(input('Enter 3rd number: '))

# user(num1, num2, num3)

# Keyword Arguments

# def userdetail(**detail):
#     print('\n\nWelcome to User Details')
#     userinfo = '''
#     Name: {}
#     Couse: {}
#     Mobile: {}
#     '''.format(detail['name'],detail['course'],detail['mobile'])
#     print('\n',userinfo)

# # call function
# name = input('Enter your name: ')
# course = input('Enter your course name: ')
# mobile = input('Enter your mobile number')

# userdetail(name = name, course = course, mobile = mobile)

# Default Parameter Value
def multiply(a = 3, b = 4):
    print('\n\nMultiplication Answer: ',a * b)

# function call
multiply(10)

# Passing a List as an Argument
def listfun(data):
    print(type(data))
    print('\n\nList value: ',data)

# functon call
listval = ['hello','hi']
listfun(listval)

# Return Values
def retrunChek():
    # The pass Statement
    pass
    # print('\n\nWelcome to return checker function')
    # return 'Yes'

# function call
# print(retrunChek())
result = retrunChek()

# use condtion to verfiy funciton is worked or not
if result == 'Yes':
    print('\nFurnction successfully returned')
else:
    print('\nFuntion have problem')


# Recursion
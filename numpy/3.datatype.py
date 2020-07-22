# Numpy Data Types

'''
Datatypes in Numpy

i - interger
u - unsigned inter
f - float
c - complex
b - bollean
m - timedetla
M - datetime
O - object
S - sting
U - unicode string
V - fixed chunk of memory for other type (void)
'''

import numpy as np

arr = np.array([1,2,3,4,5,6,'hello'])
print('\nChec datatype by python type(): ',type(arr))
print('Check datatype by numpy mehtod: ', arr.dtype)

stringArrayValues = np.array(['ram','shyam','radha'])
print('check sting datatype: ',stringArrayValues.dtype)

# define datatype at defing value of array
# dtype also have power to difne length of variable
valueWithDtype = np.array([1,2,3,4], dtype='S3')
print('Vlaus: ',valueWithDtype)
print('decode values: ',valueWithDtype[0].decode('utf-8'))
print('Dataype of value: ',valueWithDtype.dtype)

# to conver sting into interger
stringtoInter = np.array([1,2,3,4,6,7,8], dtype='i')
print('Chek int value: ',stringtoInter.dtype)

# copy array 
newInterValues = stringtoInter.copy()
viewValues = stringtoInter.view()

stringtoInter[0] = 11
print('newInterValues: ',newInterValues)

# view use to get the array values

print('viewValues: ',viewValues)

'''
copy vs view methos

1. copy use to store the values in new varaible but remeber in this case then new varibale will not able to retive changes of main variable.
2. view : in this case it's like image of main varable and in case any changes made in main varaible then the changes alos reflexc in view varaible
'''

# matix: 2*3 row and cloumn
# how to find shap of array

# this is a 1*5 matix [[[[[]]]]]
matixarray = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]], ndmin=5)
print('Find the shap of matixarray: ',matixarray.shape)

'''
Matix of 3*3

[00 01 02]
[10 11 12]
[20 21 22]


Pyramix examples:
  *
 ***
*****
'''
# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion


import numpy as np

myarrary = np.array([1,2,3,4,5])
print('\nTye of myarray: ',type(myarrary))
print('Filllay get the array: ',myarrary)
print(np.__version__)

'''
Array type:

0D = 0 Dimention
1D
2D
3D
.
.
n
'''

# 0d
arr0 = np.array(44)
print('arr0: ',arr0)

# 1D
arr1 = np.array([1,2,3,4,5,6,7,8]) 
print('arr1: ',arr1)

# 2D
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print('arr2: ',arr2)

# 3D
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]]])
print('arr3: ',arr3)

# all dimethoions are representing matirx
# ndim is use to find the matrix dimention
print('arr0 d: ',arr0.ndim)
print('arr1 d: ',arr1.ndim)
print('arr2 d: ',arr2.ndim)
print('arr3 d: ',arr3.ndim)

# higher dimension: ndmin
newmanualDim = np.array([1,2,3,4,5], ndmin=5)
print('newmanualDim: ',newmanualDim)
print('newmanualDim d: ',newmanualDim.ndim)


'''
List methods:
    append
    pop
    clear
    remove

Question:

1. find array index value
2. use slicing to print range value [start:endpoint] = endpoint (n-1) [2:7]


List = array
Array:
    searching
    sort
    filtter
'''

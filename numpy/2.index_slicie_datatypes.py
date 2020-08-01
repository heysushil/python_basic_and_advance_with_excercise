# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion


# find index possition values in array
import numpy as np
# arrty start from 0 possition
arrayvalue = np.array([1,2,3,4,5,6])
print('\narrayvalue[0]: ',arrayvalue[0])

# to add 2 index values
print('arrayvalue sum 2 index [0]+[2]: ',arrayvalue[0] + arrayvalue[2])

# 2d array index
array2d = np.array([[1,2,3,4,5,6], [7,8]])
# listval[0][1]
print('Get 2d array value: ',array2d[0][1])


# 3D array
arrayOf3d = np.array([[[1,2,3,4,5,6,7]]])
print('chekc dim: ',arrayOf3d.ndim)
print('Get3d value: ',arrayOf3d[0][0][2])

# negtaive index possiton value
print('3d negative value: ',arrayOf3d[0][0][-1])

# slicing [start:end:steps]
slicearray = np.array([1,2,3,4,5,6,7,8])
# only start number
print('SLice value: ',slicearray[3:])
# start n end point use (n-1)
print('Slic with starta nad end: ',slicearray[2:5])
# only end posstion
print('Slice end: ',slicearray[:5])

# negative 
print('Slice negative: ',slicearray[-3:-1])

# get steps
print('Slice steps: ',slicearray[1:5:2])

# default start and end with step
print('Slice default: ',slicearray[::3])

# slicing in 2d array
array2d = np.array([[1,2,3,4],[5,6,7,8]])
print('2d array slicing: ',array2d[1][1::2])

# 3d slicing
array3d = np.array([[[1,2,3,4,5,6]]])
print('3d slicing: ',array3d[0][0][::2])

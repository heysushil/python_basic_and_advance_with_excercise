# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion


# split
import numpy as np

# array_split()
arr = np.array([1,2,3,4,5,6,7,8])

splitarr = np.array_split(arr, 4)

print('\nsplitarr: ',splitarr)


# split():  vs array_split():

arr = np.array([1,2,3,4,5,6,7])
splitarr = np.array_split(arr, 4)
print('\nsplitarr using split(): ',splitarr)


# get array_spil index values
arr = np.array([1,2,3,4,5,6])
splitarr = np.array_split(arr, 3)

print('\n\nspliarr to get values: ',splitarr)
print('spliarr[0]: ',splitarr[0])


# use array_spilt with 2D
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
splitarr = np.array_split(arr, 3)
print('\n\nsplitarr 2D: ',splitarr)
print('splitarr[0]: ',splitarr[0])
print('splitarr[0][0]: ',splitarr[0][0])
print('splitarr[0][0][0]: ',splitarr[0][0][0])


# hsplit()
arr = np.array([[1,2,3],[3,4,5],[5,6,7]])
hsplitarr = np.hsplit(arr, 3)
print('\n\nhsplitarr: ',hsplitarr)
'''
[1 2 3]
[3 3 4]
[5 4 5]
'''

# vsplit
arr = np.array([[1,2],[3,4],[5,6],[7,8]])
vsplitarr = np.vsplit(arr, 4)
print('\n\nsplitarr: ',vsplitarr)

# vsplit() = vstack || hsplit() = hstack()

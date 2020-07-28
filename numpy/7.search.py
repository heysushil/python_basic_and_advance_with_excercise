# searaching = where()
import numpy as np

arr = np.array([1,2,3,4,5,6,3,4,6,1,2,1])
searchval = np.where(arr == 1)
print('\nsearchval: ',searchval)

# for geting even
getevenval = np.where(arr%2 == 0)
print('\ngetevenval: ',getevenval)

# for geting odd number

getOddval = np.where(arr%2 == 1)
print('\getOddval: ',getOddval)


# searchsorted()
arr = np.array([4,2,3,5,6,4])
searchSort = np.searchsorted(arr, 4)
print('\n\nsearchSort: ',searchSort)
# assenditn descenting


# side=right
arr = np.array([3,4,5,6,7,1,4])
serchSortedRight = np.searchsorted(arr, 4, side="right")
print('\n\nserchSortedRight: ',serchSortedRight)


# multiple values serach sort
arr = np.array([2,4,6])
serachMultiple = np.searchsorted(arr, [5,7])
print('\n\nserachMultiple: ',serachMultiple)
# join +
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

conarr = np.concatenate((arr1, arr2))
print('conarr: ',conarr)

# 2D
arr1 = np.array([[1,2,3],[5,6,7]])
arr2 = np.array([[4,5,6], [7,8,9]])
con2d = np.concatenate((arr1, arr2), axis=1)
print('con2d: ',con2d)

# stack
stack2d = np.stack((arr1, arr2), axis=0)
print('stack2d: ',stack2d)

rowvar = np.hstack((arr1, arr2))
print('rowvar: ',rowvar)

coloumnvar = np.vstack((arr1, arr2))
print('coloumnvar: ',coloumnvar)

# height or depth of matrix
heightvar = np.dstack((arr1, arr2))
print('heightvar: ',heightvar)
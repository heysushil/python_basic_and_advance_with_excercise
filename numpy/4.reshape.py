# numpy array reshap
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# reshapr array 2D
reshaparr = arr.reshape(4,3)
print('reshaparr: ',reshaparr)

# reshap 3D
reshap3D = arr.reshape(2, 3, 2)
print('reshap3D: ',reshap3D)

# find coty or view in reshap
newarr = np.array([1,2,3,4,5,6,7,8])
print('newarr: ',newarr.reshape(2, 4).base)

# to create unknow dimention -1
unknowarr = newarr.reshape(2,2, -1)
print('unknowarr: ',unknowarr)

arr2D = np.array([[1,2,3], [4,5,6]])
print('reshap arr2d: ',arr2D.reshape(-1))


# iteration
arr = np.array([1,2,3,4,5,6])

for n in arr:
    print(n)

arr = np.array([[1,2,3,4],[5,6,7,8]])

for n in arr:
    # print(n)
    for y in n:
        print(y)
    print('end arr[0]')


# 3d iteration
arr = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

for n in arr:
    # 1D 
    print('1D')
    for y in n:
        print('2D')
        for z in y:
            print(z)
        
# numpy diferent step 
arr2D = np.array([[1,2,3], [4,5,6]])
for n in np.nditer(arr2D[:, ::2]):
    print(n)





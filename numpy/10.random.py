# random
import numpy as np
from numpy import random as r

print('\nRandom interger number: ',r.randint(10))
# 0 to 1 
print('\nRandom float number: ',r.rand())
# randint with size
print('\nRandom interger number: ',r.randint(100, size=(5)))
# 2D random number
print('\nRandom interger number: ',r.randint(1000, size=(5, 5)))

# rand use to gerneat number
print('\nRandom float number: ',r.rand(5))
# rand to defin rows with randnum number
print('\nRandom float number: \n',r.rand(5, 5))

# random choice methos
print('\nRandom choice: \n\n',r.choice([2,4,5,6,7,8,9,0], size=(3,3)))


# random distuributon
randchoice = r.choice([2,4,5,6], p=[0.2,0.1,0.7,0.0], size=(5,5))
print('\nrandchoice: \n\n',randchoice)


# shuffinling array
shuffleArr = np.array([1,2,3,4,5])
r.shuffle(shuffleArr)
print('\nr.shuffle(shuffleArr): \n',shuffleArr)

# geranter permuation of array
parmarray = np.array([1,2,3,4,5])

print('\nr.permutation(parmarray): \n',r.permutation(parmarray))

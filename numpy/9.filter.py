# filtter
import numpy as np

arr = np.array([1,2,3,4,5])
# True = 1, False = 0
trueFalse = [True, False, False, True, True]

finalResult = arr[trueFalse]
print('\nfinalResult: ',finalResult)

# filter hight then value
# filterArr = arr > 3
filterArr = arr % 2 == 0
finalResult = arr[filterArr]
print('\nfinalResult of greaterthen: ',finalResult)
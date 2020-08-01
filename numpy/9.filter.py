# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion


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
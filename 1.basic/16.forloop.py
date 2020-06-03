# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

# LOOP'S

# WHILE LOOP
'''
3 PARAMETS
    INITIALIZATION
    CONDTION
    INCREMENT/DECREMENT

PHP Syntax of foor loop:
  for(intializaiot;condition;incremene/decremtn)

  intitliaziton
  while(condtion){
    increment/decrement
  }


'''
# i initialization
i = 1
# condtion
# while i < 6:
#     # print i value 
#   print(i)
# #   check condtion if i value 
#   # if i == 5:
#   #   break
#   i += 1

while i < 10:
    # pass
    print(i)
    i += 1 # i = i + 1
else:
    print('\nI in not less then 10 anymore')

# FOR LOOP
# fruits is a list and holds index values
fruits = ["apple", "banana", "cherry"]
print('\n fruits o index value',fruits[0])
for x in fruits:
  print(x)

# for x in fruits:  
#   if x == "banana":
#     break
#   print('\n',x)

# for i in range(3,31,3):
#     print(i)
# else:
#   print("Finally finished!")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)
# CHECK DO-WHICL LOOP IN C OR C++



'''
# Excecise of Loop

1. read about loops
2. why not use do-while loop in python

'''
# range starting point : end point : diff kitna hoga
# 
for i in range(2,21,2):
  # print('Number => ',i)
  pass

# string
for i in 'hello team':
  print(i)

# list exapml
listval = ['shubham','ankit','rohan','ankita']
for name in listval:
  print('Nmae => ',name)
  # continue and brek
  if 'shubham' not in listval:
    break
  else:
    # print('Shubham in list')
    name1 = 'ankit'
    if name1 != name:
      print('valie of name1 => ',name1)
      continue
else:
  print('For loop ended successfully')

print('\n\n')
userlist = ['ankit','subham','himanshu']
for i in userlist:
  print('\nName: ',i)
  detail = {'course':'python','mobile':8987987987,'address':'Uttar Pradesh'}
  for j in detail:
    print(j,' : ',detail[j])

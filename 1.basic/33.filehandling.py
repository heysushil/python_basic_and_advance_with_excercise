'''
file handling

1. file = filehandling.py
    create
    modify
    delte
2. folder = linux (dir)
    create
    modify
    delte

Filehandling me permission =  read / write

Web site launch

    domain = www.python.com
    hosting = www.python.com content

    google drive/ amazon / mircrosft
        upload/ read/ write

'''

'''
File Handling

open()

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

# check file. for opeing file method open()
file = open('c:/xampp/htdocs/htmldemo/python_basic_and_advance_with_excercise/1.basic/31.input.py','rt')

# read file = read()
# read() is ke andar hum number character pass karte hain.
# readfile = file.read(15)

# readline method to read the lines
readline = file.readline()

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())


# file write
newfile = open('c:/xampp/htdocs/htmldemo/python_basic_and_advance_with_excercise/2.advance/text.txt','a')
# contnect add karne ke liye hun write method ka use karte hai
# get user name
username = input('Enter your name')
name = '\nUser Name is {}'.format(username)
newfile.write(name)

# after create newfile read it
readnewfile = open('c:/xampp/htdocs/htmldemo/python_basic_and_advance_with_excercise/2.advance/text.txt','r')
print('\n\nRead newfile: ',readnewfile.read())
# print(newfile)

newfile.close()
file.close()
readnewfile.close()
# for deleteing file use os library

import os

os.remove('c:/xampp/htdocs/htmldemo/python_basic_and_advance_with_excercise/2.advance/text.txt')



# print(file.readline())
'''
Questions:

what is diff b/w r and a?
what is diff b/w w and x?

'''



'''
Excerciese:

1. ek method bano jisme user input se uka name, email get karo aur usko username ke name se file create kare ke usme save karo. Remebere har file username se hi save karni hai.

2. create method jismem ki file name user se input karanke ke baaad use file ko delete karna hai.
'''


# change list value
l = ['Hello','Python','How','Are','You']
l[2] = 'Yogesh'
# fist way to change list index value
print('L[2]: ',l[2])

# del is a keyword which use for anything to delete
del l[2]

# remove: it's remove the value by providing the name of value.
# In this case 4 is a value. Dosn't matter in which possiton the value relas.
l.remove('Are')

# pop method
l.pop(0)

print('\n\nFUll List: ',l)


'''
1. number system: how many datatypes in number system?
2. 
'''

val = 3+7j 

print('\n\n\n')
l1 = []
l2 = [1,2]

print('Bool value: ',bool(l1))
# if l1 == [] and l2 == []:
if bool(l1) == False and bool(l2) == True:
    print('L1 list is empty and L2 is not empty: ',l2)
else:
    print('L1 is not null')

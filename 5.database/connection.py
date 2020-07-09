# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

'''
Python + Database

Default: Sqlite
'''

# Step 1: Sabse pahel xampp server dwonload and install karna hai
# https://www.apachefriends.org/index.html

# MySQL Database
# Step 2: Install MySQL Driver:
#     python -m pip install mysql-connector-python
# Test MySQL Connector
import mysql.connector as my

# Create Connection
'''
Mysql:
    hostname: loclhost
    username: root
    password: ''
'''
mydb = my.connect(
    host = 'localhost',
    username = 'root',
    password = '',
    database = 'pythondemo'
)
print(mydb)

# Creating a Database
# connection me cursor method me kai aur methods hain jinka use karna hai. 
mycursor = mydb.cursor()

# finally mycursor object me se excecute method ka use karna hai. querys ko run karne ke liye
createnewDB = 'CREATE DATABASE IF NOT EXISTS pythondemo'

# query ko exicute karne ke liye
mycursor.execute(createnewDB)

# Check if Database Exists
# mycursor.execute('SHOW DATABASES')

# for i in mycursor:
#     print(i)

# Creating a Table
'''
Table ke column name
column name ka datatype aur numbers of char
varaible ka datatype aur varaible ki lenght
'''
# VARCHAR datatype alphabet, digits aur special character sabhi accept karta hai
createNewTable = "CREATE TABLE IF NOT EXISTS users (id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,username VARCHAR(100),email VARCHAR(100), userpassword VARCHAR(100))"
mycursor.execute(createNewTable)

# Check if Table Exists

# Primary Key


'''
Question:

1. what is key in database?
2. Kitne tyep ke key databse me hote hai?
3. database me main datatypes kitna-kitna space late hain
4. Kuch key names:
    primary key
    candiate key
    frogen key
    super key
'''
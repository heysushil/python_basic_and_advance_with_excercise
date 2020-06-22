'''
Python + Database

SqlLite

MySqli

Xampp server = xampp
    phpMyAdmin


Mysql / sql / Oracle / SqlLite
4 arguments to connect with data base:
    host: localhost
    username: root
    password: ''
    databasename: 'python'

Hame database ke sath connection create karna hai.

Programming Lang + DataBase

Facebook:
    login:
        facebook login url
        email
        password
'''
# mysql.connector library use to connect python with databse
import mysql.connector as m

# mydb ye connection ko store kar ke rakha hai
mydb = m.connect(
  host="localhost",
  user="root",
  password=""
)

# cursor() method use to run mysql querys
# discuss karna hai: xampp run karne pe problem kar raha tha uske liye jab apache ko bhi start kiya to phpmyadmin chal gaya ye batana hai
# iske baad cursor se start karna hai
mycursor = mydb.cursor()



print(mydb)
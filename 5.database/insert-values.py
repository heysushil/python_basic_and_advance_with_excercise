import connection as con

'''
1. Sabse pahle connection create kiya
2. use ek object ke andar store kiya
3. iske baad isi object ke behalf pe cursor method ko get kiya
4. cursor ko new object mycursome me store kiya
5. mysql ki query ko run karne ke liye mycourse object ke behalf pe excute method ko call kiya
'''

# Insert Into Table
# get details by user
name = input('Enter your name: ')
email = input('Enter your emial id: ')
password = input('Enter your password: ')
insertData = "INSERT INTO users(username, email, userpassword) VALUES('{}','{}','{}')".format(name,email,password)
con.mycursor.execute(insertData)
con.mydb.commit()

# mydb.commit()
# mycursor.rowcount
print('\n\nRow count: ',con.mycursor.rowcount, 'Last inserted row is: ',con.mycursor.lastrowid)

# Get Inserted ID: mycursor.lastrowid

# Select From a Table
userid = con.mycursor.lastrowid
# where ka use karke hum specific row details get kar sakte hain
con.mycursor.execute('SELECT * FROM users WHERE id="{}"'.format(userid))
print(con.mycursor.fetchone())
# print(con.mycursor.fetchall())
# Selecting Columns
# Using the fetchone() Method
con.mycursor.execute('SELECT * FROM users')
getData = con.mycursor.fetchall()
for k in getData:
    print(k)


'''
Excersice:

1. programm bano ki user inofrmaiton like name, course, fee, timing etc details ko user se get karo aur usko database me store karna hai user table me and user ko output me uski details multi line me sahi tarike se dikhana hai with thank you message ki aap ki details successfully store ki ja chuki hai.

2. user table se user ki course realted details ko show karan hai. aur result ko multiline string ka use karke ache formate me show karna hai

Example:

            User COurse Details
-------------------------------------------
1   username    useremail            
'''
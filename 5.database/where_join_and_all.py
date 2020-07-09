# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion


import connection as con

# Alter table column detail: keyword alter
changeColumName = "ALTER TABLE users CHANGE userpassword upassword VARCHAR(100)"
addNewCol = "ALTER TABLE users ADD mobile int(10)"
# con.mycursor.execute(addNewCol)
# con.mydb.commit()

# Insert data: use main connections method mydb.commit()
# Select data
# Select limit data
select = "SELECT * FROM users LIMIT 10"
con.mycursor.execute(select)

tableData = con.mycursor.fetchall()

for i in tableData:
    print(i)

# Select data with where condtion
selectwhere = "SELECT * FROM users WHERE user='Ram'"
con.mycursor.execute(selectwhere)

tableData = con.mycursor.fetchall()
print('\n\n\n')
for i in tableData:
    print(i)

# Orderby: asc desc
order = "SELECT * FROM users ORDER BY id ASC"
con.mycursor.execute(order)

tableData = con.mycursor.fetchall()
print('\n\n\n')
for i in tableData:
    print(i)

# creat new table
newtabel = "CREATE TABLE IF NOT EXISTS qualification(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, degreeName VARCHAR(50))"
con.mycursor.execute(newtabel)

alltable = "SHOW TABLES"
con.mycursor.execute(alltable)
print(con.mycursor.fetchall())

# USER INPUT
degreeName = input('Enter your degree name: ')
inserdegree = "INSERT INTO qualification(degreeName) VALUES('%s')" % degreeName

con.mycursor.execute(inserdegree)
con.mydb.commit()

# get qualiftiactn table data
tabldata = "SELECT * FROM qualification"
con.mycursor.execute(tabldata)

tableData = con.mycursor.fetchall()
print('\n\n\n')
for i in tableData:
    print(i)

# Join
# hum users and qualification table ke bich join karenge
join = "SELECT u.*,q.* FROM users u JOIN qualification q ON q.id = u.id "
con.mycursor.execute(join)
# get join table output

tableData = con.mycursor.fetchall()
print('\n\n\n')
for i in tableData:
    print(i)


# Left join
# Right join
# Inner join

# mydb.rollback(): in case db have error message
try:
    selectwhere = "SELECT * FROM users WHERE user='Ram'"
    con.mycursor.execute(selecatwhere)

    tableData = con.mycursor.fetchall()
    print('\n\n\n')
    for i in tableData:
        print(i)
except:
    # mydb.rollback()
    print('\nAppne syntex error kar diya hai. Dubara check karo')
# Read operations:
# fetchone()
# fetchall(): use for loop
# rowcount
# Update data in table: kyword = update set
update = "UPDATE users SET user = 'Seetaram' WHERE user='Ram'"
con.mycursor.execute(update)
con.mydb.commit()
try:
    selectwhere = "SELECT * FROM users"
    con.mycursor.execute(selectwhere)

    tableData = con.mycursor.fetchall()
    print('\n\n\n')
    for i in tableData:
        print(i)
except:
    # mydb.rollback()
    print('\nAppne syntex error kar diya hai. Dubara check karo')
# Delete row data in table: kyeword = delete
delet = "DELETE FROM users WHERE id='10'"
con.mycursor.execute(delet)
con.mydb.commit()

try:
    selectwhere = "SELECT * FROM users"
    con.mycursor.execute(selectwhere)

    tableData = con.mycursor.fetchall()
    print('\n\n\n')
    for i in tableData:
        print(i)
except:
    # mydb.rollback()
    print('\nAppne syntex error kar diya hai. Dubara check karo')


mydb.close()
# Main methods working in db
# mydb.commit() operation: final to change no revertback
# mydb.rollback(): get db error message
# mydb.close()



'''
Programms

1. program bana hai jisme table ke sabhi data ko fetch karna hai aur usko sahi tarike se means: 
    Example:
     name = yourname | email = youremail | 
     name = yourname | email = youremail | 
     name = yourname | email = youremail | 


2. proram banao jisme user se input lena hai ek integer number aur agar wo id tablel me exist karta hai to uski details ko user ko sahi format me show kara hai.
    emaple:

    ------------------------------
                User Details
    ------------------------------
    name:
    emial:
    password:
    mobile:
    ------------------------------

3. PROGRAM bana hai ki table ke last ke 5 row fetch karke dikhane hai aur sahi tairke se means name = yourname email = youremail   

4. program banao jisme ki 2 table bane hai ek table user details ki aur usme user se input le ke table me data stor karna hai
    user table feilds name: id,rollno,name,fathername,mothername,address,email
user detilas input karne ke baad useko thank you message show karna hai
2nd talle marks bana hai
    marks table fiels: id,rollno,hinid,english,math,sci
user marks input karne ke bad ek success and thank you ka message show karna hai

last me studetn ko uski marks details dikhane ke liye ek input bana hai jiseme ki student apna roll number input kare aur agar wo roll number par marks update kiye ja chuke hain to student ko uske marks detils sahi table ke form me dikhane hai.

5. programmm bana hai jisme ki admin kisi bhi user ko uske rollnumer ya name ke behalf par delelte kar sate aur delee karne ke bad ek success message dikhan hai.
'''
import mysql.connector

mydb = mysql.connector.connect(
       host = "8.208.26.133",
       user = "dms",
       passwd = "Edinburgh2020$",
       database = "junitserver"
       )
mycursor = mydb.cursor()

sql = "SELECT * FROM users WHERE stuid = 's1948679'"
mycursor.execute(sql)

userdata = mycursor.fetchall()

for x in userdata:
    print(x)

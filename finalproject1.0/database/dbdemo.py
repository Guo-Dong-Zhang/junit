import mysql.connector

mydb = mysql.connector.connect(
       host = "8.208.26.133",
       user = "dms",
       passwd = "Edinburgh2020$",
       database = "junitserver"
       )
mycursor = mydb.cursor()

#commit student information
sql = "INSERT INTO users (name,stuid,pwd) VALUES (%s,%s,%s)"
val1 = ("GuoDong","s1948679","123456")
val2 = ("TianLu","s1909850","123456")
mycursor.execute(sql,val1)
mycursor.execute(sql,val2)
mydb.commit()

print(mycursor.rowcount,"Data Insert succeeded!")

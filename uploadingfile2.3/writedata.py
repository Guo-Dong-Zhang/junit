import mysql.connector

mydb = mysql.connector.connect(
       host = "8.208.26.133",
       user = "dms",
       passwd = "Edinburgh2020$",
       database = "junitserver"
       )
mycursor = mydb.cursor()

def dbwrite(_stuid,_pwd):
       id = _stuid
       password = _pwd
       sql = "INSERT INTO users (stuid,pwd) VALUES (%s,%s)"
       val = (id,password)
       mycursor.execute(sql,val)
       mydb.commit()



#commit student information
# sql = "INSERT INTO users (stuid,pwd) VALUES (%s,%s)"
# val1 = ("s1948679","123456")
# val2 = ("s1909850","123456")
# mycursor.execute(sql,val1)
# mycursor.execute(sql,val2)
# mydb.commit()

print(mycursor.rowcount,"Data Insert succeeded!")

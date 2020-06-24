import mysql.connector

def getinfor(_id):
       mydb = mysql.connector.connect(
              host="8.208.26.133",
              user="dms",
              passwd="Edinburgh2020$",
              database="junitserver"
       )
       mycursor = mydb.cursor()

       id = _id
       sql = "SELECT * FROM users WHERE stuid = " + "'"+id+"'"
       # sql = "SELECT * FROM users WHERE stuid = 's1948679'"
       mycursor.execute(sql)
       userdata = mycursor.fetchall()
       return userdata

# result = getinfor("s1948679")
# for x in result:
#     print(x)

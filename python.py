#!C:\Users\Admin\AppData\Local\Programs\Python\Python310\python.exe
 

import cgi
import MySQLdb
import cgitb

cgitb.enable()
try:
    myDB= MySQLdb.connect(host="localhost",user="root",password="",db="example")
    myCursor = myDB.cursor()
    
    form=cgi.FieldStorage()
    username= form.getvalue('name')
    email= form.getvalue('email')

    sql="INSERT INTO users(username,email) VALUES(%s,%s)"
    myCursor.execute(sql,(username,email))
    myDB.commit()

    print("Content-type: text/html")
    print()
    print('''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SUCCESSFULL</title>
            </head>
            <body>
                <h1>SUCCESS</h1>
                <a href='index.html'>Back</a>
            </body>
            </html>''')
except Exception as e:
    print("Content-type: text/html\n")
    print("Error: Unable to connect to MySQL database")
    print(e)


finally:
    myDB.close()
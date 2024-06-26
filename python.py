#!C:\Users\Admin\AppData\Local\Programs\Python\Python310\python.exe
import cgi
print("Content-type: text/html\n\n")

form=cgi.FieldStorage()

username=form.getvalue("username")

print("<html>")
print("<head>")
print("<title>Success page </title>")
print("</head>")
print("<body>")

print("<p><strong><span style='font-size:20px;'>{}</span></strong> Congratulations!!</p>".format(username))
print("You have successfully sent data from HTML form to a CGI Python Script.</p>")

print("</body>")
print("</html>")
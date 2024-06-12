import os

try:

    file1=open("text.txt","w")
    file1.write("Hello\nWellcome to the world of Python")
    file1=open("text.txt","a")
    file1.write("\nPhyton is a simple language")
    file1.close()
    file1=open("text.txt","r")
    print(file1.read())

    os.remove("text.txt")
    print("File is removed")
except:
    print("The file don't exist...")

str=input("Enter a word: ")
str2=input("Enter another word: ")
ch=int(input("\n1.Check if the String is a Substring of Another String\n2.Count Occurrences of Character\n3.Replace a substring with another substring\n4.Convert to Capital Letters\n5.Exit\nYour Choice..."))
for ch in (1,2,3,4,5):
    if ch==1:
        if str2 in str:
            print("The string is a substring of another string")
        else:
            print("The string is not a substring of another string")
    elif ch==2:
        char=input("Enter a character: ")
        count=str.count(char)
        print("The character occurs",count,"times")
    elif ch==3:
        substr=input("Enter a substring to replace: ")
        substr2=input("Enter a substring to replace with: ")
        str=str.replace(substr,substr2)
        print("The new string is: ",str)
    elif ch==4:
        if(str==str.upper()):
            print("The string is already capitalised!")
        else:
            str=str.upper()
            print("The string is capitalised: ",str)
    elif ch==5:
        print("You have exited from the program...")
        break
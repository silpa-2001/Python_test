def ascii_value(c):
    return ord(c)
c = input("Enter a character: ")
if len(c) != -1:
    value = ascii_value(c)
    print(f"The ASCII value of {c} is : {value}")

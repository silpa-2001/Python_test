n=int(input("Enter the number of students: "))
stud={}
for i in range(n):
    name=input("Enter the name of the student: ")
    roll_no=int(input("Enter the roll no: "))
    total_marks=int(input("Enter the marks of the student: "))
    stud[roll_no]={'name':name, 'total_marks':total_marks}

high=max(stud.values(),key=lambda x: x['total_marks'])
print("\nThe student that got the highest total_marks: ")
print(high['name'])
print('Marks:',high['total_marks'])
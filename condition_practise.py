# wap to find the greatest of four numbers entered by the user.

"""
a1 = int(input("enter a numbers:"))
a2 = int(input("enter a numbers:"))
a3 = int(input("enter a numbers:"))
a4 = int(input("enter a numbers:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greartest numbers.",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greartest numbers.",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greartest numbers.",a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greartest numbers.",a4) """



#wap to find the student fail or pass

"""
marks1= int(input("enter subject1 marks:"))
marks2= int(input("enter subject2 marks:"))
marks3= int(input("enter subject3 marks:"))

total_percentage = ((marks1 + marks2 + marks3)/300 )*100

if(total_percentage>=40):
    print("you are passed with the percentage of" ,total_percentage)
else:
    print("you are failed and percentage is", total_percentage) """


# A spam comment is defined as a text containing following keywords "make a lot of money","buy now","watch this","clickh this". WAP to these spams.

p1= "make a lot of money"
p2= "buy now"
p3= "watch this"
p4= "click this"

message = input("enter your comment:")

if((p1 in message)or(p2 in message)or(p3 in message)or (p4 in message)):
    print("spam comment..")
else:
    print("not a spam..")    

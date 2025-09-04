# Grade Calculator

marks = int(input("enter your marks: "))

if(marks>=90 and marks<=100):
    print("Congratulations, You got grade 'A'")
elif(marks>=80 and marks<=89):    
    print("Congratulations, You got grade 'B'")
elif(marks>=70 and marks<=79):    
    print("Congratulations, You got grade 'C'")
elif(marks>=60 and marks<=69):    
    print("Congratulations, You got grade 'D'")
elif(marks<60):
    print("Congratulations, You got grade 'F'")

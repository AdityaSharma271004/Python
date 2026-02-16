# recursion -> it is a function which calls itself.

'''
def factorial(n):
    if(n==0):
        return 1
    
    return  n*factorial(n-1)    

n= int(input("enter any number:"))
print(f"the factorial of this number is:{factorial(n)}")'''


# find the greatest of 3 using function

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c    

a = int(input("enter 1 number:"))        
b = int(input("enter 2 number:"))        
c = int(input("enter 3 number:"))  
print(f"the greatest one is: {greatest(a,b,c)}")


#function -> it is the group of statements which do  a specific task

'''
def avg():  #function definition
    avg = (a+b+c)/3
    print(avg)


a=int (input("enter first number:"))    
b=int (input("enter second number:"))    
c=int (input("enter third number:"))    
avg() #function call '''

# print a user greet

'''
def greet(name):
    print(name,"namaskar..")

name=input("enter your name:")
greet(name) '''

#function with arguments
'''
def good(name, end):
    print("hi", name)
    print(end)

good("adi","thanks for coming..")    '''


# default argument

def say(name,ending="thank you ji.."):#here i give default argument(thank you ji) if user not give any parameter so it default print it.
    print(f"good day,{name}")
    print(ending)

say("aditya")    



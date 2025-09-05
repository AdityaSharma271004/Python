# find the first  non-repeated character

my_str = input("enter your string:")

for char in my_str:
    if my_str.count(char) == 1:
        print("char is : ",char)
        break
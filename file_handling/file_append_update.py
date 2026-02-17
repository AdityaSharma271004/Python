'''
str = "you are amazing"

f = open("myfile.txt","a") #here we give the file name and "a" append in the open file and it add at the last of the string.

f.write(str)

f.close()

'''


# modify the content in file
with open("myfile.txt","r") as f:
    content = f.read()



update  = content.replace("amazing","great")

with open("myfile.txt","w") as f:
    f.write(update)


f.close()
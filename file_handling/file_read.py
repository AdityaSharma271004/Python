'''
f = open("file.txt") #for opening the existing files
data = f.read() #for reading the files
print(data)
f.close() #for closing the open files
'''

f= open("file.txt")
data = f.readline() #it read single line from the file.
data2 = f.readlines() #it read multiple lines and return a string.

print(data)
print(data2)

f.close()


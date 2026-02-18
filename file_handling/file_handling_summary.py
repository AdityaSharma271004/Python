
# For reading file
'''
with open("file.txt","r") as f: 
    content = f.read()
    print(content) 
    f.close()'''

# For writing file 
'''
str = "good morning ji"
with open("mynew.txt","w")as f:
    content = f.write(str)
    f.close()'''

# For update file
'''
with open("mynew.txt","r")as f:
    content = f.read()
    
update_content = content.replace("ji","sir ji")  

with open("mynew.txt","w")as f:
    f.write(update_content)
    f.close()    '''

# Practise Questions:
     
#Question-> The game() function in a program lets a user play a game and returns the score as an integer. You need to read  a file 'Hi-score.txt' which is either blank or contains the previous hi-score. You need to write a program to update the hi-score whernever the game() function breaks the hi-score.

import random

def game():
    print("you are playing a game..")
    score = random.randint(2,10)
    # fetch the hiscore
    with open("hi_score.txt")as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0    
    print(f"your score:{score}")
    if(score>hiscore ):
        #write this hiscore to the file
        with open("hi_score.txt","w")as f:
            f.write(str(score))
    return score        
game()            
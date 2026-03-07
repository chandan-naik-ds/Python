'''
the first  game multiline code could be replace by few lines by taking out any pattern 
from above we are getting the pattern 
You win at -1,2
You loss at 1,-2
so we can shorten the program like below(Not recomended becoz its not finely readable)
'''

import random
'''
1 for stone 
-1 for paper 
0 for siscor
'''

computer = random.choice([1,-1,0])
yourStr = input("Enter your choice : ")
yourdict = {"s":1 , "p":-1, "si":0}
revdict = {1:"Stone", -1:"Paper", 0:"Siscor"}

you = yourdict[yourStr]

print(f"You choose {revdict[you]}\nComputer choose {revdict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    '''
    if(computer == 1 and you == 0): # 1-0 = 1
        print("You loss!")
    elif(computer == 1 and you == -1): # 1-(-1) = 2
        print("You win!")
    elif(computer == -1 and you == 0): # -1-0 = -1
        print("You win!")
    elif(computer == -1 and you == 1): # -1-1 = -2
        print("You loss!")
    elif(computer == 0 and you == 1): # 0-1 = -1
        print("You win!")
    elif(computer == 0 and you == -1): # 0-(-1) = 1
        print("You loss!")
    else:
        print("Something went wrong")
    '''
    if((computer-you)== -1 or 2):
       print("You win!")
    else:
       print("You lose!")
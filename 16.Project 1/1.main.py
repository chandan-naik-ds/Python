import random
'''
1 for stone 
-1 for paper 
0 for siscor
'''

computer = random.choice([1,-1,0])
yourStr = input("Enter your choice : ")
yourdict = {"r":1 , "p":-1, "s":0}
revdict = {1:"Rock", -1:"Paper", 0:"Siscor"}

you = yourdict[yourStr]

print(f"You choose {revdict[you]}\nComputer choose {revdict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    
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




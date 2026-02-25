import random

def game():
    print("You are playing a game")
    score = random.randint(1, 100)
    # fetch the high score 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score : {score}")
    # write the highscore in the file
    if (score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))

game()
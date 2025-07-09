# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
import random

def game(): # so we made a function named game
    print("You are playing the game...") # this will print the given line inside the bracket
    score = random.randint(1, 62) # this will choose a random integer between 1 to 62
    # Fetch the hiscore
    with open("hiscore.txt") as f: # we opened the file(hiscore.txt)
        hiscore = f.read() # reading the content in hiscore.txt
        if (hiscore!=""): # if hiscore is not empty,
            hiscore = int(hiscore) # then hiscore will be equal to int(hiscore)
        else: # if hiscore(file) is empty then hiscore will be taken as zero
            hiscore = 0

    print(f"Your score: {score}") # now priting the score
    if(score>hiscore): # if our score is > than hiscore, then only write that hiscore in hiscore.txt (file)
        # write this hiscore to the file
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))

    return score

game()
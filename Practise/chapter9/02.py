import random
def game():
    print('you are playing the game..')
    score=random.randint(1,66)
    #to fetch the highscore
    with open('hiscore.txt') as file:
        hiscore=file.read()
        if(hiscore!=''):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f'your score : {score}')
    if(score>hiscore):
        #it writes the high score to the file
        with open('hiscore.txt','w') as file:
            file.write(str(score))
    return score

game()
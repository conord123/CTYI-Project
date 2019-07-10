import numpy as np

# making grid

grid = np.arange(210).reshape(21,10)

# asking to play
playchoice = raw_input("play game[y/n] ")
if(playchoice == 'y'):
    print"starting game..."
    score = 0
    print(grid)

    #the game working maybe
    gameover = 0
    while (gameover == 0):
        if (grid(0,1,2,3,4,5,6,7,8,9,) == 1):
            print("better luck next time \n your score: " + score)
            time.sleep(10)
            gameover = 1
        '''if ()
            score = score + 100
            line = 0 '''
# the game stopping (actually works dont edit)
if(playchoice == 'n'):
    print"come back soon"
    exit
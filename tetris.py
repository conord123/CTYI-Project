import numpy as np
import os
os.system('cls') 
# making grid

grid = np.arange(210).reshape(21,10)

# making each line
line1 = grid[(grid > 0) & (grid < 9)]
line2 = grid[(grid > 10) & (grid < 19)]
line3 = grid[(grid > 20) & (grid < 29)]
line4 = grid[(grid > 30) & (grid < 39)]
line5 = grid[(grid > 40) & (grid < 49)]
line6 = grid[(grid > 50) & (grid < 59)]
line7 = grid[(grid > 60) & (grid < 69)]
line8 = grid[(grid > 70) & (grid < 79)]
line9 = grid[(grid > 80) & (grid < 89)]
line10 = grid[(grid > 90) & (grid < 99)]
line11 = grid[(grid > 100) & (grid < 109)]
line12 = grid[(grid > 110) & (grid < 119)]
line13 = grid[(grid > 120) & (grid < 129)]
line14 = grid[(grid > 130) & (grid < 139)]
line15 = grid[(grid > 140) & (grid < 149)]
line16 = grid[(grid > 150) & (grid < 159)]
line17 = grid[(grid > 160) & (grid < 169)]
line18 = grid[(grid > 170) & (grid < 179)]
line19 = grid[(grid > 180) & (grid < 189)]
line20 = grid[(grid > 190) & (grid < 199)]
line21 = grid[(grid > 200) & (grid < 209)]
# asking to play
playchoice = raw_input("play game[y/n] ")
gameover = 0
if(playchoice == 'y'):
    print ("starting game...")
    print ("#### \n\n #  \n###\n\n#  \n###\n\n  #\n###\n\n##\n##\n\n # \n###\n\n## \n ##\n\n ##\n##")
    while (gameover == 0):
        score = 0
        line2 = '#'
        os.system('clear')
        print(grid)
        print "\nscore: " + str(score)
        print ("#### \n\n #  \n###\n\n#  \n###\n\n  #\n###\n\n##\n##\n\n # \n###\n\n## \n ##\n\n ##\n##")
        gameover =1
        #the game working maybe
        while(score > 1):
            time.sleep(5)
            score = score -1
            while (gameover == 0):
                if (line1 == '#'):
                    print("better luck next time \n your score: " + score)
                    gameover = 1

                if (line2 == '#'):
                    score = score + 100
                    line2 = 0
        # the game stopping (actually works dont edit)
        if(playchoice == 'n'):
            print "come back soon"
            exit
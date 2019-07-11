import numpy as np
import os
os.system('clear') 
# making grid of ~
grid = np.chararray((21,10))
grid[:] = "~"
# making each line
'''
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
line11 = grid[(grid > 100) & (grid < 110)]
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
'''
# asking to play
playchoice = raw_input("play game[y/n] ")
gameover = 0
if(playchoice == 'y'):
    print ("starting game...")
    while (gameover == 0):
        score = 0
        line2 = '#'
        os.system('clear')
        print(grid)
        print "\nscore: " 
        print str(score)
        #making the pieces in their various forms
        zeroturn = "#### \n\n #  \n###\n\n#  \n###\n\n  #\n###\n\n##\n##\n\n # \n###\n\n## \n ##\n\n ##\n##\n"
        firstturn = "#\n#\n#\n#\n\n##\n#\n#\n\n#\n#\n##\n\n##\n##\n\n#\n##\n#\n\n #\n##\n#\n\n#\n##\n #\n"
        secondturn = "####\n\n###\n  #\n\n###\n#\n\n##\n##\n\n###\n # \n\n## \n ##\n\n ##\n##\n"
        thirdturn = "#\n#\n#\n#\n\n #\n #\n##\n\n##\n #\n #\n\n##\n##\n\n #\n##\n #\n\n #\n##\n#\n\n#\n##\n #\n"
        #print "no turn\n\n" + zeroturn
        #print "first turrn\n\n" + firstturn
        #print "second turn\n\n" + secondturn
        #print "third turn\n\n" + thirdturn
        grid[1] = '#'
        grid[2] = '#'
        #the game working maybe
        print(grid)
        if (grid[0] is '#'):
            print("better luck next time \n your score: " + score)
            #gameover = 1
        elif (grid[1] is '#'):
            score = score + 100
            #grid[1] = '~'
        elif (grid[2] == '#'):
            score = score + 100
            grid[2] = '~'
        elif (grid[3] is '#'):
            score = score + 100
            grid[3] = '~'
        elif (grid[4] is '#'):
            score = score + 100
            grid[4] = '~'
        elif (grid[5] is '#'):
            score = score + 100
            grid[5] = '~'
        elif (grid[6] is '#'):
            score = score + 100
            grid[6] = '~'
        elif (grid[7] is '#'):
            score = score + 100
            grid[7] = '~'
        elif (grid[8] is '#'):
            score = score + 100
            grid[8] = '~'
        elif (grid[9] is '#'):
            score = score + 100
            grid[9] = '~'
        elif (grid[10] is '#'):
            score = score + 100
            grid[10] = '~'
        elif (grid[11] is '#'):
            score = score + 100
            grid[11] = '~'
        elif (grid[12] is '#'):
            score = score + 100
            grid[12] = '~'
        elif (grid[13] is '#'):
            score = score + 100
            grid[13] = '~'
        elif (grid[14] is '#'):
            score = score + 100
            grid[14] = '~'
        elif (grid[15] is '#'):
            score = score + 100
            grid[15] = '~'
        elif (grid[16] is '#'):
            score = score + 100
            grid[16] = '~'
        elif (grid[17] is '#'):
            score = score + 100
            grid[17] = '~'
        elif (grid[18] is '#'):
            score = score + 100
            grid[18] = '~'
        elif (grid[19] is '#'):
            score = score + 100
            grid[19] = '~'
        elif (grid[20] is '#'):
            score = score + 100
            grid[20] = '~'
        print "\n\n"
        print(grid)
        gameover = 1
        # the game stopping (actually works dont edit)
        if(playchoice == 'n'):
            print "come back soon"
            exit
#rock paper scissors

import random

print ('Welcome to <<<ROCK, PAPER, SCISSSORS!>>>')

playerList = [ ]

r = 'ROCK'
p = 'PAPER'
s = 'SCISSORS'

rps = [r,p,s] #this list named rps contains variables r, p and s
#print (rps) 

plyr1scr = [] #player1 score
plyr2scr = [] #player2 score

player1 = 'COMPUTER'
playerList.append(player1)

player2 = input('Enter your name\n')
player2 = player2.upper()
playerList.append(player2)

print ('%s vs %s' %(playerList[0], playerList[1]))
#print ('Are you ready %s???\nGO!\n' %(player2))

def gameplay():
    plyr1mv = random.choice(rps) #player move
    plyr2mv = str(input('Play your move\n"R" for Rock\n"P" for Paper\n"S" for Scissors\n*("E" for End)*\n'))
    plyr2mv = plyr2mv.lower()

    if plyr2mv == 'r':
        print(r + '\n' + plyr1mv + '\n')
        if plyr1mv == r:
            print('Draw! No winner...\n')
            gameplay()
        elif plyr1mv == p:
            plyr1scr.append(1)
            print('Computer Wins!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
            gameplay()
        else:
            print('You Win!\n')
            plyr2scr.append(1)
            print('You Win!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
            gameplay()

    elif plyr2mv == 'p':
        print(p + '\n' + plyr1mv + '\n')
        if plyr1mv == p:
            print('Draw! No winner...\n')
            gameplay()
        elif plyr1mv == s:
            plyr1scr.append(1)
            print('Computer Wins!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
            gameplay()
        else:
            plyr2scr.append(1)
            print('You Win!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
            gameplay()

    elif plyr2mv == 's':
        print(s + '\n' + plyr1mv + '\n')
        if plyr1mv == s:
            print('Draw! No Winner...\n')
            gameplay()
        elif plyr1mv == r:
            plyr1scr.append(1)
            print('Computer Wins!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
            gameplay()
        else:
            plyr2scr.append(1)
            print('You Win!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
            gameplay()

    elif plyr2mv == 'e':
        print('GAME OVER!\n%s %d vs %d %s\n' %(playerList[0], (sum(plyr1scr)), (sum(plyr2scr)), playerList[1]))
        if (sum(plyr1scr)) > (sum(plyr2scr)):
            print ('%s WINS!!' %(playerList[0]))
        elif (sum(plyr1scr)) < (sum(plyr2scr)):
            print ('%s WINS!!' %(playerList[1]))
        else:
            print('DRAW! No Winner!')

    else:
        print('Invalid Entry! Try Again...\n')
        gameplay()
    
gameplay()
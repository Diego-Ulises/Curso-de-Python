#Positions
center='-'
up='-'
down='-'
left='-'
rigth='-'
cornerUpLeft='-'
cornerUpRigth='-'
cornerDownLeft='-'
cornerDownRigth='-'
continueGame=True

def printGame():
    print('%s  %s  %s' % (cornerUpLeft, up, cornerUpRigth))
    print('%s  %s  %s' % (left, center, rigth))
    print('%s  %s  %s' % (cornerDownLeft, down, cornerDownRigth))
    print()

def inputPosition(player):
    print("Elija una posición:")
    print("1 2 3\n4 5 6\n7 8 9\n")
    global cornerUpLeft
    global up
    global cornerUpRigth
    global left
    global center
    global rigth
    global cornerDownLeft
    global down
    global cornerDownRigth
    global continueGame
    position = input()
    if(position=='1'):
        if cornerUpLeft=='-':
            cornerUpLeft = player
        else:
            inputPosition(player)
    elif(position=='2'): 
        if up=='-':    
            up = player 
        else:
            inputPosition(player)
    elif(position=='3'): 
        if cornerUpRigth=='-':    
            cornerUpRigth=player
        else:
            inputPosition(player)
    elif(position=='4'): 
        if left=='-':    
            left=player
        else:
            inputPosition(player)
    elif(position=='5'): 
        if center=='-':    
            center=player
        else:
            inputPosition(player)
    elif(position=='6'): 
        if rigth=='-':
            rigth=player
        else:
            inputPosition(player)
    elif(position=='7'): 
        if cornerDownLeft=='-':    
            cornerDownLeft=player
        else:
            inputPosition(player)
    elif(position=='8'): 
        if down=='-':    
            down=player
        else:
            inputPosition(player)
    elif(position=='9'): 
        if cornerDownRigth=='-':    
            cornerDownRigth=player
        else:
            inputPosition(player)
    else:
        continueGame=False
        print('Lo sentimos perdiste')

def caseOne(player):
    global cornerUpLeft
    global up
    global cornerUpRigth
    global left
    global center
    global rigth
    global cornerDownLeft
    global down
    global cornerDownRigth
    ######################Buscar ganar######################
    #find cornerUpLeft
    if (up=='O' and cornerUpRigth=='O') or (left=='O' and cornerDownLeft=='O') or (center=='O' and cornerDownRigth=='O'):
        if cornerUpLeft=='-':
            cornerUpLeft='O'
            return 1
    #find up
    if (cornerUpLeft=='O' and cornerUpRigth=='O') or (center=='O' and down=='O'):
        if up=='-':
            up='O'
            return 1
    #find cornerUpRigth
    if (up=='O' and cornerUpLeft=='O') or (rigth=='O' and cornerDownRigth=='O') or (center=='O' and cornerDownLeft=='O'):
        if cornerUpRigth=='-':    
            cornerUpRigth='O'
            return 1
    #find left
    if (cornerUpLeft=='O' and cornerDownLeft=='O') or (center=='O' and rigth=='O'):
        if left=='-':
            left='O'
            return 1
    #find center
    if (cornerUpLeft=='O' and cornerDownRigth=='O') or (up=='O' and down=='O') or (cornerUpRigth=='O' and cornerDownLeft=='O') or (left=='O' and rigth=='O'):
        if center=='-':
            center='O'
            return 1
    #find rigth
    if (cornerUpRigth=='O' and cornerDownRigth=='O') or (center=='O' and left=='O'):
        if rigth=='-':
            rigth='O'
            return 1
    #find cornerDownLeft
    if (down=='O' and cornerDownRigth=='O') or (left=='O' and cornerUpLeft=='O') or (center=='O' and cornerUpRigth=='O'):
        if cornerDownLeft=='-':
            cornerDownLeft='O'
            return 1
    #find down
    if (cornerDownLeft=='O' and cornerDownRigth=='O') or (center=='O' and up=='O'):
        if down=='-':
            down='O'
            return 1
    #find cornerDownRigth
    if (down=='O' and cornerDownLeft=='O') or (rigth=='O' and cornerUpRigth=='O') or (center=='O' and cornerUpLeft=='O'):
        if cornerDownRigth=='-':    
            cornerDownRigth='O'
            return 1
    ####################Buscar bloquear#####################
    #find cornerUpLeft
    if (up=='X' and cornerUpRigth=='X') or (left=='X' and cornerDownLeft=='X') or (center=='X' and cornerDownRigth=='X'):
        if cornerUpLeft=='-':
            cornerUpLeft='O'
            return 2
    #find up
    if (cornerUpLeft=='X' and cornerUpRigth=='X') or (center=='X' and down=='X'):
        if up=='-':
            up='O'
            return 2
    #find cornerUpRigth
    if (up=='X' and cornerUpLeft=='X') or (rigth=='X' and cornerDownRigth=='X') or (center=='X' and cornerDownLeft=='X'):
        if cornerUpRigth=='-':
            cornerUpRigth='O'
            return 2
    #find left
    if (cornerUpLeft=='X' and cornerDownLeft=='X') or (center=='X' and rigth=='X'):
        if left=='-':
            left='O'
            return 2
    #find center
    if (cornerUpLeft=='X' and cornerDownRigth=='X') or (up=='X' and down=='X') or (cornerUpRigth=='X' and cornerDownLeft=='X') or (left=='X' and rigth=='X'):
        if center=='-':
            center='O'
            return 2
    #find rigth
    if (cornerUpRigth=='X' and cornerDownRigth=='X') or (center=='X' and left=='X'):
        if rigth=='-':
            rigth='O'
            return 2
    #find cornerDownLeft
    if (down=='X' and cornerDownRigth=='X') or (left=='X' and cornerUpLeft=='X') or (center=='X' and cornerUpRigth=='X'):
        if cornerDownLeft=='-':
            cornerDownLeft='O'
            return 2
    #find down
    if (cornerDownLeft=='X' and cornerDownRigth=='X') or (center=='X' and up=='X'):
        if down=='-':
            down='O'
            return 2
    #find cornerDownRigth
    if (down=='X' and cornerDownLeft=='X') or (rigth=='X' and cornerUpRigth=='X') or (center=='X' and cornerUpLeft=='X'):
        if cornerDownRigth=='-':
            cornerDownRigth='O'
            return 2
    ################Colocar en alguna ezquina###############
    if cornerUpLeft=='-':
        cornerUpLeft='O'
        return 3
    if cornerUpRigth=='-':
        cornerUpRigth='O'
        return 3
    if cornerDownLeft=='-':
        cornerDownLeft='O'
        return 3
    if cornerDownRigth=='-':
        cornerDownRigth='O'
        return 3
    if center=='-':
        center='O'
        return 4
    if up=='-':
        up='O'
        return 5
    if down=='-':
        down='O'
        return 5
    if left=='-':
        left='O'
        return 5
    if rigth=='-':
        rigth='O'
        return 5
    return 0

def caseTwo(player):
    global cornerUpLeft
    global up
    global cornerUpRigth
    global left
    global center
    global rigth
    global cornerDownLeft
    global down
    global cornerDownRigth
    ####################Buscar bloquear#####################
    #find cornerUpLeft
    if (up=='X' and cornerUpRigth=='X') or (left=='X' and cornerDownLeft=='X') or (center=='X' and cornerDownRigth=='X'):
        if cornerUpLeft=='-':
            cornerUpLeft='O'
            return 2
    #find up
    if (cornerUpLeft=='X' and cornerUpRigth=='X') or (center=='X' and down=='X'):
        if up=='-':
            up='O'
            return 2
    #find cornerUpRigth
    if (up=='X' and cornerUpLeft=='X') or (rigth=='X' and cornerDownRigth=='X') or (center=='X' and cornerDownLeft=='X'):
        if cornerUpRigth=='-':
            cornerUpRigth='O'
            return 2
    #find left
    if (cornerUpLeft=='X' and cornerDownLeft=='X') or (center=='X' and rigth=='X'):
        if left=='-':
            left='O'
            return 2
    #find center
    if (cornerUpLeft=='X' and cornerDownRigth=='X') or (up=='X' and down=='X') or (cornerUpRigth=='X' and cornerDownLeft=='X') or (left=='X' and rigth=='X'):
        if center=='-':
            center='O'
            return 2
    #find rigth
    if (cornerUpRigth=='X' and cornerDownRigth=='X') or (center=='X' and left=='X'):
        if rigth=='-':
            rigth='O'
            return 2
    #find cornerDownLeft
    if (down=='X' and cornerDownRigth=='X') or (left=='X' and cornerUpLeft=='X') or (center=='X' and cornerUpRigth=='X'):
        if cornerDownLeft=='-':
            cornerDownLeft='O'
            return 2
    #find down
    if (cornerDownLeft=='X' and cornerDownRigth=='X') or (center=='X' and up=='X'):
        if down=='-':
            down='O'
            return 2
    #find cornerDownRigth
    if (down=='X' and cornerDownLeft=='X') or (rigth=='X' and cornerUpRigth=='X') or (center=='X' and cornerUpLeft=='X'):
        if cornerDownRigth=='-':
            cornerDownRigth='O'
            return 2
    ################Colocar en alguna ezquina###############
    if cornerUpLeft=='-':
        cornerUpLeft='O'
        return 3
    if cornerUpRigth=='-':
        cornerUpRigth='O'
        return 3
    if cornerDownLeft=='-':
        cornerDownLeft='O'
        return 3
    if cornerDownRigth=='-':
        cornerDownRigth='O'
        return 3
    if center=='-':
        center='O'
        return 4
    if up=='-':
        up='O'
        return 5
    if down=='-':
        down='O'
        return 5
    if left=='-':
        left='O'
        return 5
    if rigth=='-':
        rigth='O'
        return 5
    return 0


##START GAME
print("Tic Tac Toe")
printGame()

turn = input("Elige tu turno (1 - 2):  ")
print()

## CASO 1 Empieza primero (Ganar - Empatar)
if (turn=='1'):                         
    while continueGame:
        ##Computer
        end=caseOne("O")
        if end==1:
            print('Haz ganado [ O ]')
            printGame()
            break
        printGame()
        ##Person
        inputPosition("X")
        printGame()
## CASO 2 Empieza segundo (Empatar)
else:  
    while continueGame:                                 
        ##Person
        inputPosition("X")
        printGame()
        ##Computer
        caseTwo("O")
        printGame()

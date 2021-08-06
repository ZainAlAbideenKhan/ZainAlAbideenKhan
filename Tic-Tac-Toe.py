print('+'+'-'*50+'+\n'+'|'+' '*20+'Tic Tac Toe'+' '*19+'|\n+'+'-'*50+'+\n'+'|'+' '*26+'by-ZAIN UL ABIDEEN KHAN |\n'+'+'+'~'*50+'+')
def Chose_player1():
    player1 = input('\nChoose X or O:').upper()
    if(player1 not in ['X','O']):
        print('\n⚠ Invalid Selection ⚠')
        Chose_player1()
    else:
        return player1

def Chose_board_size():
    while(True):   
        try:
            boardSize = int(input('\nChoose Board size(Enter a int>2): '))
            board=[['_']*boardSize for j in range(boardSize)]
            return board
        except :
            print('\n⚠ Invalid Entery ⚠')

def Game_confi():
    game_confi = 3
    if(len(board)>3):
        while(True):
            confi=input('\nEnter Game configration [N(int)/B]\nEnter N(int) for ending game when there are N consecutive Xs or Os\n or end when Xs or Os are from starting to end either digonaly or cross-wise\n>').upper()
            if(confi.isnumeric() and int(confi)<len(board)):
                game_confi=int(confi)
                break
            elif(confi == 'B'):
                game_confi=len(board)
                break
            print('\n⚠ Either select valid value or Your value is out of range ⚠')
    return game_confi

def Select_player():
    global player2
    player2 = [input('Enter Select H for Human :').upper(),'']# or C for Computer
    if(player2[0] not in ['H','C']):
        print('⚠ Select a valid option ⚠')
        Select_player()
    else:
        if(player1 == 'X'):
            player2[1] = 'O'
        else:
            player2[1] = 'X'
        return player2

def Show_board():
    for i in range(0,len(board)):
        if(i==0):
           print(' ',*list(chr(65+j) for j in range(0,len(board))),sep=" ")
        if(i<len(board)-1):
            print(i,end=' ')
            for j in range(0,len(board[i])):
                if(j<len(board[i])-1):
                    print(board[i][j]+'\u0332'+'|',end='')
                else:
                    if(board[i][j] != '_'):
                        print(board[i][j]+'\u0332')
                    else:
                        print(board[i][j])
        else:
            print(i,end=' ')
            for j in range(0,len(board[i])):
                if(j<len(board[i])-1):
                    print(board[i][j].replace('_',' ')+'|',end='')
                else:
                    print(board[i][j].replace('_',' '))

def Human_plays():
    for i in range(0,len(board)**2):
        while True:
            try:
                if(i%2==0):
                    posi = ['X',input("\nX turn enter position (eg 2C):")]
                else:
                    posi = ['O',input("\nO turn enter position (eg 2C):")]
                posi+=[int(posi[1][0]),ord(posi[1][1])-65]
                if([posi[2],posi[3]] in playerEntry['X'] or [posi[2],posi[3]] in playerEntry['O']):
                    print('\nAlready Choosen try again')
                    continue
                board[posi[2]][posi[3]]=posi[0]
                playerEntry[posi[0]]+=[[posi[2],posi[3]]]
                Show_board()
                state = Game_over()
                break
            except:
                print('\n⚠ Invalid entry ⚠')
        if('S' in str(state)):
            break
    if('S' not in str(state)):
        print('\nIts a Draw')
def Game_over():
    for i in range(0,len(board)):
        win_check={'R':{'X':0,'O':0},'C':{'X':0,'O':0}}
        for j in range(0,len(board)):
            if('X'==board[i][j]):
                win_check['C']['O']=0
                win_check['C']['X']+=1
                if(win_check['C']['X']==gameConfi):
                    break
            else:
                win_check['C']['X']=0
            if('O'==board[i][j]):
                win_check['C']['X']=0
                win_check['C']['O']+=1
                if(win_check['C']['O']==gameConfi):
                    break
            else:
                win_check['C']['O']=0

            if('X'==board[j][i]):
                win_check['R']['O']=0
                win_check['R']['X']+=1
                if(win_check['R']['X']==gameConfi):
                    break
            else:
                win_check['R']['X']=0
            if('O'==board[j][i]):
                win_check['R']['X']=0
                win_check['R']['O']+=1
                if(win_check['R']['O']==gameConfi):
                    break
            else:
                win_check['R']['O']=0

        if(win_check['C']['X']==gameConfi or win_check['R']['X']==gameConfi):
            print('++~~~~~~~~~~~~~~~++\n||X is the winner||\n++~~~~~~~~~~~~~~~++')
            return 'S X'
        if(win_check['C']['O']==gameConfi or win_check['R']['O']==gameConfi):
            print('++~~~~~~~~~~~~~~~++\n||O is the winner||\n++~~~~~~~~~~~~~~~++')
            return 'S O'

    for i in range(len(board)-2):
        win_checkD={'DLU':{'X':0,'O':0},'DLD':{'X':0,'O':0},'DRU':{'X':0,'O':0},'DRD':{'X':0,'O':0}}
        rowIdx=0
        for j in range(i,len(board)):
            #Digonal left U side
            if(board[j][rowIdx]=='X'):
                win_checkD['DLU']['O']=0
                win_checkD['DLU']['X']+=1
                if(win_checkD['DLU']['X']==gameConfi):
                    break
            else:
                win_checkD['DLU']['X']=0
            if(board[j][rowIdx]=='O'):
                win_checkD['DLU']['X']=0
                win_checkD['DLU']['O']+=1
                if(win_checkD['DLU']['O']==gameConfi):
                    break
            else:
                win_checkD['DLU']['O']=0
            #lower board check
            if(board[rowIdx][j]=='X'):
                win_checkD['DLD']['O']=0
                win_checkD['DLD']['X']+=1
                if(win_checkD['DLD']['X']==gameConfi):
                    break
            else:
                win_checkD['DLD']['X']=0
            if(board[rowIdx][j]=='O'):
                win_checkD['DLD']['X']=0
                win_checkD['DLD']['O']+=1
                if(win_checkD['DLD']['O']==gameConfi):
                    break
            else:
                win_checkD['DLD']['O']=0
            #Digonal Right-side Upper-half check
            if(board[rowIdx][(len(board)-1)-i-rowIdx]=='X'):
                win_checkD['DRU']['O']=0
                win_checkD['DRU']['X']+=1
                if(win_checkD['DRU']['X']==gameConfi):
                    break
            else:
                win_checkD['DRU']['X']=0
            if(board[rowIdx][(len(board)-1)-i-rowIdx]=='O'):
                win_checkD['DRU']['X']=0
                win_checkD['DRU']['O']+=1
                if(win_checkD['DRU']['O']==gameConfi):
                    break
            else:
                win_checkD['DRU']['O']=0
            #Digonal Right-side Down-half check
            if(i>0):
                if(board[i+rowIdx][(len(board)-1)-rowIdx]=='X'):
                    win_checkD['DRD']['O']=0
                    win_checkD['DRD']['X']+=1
                    if(win_checkD['DRD']['X']==gameConfi):
                        break
                else:
                    win_checkD['DRD']['X']=0
                if(board[i+rowIdx][(len(board)-1)-rowIdx]=='O'):
                    win_checkD['DRD']['X']=0
                    win_checkD['DRD']['O']+=1
                    if(win_checkD['DRD']['O']==gameConfi):
                        break
                else:
                    win_checkD['DRD']['O']=0
            rowIdx+=1
        if(rowIdx!=3):
            rowIdx = gameConfi
        if(rowIdx==win_checkD['DLU']['X'] or gameConfi==win_checkD['DLD']['X'] or gameConfi==win_checkD['DRU']['X'] or gameConfi==win_checkD['DRD']['X']):
            print('++~~~~~~~~~~~~~~~++\n||X is the winner||\n++~~~~~~~~~~~~~~~++')
            return 'S X'
        elif(rowIdx==win_checkD['DLU']['O'] or gameConfi==win_checkD['DLD']['O'] or gameConfi==win_checkD['DRU']['O'] or gameConfi==win_checkD['DRD']['O']):
            print('++~~~~~~~~~~~~~~~++\n||O is the winner||\n++~~~~~~~~~~~~~~~++')
            return 'S O'

def exe1():
    global player1,board,player2,playerEntry,gameConfi
    playerEntry = {'X':[],'O':[]}
    player1 = Chose_player1()
    board = Chose_board_size()
    gameConfi=Game_confi()
    player2 = Select_player()
    Show_board()
    Human_plays()
    if(input('Want to play again[Y/N]').upper()=='Y'):
        exe1()
    else:
        print('+++~~~~~~~~~~~~~~~~~~~~~+++'+'\n|||GIVE ME A STAR PLEASE|||\n'+'+++~~~~~~~~~~~~~~~~~~~~~+++')
exe1()
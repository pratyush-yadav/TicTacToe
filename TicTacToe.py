import os , random , time
os.terminal_size((25,20))
win=[['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']] # Winning_combinations
p=['1','2','3','4','5','6','7','8','9']  # p = plot_location
player,bot,bi=[],[],0 #player_moves , bot_moves , bot_input
l0='\n :=====================:\n |   Tic - Tac - Toe   |\n |=====================|'
l1=l3=l5=l7=l9=l11=' |       |     |       |'
l4=l8=' |  -----+-----+-----  |'
l2,l6,l10=' |    '+p[0]+'  |  '+p[1]+'  |  '+p[2]+'    |',' |    '+p[3]+'  |  '+p[4]+'  |  '+p[5]+'    |',' |    '+p[6]+'  |  '+p[7]+'  |  '+p[8]+'    |'
while True:
    os.system('cls')
    l2,l6,l10=' |    '+p[0]+'  |  '+p[1]+'  |  '+p[2]+'    |',' |    '+p[3]+'  |  '+p[4]+'  |  '+p[5]+'    |',' |    '+p[6]+'  |  '+p[7]+'  |  '+p[8]+'    |'
    print(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,' |---------------------|',sep='\n')
    for chance in win:
        count_p=count_b=0 # p , b = player , bot
        for item in chance:
            if item in player: # if player wins
                count_p+=1
            if item in bot: # if bot wins
                count_b+=1
            if count_p==3:
                input(' |'+'You Won!'.center(21)+'|\n :=====================:\n')
                quit()
            elif count_b==3:
                input(' |'+'You Lost!'.center(21)+'|\n :=====================:\n')
                quit()
            elif len(player)==5:
                input(' |'+'Draw!'.center(21)+'|\n :=====================:\n')
                quit()
    pi=input(' |      Check:         |\r\t\t\b\b') # pi = player_input
    if pi in p and len(player)<6:
        for u in range(9): # u = update_plot_locations_to_symbols
            if pi==str(u+1):
                p[u]='X'
        player.append(pi)
        time.sleep(1)
        while bi not in p and len(bot)<4:
            bi=str(random.randrange(1,10))
        for u in range(9): # u = update_plot_locations_to_symbols
            if bi==str(u+1):
                p[u]='#'
        bot.append(bi)
    else:
        print(' |'+'Invalid Input!'.center(21)+'|\n :=====================:\n')
        time.sleep(1)
        os.system('cls')
        continue

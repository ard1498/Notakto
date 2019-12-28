'''
This code will take time to run, pruning is applied but still will take much time
because it has to check all the possible positions before
This contains Game theory's maxmin concept and it optimization using
alpha-beta pruning.

You can check the print order and modify the print_boards function accordingly.
'''


available_boards = 3
INFINITY = 10000

def print_boards(boards):
    print('-------------------------------------------')
    for b in boards.keys():
        if boards[b][1]:
            print(b)
            for i in range(3):
                for j in range(3):
                    print(boards[b][0][i][j], end =' ')
                print()
            
    print('-------------------------------------------')

def isMovesLeft(boards):
    for b in boards.keys() :
        if boards[b][1]:
            for i in range(3):
                for j in range(3):
                    if boards[b][0][i][j] != 'X':
                        return True
    return False

def evaluate(boards, curplayer, available_boards):
    #checking each board for a winner
    for board in boards.keys():
        if boards[board][1] :
            # checking each row for a winner
            for row in range(3):
                if boards[board][0][row][0] == boards[board][0][row][1] == boards[board][0][row][2] :
                    if curplayer == 'computer' :
                        if available_boards == 1:
                            return -10
                        else:
                            return +10
                    else:
                        return -10
            # checking each col for a winner
            for col in range(3):
                if boards[board][0][0][col] == boards[board][0][1][col] == boards[board][0][2][col] :
                    if curplayer == 'computer' :
                        if available_boards == 1:
                            return -10
                        else:
                            return +10
                    else:
                        return -10             
            # checking diagonals for a winner
            if boards[board][0][0][0] == boards[board][0][1][1] == boards[board][0][2][2] :
                if curplayer == 'computer' :
                    if available_boards == 1:
                        return -10
                    else:
                        return +10
                else:
                    return -10
            if boards[board][0][0][2] == boards[board][0][1][1] == boards[board][0][2][0] :
                if curplayer == 'computer' :
                    if available_boards == 1:
                        return -10
                    else:
                        return +10
                else:
                    return -10
    
    # no one wins then return 0
    return 0

def minimax(boards, depth, isComputer, alpha, beta, available_boards):
    curplayer = ''
    if isComputer: curplayer = 'computer'
    else : curplayer = 'player'

    score = evaluate(boards, curplayer, available_boards)

    # if computer wins
    if score == 10:
        return score
    
    # if player wins
    if score == -10:
        return score

    if isComputer:
        best = -INFINITY
        # Traverse all Boards
        all_moves = get_all_moves(boards)
        for move in all_moves:
            val = boards[move[0]][0][move[1]][move[2]]
            boards[move[0]][0][move[1]][move[2]] = 'X'
            curplayer = 'computer'
            best = max(best, minimax(boards, depth+1, False, alpha, beta, available_boards))
            alpha = max(best, alpha)
            boards[move[0]][0][move[1]][move[2]] = val
            if beta <= alpha:
                break

    else:
        best = INFINITY
        # Traverse all Boards
        all_moves = get_all_moves(boards)
        for move in all_moves:
            val = boards[move[0]][0][move[1]][move[2]]
            boards[move[0]][0][move[1]][move[2]] = 'X'
            curplayer = 'player'
            best = min(best, minimax(boards, depth+1, True, alpha, beta, available_boards))
            beta = min(best, beta)
            boards[move[0]][0][move[1]][move[2]] = val
            if beta <= alpha:
                break
    return best

def get_all_moves(boards):
    all_moves = []
    for board in boards.keys():
        if boards[board][1]: 
            for i in range(3):
                for j in range(3):
                    if boards[board][0][i][j] != 'X':
                        all_moves.append([board,i,j])
    return all_moves

def findBestMove(boards, available_boards):
    bestVal = -1e5
    bestmove = ('',-1,-1)
    curplayer = ''    

    for board in boards.keys():
        if boards[board][1]: 
            for i in range(3):
                for j in range(3):
                    if boards[board][0][i][j] != 'X':
                        val = boards[board][0][i][j]
                        boards[board][0][i][j] = 'X'
                        curplayer = 'computer'
                        moveVal = minimax(boards, 0, False, -INFINITY, INFINITY, available_boards)
                        boards[board][0][i][j] = val
                        if moveVal > bestVal:
                            bestVal = moveVal
                            bestmove = (board, i, j)
    return bestmove

boards = {
    'A' : [[['1','2','3'],
            ['4','5','6'],
            ['7','8','9']], True],
    'B' : [[['1','2','3'],
            ['4','5','6'],
            ['7','8','9']], True],
    'C' : [[['1','2','3'],
            ['4','5','6'],
            ['7','8','9']], True]
}

pos_Dic = {
    '1' : (0,0),
    '2' : (0,1),
    '3' : (0,2),
    '4' : (1,0),
    '5' : (1,1),
    '6' : (1,2),
    '7' : (2,0),
    '8' : (2,1),
    '9' : (2,2)
}

player = 'computer'
print_boards(boards)

while available_boards>0:
    if player=='computer':
        move = findBestMove(boards, available_boards)
        boards[move[0]][0][move[1]][move[2]] = 'X'
    else:
        to_move=input("Human: ")
        move2 = [i for i in to_move]
        move = (move2[0], pos_Dic[move2[1]][0], pos_Dic[move2[1]][1])
        boards[move[0]][0][move[1]][move[2]] = 'X'

    print_boards(boards)
    flag = False
    for board in boards.keys():
        if boards[board][1] :
            # checking each row for a winner
            for row in range(3):
                if boards[board][0][row][0] == boards[board][0][row][1] and boards[board][0][row][1] == boards[board][0][row][2] :
                    flag = True
            # checking each col for a winner
            for col in range(3):
                if boards[board][0][0][col] == boards[board][0][1][col] and boards[board][0][1][col] == boards[board][0][2][col] :
                    flag = True
            # checking diagonals for a winner
            if boards[board][0][0][0] == boards[board][0][1][1] and boards[board][0][1][1] == boards[board][0][2][2] :
                flag = True
            if boards[board][0][0][2] == boards[board][0][1][1] and boards[board][0][1][1] == boards[board][0][2][0] :
                flag = True
            if flag :
                boards[board][1] = False
                available_boards -= 1
                break
    


    if player == 'computer':
        player = 'player'
    else:
        player = 'computer'

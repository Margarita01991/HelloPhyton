# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

def choice(move):
    inpt = False
    while not inpt:
        player_index = input('Ваш ход, выберите ячейку ' + move + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Неправильный ввод')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = move
                inpt = True
            else:
                print('Ячейка занята')
        else:
            print('Неправильный ввод')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    count = 0
    vic = False
    while not vic:
        draw_board(board)
        if count % 2 == 0:
            choice('X')
        else:
            choice('0')
        count +=1
        if count > 4:
            winner = victory_check(board)
            if winner:
                print('Победили', winner)
                vic = True
                break
            if count == 9:
                print('Ничья)')
        draw_board(board)
game(board)
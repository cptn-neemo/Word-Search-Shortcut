def horizontal_check(word_1, board_1):
    # index of place on the board
    count = 0
    # index of place in the word
    place = 0

    # check right

    # Go through each row in the board, then each index of the row. if the start of the word is that letter, then
    # check if each letter to the right is in the board
    for col in board_1:
        for p in range(len(col)):
            place = 0
            if word_1[place] == col[p]:
                count = p
                for pl in word_1:
                    try:
                        if pl == col[count]:
                            count += 1
                        else:
                            break
                    except:
                        break
                else:
                    count = p
                    place = 0
                    for i in range(len(word_1)):
                        col[count] = word_1[place].upper()
                        count += 1
                        place += 1
                    return board
def right_horizontal_check(word, board):
    horizontal_check(word, board)
    return board
#Reverse the board and then do the horizontal check
def left_horizontal_check(word, board):
    new_board = [row[::-1] for row in board]
    horizontal_check(word, new_board)
    board = []
    for row in new_board:
        board.append(row[::-1])
    return board

def up_down_check(word,board):
    new_board = []
    each_col = []
    count = 0
    len_row = len(board[0])
    for col in range(len_row):
        for i in range(len(board)):
            each_col.append(board[i][col])
        new_board.append(each_col)
        each_col = []

    horizontal_check(word,new_board)

    len_row = len(new_board[0])

    board = []
    each_col = []
    for col in range(len_row):
        for i in range(len(new_board)):
            each_col.append(new_board[i][col])
        board.append(each_col)
        each_col = []


    return board



def all_check(word, board):
    board = right_horizontal_check(word, board)
    board = left_horizontal_check(word, board)
    board = up_down_check(word,board)
    return board


board = [['m', 'o', 'n', 'k', 'e'], ['a', 'k', 'n', 'o', 'm'], ['x', 'b', 'c', 'd', 'd']]
words = 'max'
print('Original board: '),
print(range(len(board)))
board = all_check(words, board)
print('new board: '), print(board)



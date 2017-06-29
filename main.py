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

def up_down_reverse(board,new_board):
    new_board = []
    each_col = []

    len_row = len(board[0])
    for col in range(len_row):
        for i in range(len(board)):
            each_col.append(board[i][col])
        new_board.append(each_col)
        each_col = []
    return new_board
def up_down_check(word,board):
    new_board = []
    new_board = up_down_reverse(board,new_board)

    horizontal_check(word,new_board)

    board = []
    board = up_down_reverse(new_board,board)
    return board

def down_up_check(word,board):
    new_board = []
    #Switch the orientation
    new_board = up_down_reverse(board,new_board)

    for row in range(len(new_board)):
        new_board[row] = new_board[row][::-1]

    horizontal_check(word,new_board)

    for row in range(len(new_board)):
        new_board[row] = new_board[row][::-1]

    board = []
    board = up_down_reverse(new_board,board)

    return board

def right_down_check(word,board):


    """
    Start in the top right corner of the board, then works its way left
    Create a new horizointal list of the current board
    """
    new_board = board

    #List of the top column,reverse it to start in top right
    top_col = board[0]
    side_col = []
    #Index of the row
    r = len(board) - 1
    while r >= 0:
        side_col.append(board[r][0])
        r -= 1

    #Index of the column
    c = 0
    #Index of the row
    r = len(board)

    new_list = []




def diagonal_check(word,board):

    word_place = 0

    c = 0
    r = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            word_place = 0
            if word[word_place] == board[row][col]:
                r = row
                c = col

                for let in word:
                    try:
                        if word[word_place] == board[r][c]:
                            c += 1
                            r += 1
                            word_place += 1
                        else: break
                    except:
                        break
                else:
                    c = col
                    r = row

                    for let in range(len(word)):
                        board[r][c] = word[let].upper()
                        r += 1
                        c += 1

    return board
def opp_diagonal_check(word,board):
    new_board = board

    new_board = new_board[::-1]
    for row in range(len(new_board)):
        new_board[row] = new_board[row][::-1]

    diagonal_check(word,new_board)

    new_board = new_board[::-1]
    for row in range(len(new_board)):
        new_board[row] = new_board[row][::-1]
    board = new_board

    return board

def all_check(word, board):
    board = right_horizontal_check(word, board)
    board = left_horizontal_check(word, board)
    board = up_down_check(word,board)
    board = down_up_check(word,board)
    board = diagonal_check(word,board)
    board = opp_diagonal_check(word,board)
    return board


board = [['m', 'd', 'x', 'k', 'e'], ['a', 'a', 'o', 'a', 'm'], ['m', 'b', 'x', 'g', 'm']]
words = 'max'
print('Original board: '), print(board)
board = all_check(words, board)
print('new board: '), print(board)
print()




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
            if word_1[place] == col[p] or word_1[place] == col[p].lower():
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


#The main check diagonal function: Top right -> Bottom left
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
                        if word[word_place] == board[r][c] or word[word_place] == board[r][c].lower():
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

#Diagonal check: Bottom right -> Top left
def brTL_diagonal_check(word,board):
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


#Diagonal check: Top left -> Bottom right
def trBL_diagonal_check(word,board):
    new_board = board

    for row in range(len(new_board)):
        new_board[row] = new_board[row][::-1]

    diagonal_check(word,new_board)

    for row in range(len(new_board)):
        new_board[row] = new_board[row][::-1]

    return board

def blTR_diagonal_check(word,board):
    new_board = board[::-1]

    diagonal_check(word,new_board)

    board = new_board[::-1]

    return board


def all_check(word, board):
    board = right_horizontal_check(word, board)
    board = left_horizontal_check(word, board)
    board = up_down_check(word,board)
    board = down_up_check(word,board)
    board = diagonal_check(word,board)
    board = brTL_diagonal_check(word,board)
    board = trBL_diagonal_check(word,board)
    board = blTR_diagonal_check(word,board)
    return board

"""
board = [['m', 'd', 'g', 'k', 'a'], ['a', 'o', 'o', 'o', 'm'], ['d', 'b', 'g', 'a', 'm']]
words = 'dog'
print('Original board: '), print(board)
board = all_check(words, board)
print('new board: '), print(board)
print()
"""

#Create a list of lists with the board
board = []
with open('Sample_Input.txt') as o:
    for line in o:
        board.append(line.rstrip().split(' '))



words = ['dog','cat','max','dad','hello','good','bad','true']

for word in words:
    board = all_check(word,board)

for row in board:
    print(row)





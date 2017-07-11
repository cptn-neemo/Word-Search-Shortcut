#Function definitions

#Main left to right horizontal check
def horizontal_check(word, board):
    # index of place on the board
    count = 0
    # Go through each row in the board, then each index of the row. if the start of the word is that letter, then
    # check if each letter to the right is in the board
    for row in board:
        for p in range(len(row)):
            #Index of place in the word
            place = 0
            if word[place] == row[p] or word[place].lower() == row[p].lower():
                count = p
                for pl in word:
                    #Check to see if going off of the board
                    try:
                        if pl == row[count] or pl.lower() == row[count].lower():
                            count += 1
                        else:
                            break
                    except:
                        break
                #Make the word uppercase
                else:
                    count = p
                    place = 0
                    for i in range(len(word)):
                        row[count] = word[place].upper()
                        count += 1
                        place += 1
                    return board

#Check from left to right
def right_horizontal_check(word, board):
    horizontal_check(word, board)
    return board

#Reverse the board from right to left and then do the horizontal check
def left_horizontal_check(word, board):
    new_board = [row[::-1] for row in board]
    horizontal_check(word, new_board)
    board = []
    for row in new_board:
        board.append(row[::-1])
    return board

#Flip the board to apply the horizontal check method
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

#Up to down vertical check
def up_down_check(word,board):
    new_board = []
    new_board = up_down_reverse(board,new_board)

    horizontal_check(word,new_board)

    board = []
    board = up_down_reverse(new_board,board)
    return board

#Down to up vertical check
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
            if word[word_place] == board[row][col] or word[word_place].lower() == board[row][col].lower():
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

#Bottom left -> Top right check
def blTR_diagonal_check(word,board):
    new_board = board[::-1]

    diagonal_check(word,new_board)

    board = new_board[::-1]

    return board

#Do all of the checks and return the board
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

#--------------------------------------------------------------------------
#Main

#Create a list of lists for the board
board = []

text_file = input('Please enter the name of the text file: ')

#Append the lines of the text file to the board
with open(text_file) as txt:
    for line in txt:
        board.append(line.rstrip().split(' '))

#List for the words
words = []

#Get all of the words
while(True):
    dec = input('Enter 1 to add a word, enter 2 to find the words: ')
    if dec == '1':
        w = input('Please enter the word: ')
        w.lower()
        words.append(w)
        print()
    else:
        break

#Create the final text file
txt = open('Final_Output.txt','w+')


for word in words:
    board = all_check(word,board)

#Write the new board to the text file
for row in board:
    for let in row:
        txt.write(let + ' ')
    txt.write('\n')
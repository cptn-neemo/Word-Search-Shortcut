def horizontal_check(word,board):
    # index of place
    count = 0
    # place in word
    place = 0

    #check right
    for col in board:
        for p in range(len(col)):
            place = 0
            if word[place] == col[p]:
                count = p
                for pl in word:
                    try:
                       pass
                    except:
                        break
                    else:
                        if pl == col[count]:
                            count += 1
                        else:
                            break
                else:
                    count = p
                    place = 0
                    for i in range(len(word)):
                        col[count] = word[place].upper()
                        count += 1
                        place += 1
                    return 1


board = [['m','m','m','o','e'],['m','m','o','n','k'],'a','b','c','d','d']
words = 'monk'
print('Original board: '),

for i in board:
    for n in i:
        print(n),
    print()

result = horizontal_check(words,board)
print('new board: '), print(board)




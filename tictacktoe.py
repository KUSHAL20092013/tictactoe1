import numpy
board = numpy.array([['-','-','-'],
                     ['-','-','-'],
                     ['-','-','-']]) #creation of board

p1s = 'x'
p2s = 'o'
def place(symbol):
    print(board)
    row = int(input("Enter the row number - 1/2/3 : "))
    col = int(input("Enter the column number - 1/2/3 : "))

    if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1] == '-':
        board[row-1][col-1] = symbol
    else:
        print("Please enter a valid row number or column number")
def check_row(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, 'won')
            return True
def check_column(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, 'won')
            return True       
def check_diagonal(symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        print(symbol, 'won') 
        return True
    elif board[0][2] == board[1][1] == board[2][0] == symbol:
        print(symbol, 'won')
        return True
def won(symbol):
    return check_row(symbol) or check_column(symbol) or check_diagonal(symbol)
def play():
    for turn in range(9):
        if turn%2 == 0: #for x turn
            print('x turn')
            place(p1s)
            if won(p1s):
                print(board)
                break
        else:
            print('o turn')
            place(p2s)
            if won(p1s):
                print(board)
                break
play()
board = []
#creates the board
def initializeBoard():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    return board

#displays the board
def dispBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def validateInput(input):
    if(input.isnumeric):
        input = int(input) - 1
        if(takenPositions.__contains__(input)):
            return False
        takenPositions.append(input)
        return True

def playerOneMovement():
    index = input("PLAYER ONE | Please enter one position from 1 to 9 : ")
    while(not validateInput(index)):
        playerOneMovement()
        break
    board[int(index) - 1] = "X"
    checkWin("X")
    
def playerTwoMovement():
    index = input("PLAYER TWO | Please enter one position from 1 to 9 : ")
    while(not validateInput(index)):
        playerTwoMovement()
        break
    board[int(index) - 1] = "O"
    checkWin("O")

def setWin():
    global isPlayerWin
    isPlayerWin = True

def checkWin(sign):
    checkHorizontalWin(sign)
    checkVerticalWin(sign)
    checkDiagonalWin(sign)

def checkHorizontalWin(sign):
    if((board[0] == sign and board[1] == sign and board[2] == sign) or (board[2] == sign and board[1] == sign and board[0] == sign)):
        setWin()
    elif((board[3] == sign and board[4] == sign and board[5] == sign) or (board[5] == sign and board[4] == sign and board[3] == sign)):
        setWin()
    elif((board[6] == sign and board[7] == sign and board[8] == sign) or (board[8] == sign and board[7] == sign and board[6] == sign)):
        setWin()

def checkVerticalWin(sign):
    if((board[0] == sign and board[3] == sign and board[6] == sign or (board[6] == sign and board[3] == sign and board[0] == sign))):
        setWin()
    elif((board[1] == sign and board[4] == sign and board[7] == sign) or (board[7] == sign and board[4] == sign and board[1] == sign)):
        setWin()
    elif(board[2] == sign and board[5] == sign and board[8] == sign) or (board[8] == sign and board[5] == sign and board[2] == sign):
        setWin()

def checkDiagonalWin(sign):
    if((board[0] == sign and board[4] == sign and board[8] == sign or (board[8] == sign and board[4] == sign and board[0] == sign))):
        setWin()
    elif((board[2] == sign and board[4] == sign and board[6] == sign or (board[6] == sign and board[4] == sign and board[2] == sign))):
        setWin()

def isWin():
    return isPlayerWin

#game engine method
def game():
    dispBoard()
    while(True):
        playerOneMovement()
        dispBoard()
        if(isWin()):
            print("PLAYER ONE WON THE MATCH")
            break
        playerTwoMovement()
        dispBoard()
        if(isWin()):
            print("PLAYER TWO WON THE MATCH")
            break

#main
board = initializeBoard()
takenPositions = []
isPlayerWin = False
game()
# Tic Tac Toe game | Raymond.Ginting@gmail.com

import random

def drawBoard(board):
    # This function prints out the board.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Confirm player wants to use "X" or "O"
    # Returns a list with the player's letter as the first item, and the AI's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to play as "X" or "O"? (type x or o)')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the AI's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Random play between Player or AI
    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'You'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (y or n | yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getAIMove(board, AILetter):
    # Given a board and the AI's letter, determine where to move and return that move.
    if AILetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, AILetter, i)
            if isWinner(copy, AILetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('----------------------------------------------')
print('Tic-Tac-Toe game by: Raymond.Ginting@gmail.com')
print('----------------------------------------------')
print('Here is the Tic-Tac-Toe board:')
print('   |   |')
print(' 7 | 8 | 9 ')
print('   |   |')
print('-----------')
print('   |   |')
print(' 4 | 5 | 6 ')
print('   |   |')
print('-----------')
print('   |   |')
print(' 1 | 2 | 3 ')
print('   |   |')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, AILetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' play first. (it\'s random)')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'You':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congrats! You win the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is draw!')
                    break
                else:
                    turn = 'AI'

        else:
            # AI's turn.
            move = getAIMove(theBoard, AILetter)
            makeMove(theBoard, AILetter, move)

            if isWinner(theBoard, AILetter):
                drawBoard(theBoard)
                print('The AI win! Sorry but you lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is draw!')
                    break
                else:
                    turn = 'You'

    if not playAgain():
        break

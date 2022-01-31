"""
Tic Tac Toe Player
"""

import math
from time import process_time
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
# Tells us who the current player is (X goes first)
currentPlayer = ""

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    global currentPlayer
    X_count = 0
    O_count = 0
    EMPTY_count = 0

    for row in board:
      X_count += row.count(X)
      O_count += row.count(O)
      EMPTY_count += row.count(EMPTY)

    # If X has more squares than O, its O's turn:
    if X_count > O_count:
      currentPlayer=O
      return O

    # Otherwise it is X's turn:
    else:
      currentPlayer=X
      return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    global currentPlayer
    nBoard = deepcopy(board)
    nBoard[action[0]][action[1]]=currentPlayer
    return nBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if there was a winner anywhere
    rowWinner = checkRows(board)
    columnWinner = checkColumns(board)
    diagonalWinner = checkDiagonals(board)
    # Get the winner
    if rowWinner:
        return  rowWinner
    elif columnWinner:
        return  columnWinner
    elif diagonalWinner:
        return diagonalWinner
    else:
        return  None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    global game_still_going
    # If board is full
    if EMPTY not in board:
        game_still_going = True
    # Else there is no tie
    else:
      game_still_going = False
    return game_still_going

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestVal = -1000
    bestMove = (-1, -1)
 
    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3) :    
        for j in range(3) :
         
            # Check if cell is empty
            if (board[i][j] == EMPTY) :
             
                # Make the move
                board[i][j] = X
 
                # compute evaluation function for this
                # move.
                moveVal = funMinimax(board, 0, False)
 
                # Undo the move
                board[i][j] = EMPTY
 
                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
 
    return bestMove

def funMinimax(board, depth, isMax) :
    score = utility(board)
    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 1) :
        return score
    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -1) :
        return score
    # If there are no more moves and no winner then
    # it is a tie
    if (terminal(board) == False) :
        return 0
 
    # If this maximizer's move
    if (isMax) :    
        best = -1000
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
                # Check if cell is empty
                if (board[i][j]==EMPTY) :
                    # Make the move
                    board[i][j] = X
                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, funMinimax(board,
                                              depth + 1,
                                              not isMax) )
                    # Undo the move
                    board[i][j] = EMPTY
        return best
    # If this minimizer's move
    else :
        best = 1000
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
                # Check if cell is empty
                if (board[i][j] == EMPTY) :
                    # Make the move
                    board[i][j] = O
                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, funMinimax(board, depth + 1, not isMax))
                    # Undo the move
                    board[i][j] = EMPTY
        return best

# Check the rows for a win
def checkRows(board):
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0][0] == board[0][1] == board[0][2] != EMPTY
  row_2 = board[1][0] == board[1][1] == board[1][2] != EMPTY
  row_3 = board[2][0] == board[2][1] == board[2][2] != EMPTY
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0][0] 
  elif row_2:
    return board[1][0] 
  elif row_3:
    return board[2][0]
  # Or return None if there was no winner
  else:
    return None

# Check the columns for a win
def checkColumns(board):
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0][0] == board[1][0] == board[2][0] != EMPTY
  column_2 = board[0][1] == board[1][1] == board[2][1] != EMPTY
  column_3 = board[0][2] == board[1][2] == board[2][2] != EMPTY
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0][0]
  elif column_2:
    return board[0][1] 
  elif column_3:
    return board[0][2] 
  # Or return None if there was no winner
  else:
    return None

# Check the diagonals for a win
def checkDiagonals(board):
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0][0] == board[1][1] == board[2][2] != EMPTY
  diagonal_2 = board[2][0] == board[1][1] == board[2][0] != EMPTY
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0][0] 
  elif diagonal_2:
    return board[2][0]
  # Or return None if there was no winner
  else:
    return None

"""
Tic Tac Toe Player
"""
import random
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
currentPlayer=""

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
    XC = 0
    OC = 0

    for row in board:
      XC += row.count(X)
      OC += row.count(O)
    if XC > OC:
      currentPlayer=O
    else:
      currentPlayer=X
    return currentPlayer

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    listM = set()
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          listM.add((i, j))

    return listM

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nBoard = deepcopy(board)
    nBoard[action[0]][action[1]]=player(board)
    return nBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
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
    if winner(board) or not actions(board):
      return True
    else:
      return False

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
    if terminal(board):
      return None
    if player(board) == 'X':
      bestMove = maximize(board,1)[1]
    else:
      bestMove = minimize(board,-1)[1]
    return bestMove

def maximize(board, bestMin):
      if terminal(board):
        return (utility(board), None)

      bestVal = -1
      bestAction = None
      actionSet = actions(board)

      while len(actionSet) > 0:
        action = random.choice(tuple(actionSet))
        actionSet.remove(action)
        if bestMin <= bestVal:
          break
        minPlayerResult = minimize(result(board, action), bestVal)
        if minPlayerResult[0] > bestVal:
          bestAction = action
          bestVal = minPlayerResult[0]

      return (bestVal, bestAction)

def minimize(board, bestMax):
    if terminal(board):
        return (utility(board), None)

    bestVal = 1
    bestAction = None
    actionSet = actions(board)

    while len(actionSet) > 0:
        action = random.choice(tuple(actionSet))
        actionSet.remove(action)
        if bestMax >= bestVal:
            break
    maxPlayerResult = maximize(result(board, action), bestVal)

    if maxPlayerResult[0] < bestVal:
        bestAction = action
        bestVal = maxPlayerResult[0]

    return (bestVal, bestAction)

def checkRows(board):
    for row in board:
      if row.count(X) == 3:
        return X
      if row.count(O) == 3:
        return O

def checkColumns(board):
    for j in range(3):
        k=0
        l=0
        for i in range(3):
            if(board[i][j]==X):
                k+=1
            elif(board[i][j]==O):
                l+=1

        if k==3:
            return X
        if l==3:
            return O

def checkDiagonals(board):
    j = 2
    k=0
    l=0
    for i in range(3):
        
        if(board[i][i]==X):
            k+=1
        elif(board[i][i]==O):
            l+=1
    if k==3:
        return X
    if l==3:
        return O
    k=0
    l=0

    for i in range(3):
        if(board[i][j]==X):
            k+=1
        elif(board[i][j]==O):
            l+=1
        j -= 1
    if k==3:
        return X
    if l==3:
        return O
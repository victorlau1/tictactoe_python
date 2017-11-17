def main(previous = 0):
  """ Main ticatactoe game

  Args:  
    previous (int): previous game number, starts at 0 if initialize

  Returns:
  
  """

  #Only 2 players
  max_players = [1,2]
  
  #Prompts user to start a game
  while True:
    start_game = str(input('Start Game? (Y/N)? '))
    if start_game.upper() == 'Y' or not start_game.upper() == 'N':
      break
    else:
      print('Only Y/N are allowed. Please Try Again.')
      continue
  
  game_count = 0 + previous
  newGame = Board.matrix
  game = True
  currentPlayer = 0

  print('Starting Game: ', game_count)

  #Game Runs On Loop Until Over
  while(game):
    print('Current Player is Player: ',max_players[currentPlayer])
    print(newGame)
    
    invalidPosition = True


    while(invalidPosition):
      position = inputPosition()
      print(position)
      invalidPosition = existingToken(position, newGame)
      if not invalidPosition:
        print('player ', currentPlayer,' placed at ', position[0], position[1])
        newGame = placeToken(position, newGame, currentPlayer)
        currentPlayer = changePlayer(currentPlayer)
    

  newgame = str(input('Would you like to start a new game?'))
  if newgame.upper() == 'Y':
    main(game_count + 1)
  else:
    sys.exit()

def inputPosition():
  """Handles user input for inputting in positions

    Returns:
      array: returns the array position
  """

  position = [10,10]
  position[0] = int(input('Type the row you would like to place the token: '))
  position[1] = int(input('Type the column you would like to place the token: '))
  return position

def existingToken(positions, board):
  """ Takes positions on the board and the board to evaluate against
    - positions (tuple): x and y position 
    - board (array of array): game board currently played 
  """

  if board[positions[0]][positions[1]] == 0:
    return False 
  else:
    return True

def userInput(x, y):
  """Takes in userinputs and checks board 

  Args:
    x (int): x position on the board
    y (int): y position on the board  
  """
  if newGame[x][y] == 0:
    newGame[x][y] = 1
  else:
    print('Try Again:', player) 

def winner(board):
  """Checks the three helper functions to verify if game is won or to continue
  
  Args:
    board (array of arrays): current game state board (array of arrays)
  """
  game = vertical(board) or horizontal(board) or diagonal(board)
  return game

def diagonal(board):
  """Checks diagonal positional of a 3 x 3 board
    If any position is true (left to right and right to left) it returns true otherwise false
  
  Args:
    board (array): current gamestate board
  """
  if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
    return True
  elif (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    return True
  return False

def vertical(board):
  """Checks vertical positions of the 3 x 3 board
    If any row is contains three of the same, it returns true otherwise false

  Args:
    board (array): current gamestate board
  """
  for i in range(3):
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
      return True
  return False

def horizontal(board):
  """Checks horizontal positions of the 3 x 3 board
     If any column is contains three of the same, it returns true otherwise false

  Args: 
    board (array): array of the current game state

  Returns:
  """
  for i in range(3):
    if (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
      return True
  return False

def changePlayer(currentPlayer):
  """Changes players from currentPlayer to other player
  
  Args:
    currentPlayer (int): currentPlayer 
  
  Returns:
    int: returns other player position
  """

  return int(not currentPlayer)

def createToken(currentPlayer):
  """Returns a token that can be used to placed on the board

  Args:
    currentPlayer (int): current player number 
  Returns:
    token (string): string depending on player number
  """
  
  if currentPlayer == 1:
    token = 'X'
  else:
    token = 'O'
  return token

def placeToken(position, board, currentPlayer):
  """ Places the token within the currentgame state board for current player

  Args:
    currentPlayer (int) : the current player's turn
    board (array) : current game board (array of arrays)
    position (tuple): x and y position
  Return:
    board (array): new board with token placed
  """

  board[position[0]][position[1]] = createToken(currentPlayer)
  return board

class Board():
  """ Creates a brand new board

  """
  matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
  ]

def __init__(self, name):
    self.name = name

if __name__ == '__main__':
  main()

if __name__ == '__main__':
  main()

def main():

  max_players = [1,2]

  while True:
    start_game = input('Start Game? (Y/N)?')
    if start_game.upper() == 'Y' or not start_game.upper() == 'N':
      break
    else:
      print('Only Y/N are allowed')
      continue

  game_count = 0
  newGame = Board(game_count)
  game_count += 1
  currentplayer = 0

  print('Starting Game: ', game_count)

  while(game):
    print('It\'s Player' % (player[currentplayer]))

    game = winner(board)
    

def existingToken(positions, board):
  if board[position[0]][position[1]] != 0:
    return false 
  else:
    return true

def userInput(x, y):
  if newGame[x][y] == 0:
    newGame[x][y] = 1
  else:
    print('Try Again:', player) 

def winner(board):
  game = vertical(board)
  game = horizontal(board)

  return game

def diagonal(board):
  for i in range(2):

def vertical(board):
  for (i in range(3)):
    if (board[0][i] == board[1][i] AND board[1][i] == board[2][i]):
      return true

def horizontal(board):
  for (i in range(3)):
    if (board[i][0] == board[i][1] AND board[i][1] == board[i]array[2]):
      return true


def changePlayer(currentplayer):
  return !currentplayer

def addToken(player):
  if player == 1:
    token = 'x'
  else:
    token = 'O'
  return token

def placeToken(position, board, player):
  if (existingToken(position)):
    board[position[0]][position[1]] = addToken(player)
  else:
    return 'Please Try Again'

  return board

class Board:
  
  matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
  ]

  def __init__(self, name):
    self.name = name
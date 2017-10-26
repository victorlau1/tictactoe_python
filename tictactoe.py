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

  print('Starting Game: ', game_count)

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

class Board:
  
  matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
  ]

  def __init__(self, name):
    self.name = name

def addToken(player):
  if player == 1:
    token = 'x'
  else:
    token = 'O'
  return token

def placeToken(position, board):


  return board

if __name__ == '__main__':
  main()
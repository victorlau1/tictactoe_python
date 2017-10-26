def main():

max_players = [1,2]

  while True:
      start_game = input('Start Game? (Y/N)?')
    if not start_game.upper() !== 'Y' or start_game.upper() !== 'N':
      print('Sorry, only Y/N is allowed')
      continue
    else:
      break

game_count = 0
newGame = Board(GameCount)
game_count += 1

print('Starting Game: ', game_count)

def userInput(x, y):
  if newGame[x][y] === 0:
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
    self.name = name:

if __name__ = '__main__':
  main()
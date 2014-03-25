#Version 1.0.0

def getDisplayBoard(board):
  new = [[-2 for a in range(len(board))] for b in range(len(board[0]))]
  for a in range(len(board)):
    for b in range(len(board[a])):
      new[b][a] = board[a][b]
  return new
      
def printPositions(board):
  new = getDisplayBoard(board)   
  for a in range(len(new)):
    print("Row ",a,": ",new[a])
    
def printSimple(board):
  new = getDisplayBoard(board)
  for a in range(len(new)):
    print(" ".join("%3s" % repr(i) for i in new[a]))
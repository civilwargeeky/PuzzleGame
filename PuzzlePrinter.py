#Version 1.0.0

def printPositions(board):
  new = [[-2 for a in range(len(board))] for b in range(len(board[0]))]
  for a in range(len(board)):
    for b in range(len(board[a])):
      new[b][a] = board[a][b]

    
  for a in range(len(new)):
    print("Row ",a,": ",new[a])
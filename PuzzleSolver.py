#Puzzle Solver
#Version 1.0.0
#Website: http://courses.missouristate.edu/KenVollmar/PummillRelays
import PuzzleReader
import PuzzlePrinter

def coterm(num, range = 4): #Makes so 1-2 = 3, for side handling
  return num%range

dim, pieces = PuzzleReader.init('E:\\Coding\\Puzzle Game\\MediumBoard.txt')
slotNums = range(len(pieces))
nil = PuzzleReader.piece(-1) #All places of this should be copies, but I am not changing it, so it should be fine.
board = [[nil for a in range(dim[1])] for b in range(dim[0])] #Makes a dim[0] x dim[1] board of -1s
print(board)

def getPiece(pos, side):
  return board[pos[0] + (-1*int(side==3)) + int(side==1)][pos[1] + (-1*int(side==0)) + int(side==2)]

def setPos(piece, pos):
  board[pos[0]][pos[1]] = piece
  piece.setPos(pos)

def tryPlace(piece, pos, doRaise = True): #Expects a piece and a pos tuple/list
  print("Trying to place ",piece," at slot ",pos)
  if board[pos[0]][pos[1]] != nil:
    if doRaise: raise AssertionError("tried placing piece "+str(piece.id)+" in slot "+str(pos)) 
    else: return False
  if pos[0] == 0 and not piece.isEdge(3): print("FAIL3"); return False #If on left edge, but left side is not an edge
  if pos[0] == dim[0]-1 and not piece.isEdge(1): print("FAIL1"); return False #right
  if pos[1] == 0 and not piece.isEdge(0): print("FAIL0"); return False #top
  if pos[1] == dim[1]-1 and not piece.isEdge(2): print("FAIL0"); return False #bottom
  setPos(piece, pos)
  return True
  
for i in slotNums: #This should get all the corners
  for a in [0, dim[0]-1]:
    for b in [0, dim[1]-1]:
      tryPlace(pieces[i], [a,b], False)
  """print("Top Left: ",tryPlace(pieces[i], [0,0], False))
  print("Top Right: ",tryPlace(pieces[i], [dim[0]-1,0], False))
  print("Bottom Left: ",tryPlace(pieces[i], [0, dim[1]-1], False))
  print("Bottom Right: ",tryPlace(pieces[i], [dim[0]-1, dim[1]-1], False))
  print("Board: ",board)
  print("-----")"""

counter = 0
  
for a in range(len(board)):
  for b in range(len(board[a])): #b is current board slot
    if board[a][b] != nil: #If this slot already exists
      print("A,B: ",a," ",b," Breaking")
      continue
    for i in slotNums:
      counter += 1
      print("A ",a," B ",b," Piece ", i)
      print(board[a][b])
      input()
      if pieces[i].pos != [-1,-1]: continue
      if pieces[i].getMatch(3) == getPiece([a,b],3).getSide(1):
        if tryPlace(pieces[i], [a,b]): break #Don't need to try other pieces
      if pieces[i].getMatch(0) == getPiece([a,b],0).getSide(2):
        if tryPlace(pieces[i], [a,b]): break
      
print("Count: ",counter)
print(board)
print(board[dim[0]-1])

print("")
print(dim)
PuzzlePrinter.printPositions(board)

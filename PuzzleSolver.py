#Puzzle Solver
#Version 1.0.0
#Website: http://courses.missouristate.edu/KenVollmar/PummillRelays
import PuzzleReader
import sys

#Arguments (and associated error checking)
try:
  VERBOSE = sys.argv[2][0].lower() == "t"
except IndexError:
  VERBOSE = False

def printUsage():
  print("Error in argument usage")
  print("    usage: fileName [t/f verbose]")
try:
  fileName = sys.argv[1]
except IndexError:
  printUsage()
  sys.exit()
  
#Display functions to be used.
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

#Initializing the table of piece objects and other helpful things
try:
  dim, pieces = PuzzleReader.init(fileName)
except FileNotFoundError:
  print("The file you specified does not exist")
  printUsage()
  sys.exit()
slotNums = range(len(pieces))
nil = PuzzleReader.piece(-1) #All places of this should be the same object, but I am not changing it, so it should be fine.
board = [[nil for a in range(dim[1])] for b in range(dim[0])] #Makes a dim[0] x dim[1] board of -1s
#The board is arranged like this: [0][0]  [1][0] [2][0]
#                                 [0][1]  [1][1] [2][1]
#                                 [0][2]  [1][2] [2][2] and so on

#Important puzzle-solving functions
def getPiece(pos, side):
  return board[pos[0] + (-1*int(side==3)) + int(side==1)][pos[1] + (-1*int(side==0)) + int(side==2)]

def setPos(piece, pos):
  board[pos[0]][pos[1]] = piece
  piece.setPos(pos)

def tryPlace(piece, pos, doRaise = True): #Expects a piece and a pos tuple/list
  if VERBOSE: print("Trying to place ",piece," at slot ",pos)
  if board[pos[0]][pos[1]] != nil:
    if doRaise: raise AssertionError("tried placing piece "+str(piece.id)+" in slot "+str(pos)) 
    else: return False
  if pos[0] == 0 and not piece.isEdge(3): return False #If on left edge, but left side is not an edge
  if pos[0] == dim[0]-1 and not piece.isEdge(1): return False #right
  if pos[1] == 0 and not piece.isEdge(0): return False #top
  if pos[1] == dim[1]-1 and not piece.isEdge(2): return False #bottom
  setPos(piece, pos)
  return True

#This finds the top left corner
for i in slotNums:
  if pieces[i].isEdge(0) and pieces[i].isEdge(3):
    tryPlace(pieces[i], [0,0])

#Verbose counter for how many tries there are total
counter = 0
  
for a in range(len(board)):
  for b in range(len(board[a])): #b is current board slot
    if board[a][b] != nil: #If this slot already exists
      if VERBOSE: print("A,B: ",a," ",b," already placed, Breaking")
      continue
    if VERBOSE: printPositions(board); input()
    for i in slotNums:
      if pieces[i].pos != [-1,-1]: continue
      counter += 1
      if VERBOSE: print("A ",a," B ",b," Piece ", i)
      if pieces[i].getMatch(0) == getPiece([a,b],0).getSide(2): #If matches bottom side of top piece
        if tryPlace(pieces[i], [a,b]): break
      if pieces[i].getMatch(3) == getPiece([a,b],3).getSide(1): #If matches right side of left piece
        if tryPlace(pieces[i], [a,b]): break #Don't need to try other pieces

      
if VERBOSE:
  print("\n"*3)
  print("Count: ",counter)
  print(board)

  print("")
  print(dim)
  printPositions(board)

printSimple(board)
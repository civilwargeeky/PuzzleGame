#Puzzle Reader
#Version 1.0.0

#piece order is top, right, bottom, left
jaggiesDefault = 6

class piece:
  jaggies = jaggiesDefault
  #This is so all pieces have the proper number of "Jaggies"
  def classInit(num):
    piece.jaggies = num
    
  #This creates a new piece from a raw string of numbers on seperate lines
  def __init__(self, rawString):
    if rawString == -1:
      linesTab = [-1] * (piece.jaggies**2 + 1)
    else:
      linesTab = [int(a) for a in rawString.splitlines()]
    self.id = linesTab[0] #First line is piece id
    linesTab.pop(0) #The first line is not, however, a match-able jaggie
    self.sides = [ linesTab[piece.jaggies*a:piece.jaggies*(a+1)] for a in range(4)] #More compact: Seperates the list of numbers into individual sides.
    self.edge = [ a == [1] * piece.jaggies for a in self.sides] #Same numbering scheme as sides. true if all numbers on side are 1: This is for ease of use, a list that is true if the specified side is an edge (all 1s)
    self.pos = [-1,-1] #Position in the board, will be set later
  
  #These are so a piece can easily be printed
  def __str__(self):
    return str(self.id)
  def __repr__(self):
    return str(self.id)
    
  #Returns the negation of a side, e.g. the side's "match"
  def getMatch(self, side):
    if not side in range(4): raise ValueError("Improper Side")
    toRet = [a^1 for a in self.sides[side]]
    toRet.reverse()
    return toRet
  
  #Just some getter and setter methods (looks nicer than piece.sides[x])
  def getSide(self, side):
    return self.sides[side]
    
  def isEdge(self, side):
    return self.edge[side]
    
  def setPos(self, pos):
    self.pos = tuple(pos)
        
    
    
#Get data from a file
def getRawData(fileName):
  readObj = open(fileName, "r")
  toRet = readObj.read()
  readObj.close()
  return toRet
  
def init(fileName): #Returns list of dimensions and sides per piece
  text = getRawData(fileName)
  dimensions = [int(i) for i in text.splitlines()[:3]] #This is a list of x dim, y dim, number of "jaggies"
  piece.classInit(dimensions[2]) #Set proper number of jaggies
  pieces = [piece(a) for a in text.split("-1\n")[1:]] #Creates a list of piece objects (the for loop seperates the text into individual pieces.)
  
  return dimensions, pieces
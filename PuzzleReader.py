#Puzzle Reader
#Version 1.0.0

#piece order is top, right, bottom, left
jaggiesDefault = 6

class piece:
  jaggies = jaggiesDefault
  pos = [-1,-1] #Position in the board
  def classInit(num):
    piece.jaggies = num
    
  def __init__(self, rawString):
    if rawString == -1:
      linesTab = [-1] * (piece.jaggies**2 + 1)
    else:
      linesTab = [int(a) for a in rawString.splitlines()]
    self.id = linesTab[0]
    linesTab.pop(0)
    self.sides = [ linesTab[piece.jaggies*a:piece.jaggies*(a+1)] for a in range(4)] #More compact
    self.edge = [ a == [1] * piece.jaggies for a in self.sides] #Same numbering scheme as sides. true if all numbers on side are 1
    
  def __str__(self):
    return str(self.id)
  def __repr__(self):
    return str(self.id)
    
  def getMatch(self, side):
    if not side in range(4): raise ValueError("Improper Side")
    toRet = [a^1 for a in self.sides[side]]
    toRet.reverse()
    return toRet
  
  def getSide(self, side):
    return self.sides[side]
    
  def isEdge(self, side):
    return self.edge[side]
    
  def setPos(self, pos):
    self.pos = tuple(pos)
        
    
    

def getRawData(fileName):
  readObj = open(fileName, "r")
  toRet = readObj.read()
  readObj.close()
  return toRet
  
def init(fileName): #Returns list of dimensions and sides per piece
  text = getRawData(fileName)
  toRet = [int(i) for i in text.splitlines()[:3]] #This is a list of x dim, y dim, number of "jaggies"
  piece.classInit(toRet[2]) #Set proper number of jaggies
  pieces = [piece(a) for a in text.split("-1\n")[1:]] #Creates a list of piece objects (the for loop seperates the text into individual pieces.)
  
  return toRet, pieces
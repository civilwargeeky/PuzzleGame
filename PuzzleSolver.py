#Puzzle Solver
#Version 1.0.0
#Website: http://courses.missouristate.edu/KenVollmar/PummillRelays
import PuzzleReader

def coterm(num, range = 4) #Makes so 1-2 = 3, for side handling
  return num%range

dim, pieces = PuzzleReader.init("SmallBoard.txt")


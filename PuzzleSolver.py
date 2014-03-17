#Puzzle Solver
#Version 1.0.0
#Website: http://courses.missouristate.edu/KenVollmar/PummillRelays
import PuzzleReader

dim, pieces = PuzzleReader.init("SmallBoard.txt")
print(pieces[3].sides)
print(pieces[3].isEdge[2])
for a in range(len(pieces)):
  print("-----")
  print(pieces[3].sides[3])
  print(pieces[a].getMatch(1))
  if pieces[a].getMatch(1) == pieces[3].sides[3]: print("!!!!!!!!!")

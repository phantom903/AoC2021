from aoc import *
from queue import Queue

class DayFifteen:

  mem = []
  grid = []

  def __init__(self, mem):
    self.mem = [[int(x) for x in line] for line in mem]

  def getAdj(self, current):
    res = []
    locX = [1, 0]
    locY = [0, 1]
    lowPoint = True
    for i in range(2):
      row, col = current[0] + locX[i], current[1] + locY[i]
      if row >= 0 and row < len(mem[0]) and col >= 0 and col < len(mem):
        res.append((row,col))
    return res

  def findPath(self, start, end):
    checked = set()
    toCheck = Queue()
    path = [[x for x in line] for line in self.mem]
    toCheck.put(start)
    while toCheck.qsize() != 0:
      current = toCheck.get()
      checked.add(current)
      adj = self.getAdj(current)
      if len(adj) == 1:
        toCheck.put(adj[0])
      else:
        if manhattan(adj[0], end) == manhattan(adj[1], end):
          toCheck.put(adj[0])
          toCheck.put(adj[1])
        elif manhattan(adj[0], end) > manhattan(adj[1], end):
          toCheck.put(adj[1])
        else:
          toCheck.put(adj[0])
    return(path)

  def printBoard(self, mem):
    for line in mem:
      print(''.join([str(i) for i in line]))
    print('============')
    return

  def partOne(self):
    start = (0,0)
    end = (len(self.mem[0])-1, len(self.mem)-1)
    path = self.findPath(start, end)
    # for (x, y) in path:
    #   print(self.mem[x][y])
    # return sum(self.mem[x][y] for (x,y) in path)
    self.printBoard(path)

  def partTwo(self):
    pass
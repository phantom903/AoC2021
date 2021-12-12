from aoc import *
from queue import Queue

class DayNine:

  mem = []

  def __init__(self, mem):
    self.mem = [[int(i) for i in memLine] for memLine in mem]
    self.lowPoints = set()

  def getNeighbs(self, x, y):
    locX = [1, 0, -1, 0]
    locY = [0, 1, 0, -1]
    lowPoint = True
    for i in range(4):
      row, col = x + locX[i], y + locY[i]
      if row >= 0 and row < len(self.mem[0]) and col >= 0 and col < len(self.mem):
        if self.mem[row][col] <= self.mem[x][y]:
          lowPoint = False
    return lowPoint

  def partOne(self):
    lowSum = 0
    for x in range(len(self.mem[0])):
      for y in range(len(self.mem)):
        if self.getNeighbs(x, y):
          lowSum += 1 + self.mem[x][y]
          self.lowPoints.add((x,y))
    return lowSum

  def partTwo(self):
    basins = set()
    for lowPoint in self.lowPoints:
      cavern = Queue()
      visited = set()
      cavern.put(lowPoint)
      visited.add(lowPoint)
      while not cavern.empty():
        current = cavern.get()
        for next in neighbours(current, self.mem):
          x, y = next
          if (x, y) not in visited and self.mem[x][y] != 9:
            cavern.put((x,y))
            visited.add((x,y))      
      basins.add(len(visited))
    return(basins)
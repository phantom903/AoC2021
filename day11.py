from aoc import *

class DayEleven:

  mem = []

  def __init__(self, mem):
    self.mem = [[int(i) for i in line] for line in mem]

  def cycle(self):
    for x in range(len(self.mem[0])):
      for y in range(len(self.mem)):
        self.mem[x][y] += 1
    return
  
  def flash(self):
    flashCoords = set()
    for x in range(len(self.mem[0])):
      for y in range(len(self.mem)):
        if self.mem[x][y] == 10:
          flashCoords.add((x, y))
    for row, col in flashCoords:
      self.flashOcto(row, col)
    return
  
  def flashOcto(self, x, y):
    for next in neighbours((x, y), self.mem):
      row, col = next
      self.incr(row, col)
    return
  
  def incr(self, x, y):
    self.mem[x][y] += 1
    if self.mem[x][y] == 10:
      self.flashOcto(x, y)

  def cleanUp(self):
    count = 0
    for x in range(len(self.mem[0])):
      for y in range(len(self.mem)):
        if self.mem[x][y] > 9:
          self.mem[x][y] = 0
          count += 1
    return count
  
  def printBoard(self):
    for line in self.mem:
      print(''.join([str(i) for i in line]))
    print('============')
    return

  def step(self):
    self.cycle()
    self.flash()
    self.printBoard()
    return self.cleanUp()

  def partOne(self, runs=10):
    return sum(self.step() for _ in range(0, runs))


  def partTwo(self):
    pass
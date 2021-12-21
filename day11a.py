from aoc import *
from queue import SimpleQueue

class DayEleven:

  mem = []
  count = 0
  flashing = SimpleQueue()

  def __init__(self, mem):
    self.mem = [[int(i) for i in line] for line in mem]
  
  def printBoard(self):
    for line in self.mem:
      print(''.join([str(i) for i in line]))
    print('============')
    return
  
  def cycle(self):
    for x in range(len(self.mem[0])):
      for y in range(len(self.mem)):
        self.mem[x][y] += 1
        if self.mem[x][y] >9:
          self.flashing.put((x, y))
    return

  def partOne(self, runs):
    for i in range(0, runs):
      self.cycle()
      while self.flashing.qsize() > 0:
        (nextX, nextY) = self.flashing.get()
        if self.mem[nextX][nextY] > 9:
          self.count += 1
          self.mem[nextX][nextY] = 0
          for x, y in neighbours((nextX, nextY), self.mem.copy(), True):
            if self.mem[x][y] != 0:
              self.mem[x][y] += 1
            if self.mem[x][y] > 9:
              self.flashing.put((x, y))
      if sum(sum(a) for a in self.mem) == 0:
        print(f"Synchronized: {i+1}")
        self.printBoard()
        break
    return self.count


  def partTwo(self):
    return self.partOne(1000)
    
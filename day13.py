from aoc import *
from queue import Queue
from operator import itemgetter

class DayThirteen:

  mem = set()
  folds = []

  def __init__(self, instr):
    i = 0
    while instr[i] != '':
      x, y = instr[i].split(',')
      self.mem.add((int(x), int(y)))
      i += 1
    i += 1
    for j in range(i, len(instr)):
      self.folds.append(instr[j].strip("fold along ").split('='))

  def doFold(self, steps):
    for i in range(steps):
      axis = self.folds[i][0]
      val = int(self.folds[i][1])
      remCoords = Queue()
      addCoords = Queue()
      if axis == 'x':
        for coord in self.mem:
          (x, y) = coord
          if x > val:
            remCoords.put(coord)
            addCoords.put((val-(x-val) , y))
      else:
         for coord in self.mem:
          (x, y) = coord
          if y > val:
            remCoords.put(coord)
            addCoords.put((x, val-(y-val)))
    while remCoords.qsize() != 0:
      self.mem.remove(remCoords.get())   
    while addCoords.qsize() != 0:
      self.mem.add(addCoords.get())
    return

  def displayMem(self):
    printOut = [['.' for x in range(max(self.mem, key=itemgetter(1))[1]+1)] for y in range(max(self.mem, key=itemgetter(0))[0]+1)]
    for (x, y) in self.mem:
      printOut[x][y] = '#'
    for line in range(len(printOut)):
      output = ''.join(printOut[line])
      print(output)
    return

  def partOne(self):
    self.doFold(1)
    return(len(self.mem))

  def partTwo(self): # I don't know why this works (not counting fudged orientation of letters) instead of just running doFold len(self.folds) times
    for i in range(len(self.folds)-1):
      self.folds.remove(self.folds[0])
      self.doFold(1)
      print("step " + str(i) + ' ' + str(max(self.mem, key=itemgetter(1))[1]+1))
    self.displayMem()
    return
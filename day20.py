from aoc import *
from collections import defaultdict

class DayTwenty:

  algo = ''
  image = defaultdict(lambda: 0)
  startX, startY, width, height = 0, 0, 0, 0

  def __init__(self, mem):
    self.algo = ''.join(['1' if x == '#' else '0' for x in mem[0]])
    self.width = len(mem[2])
    self.height = len(mem)-2
    for x in range(len(mem[2])):
      for y in range(2, len(mem)):
        if mem[y][x] == '#':
          self.image[(x, y-2)] = 1

  # def padMem(self, mem):
  #   newMem = [['.' for x in range(len(mem[0])+4)] for y in range(len(mem)+4)]
  #   for x in range(2, len(newMem[0])-2):
  #     for y in range(2, len(newMem)-2):
  #       newMem[y][x] = mem[y-2][x-2]
  #   return newMem

  def getCode(self, x, y):
    locs = [
      (-1,-1), (0,-1), (1,-1),
      (-1, 0), (0, 0), (1, 0),
      (-1, 1), (0, 1), (1, 1)
    ]
    code = []
    for loc in locs:
      newX, newY = loc
      code.append(str(self.image[(x+newX, y+newY)]))
    binCode = ''.join(code)
    return(int(binCode, 2))

  def inImage(self, coord):
    (x, y) = coord
    if (x in [self.startX, self.startX+1, self.startX + self.width-1, self.startX + self.width]) or (y in [self.startY, self.startY+1, self.startY + self.height-1, self.startX + self.height]):
      return(False)
    else:
      return(True)

  def step(self, isOdd):
    newImage = dict()
    for x in range(self.startX, self.width):
      for y in range(self.startY, self.height):
        if self.algo[self.getCode(x, y)] == '1':
          newImage[(x,y)] = 1
    self.image.clear()
    self.image.update(newImage)
    # for coord in self.image:
    #   if not self.inImage((coord)):
    #     if isOdd != 0:
    #       self.image[coord] = 0
    #     else:
    #       self.image[coord] = 1

  def prettyPrint(self):
    newImage = defaultdict(lambda: 0)
    newImage.update(self.image)
    board = [['.' for x in range(self.width)] for y in range(self.height)]
    for x in range(self.width):
      for y in range(self.height):
        if newImage[(x+self.startX,y+self.startY)]:
          board[y][x] = '#'
    printBoard(board)

  def partOne(self):
    bitFlip = {'0':'1','1':'0'}
    for i in range(2):
      self.startX -= 2
      self.startY -= 2
      self.width += 4
      self.height += 4
      self.step(i % 2)
      self.algo = bitFlip[self.algo[0]] + self.algo[1:len(self.algo)-1] + bitFlip[self.algo[-1]]
    self.prettyPrint()
    return(len(self.image))

  def partTwo(self):
    pass
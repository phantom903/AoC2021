from aoc import *
from queue import LifoQueue

class DayTen:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.lefts = ['(','[','{','<']
    self.rights = [')',']','}','>']
    self.scores = [3,57,1197,25137]
    self.incLines = set()
    self.p2scores = {')': 1, ']': 2, '}': 3, '>': 4}
  
  def getIdx(self, c):
    if c in self.rights:
      return list(self.rights).index(c)
    elif c in self.lefts:
      return list(self.lefts).index(c)

  def ordTrans(self, c):
    if c in ['>','}',']']:
      return str(ord(c) - 2)
    else:
      return str(ord(c) - 1)

  def partOne(self):
    totErrs = 0
    mem = self.mem.copy()
    for line in mem:
      lineOrig = line
      lineAfter = 0
      lineStart = len(line)
      while lineStart != lineAfter:
        lineStart = len(line)
        line = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
        lineAfter = len(line)
      lineAfter = 0
      lineStart = len(line)
      while lineStart != lineAfter:
        lineStart = len(line)
        line = line.replace('(', '').replace('[', '').replace('{', '').replace('<', '')
        lineAfter = len(line)
      if line and line[0] in self.rights:
        totErrs += self.scores[self.getIdx(line[0])]
      elif not line:
        self.incLines.add(list(self.mem).index(lineOrig))
    return totErrs


  def partTwo(self):
    mem = [self.mem[i] for i in self.incLines]
    masterScores = set()
    for line in mem:
      runningScore = 0
      lineOrig = line
      lineAfter = 0
      lineStart = len(line)
      while lineStart != lineAfter:
        lineStart = len(line)
        line = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
        lineAfter = len(line)
      secondHalf = list(line[::-1])
      for i in range(len(secondHalf)):
        secondHalf[i] = self.rights[self.getIdx(secondHalf[i])]
      for i in secondHalf:
        runningScore = runningScore * 5
        runningScore += self.p2scores[i]
      masterScores.add(runningScore)
    return(sorted(masterScores)[int(((len(masterScores)-1)/2)+.5)])
from aoc import *

class DayEight:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    for i in range(len(self.mem)):
      self.mem[i] = self.mem[i].split(' | ')
      for j in range(len(self.mem[i])):
        self.mem[i][j] = self.mem[i][j].split(' ')
  
  def partOne(self):
    sumDigs = 0
    for i in range(len(self.mem)):
      for j in range(len(self.mem[i][1])):
        if len(self.mem[i][1][j]) in [2, 3, 4, 7]:
          sumDigs += 1
    return sumDigs

  def partTwo(self):
    sumDigs = 0
    for i in range(len(self.mem)):
      codes = dict()
      result = [0,0,0,0]
      for j in range(len(self.mem[i][0])):
        digit = set(self.mem[i][0][j])
        digLength = len(digit)
        if digLength == 2:
          codes[1] = digit
        elif digLength == 3:
          codes[7] = digit
        elif digLength == 4:
          codes[4] = digit
        elif digLength == 7:
          codes[8] = digit
      fourDiff = codes[4] - codes[1]
      for j in range(len(self.mem[i][0])):
        digit = set(self.mem[i][0][j])
        digLength = len(digit)
        if digLength == 5 and digit.issuperset(codes[1]):
          codes[3] = digit
        elif digLength == 5 and digit.issuperset(fourDiff):
          codes[5] = digit
        elif digLength == 5:
          codes[2] = digit
        elif digLength == 6 and digit.issuperset(codes[4]):
          codes[9] = digit
        elif digLength == 6 and digit.issuperset(fourDiff):
          codes[6] = digit
        elif digLength not in [2,3,4,7]:
          codes[0] = digit
      for j in range(len(self.mem[i][1])):
        digit = set(self.mem[i][1][j])
        for k,v in codes.items():
          if v == digit:
            result[j] = k
      result = [str(i) for i in result]
      result = int("".join(result))
      sumDigs += result
    return sumDigs
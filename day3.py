from aoc import *

class DayThree:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.gamma = ""
    self.epsilon = ""

  def partOne(self):
    counters = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(self.mem)-1):
      for l in range(len(self.mem[i])):
        if self.mem[i][l] == '0': 
          counters[l] -= 1
        else:
          counters[l] += 1
    for i in counters:
      if i >= 0:
        self.gamma += '1'
        self.epsilon += '0'
      else:
        self.gamma += '0'
        self.epsilon += '1'
    return int(self.gamma, 2) * int(self.epsilon, 2)

  def partTwo(self):
    # oxy = self.mem.copy()
    # co2 = self.mem.copy()
    # curDig = []

    # while len(oxy > 2):
    #   curDig = 
        
    
    # return int(oxy[0],2) * int(co2[0], 2)
    pass
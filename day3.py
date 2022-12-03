from aoc import *

class DayThree:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.gamma = ""
    self.epsilon = ""
    self.counters = [0,0,0,0,0,0,0,0,0,0,0,0]

  def parseMem(self, mem):
    self.counters = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(mem)):
      for l in range(len(mem[i])):
        if mem[i][l] == '0': 
          self.counters[l] -= 1
        else:
          self.counters[l] += 1

  def partOne(self):
    self.parseMem(self.mem)
    for i in self.counters:
      if i >= 0:
        self.gamma += '1'
        self.epsilon += '0'
      else:
        self.gamma += '0'
        self.epsilon += '1'
    return int(self.gamma, 2) * int(self.epsilon, 2)

  def partTwo(self):
    oxy = self.mem.copy()
    co2 = self.mem.copy()
    i = 0
    while len(oxy) > 1:
      critBit = '1' if self.counters[i] >= 0 else '0'
      oxy = [item for item in oxy if item[i] == critBit]
      i += 1
      self.parseMem(oxy)
    i = 0
    while len(co2) > 1:
      critBit = '0' if self.counters[i] >= 0 else '1'
      co2 = [item for item in co2 if item[i] == critBit]
      i += 1
      self.parseMem(co2)   
    return int(oxy[0], 2) * int(co2[0], 2)
        
    
    # return int(oxy[0],2) * int(co2[0], 2)
    pass
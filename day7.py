from aoc import *
import statistics, math

class DaySeven:

  mem = []

  def __init__(self, mem):
    self.mem = [int(i) for i in mem[0].split(',')]

  def partOne(self):
    #crabPoint = max(set(self.mem), key=self.mem.count)
    crabPoint = round(statistics.median(self.mem))
    fuelUsed = sum([abs(i - crabPoint) for i in self.mem])
    return fuelUsed

  def partTwo(self):
    crabPoint = math.floor(statistics.mean(self.mem))
    fuelUsed = sum([sum(range(abs(max(i, crabPoint)-min(i, crabPoint)+1))) for i in self.mem])
    return fuelUsed
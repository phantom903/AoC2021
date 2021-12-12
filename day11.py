from aoc import *

class DayEleven:

  mem = []

  def __init__(self, mem):
    self.mem = [[int(i) for i in line] for line in mem]

  def partOne(self):
    print(self.mem)

  def partTwo(self):
    pass
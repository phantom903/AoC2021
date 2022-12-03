from aoc import *

class DayFour:

  mem = []
  calls = []
  boards = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.calls = self.mem[0].split(',')
    self.boards = self.mem[1:].split('\n\n')

  def partOne(self):
    print(self.calls)
    print(self.boards)

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(4)
  dayFour = DayFour(y)
  print('Day Four part one : ', dayFour.partOne())
  print('Day Four part two : ', dayFour.partTwo())
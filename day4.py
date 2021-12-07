from aoc import *

class DayFour:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.calls = []
    self.boards = []

  def partOne(self):
    self.calls = self.mem.pop(0)
    numBoards = int(len(self.mem)-1)
    board = []
    boards = []
    for i in range(1, numBoards):
      if self.mem[i] == '':
        boards.append(board)
        board.clear()
      else:
        board.append([int(i) for i in self.mem[i].split(' ')])
    print(boards)
  def partTwo(self):
    pass
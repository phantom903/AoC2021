from aoc import *

class DayFour:

  mem = []
  calls = []
  boards = []
  scores = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.calls = [int(x) for x in self.mem[0].split(',')]
    board = []
    for line in mem[2:]:
      if line in (None, '', '\n\n'):
        self.boards.append(board)
        board = []
      else:
        board.append([int(x) for x in line.split()])
    self.boards.append(board)

  def checkBoard(self, board):
    for call in self.calls:
      for line in board:
        if call in line:
          k = line.index(call)
          board[board.index(line)][k] = -1
          if (len(set(line)) == 1) or (len(set([board[i][k] for i in range(len(board))])) == 1):
            return ((self.calls.index(call) + 1), call * sum([sum([x for x in lines if x != -1]) for lines in board]))

  def runBoards(self):
    self.scores = [self.checkBoard(board) for board in self.boards]
    self.scores.sort(key=lambda x: x[0])

  def partOne(self):
    self.runBoards()
    return self.scores[0][1]

  def partTwo(self):
    return self.scores[-1][1]

if __name__ == "__main__":
  y = fileOpenLines(4)
  dayFour = DayFour(y)
  print('Day Four part one : ', dayFour.partOne())
  print('Day Four part two : ', dayFour.partTwo())
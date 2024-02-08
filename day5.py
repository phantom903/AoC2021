from aoc import *

class DayFive:
  
  lines = []
  plots = []

  def __init__(self, mem):
    for line in mem:
      start, end = line.split(' -> ')
      start = [int(i) for i in start.split(',')]
      end = [int(i) for i in end.split(',')]
      self.lines.append((start, end))

  def plotLine(self, line):
    start, end = line
    plot = []
    for x in range(start[0], end[0]+1):
      for y in range(start[1], end[1]+1):
        plot.append((x,y))
    self.plots.append(plot)


  def partOne(self):
    total = 0
    for i in self.lines:
      if (i[0][0] == i[1][0]) or (i[1][0] == i[1][1]):
         self.plotLine(i)
    for i in range(len(self.plots)):
      for j in range(i +1, len(self.plots)):
        if set(self.plots[i]).intersection(set(self.plots[j])):
          total += 1
    return total


  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(5)
  dayFive = DayFive(y)
  print('Day Five part one : ', dayFive.partOne())
  print('Day Five part two : ', dayFive.partTwo())
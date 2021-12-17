from aoc import *

class DayTwelve:

  caves = dict()
  visited = set()
  paths = 0

  def __init__(self, mem):
    keys = set()
    for line in mem:
      for i in line.split('-'):
        keys.add(i)
    for key in keys:
      conns = set()
      for line in mem:
        c1, c2 = line.split('-')
        if c1 == key:
          conns.add(c2)
        elif c2 == key:
          conns.add(c1)
      self.caves[key] = conns

  def getNeighbours(self, cave):
    for i in self.caves[cave]:
     yield i

  def traverse(self, cave, visited):
    print(cave)
    if cave == 'end':
      self.paths += 1
    else:
      for next in self.getNeighbours(cave):
        if next not in visited:
          if not next.isupper() and next != 'end':
            visited.add(next)
          self.traverse(next, visited)  

  def partOne(self):
    self.traverse('start', set())
    return self.paths

  def partTwo(self):
    pass
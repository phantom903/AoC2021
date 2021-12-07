from aoc import *

class DayTwo:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    cmds = self.mem.copy()
    x, y = 0, 0
    for i in range(len(cmds)):
      cmds[i] = cmds[i].split(' ')
    for cmd in cmds:
      if cmd[0] == 'forward':
        x += int(cmd[1])
      elif cmd[0] == 'up':
        y -= int(cmd[1])
      elif cmd[0] == 'down':
        y += int(cmd[1])
    return x * y

  def partTwo(self):
    cmds = self.mem.copy()
    x, y, aim = 0, 0, 0
    for i in range(len(cmds)):
      cmds[i] = cmds[i].split(' ')
    for cmd in cmds:
      if cmd[0] == 'forward':
        x += int(cmd[1])
        y += int(cmd[1]) * aim
      elif cmd[0] == 'up':
        aim -= int(cmd[1])
      elif cmd[0] == 'down':
        aim += int(cmd[1])
    return x * y
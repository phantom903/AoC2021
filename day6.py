from aoc import *
import collections

class DaySix:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def simFish(self, days):
    initState = ints(self.mem[0])
    fishes = dict.fromkeys(range(0,9),0)
    spawns = 0
    for i in initState:
      fishes[i] += 1
    for i in range(days):
      for idx in range(0,8):
        if idx == 0:
          spawns = fishes[idx]
        fishes[idx] = fishes[idx + 1]
      fishes[6] += spawns
      fishes[8] = spawns
      spawns = 0
    return sum(fishes.values())

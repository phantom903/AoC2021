from aoc import *
from collections import Counter
import string

class DayFourteen:
#   mem = []
#   codes = dict()
#   polymerCode = ''
#   polymer = dict()

#   def __init__(self, mem):
#     self.polymerCode = mem[0]
#     keys = set()
#     for i in range(len(self.polymerCode) -1):
#       keys.add(str(self.polymerCode[i] + self.polymerCode[i+1]))
#     self.polymer = dict.fromkeys([i for i in keys], 1)
#     self.codes = {k:v for (k, v) in [line.split(' -> ') for line in mem[2:]]}

#   def simPolymer(self, days):
#     elemNums = {}
#     for i in range(days):
#       newComps = set()
#       for comp in self.polymer:
#         newComps.add(str(comp[0] + self.codes[comp]))
#         newComps.add(str(self.codes[comp] + comp[1]))
#         print(newComps)
#       for comp in newComps:
#         if comp in self.polymer.keys():
#           self.polymer[comp] += 1
#         else:
#           self.polymer[comp] = 1
#       print(self.polymer)
#     for i in self.polymer.keys():
#       for j in list(i):
#         if j in elemNums.keys():
#           elemNums[j] += self.polymer[i]
#         else:
#           elemNums[j] = self.polymer[i]
#     print(elemNums)
#     # print(self.polymer)
#     return (max(elemNums.values())/2 - min(elemNums.values())/2)
  codes = dict()
  polymerCode = ''
  pairs = []

  def __init__(self, mem):
    self.polymerCode = mem[0].strip()
    self.pairs = [''.join(p) for p in zip(self.polymerCode, self.polymerCode[1:])]
    self.codes = [rule.split(' ') for rule in mem[2:]]
    self.codes = {a: (a[0]+c,c+a[1]) for a,b,c in self.codes}

  def simPolymer(self, runs):
    ctr = Counter(self.pairs)
    for i in range(runs):
      newCtr = {key : 0 for key in self.codes.keys()}
      for k, v in ctr.items():
        newCtr[self.codes[k][0]] += v
        newCtr[self.codes[k][1]] += v
      ctr = newCtr
    letterTotals = {letter : 0 for letter in list(string.ascii_uppercase)}
    for k, v in ctr.items():
      letterTotals[k[0]] += v
    letterTotals[self.polymerCode[-1]] += 1
    return max(letterTotals.values()) - min([val for val in letterTotals.values() if val > 0])

        

      
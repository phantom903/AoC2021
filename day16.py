from aoc import *

class DaySixteen:

  mem = ''

  def __init__(self, mem):
    rawData = bytes.fromhex(mem[0])
    for byte in rawData:
      self.mem += format(byte, '08b')
    print(self.versID(self.mem))
    print(self.typeID(self.mem))
    print(self.lengthVal(self.mem))

  def versID(self, packet):
    ver = packet[0:3]
    return(int(ver, 2))
  
  def typeID(self, packet):
    tid = packet[3:6]
    return(int(tid, 2))
  
  def lengthVal(self, packet):
    if packet[7] == '0':
      return(int(packet[7:22], 2))


  def partOne(self):
    pass

  def partTwo(self):
    pass
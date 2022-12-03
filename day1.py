class DayOne():

  def partOne(self, depths):
    incrs = 0
    for i in range(len(depths)-1):
      if depths[i] < depths[i+1]:
        incrs += 1
    return incrs

  def partTwo(self, depths):
    incrs = 0
    for i in range(0, len(depths)-3, 1):
      runTot = depths[i] + depths[i+1] + depths[i+2]
      nextTot = depths[i+1] + depths[i+2] + depths[i+3]
      if nextTot > runTot:
        incrs += 1
    return incrs
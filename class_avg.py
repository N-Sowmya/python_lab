marks=[6,8,3,5,9,0,6,5]
import numpy as np
npMarks=np.array(marks)
print("Above average in class :",np.max(npMarks))
print("Below average in class :",np.min(npMarks))
print("Average in class :",np.mean(npMarks))
print(npMarks)
print(np.where(npMarks>5,"Above average",
      np.where(npMarks<5,"Below Average","Average")))

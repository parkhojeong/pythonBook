import math
def mean(list):
    return sum(list)/len(list)

def standardDeviation(list):
    dSum = 0
    m = mean(list)
    for num in list:
        dSum += (num-m)**2
    return math.sqrt(dSum/len(list))

file = open("Scores.txt")
list = [eval(line.rstrip()) for line in file]
m = mean(list)
s = standardDeviation(list)
print("Number of scores:{}".format(len(list)))
print("Average score:{}".format(m))
print("Standard deviation of scores:{0:.2f}".format(s))
print("GRADE DISTRIBUTION AFTER CURVING GRADES.")
gradeDict = {"A":0,"B":0,"C":0,"D":0,"F":0}
for num in list:
    if num >= m+1.5*s:
        gradeDict["A"]= gradeDict["A"]+1
    elif num >= m+ 0.5*s:
        gradeDict["B"] = gradeDict["B"] + 1
    elif num >= m - 0.5 * s:
        gradeDict["C"] = gradeDict["C"] + 1
    elif num >= m- 1.5*s:
        gradeDict["D"] = gradeDict["D"] + 1
    else:
        gradeDict["F"] = gradeDict["F"] + 1

print("A:{0:<10}B:{1:<10}C:{2:<10}D:{3:<10}F:{4:<10}"
      .format(gradeDict["A"],gradeDict["B"],gradeDict["C"],gradeDict["D"],gradeDict["F"]))


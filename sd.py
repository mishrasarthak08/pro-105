import csv
import math

file = open("data.csv",newline = "")
reader = csv.reader(file)

filedata = list(reader)

data = filedata[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total + int(i)

    mean = total / n 
    return mean

squaredlist = []
for i in data:
    a = int(i)-mean(data)
    a = a**2
    squaredlist.append(a)

sum = 0
for i in squaredlist:
    sum = sum+i  

result = sum/(len(data)-1)

standarddeviation = math.sqrt(result)

print(standarddeviation)
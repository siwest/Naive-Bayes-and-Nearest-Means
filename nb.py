# Nearest means algorithm
# Input:
# 1. Data matrix of dimension n by m (n rows and m columns)
# 2. Training labels L. Each label li is an integer indicating the class that row i belongs to.

# Algorithm:
# 1. Training:
#	 a. Initialize the mean mj of each class to the vector of all 1's (not 0's). These are pseudocounts to avoid zero variance.
#	 b. Compute mean mj of each class by adding each datapoint to mj and dividing by number of datapoints
# 2. Prediction: Assign point x'i to class j if x'i is closest to the mean of class j normalized by standard deviation.

import sys
import math

datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

# Read Data
while (l != ''):
	a = l.split()
	l2 = []
	for j in range (0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()

# Read Labels
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()
while (l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1

# Compute means
m0 = []
sd0 = []

for j in range(0, cols, 1):
	m0.append(1)
	sd0.append(0)

m1 = []
sd1 = []

for j in range(0, cols, 1):
	m1.append(1)
	sd1.append(0)


for i in range(0, rows, 1):
		if (trainlabels.get(i) != None and trainlabels[i] == 0):
			for j in range(0, cols, 1):
				m0[j] = m0[j] + data[i][j]
		if (trainlabels.get(i) != None and trainlabels[i] == 1):
			for j in range(0, cols, 1):
				m1[j] = m1[j] + data[i][j]
for j in range(0, cols, 1):
	m0[j] = m0[j] / n[0]
	m1[j] = m1[j] / n[1]


# print(m0)
# print(m1)


# Get std deviation sd0 and sd1
for i in range (0, rows, 1):
	for j in range (0, cols, 1):
		if (trainlabels.get(i) != None and trainlabels[i] == 0):
			sd0[j] += (data[i][j] - m0[j])**2
		if (trainlabels.get(i) != None and trainlabels[i] == 1):
			sd1[j] += (data[i][j] - m1[j])**2
for j in range(0, cols, 1):
	sd0[j] = math.sqrt(sd0[j] / (n[0] - 1))
	sd1[j] = math.sqrt(sd1[j] / (n[1] - 1))

# print ("Print sd")
# print sd0
# print sd1


# Classify unlabeled points, normalized by std deviation
for i in range ( 0, rows, 1):
	if (trainlabels.get(i) == None):
		d0 = 0
		d1 = 0
		for j in range (0, cols, 1): # should do sqr root, technically
			d0 = d0 + ( (m0[j] - data[i][j]) / sd0[j] )**2
			d1 = d1 + ( (m1[j] - data[i][j]) / sd1[j] )**2

		if (d0 < d1):
			print("0 {id}".format(id=i))
		else:
			print("1 {id}".format(id=i))

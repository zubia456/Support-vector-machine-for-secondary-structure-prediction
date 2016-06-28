import numpy
import sys
import re
import neurolab as nl

training = open('nnTraining.txt', 'r').readlines()
trainingIN =[]
trainingOUT = []
for line in training:
	tokens = line.rstrip().split()
	nextIn = [float(x) for x in tokens[3:]]
	trainingIN.append(nextIn)
	nextOut = [float(x) for x in tokens[:3]]
	trainingOUT.append(nextOut)
#inputs = [ [-1.0, 1.0] for j in range( 0, 3 ) ]
#net = neurolab.net.newff( inputs, [10,18,3] )
#net.trainf = neurolab.train.train_rprop
#net.train( trainingIN, trainingOUT, show=10 )

#net = nl.load('final_network')# topology[10,3]
net = nl.load('final_network2') #topology[10,18,3]
Validation = open('nnvalidation.txt', 'r').readlines()
ValidationIN =[]
ValidationOUT = []
for line in Validation:
	tokens = line.rstrip().split()
	nextIn = [float(x) for x in tokens[3:]]
	ValidationIN.append(nextIn)
	nextOut = [float(x) for x in tokens[:3]]
	ValidationOUT.append(nextOut)
res = net.sim(ValidationIN)
j =0
predicted =[]
while j in range(0, len(res)):
	predicted.append([1.0 if x == res[j].max() else -1.0 for x in res[j]])
	j+=1
tp = 0
tn =0
fp =0
fn =0
j=0
while j in range(0, len(predicted)):
	for x, y in zip(range(0,len(ValidationOUT[j])), range(0,len(predicted[j]))):
	             if ValidationOUT[j][x] == 1.0 and predicted[j][y]== 1.0:
	                    tp +=1
	             if ValidationOUT[j][x] == -1.0 and predicted[j][y]== -1.0:
	                    tn +=1
	             if ValidationOUT[j][x] == -1.0 and predicted[j][y]== 1.0:
	                    fp +=1
	             if ValidationOUT[j][x] == 1.0 and predicted[j][y]== -1.0:
	                    fn +=1
	j +=1 
sum = tp + tn
total = tp +tn + fp + fn
accuracy = sum/float(total)

print "\taccuracy = %f" %(accuracy)



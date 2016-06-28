import sys
import re
import random

seqData = {}

fHTr = open( 'H.training', 'w' )
fETr = open( 'E.training', 'w' )
fCTr = open( 'C.training', 'w' )

fHVa = open( 'H.validation', 'w' )
fEVa = open( 'E.validation', 'w' )
fCVa = open( 'C.validation', 'w' )

training = {'H':fHTr, 'E':fETr, 'C':fCTr }
validation = {'H':fHVa, 'E':fEVa, 'C':fCVa }


lines = open('rs126.txt', 'r').readlines()

for line in lines:
	line = re.sub( r'[\s\n]+$', '', line )
	
	if line.startswith('>') :
		ID = line[1:]
		seqData[ID] = []
		sequence = ''
		structure = None
		continue
		
	if structure == None :
		sequence += line
		
		if sequence.endswith('*') :
			sequence = sequence[:-1]
			seqData[ID].append( sequence )
			structure = ''
	else :
		structure += line
		
		if structure.endswith('*') :
			structure = structure[:-1]
			seqData[ID].append( structure )
	
aaOrder = 'ARNDCEQGHILKMFPSTWYVX'

aaToIndex = {}

idx = 1

for aa in aaOrder :
	aaToIndex[aa] = idx 
	idx += 1

	
		
for ID in seqData :
	sequence, structure = seqData[ID]
	
	lth = len(sequence)
	sequence = 'XXXXX' + sequence + 'XXXXX'
	
	for i in range(5,5 + lth) :
		window = sequence[i-5:i+6]
		ss = structure[i-5] ## NOTE: the -5 compensates for the XXXXX added to the sequence
		if ss == 'T' : ss = 'C'
		##print 'ID:%s\t%s\t%s' % (ID, ss, window)
		
		vector = ''
		
		for w in range(0,11) :
			aa = window[w]
			if aa not in aaToIndex :
				vector = ''
				break
			idx = aaToIndex[window[w]] + w*21
			v = '\t%d:1' % idx
			vector += v
			
		if vector != '' : 
			if random.random() < 0.8 :
				## Write to training
				for t in training :
					if t != ss :
						training[t].write( '-1.0\t' + vector + '\n' )
					else :
						training[t].write( '+1.0\t' + vector + '\n' )
			else :
				#Write to validation
				for t in validation :
					if t != ss :
						validation[t].write( '-1.0\t' + vector + '\n' )
					else :
						validation[t].write( '+1.0\t' + vector + '\n' )
			

		
		
		

	

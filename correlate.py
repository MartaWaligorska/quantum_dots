import numpy as np
import matplotlib.pyplot as plt
import sys, getopt 
import pylab as pl

# jakies zmiany

def corr(x,y):
	result = np.correlate(x, y, mode='full')
	return result#[result.size/2:]
def corrS(x,y):
	result = np.correlate(x, y, mode='same')
	return result

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
			opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	#print 'Input file is "', inputfile
	#print 'Output file is "', outputfile
 
 
	# Read data
	f = open (inputfile, "rt")
	l = f.readline()
	on = []
	off = []
	while l:
		va = l.split()
		on.append(float(va[0]))
		off.append(float(va[1]))
		l = f.readline()
	

	pl.figure(1)
	pl.subplot(3,1,1)
	pl.ylabel('on-on correlation')
	ac = corr(on,on)
	print ac
	
	plt.plot(ac)
	pl.subplot(3,1,2)
	pl.ylabel('off-off correlation')
	ac = corr(off,off)
	plt.plot(ac)
	pl.subplot(3,1,3)
	pl.ylabel('on-off correlation')
	ac = corrS(on,off)
	plt.plot(ac)
	
	
	on2=[]
	for i in range(len(on)):
		on2.append((on[i])-np.mean(on))
	off2=[]
	for i in range(len(off)):
		off2.append((off[i])-np.mean(off))
	
	pl.figure(2)
	pl.subplot(3,1,1)
	pl.ylabel('on-on correlation')
	ac = corr(on2,on2)
	plt.plot(ac)
	pl.subplot(3,1,2)
	pl.ylabel('off-off correlation')
	ac = corr(off2,off2)
	plt.plot(ac)
	pl.subplot(3,1,3)
	pl.ylabel('on-off correlation')
	ac = corr(on,off)
	plt.plot(ac)
	plt.show()
	
if __name__ == "__main__":
   main(sys.argv[1:])
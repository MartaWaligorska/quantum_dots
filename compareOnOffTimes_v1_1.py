from math import *
from random import *
import pylab as pl
import numpy as np
import sys, getopt


# Import files
#import genPL_v0_1 as gPL
import fitPL_v0_1 as fPL
import plotPLcomp_v0_1 as pPL
#import plotPL1_v0_1 as pPL1

def main(argv):
	inputfile = ''
	#outputfile = ''
	try:
		#opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
		opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
	except getopt.GetoptError:
		#print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			#print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		#elif opt in ("-o", "--ofile"):
			#outputfile = arg

	# data
	f = open (inputfile, "rt")
	#print inputfile
	l = f.readline()
	on = []
	off = []
	while l:
		va = l.split()
		on.append(float(va[0]))
		off.append(float(va[1]))
		l = f.readline()

	## simulate
	#x = gPL.randht(nsim,'powerlaw',alpha);

	# fit
	[alphaON, xminON, LON] = fPL.plfit(on)
	[alphaOFF, xminOFF, LOFF] = fPL.plfit(off)
	#print alpha
	#print xmin
	#print L

	# print
	#pl.figure(1)
	#pl.subplot(1,2,1)
	#pl.plot(x,'g*')
	#pl.subplot(1,2,2)
	#pl.hist(x, 100)
	#pl.savefig('../tmp/Raw-data.png')

	pl.figure(2)
	#pl.subplot(1,2,1)
	#h1 = pPL1.plplot(x,xmin,alpha)
	#textstr = '$a =%.2f$\n $xmin=%.2f$\n $L=%.2f$'%(alpha, xmin, L)
	#pl.text(0.05, 0.95, textstr, fontsize=14, verticalalignment='top')
	#pl.subplot(1,2,2)
	h = pPL.plplot(on,xminON,alphaON,'g-')
	h = pPL.plplot(off,xminOFF,alphaOFF,'r-')

	pl.savefig('../tmp/Fits.png')
	
	#pl.show()

if __name__ == "__main__":
	main(sys.argv[1:])
from math import *
from random import *
import pylab as pl
import numpy as np
import sys, getopt
from scipy import optimize

# Import files
import genPL_v0_1 as gPL
import fitPL_v0_1 as fPL
import plotPL_v1_1 as pPL
import plotPL1_v1_1 as pPL1

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

	#calculate histogram and logs
	hist_off, bins_off = np.histogram(off,20)
	loghist_off = np.log10(hist_off)
	logbins_off = np.log10(bins_off)

	# define our (line) fitting function
	fitfunc = lambda p, x: p[0] + p[1] * x
	errfitfunc = lambda p, x, y: fitfunc(p,x) - y
	# Define function for calculating a power law
	powerlaw = lambda x, amp, index: amp * (x**index)
	
	pl.plot(logbins_off[:-1], loghist_off)
	pinit = [1., -1.]
	
	out = optimize.leastsq(errfitfunc, pinit, args=(logbins_off[:-1],loghist_off))
	pfinal = out[0]
	covar = out[1]
	print pfinal
	print covar

	index = pfinal[1]
	amp = 10.0**pfinal[0]
	print amp
	#indexErr = sqrt( covar[0][0] )
	#ampErr = sqrt( covar[1][1] ) * amp

	pl.clf()
	pl.subplot(2, 1, 1)
	pl.plot(bins_off[:-1], powerlaw(bins_off[:-1], amp, index))     # Fit
	pl.errorbar(bins_off[:-1], loghist_off, fmt='k.')  # Data
	pl.text(5, 6.5, 'Ampli = %5.2f' % (amp))
	pl.text(5, 5.5, 'Index = %5.2f' % (index))
	pl.title('Best Fit Power Law')
	pl.xlabel('X')
	pl.ylabel('Y')
	#pl.xlim(1, 11)

	pl.subplot(2, 1, 2)
	pl.loglog(bins_off[:-1], powerlaw(bins_off[:-1], amp, index))
	pl.errorbar(bins_off[:-1], loghist_off, fmt='k.')  # Data
	pl.xlabel('X (log scale)')
	pl.ylabel('Y (log scale)')
	#pl.xlim(1.0, 11)

	pl.savefig('power_law_fit.png')






## OLD print-----------------------------------------------
	## print
	#pl.figure(1)
	#pl.subplot(1,2,1)
	#pl.plot(on,'g*')
	#pl.subplot(1,2,2)
	#pl.hist(on, 100)
	#pl.savefig('../tmp/Raw-on.png')

	#pl.figure(2)
	#pl.subplot(1,2,1)
	#h1 = pPL1.plplot(on,xminON,alphaON,'on time')
	#textstr = '$a =%.2f$\n $xmin=%.2f$\n $L=%.2f$'%(alphaON, xminON, LON)
	#pl.text(0.05, 0.95, textstr, fontsize=14, verticalalignment='top')
	#pl.subplot(1,2,2)
	#h = pPL.plplot(on,xminON,alphaON,'on time','ro', 'k--')
	#pl.savefig('../tmp/Fits-on.png')
	
	#pl.figure(3)
	#pl.subplot(1,2,1)
	#pl.plot(off,'g*')
	#pl.subplot(1,2,2)
	#pl.hist(off, 100)
	#pl.savefig('../tmp/Raw-off.png')

	#pl.figure(4)
	#pl.subplot(1,2,1)
	#h1 = pPL1.plplot(off,xminOFF,alphaOFF,'off time')
	#textstr = '$a =%.2f$\n $xmin=%.2f$\n $L=%.2f$'%(alphaOFF, xminOFF, LOFF)
	#pl.text(0.05, 0.95, textstr, fontsize=14, verticalalignment='top')
	#pl.subplot(1,2,2)
	#h = pPL.plplot(off,xminOFF,alphaOFF,'off time','g*', 'k--')
	#pl.savefig('../tmp/Fits-off.png')
	##pl.show()

	#pl.figure(5)
	#h = pPL.plplot(on,xminON,alphaON,'times','r-', 'k--')
	#h = pPL.plplot(off,xminOFF,alphaOFF,'times','g-', 'k--')

	#pl.savefig('../tmp/comp.png')
	pl.show()
if __name__ == "__main__":
	main(sys.argv[1:])
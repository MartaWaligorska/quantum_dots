import pylab as pl
import numpy as np
import sys, getopt
import matplotlib.mlab as mlab
from gaussfitter_v0_1 import multigaussfit
from gaussfitter_v0_1 import n_gaussian

def n_gausses(pars=None,a=None,dx=None,sigma=None):
    """
    Returns a function that sums over N gaussians, where N is the length of
    a,dx,sigma *OR* N = len(pars) / 3

    The background "height" is assumed to be zero (you must "baseline" your
    spectrum before fitting)

    pars  - a list with len(pars) = 3n, assuming a,dx,sigma repeated
    dx    - offset (velocity center) values
    sigma - line widths
    a     - amplitudes
    """
    if len(pars) % 3 == 0:
        a = [pars[ii] for ii in xrange(0,len(pars),3)]
        dx = [pars[ii] for ii in xrange(1,len(pars),3)]
        sigma = [pars[ii] for ii in xrange(2,len(pars),3)]
    elif not(len(dx) == len(sigma) == len(a)):
        raise ValueError("Wrong array lengths! dx: %i  sigma: %i  a: %i" % (len(dx),len(sigma),len(a)))

    def g(x):
        v = np.zeros((len(dx), len(x)))
        for i in range(len(dx)):
            v[i] = a[i] * np.exp( - ( x - dx[i] )**2 / (2.0*sigma[i]**2) )
        return v
    return g

def plot_fits(hist_x, hist_y, n_gauss, pars):
  	# plot histogram and fits
	# histogrm
	pl.plot(hist_x[:-1], hist_y)
	# multigauss fit line
	pl.plot(hist_x[:-1],n_gauss)
	# Gauss components
	comp = n_gausses(pars=pars)(hist_x[:-1])
	for i in range(len(comp)):
	  pl.plot(hist_x[:-1], comp[i],'r--')
    
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
	time = []
	counts = []
	while l:
		va = l.split()
		time.append(float(va[0]))
		counts.append(float(va[1]))
		l = f.readline()

	## calculate histogram
	## now determine nice limits by hand:
	binwidth = 1
	xmax = np.max(np.fabs(time))
	ymax = np.max(np.fabs(counts))

	bins = np.arange(-0.5, ymax + binwidth-0.5, binwidth)
	hist_y, hist_x = np.histogram(counts, bins=bins)#, normed = True
	
	print "2 Gauss fit"
	(pars,n_gauss,errors, chii) =  multigaussfit(hist_x[:-1],hist_y,ngauss=2, params=[1500,320,30, 300,720,30])
	print  chii/len(counts)
	# add a 'best fit' line
	pl.subplot(2,3,1)
	plot_fits(hist_x, hist_y, n_gauss, pars)
	
	print "3 Gauss fit"
	(pars,n_gauss,errors, chii) =  multigaussfit(hist_x[:-1],hist_y,ngauss=3, params=[1500,320,30, 200,400,30, 300,720,30])
	pl.subplot(2,3,2)
	plot_fits(hist_x, hist_y, n_gauss, pars)
	print  chii/len(counts)
	
	print "4 Gauss fit"
	(pars,n_gauss,errors, chii) =  multigaussfit(hist_x[:-1],hist_y,ngauss=4, params=[1500,320,30, 200,400,30, 200,500,30, 300,720,30])
	pl.subplot(2,3,3)
	plot_fits(hist_x, hist_y, n_gauss, pars)
	print  chii/len(counts)
	
	print "5 Gauss fit"
	(pars,n_gauss,errors, chii) =  multigaussfit(hist_x[:-1],hist_y,ngauss=5, params=[1500,320,30, 200,400,30, 200,500,30, 200,600,30, 300,720,30])
	pl.subplot(2,3,4)
	plot_fits(hist_x, hist_y, n_gauss, pars)
	print  chii/len(counts)
	
	print "6 Gauss fit"
	(pars,n_gauss,errors, chii) =  multigaussfit(hist_x[:-1],hist_y,ngauss=5, params=[200,250,30, 1500,320,30, 200,400,30, 200,500,30, 200,600,30, 300,720,30])
	pl.subplot(2,3,5)
	plot_fits(hist_x, hist_y, n_gauss, pars)
	print  chii/len(counts)
	
	pl.show()

if __name__ == "__main__":
	main(sys.argv[1:])
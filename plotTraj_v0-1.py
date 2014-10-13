import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import sys, getopt

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



	# data
	f = open (inputfile, "rt")
	l = f.readline()
	x = []
	y = []
	y1 = []

	while l:
		va = l.split()
		x.append(float(va[0]))
		y.append(float(va[1]))
		l = f.readline()

	nullfmt   = NullFormatter()         # no labels

	# definitions for the axes
	left, width = 0.05, 0.75
	bottom, height = 0.1, 0.8
	bottom_h = left_h = left+width+0.02

	rect_scatter = [left, bottom, width, height]
	rect_histy = [left_h, bottom, 0.15, height]

	# start with a rectangular Figure
	plt.figure(1, figsize=(15,3))

	axScatter = plt.axes(rect_scatter)
	axHisty = plt.axes(rect_histy)

	# no labels
	axHisty.yaxis.set_major_formatter(nullfmt)

	# the scatter plot:
	axScatter.plot(x, y,'-')

	# now determine nice limits by hand:
	binwidth = 1
	xmax = np.max(np.fabs(x))
	ymax = np.max(np.fabs(y))

	axScatter.set_xlim( (0, xmax) )
	axScatter.set_ylim( (0, ymax) )

	bins = np.arange(0, ymax + binwidth, binwidth)
	axHisty.hist(y, bins=bins, orientation='horizontal')

	axHisty.set_ylim( axScatter.get_ylim() )

	plt.savefig('../trajsPLOT/' + outputfile)
	#plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])

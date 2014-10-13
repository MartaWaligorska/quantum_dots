#!/bin/bash

#-----------------------
# Last mod: 17.07.14

#This script calculates the on-off times with different thresholds set.
# Script uses the SciLab script "ON_OFF_times.sce"

# As a result:
# -the text files with ON and OFF times are generated 
# -the text files with tresholds values are genetarted (table redy to paste into .tex file)

# input folder: 'trajsTXT'
# output folders: 'on_off_times', 'thresh'

#MW, 11.07.2014
#-----------------------

i=0
cd ptu
for filename in *.ptu
do
	file=${filename:0:-4}
	((i = $i+1))
	echo "I am working on file #" $i
	echo ".. Clculating on-off times"
	cp ../trajsTXT/$file--0-1.txt ../tmp/trajectory.txt
	scilab -nwni -f ../ON_OFF_times_v1_1.sce
	cp ../tmp/on-off_times_thresh-1.txt ../on_off_times/$file--0-1-on-off_times_thresh-1.txt
	cp ../tmp/on-off_times_thresh-2--1-3.txt ../on_off_times/$file--0-1-on-off_times_thresh-2--1-3.txt
	cp ../tmp/on-off_times_thresh-2--1-5.txt ../on_off_times/$file--0-1-on-off_times_thresh-2--1-5.txt
# 	cp ../tmp/on_times_thresh-1.txt ../on_off_times/$file--0-1-on_times_thresh-1.txt
# 	cp ../tmp/on_times_thresh-2--1-3.txt ../on_off_times/$file--0-1-on_times_thresh-2--1-3.txt
# 	cp ../tmp/on_times_thresh-2--1-5.txt ../on_off_times/$file--0-1-on_times_thresh-2--1-5.txt
	cp ../tmp/thresholds.txt ../thresh/$file--0-1-thresh.txt
	
	cp ../trajsTXT/$file--0-01.txt ../tmp/trajectory.txt
	scilab -nwni -f ../ON_OFF_times_v1_1.sce
	cp ../tmp/on-off_times_thresh-1.txt ../on_off_times/$file--0-01-on-off_times_thresh-1.txt
	cp ../tmp/on-off_times_thresh-2--1-3.txt ../on_off_times/$file--0-01-on-off_times_thresh-2--1-3.txt
	cp ../tmp/on-off_times_thresh-2--1-5.txt ../on_off_times/$file--0-01-on-off_times_thresh-2--1-5.txt
# 	cp ../tmp/on_times_thresh-1.txt ../on_off_times/$file--0-01-on_times_thresh-1.txt
# 	cp ../tmp/on_times_thresh-2--1-3.txt ../on_off_times/$file--0-01-on_times_thresh-2--1-3.txt
# 	cp ../tmp/on_times_thresh-2--1-5.txt ../on_off_times/$file--0-01-on_times_thresh-2--1-5.txt
	cp ../tmp/thresholds.txt ../thresh/$file--0-01-thresh.txt
	
	cp ../trajsTXT/$file--0-001.txt ../tmp/trajectory.txt
	scilab -nwni -f ../ON_OFF_times_v1_1.sce
	cp ../tmp/on-off_times_thresh-1.txt ../on_off_times/$file--0-001-on-off_times_thresh-1.txt
	cp ../tmp/on-off_times_thresh-2--1-3.txt ../on_off_times/$file--0-001-on-off_times_thresh-2--1-3.txt
	cp ../tmp/on-off_times_thresh-2--1-5.txt ../on_off_times/$file--0-001-on-off_times_thresh-2--1-5.txt
# 	cp ../tmp/on_times_thresh-1.txt ../on_off_times/$file--0-001-on_times_thresh-1.txt
# 	cp ../tmp/on_times_thresh-2--1-3.txt ../on_off_times/$file--0-001-on_times_thresh-2--1-3.txt
# 	cp ../tmp/on_times_thresh-2--1-5.txt ../on_off_times/$file--0-001-on_times_thresh-2--1-5.txt
	cp ../tmp/thresholds.txt ../thresh/$file--0-001-thresh.txt
done
# # rm 1.txt
# # rm 2.txt
echo "Done, are you glad? Have a nice day!"
# 	file=${filename:0:-4}

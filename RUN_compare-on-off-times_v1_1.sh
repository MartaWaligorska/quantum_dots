#!/bin/bash

#------------------------
# This script prepres the plots and fits of the ON and OFF times distributions
# As the parmeterr the input file (ON or OFF times) are given

# input folder: 'on_off_times'
# output folder: 'on_off_plots's
#------------------------

i=0
cd on_off_times
for filename in *on-off*
do
	file=${filename:0:-4}
	((i = $i+1))
	echo "I am working on file #" $i ": " $filename
	python ../compareOnOffTimes_v1_1.py -i ../on_off_times/$filename
	cp ../tmp/Fits.png ../on_off_comp/$file'-comp.png'
# 	cp ../tmp/Raw-data.png ../on_off_plots/$file'-data.png'
# 	rm ../tmp/Fits.png
# 	rm ../tmp/Raw-data.png
done

cd ..
# rm trajsTXT/tmp.txt

echo "Done, are you glad? Have a nice day!"


#!/bin/bash

#------------------------
# This script prepres the plots and fits of the ON and OFF times distributions
# As the parmeterr the input file (ON or OFF times) are given

# input folder: 'on_off_times'
# output folder: 'on_off_plots's
#------------------------

i=0
cd on_off_times
for filename in *.txt
do
	file=${filename:0:-4}
	((i = $i+1))
	echo "I am working on file #" $i ": " $filename
	python ../fitANDplot_on-off-times_v1_1.py -i ../on_off_times/$filename
	cp ../tmp/Fits-on.png ../on_off_plots/$file'-fits-on.png'
	cp ../tmp/Raw-on.png ../on_off_plots/$file'-data-on.png'
	cp ../tmp/Fits-off.png ../on_off_plots/$file'-fits-off.png'
	cp ../tmp/Raw-off.png ../on_off_plots/$file'-data-off.png'
	cp ../tmp/comp.png ../on_off_plots/$file'-comp.png'
	rm ../tmp/*.png
done

cd ..
rm trajsTXT/tmp.txt

echo "Done, are you glad? Have a nice day!"


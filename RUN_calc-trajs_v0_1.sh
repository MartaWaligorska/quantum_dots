#!/bin/bash

#---------------------------
# Last mod: 11.07.14

# This script clcultes the trjectories with the given bin size (in seconds)

# Executes the C++ progrmme "calcTrjs", as a parameter the trajectory bin size has to be given!
# The C++ programme is based on the one downloded from PicoQunt, in the output file some aditional ('string') 
#   information are given, the file hs to be "clened" to remove the text from the pure trajectory

# The final file is two-column:
# time & counts\\
#input folder: 'ptu'
#output folder: 'trjsTXT'

# At the end the python script ('plot.pl') is executed to drw the fluorescence trjectory and save it to the file
# As parameters, the name of the trajectory file (input) nd the name of the plot file (output) are given. 
#input folder: 'trjsTXT'
#output folder: 'plots'

# MW 11.07.2014
#----------------------------

#---TO_DO--------

# * automatize the bin size (loop!)

#----------------


set -e #errors
i=0
cd ptu
for filename in *.ptu
do
	file=${filename:0:-4}
	((i = $i+1))
	echo "I am working on file #" $i
	echo ".. Calculating the trajectory"
	../ReadIATandCalcTrajs_v0_2 $file.ptu ../trajsTXT/tmp.txt 0.1
	echo ".... Cleaning files" 
	sed '/[a-zA-Z]/d' ../trajsTXT/tmp.txt > 1.txt
	sed -e '/^\ *$/d' 1.txt > 2.txt
	sed '/'-'/d' 2.txt > ../trajsTXT/$file--0-1.txt
	echo "...... Plotting the trajectories"
	python ../plotTraj_v0-1.py -i ../trajsTXT/$file--0-1.txt -o $file--0-1.png

	../ReadIATandCalcTrajs_v0_2 $file.ptu ../trajsTXT/tmp.txt 0.01
	echo ".... Cleaning files" 
	sed '/[a-zA-Z]/d' ../trajsTXT/tmp.txt > 1.txt
	sed -e '/^\ *$/d' 1.txt > 2.txt
	sed '/'-'/d' 2.txt > ../trajsTXT/$file--0-01.txt
	echo "...... Plotting the trajectories"
	python ../plotTraj_v0-1.py -i ../trajsTXT/$file--0-01.txt -o $file--0-01.png

		../ReadIATandCalcTrajs_v0_2 $file.ptu ../trajsTXT/tmp.txt 0.001
	echo ".... Cleaning files" 
	sed '/[a-zA-Z]/d' ../trajsTXT/tmp.txt > 1.txt
	sed -e '/^\ *$/d' 1.txt > 2.txt
	sed '/'-'/d' 2.txt > ../trajsTXT/$file--0-001.txt
	echo "...... Plotting the trajectories"
	python ../plotTraj_v0-1.py -i ../trajsTXT/$file--0-001.txt -o $file--0-001.png
	
done

rm 1.txt
rm 2.txt
cd ..

echo "Done, are you glad? Have a nice day!"

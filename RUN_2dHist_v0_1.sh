#!/bin/bash


set -e #errors
i=0
cd trajsTXT
for filename in *.txt
do
	file=${filename:0:-4}
	((i = $i+1))
	echo "I am working on file #" $i ':' $filename
	python ../2dHistInt.py -i $filename
	cp ../tmp/int2dHist.png ../int_analysis/$file-int2dHist.png
done

rm 1.txt
rm 2.txt
cd ..

echo "Done, are you glad? Have a nice day!"

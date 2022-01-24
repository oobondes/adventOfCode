#!/bin/bash
#default set up if no options are given
day=1
pyfile="day${day}.py"
infile="day$day.txt"

#
while getopts 'd:ft' flag; do
	case "$flag" in
		d) day="${OPTARG}" #sets which days script to run and to run part 1 with puzzle input if no other arguments are given 
			pyfile="day${day}.py"
			infile="day$day.txt";;
       		f) pyfile="day${day}_f.py" ;; #sets puzzle part 2 to run
   		t) infile="day${day}-test.txt" ;; #sets test input to be used so the answer can be validated.
	esac
done

echo $pyfile
echo $infile
python3 $pyfile $infile

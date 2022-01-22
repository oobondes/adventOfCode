#!/bin/bash
day=1

while getopts 'd:ft' flag; do
	case "$flag" in
		d) day="${OPTARG}" 
			pyfile="day${day}.py"
			infile="day$day.txt";;
       		f) pyfile="day${day}_f.py" ;;
   		t) infile="day${day}-test.txt" ;;
	esac
done

echo $pyfile
echo $infile
python3 $pyfile $infile

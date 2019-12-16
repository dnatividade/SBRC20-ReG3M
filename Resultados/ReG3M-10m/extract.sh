#/bin/bash

for ((i=0; i<33;i++));
do
	cat ReG3M-10m-33x.csv |grep "General-$i-" >> ReG3M-$i.csv
done

exit 0


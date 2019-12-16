#/bin/bash

for ((i=0; i<33;i++));
do
	cat broadcast-5m-33x.csv |grep "General-$i-" >> broadcast-$i.csv
done

exit 0


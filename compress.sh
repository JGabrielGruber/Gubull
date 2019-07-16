#!/bin/bash

DIRS=`ls -l ./ | egrep '^d' | awk '{print $9}'`;

for DIR in $DIRS; do
	FILENAME=$DIR/*.jpg;
	convert -resize 1200x1200 $FILENAME $FILENAME;
done;

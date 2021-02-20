#!/bin/bash
mkdir $2

cd $2

for (( i=1; i <= 172; ++i ))
do
    . "../transf.sh" "$1/$i.html"

done

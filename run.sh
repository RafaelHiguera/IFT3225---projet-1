#!/bin/bash
mkdir -p $2
cp extractorNoSol.py $2
cp extractorSol.py $2
cd $2

for (( i=1; i <= 172; ++i ))
do
    . "../transf.sh" "$1/$i.html"

done
rm -f extractorNoSol.py
rm -f extractorSol.py

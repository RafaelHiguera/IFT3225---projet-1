#!/bin/bash
htmlPage=$1
pageNumber=${htmlPage//[!0-9]/}
newPageWithoutSolution="noSol$pageNumber.html"
newPageWithSolution="sol$pageNumber.html"
py extractorNoSol.py $htmlPage $pageNumber > $newPageWithoutSolution
py extractorSol.py $htmlPage $pageNumber > $newPageWithSolution

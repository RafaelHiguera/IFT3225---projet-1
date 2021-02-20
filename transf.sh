#!/bin/bash
htmlPage=$1
pageNumber=${htmlPage//[!0-9]/}
newPageWithoutSolution="noSol$pageNumber.html"
newPageWithSolution="sol$pageNumber.html"
echo La page html est: $htmlPage, le numero est $pageNumber et le dir current est $PWD
python extractorNoSol.py $htmlPage $pageNumber > $newPageWithoutSolution
python extractorSol.py $htmlPage $pageNumber > $newPageWithSolution

# Erreur de chemin A Revoir TODO



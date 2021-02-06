#!/bin/bash
htmlPage=$1
pageNumber=${htmlPage//[!0-9]/}
newPage="template$pageNumber.html"
py extractor.py $htmlPage $pageNumber > $newPage

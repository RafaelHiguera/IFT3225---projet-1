import sys
import random
import string
from bs4 import BeautifulSoup

testPage = sys.argv[1]
pageNumber = sys.argv[2]
templatePage = "templateSol.html"

with open(testPage) as file:
    soup = BeautifulSoup(file, 'html.parser')
    css = soup.select(".rules")[0].get_text()
    html = soup.select(".rules")[1].get_text()
    htmlText = soup.select(".testText")[0]

with open(templatePage) as file:
    soup = BeautifulSoup(file, 'html.parser')
    tempCss = soup.select(".css")[0]
    tempHtml = soup.select(".html")[0]
    tempSolution = soup.select(".solution")[0]
    previousRef = soup.find(id="previous")
    nextRef = soup.find(id="next")

tempCss.insert(0, css)
tempHtml.insert(0, html)
tempSolution.insert(0, htmlText)
soup.style.insert(0 ,css)

# this part make sure to insert the next and previous links to the others tests
if(pageNumber != '1'):
    previousRef['href'] = "noSol" + str(int(pageNumber) - 1) + ".html"

if(pageNumber != '172'):
    nextRef['href'] = "noSol" + str(int(pageNumber) + 1) + ".html"



print(soup.prettify())

import sys
from shutil import copyfile
from bs4 import BeautifulSoup
testPage = sys.argv[1]
pageNumber = sys.argv[2]
templatePage = "template.html"

with open(testPage) as file:
    soup = BeautifulSoup(file, 'html.parser')
    css = soup.select(".rules")[0].get_text()
    html = soup.select(".rules")[1]
    htmlText = soup.select(".testText")[0]

with open(templatePage) as file:
    soup = BeautifulSoup(file, 'html.parser')
    tempCss = soup.select(".css")[0]
    tempHtml = soup.select(".html")[0]
    tempSolution = soup.select(".solution")[0]

tempCss.insert(0, css)
tempHtml.insert(0, html)
tempSolution.insert(0, htmlText)

print(soup.prettify())

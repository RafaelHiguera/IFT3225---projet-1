import sys
import random
import string
from bs4 import BeautifulSoup

# This function takes a string and between > < puts random characters
def scrambleText(text):
    openingParenthisisFlag = 0;
    result = "";
    spaceFlag = False
    for i in range(0, len(text)):
        if text[i] == ' ' or text[i] == '\n':
            spaceFlag = True
        elif text[i] == '<':
            openingParenthisisFlag += 1
        elif text[i] == '>':
            openingParenthisisFlag -= 1
            result += '>'
            continue

        if openingParenthisisFlag == 0 and spaceFlag == False:
            result += random.choice(string.ascii_letters);
        else:
            result += text[i]
        spaceFlag = False
    return result


testPage = sys.argv[1]
pageNumber = sys.argv[2]
templatePage = "templateNoSol.html"

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
    previousRef = soup.find(id="previous")
    nextRef = soup.find(id="next")
    solutionRef = soup.find(id="solution")

tempCss.insert(0, css)
tempHtml.insert(0, scrambleText(html.get_text()))
tempSolution.insert(0, BeautifulSoup(scrambleText(str(htmlText)), "html.parser"))

# this part make sure to insert the next and previous links to the others tests
if(pageNumber != '1'):
    previousRef['href'] = "noSol" + str(int(pageNumber) - 1) + ".html"

if(pageNumber != '172'):
    nextRef['href'] = "noSol" + str(int(pageNumber) + 1) + ".html"

solutionRef['href'] = "sol" + pageNumber + ".html"

print(soup.prettify())

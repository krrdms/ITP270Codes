import sqlite3

# https://docs.python.org/3/library/sqlite3.html

con = sqlite3.connect('Mozilla-Data/cookies.sqlite')
cur = con.cursor()
conn = sqlite3.connect('Mozilla-Data/places.sqlite')
curr = conn.cursor()


def get_cookies():
    rows = cur.execute("SELECT name, host, value, path, expiry, lastaccessed FROM moz_cookies").fetchall()
    for row in rows:
        print('\nName:' + str(row[0]) + '\n' + 'Host:' + str(row[1]) + '\n' + 'Value:' + str(row[2]))
        print('\nPath:' + str(row[3]) + '\n' + 'Expiry:' + str(row[4]))
        print('\nLast Accessed: ' + str(row[5]))


def get_bookmarks():
    curr.execute('SELECT moz_bookmarks.title, moz_places.url FROM moz_places, moz_bookmarks WHERE moz_places.id = moz_bookmarks.fk')
    rows = curr.fetchall()
    print("Bookmarks")
    for row in rows:
        print('\033[1mTITLE:\033[0m ' + '\033[4m' + str(row[0]) + '\033[0m' + '\n' + '\033[1mURL:\033[0m ' + str(row[1]))

def get_history():
    curr.execute('SELECT moz_places.url, moz_places.title, moz_historyvisits.visit_date FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id')
    row = curr.fetchall()
    print('HISTORY')
    print('\nTitle: ' + str(row[0]) + '\n' + 'URL: ' + str(row[1]) + '\n' + 'Visit Date: ' + str(row[2]))

while True:
    x = int(input('\n\033[1m1: Get Cookies\n2: Get Bookmarks\n3: Get History\n\nEnter what You would like to see:\033[0m '))
    if x == 1:
        cookies = get_cookies()
        print(cookies)
        continue
    if x == 2:
        get_bookmarks()
        continue
    if x == 3:
        get_history()
        continue
    else:
        break

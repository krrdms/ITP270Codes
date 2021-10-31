import sqlite3
import time
import datetime


def get_cookies():
    sqlite_file = 'Mozilla-Data/cookies.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT name, host, value, path, expiry, lastAccessed FROM moz_cookies')
    rows = c.fetchall()
    print("[+] - COOKIES")
    for row in rows:
        print('(-): name:' + str(row[0]) + ' host:' + str(row[1]) + ' value:' + str(row[2]))
        print('\t(+): path:' + str(row[3]) + ' expiry:' + str(row[4]))
        print('\t(+): lastAccessed:' + time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(row[5])))


def get_bookmarks():
    sqlite_file = 'Mozilla-Data/places.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT moz_places.url, moz_bookmarks.title FROM moz_places,moz_bookmarks WHERE moz_places.id = moz_bookmarks.fk')
    rows = c.fetchall()
    print("[+] - BOOKMARKS")
    for row in rows:
        print('(+) url:' + str(row[0]) + ' title:' + str(row[1]))


def get_history():
    sqlite_file = 'Mozilla-Data/places.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT moz_places.title, moz_places.url, moz_historyvisits.visit_date FROM moz_places,moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id')
    rows = c.fetchall()
    print("[+] - HISTORY")
    for row in rows:
        print('(+) title:' + str(row[0]) + ' url:' + str(row[1]) + ' visit date:' + str(row[2]))


get_cookies()
get_bookmarks()
get_history()
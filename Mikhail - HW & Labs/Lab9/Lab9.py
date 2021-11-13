import sqlite3
import datetime

# con = sqlite3.connect('mydatabase.db')
# cursorObj = con.cursor()
# cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')
# data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
# cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
# con.commit()

conn = sqlite3.connect('Cars.db')

curr = conn.cursor()  # get a cursor
# create the table
curr.execute(
    'CREATE TABLE IF NOT EXISTS Cars (ID INT PRIMARY KEY NOT NULL, MAKE TEXTX, MODEL TEXT, YEAR TEXT, COLOR TEXT, LICENSEPLATE TEXT)')
# insert the data
curr.execute(""" INSERT INTO Cars VALUES (1, 'Chevrolet', 'Chevrolet', '2018', 'Yellow', '6spd') """)
# commit the changes
conn.commit()

curr = conn.execute("SELECT * FROM Cars")

for row in curr:
    print(row)

conn.close()
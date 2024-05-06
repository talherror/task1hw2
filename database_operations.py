import sqlite3
import csv

conn = sqlite3.connect('DINERS.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS CANTEEN
             (ID INTEGER PRIMARY KEY,
              Name TEXT,
              Location TEXT,
              time_open TEXT,
              time_closed TEXT)''')

with open('Canteens.csv', 'r') as file:
    reader = csv.reader(file)
  
    next(reader)
    for row in reader:
        c.execute("INSERT INTO CANTEEN (Name, Location, time_open, time_closed) VALUES (?, ?, ?, ?)", row)

conn.commit()
conn.close()

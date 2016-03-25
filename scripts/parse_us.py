from bs4 import BeautifulSoup
import requests
import datetime
import io

r = requests.get("http://us.halfstaff.org")
soup = BeautifulSoup(r.text, "lxml")

entry = soup.find("div", {"class":"entry"})

dates = entry.find_all("div", {"class":"date"})

if len(dates) > 1:
    start_str = str(dates[0].strong.string)
    end_str = str(dates[1].strong.string)
else:
    print "ERROR FUCK"
    start_str = "1/1/2016"
    end_str = "1/1/2016"

reason = str(entry.find("div", {"class":"short"}).string)

start_date = datetime.datetime.strptime(start_str, "%m/%d/%Y").date()
end_date = datetime.datetime.strptime(end_str, "%m/%d/%Y").date()

# print "Start: " + str(start_date)
# print "End: " + str(end_date)
# print reason

import sqlite3

# table name FlagAtHalfMast_flaghalfmastinfo

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

c.execute("INSERT INTO FlagAtHalfMast_flaghalfmastinfo"\
    + "(start_date, end_date, reason) VALUES('"\
    + str(start_date) + "','" + str(end_date)\
    + "','" + reason + "')")

conn.commit()
conn.close()

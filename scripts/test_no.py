import datetime
import sqlite3

start_date = datetime.datetime.now().date() + datetime.timedelta(days=-2)
end_date = datetime.datetime.now().date() + datetime.timedelta(days=-1)

reason = "This Should not Show"

# table name FlagAtHalfMast_flaghalfmastinfo

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

c.execute("INSERT INTO FlagAtHalfMast_flaghalfmastinfo"\
    + "(start_date, end_date, reason) VALUES('"\
    + str(start_date) + "','" + str(end_date)\
    + "','" + reason + "')")

conn.commit()
conn.close()

import datetime
from django.shortcuts import render
from .models import FlagHalfMastInfo

from bs4 import BeautifulSoup
import requests
import datetime
import threading


# Create your views here.


def main(request):
    latest_info = FlagHalfMastInfo.objects.last()
    half_mast = latest_info.end_date >= datetime.datetime.now().date() >= latest_info.start_date
    if half_mast:
        ans = 'Yes'
        reas = latest_info.reason
    else:
        ans = 'No'
        reas = ""

    thr = threading.Thread(target=update_db)
    thr.start() # will run "foo"

    return render(request, 'index.html', {'answer': ans, 'reason': reas})

def update_db():
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

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    c.execute("INSERT INTO FlagAtHalfMast_flaghalfmastinfo"\
        + "(start_date, end_date, reason) VALUES('"\
        + str(start_date) + "','" + str(end_date)\
        + "','" + reason + "')")

    conn.commit()
    conn.close()

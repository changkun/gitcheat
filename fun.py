# coding: utf-8
from datetime import date, timedelta
import os
import random

def dategenerator(start, end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

def everyday(date):
    number = random.randint(1, 10)
    datestr = str(date)
    for num in xrange(1, number):
        f = open("1.txt", "w")
        writenumber = random.uniform(0, 100)
        f.write(str(writenumber))
        f.close()
        addfile = "git add 1.txt"
        commit = "git commit --date=%s -m \"%s modify test\"" % (datestr, datestr)

        # print addfile
        # print commit

        os.system(addfile)
        os.system(commit)

    print datestr + "commit 了" + str(number) + "次"

for date in dategenerator(date(2016, 2, 1), date(2016, 4, 1)):
    everyday(date)

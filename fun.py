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
    number = random.randint(1, 50)
    datestr = str(date)
    for num in xrange(number):
        f = open("1.txt", "w")
        f.write(datestr)
        addfile = "git add 1.txt"
        commit = "git commit --date=%s -m \"%s modify test\"" % (datestr, datestr)
        # print commit, number
        os.system(addfile)
        os.system(commit)

for date in dategenerator(date(2015, 1, 1), date(2015, 3, 1)):
    everyday(date)

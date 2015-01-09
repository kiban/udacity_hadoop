#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for line in reader:
    if len(line) > 8:
        date_time = line[8]
        time = date_time.split(" ")
        # Check to see if time has both a date and time of day
        if len(time) < 2:
            continue
        # Extract hour from time of day string
        hr = int(time[1][:2])
        # print user_id and hour
        print line[3], "\t", hr

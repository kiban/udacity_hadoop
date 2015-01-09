#!/usr/bin/python


import sys
hrCnt = 0
maxHr = 0
maxCnt = 0
HourList = []
oldUser = None
oldHr = None

print "Student ID | Hour"

# Read line from input
for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    thisUser, thisHr = data_mapped

    # When User changes print and reset the hour count and max count
    if oldUser and oldUser != thisUser:
        for hour in HourList:
            print oldUser, "\t", hour
        hrCnt = 0
        maxCnt = 0

    # Create or increment count of a particular hr
    oldUser = thisUser
    if oldHr == thisHr:
        hrCnt += 1
    else:
        hrCnt = 1
    oldHr = thisHr

    # Create list of hours with the highest frequency
    if hrCnt == maxCnt:
        HourList.append(thisHr)
    if hrCnt > maxCnt:
        maxCnt = hrCnt
        HourList = [thisHr]


# Print max hour/hours of last user
if oldUser != None:
    for hour in HourList:
        print oldUser, "\t", hour

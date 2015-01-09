#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for line in reader:
    # Extract tags of question nodes only
    if line[5] == "question":
        tags = line[2].split(" ")
        for tag in tags:
            print tag, "\t", 1

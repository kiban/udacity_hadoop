#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for line in reader:
    if len(line) == 19:
        node_id = line[0]
        student_id = line[3]
        node_type = line[5]
        # if the node_type answer print the parent_id
        if node_type == "answer":
            parent_id = line[6]
            print parent_id, "\t", student_id
        else:
            # if the node type is question, print that node's id
            parent_id = "none"
            print node_id, "\t", student_id

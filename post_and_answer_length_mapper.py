#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for line in reader:
    # Check to see if line has the correct number of fields
    if len(line) == 19:
        node_id = line[0]
        body = line[4]
        node_type = line[5]
        # print parent_ids of answer nodes
        if node_type == "answer":
            parent_id = line[6]
            print parent_id, "\t", node_type, "\t", len(body)
        else:
            # parent node_ids of question nodes
            parent_id = "none"
            print node_id, "\t", node_type, "\t", len(body)

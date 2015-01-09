#!/usr/bin/python


import sys
oldId = None
node_list = []

print "Question Node |Student IDs"

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    node_id, student_id = data_mapped

    # When the node_id changes print the previous node's results and reset list
    if oldId and oldId != node_id:
        print oldId, "\t", node_list
        node_list = []

    node_list.append(student_id)
    oldId = node_id

# Print the results from the last node
if oldId != None:
    print oldId, "\t", node_list

#!/usr/bin/python


import sys
oldId = None
number_of_answers = 0
length_of_all_answers = 0
question_length = 0

print "Question Node ID|Question Length|Average Answer Length"

# Read line from input
for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    node_id, node_type, body_length = data_mapped
    body_length = int(body_length)

    # When node_id changes, print results and reset counts
    if oldId and oldId != node_id:
        print oldId, "\t",  question_length, "\t", answer_average_length
        number_of_answers = 0
        length_of_all_answers = 0

    # if node_type > 7, node is a question node
    if len(node_type) > 7:
        question_length = body_length
    # otherwise node is an answer node
    else:
        number_of_answers += 1
        length_of_all_answers += body_length
    if number_of_answers == 0:
        answer_average_length = 0
    else:
        answer_average_length = length_of_all_answers/float(number_of_answers)
    oldId = node_id

# Print values of last node
if oldId != None:
    print node_id, "\t",  question_length, "\t", answer_average_length

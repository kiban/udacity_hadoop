#!/usr/bin/python


import sys
oldTag = None
tagCount = 0
tenLargestTags = {}
numberOfTags = 0


def maxCount(topTags, tagCnt, newTag):
    newTag = {newTag: tagCnt}
    if len(topTags) < 10:
        topTags.update(newTag)
    else:
        countPerTag = topTags.values()
        sortedCounts = sorted(countPerTag)
        # Extract the smallest count from the front of the sorted list
        smallestCount = sortedCounts[0]
        smallestKey = [i for i, j in topTags.items() if j == smallestCount][0]
        # Only remove and replace on tag, count pair at a time
        if tagCnt > smallestCount:
            del topTags[smallestKey]
            topTags.update(newTag)
    return topTags


for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    tag, value = data_mapped
    value = int(value)

    # When tag changes, print results and set tagCount back to 0
    if oldTag and oldTag != tag:
        tenLargestTags = maxCount(tenLargestTags, tagCount, oldTag)
        tagCount = 0
        numberOfTags += 1
        # if numberOfTags > 9:
        #     assert len(tenLargestTags) == 10

    tagCount += value
    oldTag = tag

# print last tag
if oldTag is not None:
    tenLargestTags = maxCount(tenLargestTags, tagCount, oldTag)
    # if numberOfTags > 9:
    #     assert len(tenLargestTags) == 10
    largestCounts = sorted(tenLargestTags.values(), reverse=True)
    outputDesired = sorted(tenLargestTags,
                           key=lambda x: tenLargestTags[x], reverse=True)
    print "Tag", "\t", "Counts"
    for i, j in zip(outputDesired, largestCounts):
        print i, "\t", j

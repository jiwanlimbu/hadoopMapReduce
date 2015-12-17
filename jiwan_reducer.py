#!/usr/bin/env python
########################################################################
#
#           Jiwan Ninglekhu
#           11/30/2015
#           reduce function 
#
########################################################################
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
new_count = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
        
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if word == 'TRUE':
        current_word == word
        current_count += count
    else:
        new_word = word
        new_count += count
       
print "Number of Artificial Turf  : ", current_count
print "Number of Natural Turf     : ", new_count

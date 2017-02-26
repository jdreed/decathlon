#!/usr/bin/python

import sys
import operator
import random

def add_minutes(timestr, interval):
    hour, min = map(int, timestr.split(':'))
    min += interval
    if min >= 60:
        hour += 1
        min -= 60
    return '%02d:%02d' % (hour, min)

rooms = {'6208': ('6216', '6214', '6316', '6318', '6306'),
         '6312': ('6216', '6214', '6316', '6318', '6306'),
         '6406': ('6536', '6538', '6418', '6416', '6414'),
         '6412': ('6536', '6538', '6418', '6416', '6414'),
         '6016': ('6018', '6014', '6012', '6006', '6002'),
         '6008': ('6018', '6014', '6012', '6006', '6002'),
         '6062': ('6060', '6066', '6064', '6058', '6056'),
         '6108': ('6116', '6114', '6104', '6204', '6206'),
         '6106': ('6116', '6114', '6104', '6204', '6206'),
}

next_times = dict()

times = ('10:00', '11:30')
#times = ('1:15', '2:45')
         
def next_time(test_room):
    candidates = list(rooms[test_room])
    random.shuffle(candidates)
    rv = None
    for r in candidates:
        if next_times[r] != times[1]:
            rv = (r, next_times[r])
            next_times[r] = add_minutes(next_times[r], 10)
            break
    if rv is None:
        raise ValueError('No more times')
    return rv

if __name__ == '__main__':
    # setup
    all_rooms = set(reduce(operator.add, rooms.values(), ()))
    for r in all_rooms:
        next_times[r] = times[0]
    
    with open('rooms.txt') as infile:
        for line in infile:
            room = line.strip()
            if not room:
                continue
            print next_time(room)

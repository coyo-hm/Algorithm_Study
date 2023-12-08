import re
import datetime as dt
title = input()
parsed_title = ""
today = dt.datetime.now()
for t in title:
    char_reg = re.compile('[\d\w!?]')
    if char_reg.match(t):
        parsed_title += t
    elif parsed_title[-1] != "_":
        parsed_title += "_"
parsed_title += "/01_23"
parsed_title += str(today.month).zfill(2)
parsed_title += str(today.day).zfill(2)
print(parsed_title)
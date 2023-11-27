import re
title = input()
parsed_title = ""
for t in title:
    char_reg = re.compile('[\d\w]')
    if char_reg.match(t):
        parsed_title += t
    elif parsed_title[-1] != "_":
        parsed_title += "_"
parsed_title += "/01_231128"
print(parsed_title)
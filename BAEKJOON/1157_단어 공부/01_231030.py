import sys
from collections import Counter
input = sys.stdin.readline
word = input().rstrip().upper()
wordObj = list(Counter(word).items())
wordObj.sort(key=lambda x:-x[1])

answer = wordObj[0]
if len(wordObj) > 1 and answer[1] == wordObj[1][1]:
    print("?")
else:
    print(answer[0])

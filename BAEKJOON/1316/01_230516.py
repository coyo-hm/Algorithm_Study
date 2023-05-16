import sys
input = sys.stdin.readline
n = int(input())
words = [input().rstrip() for _ in range(n)]
ans = 0
def check(word):
    prev = word[0]
    dic = []
    for i in range(1, len(word)):
        if prev != word[i]:
            if word[i] in dic:
                return False
            dic.append(prev)
            prev = word[i]
    return True

for word in words:
    if(check(word)):
        ans += 1

print(ans)
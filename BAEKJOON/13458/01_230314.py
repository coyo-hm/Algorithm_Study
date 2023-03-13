import sys
import math

input = sys.stdin.readline
n = int(input())
applicant = list(map(int, input().split()))
direct, subdirect = map(int, input().split())

answer = n

for i in applicant:
  if i > direct:
    answer += math.ceil((i - direct) / subdirect)

print(answer)
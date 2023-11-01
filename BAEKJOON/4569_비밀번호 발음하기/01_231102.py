# https://www.acmicpc.net/problem/4659

import sys

input = sys.stdin.readline
VOWELS = ['a', 'e', 'i', 'o', 'u']

def solution(password):
    is_included_vowels = False
    vowels_count = 0
    consonants_count = 0
    for idx, c in enumerate(password):
        if vowels_count + consonants_count > 2:
            return False
        elif idx > 1 and password[idx - 2] == password[idx - 1] == c:
            return False
        elif idx > 0 and password[idx - 1] == c and c != "e" and c != "o":
            return False
        elif c in VOWELS:
            if not is_included_vowels:
                is_included_vowels = True
            vowels_count += 1
            consonants_count = 0
        else:
            consonants_count += 1
            vowels_count = 0
    return is_included_vowels and vowels_count + consonants_count < 3


while True:
    password = input().rstrip()
    if password == "end":
        break
    is_acceptable = solution(password)
    print(f'<{password}> is acceptable.' if is_acceptable else f'<{password}> is not acceptable.')

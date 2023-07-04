def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(arrayA, arrayB):
    maxA, maxB = -1, -1
    n = len(arrayA)

    setA = set(arrayA)
    setB = set(arrayB)

    if setA & setB:
        return 0
    tempA = arrayA[0]
    tempB = arrayB[0]

    for i in range(1, n):
        tempA = gcd(tempA, arrayA[i])
        tempB = gcd(tempB, arrayB[i])

    flagA = True
    for b in setB:
        if b % tempA == 0:
            flagA = False
            break
    if flagA == True:
        maxA = tempA

    flagB = True
    for a in setA:
        if a % tempB == 0:
            flagB = False
            break
    if flagB == True:
        maxB = tempB

        # print(tempA, tempB)
    # print(maxA, maxB)
    return max(maxA, maxB, 0)
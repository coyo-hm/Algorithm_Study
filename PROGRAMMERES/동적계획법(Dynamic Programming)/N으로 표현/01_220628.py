def solution(N, number):
    answer = -1
    n_list = []
    for i in range(1, 9):
        nums = set()
        nums.add(int(str(N)*i))
        for j in range(0, i - 1):
            for x in n_list[j]:
                for y in n_list[-1 - j]:
                    nums.add(x + y)
                    nums.add(x - y)
                    nums.add(x * y)
                    if y != 0 : nums.add(x // y)


        if number in nums:
            answer=i
            break
        n_list.append(nums)
    return answer
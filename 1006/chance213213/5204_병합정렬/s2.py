import sys
sys.stdin = open('input.txt')

def merge(l, r):
    if len(l) == 0:
        return r
    if len(r) == 0:
        return l
    sorted_list = []
    Nl = len(l)
    Nr = len(r)
    global cnt
    global list1
    while len(sorted_list) != len(l) + len(r):
        if l[Nl-1] < r[Nr-1]:
            sorted_list.insert(0, r[Nr-1])
            Nr -= 1
            list1.append(r[Nr-1])
            cnt += 1
        else:
            sorted_list.insert(0, l[Nl-1])
            Nl -= 1

        if Nr-1 == -1:
            sorted_list = l[:Nl] + sorted_list
            break
        if Nl-1 == -1:
            sorted_list = r[:Nr] + sorted_list

            break
    return sorted_list


def partition(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = partition(nums[:mid])
    right = partition(nums[mid:])
    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    list1 = []
    result = partition(arr)
    n = len(result)
    result = result[n//2]
    print('#{} {} {}'.format(tc, result, len(set(list1))))

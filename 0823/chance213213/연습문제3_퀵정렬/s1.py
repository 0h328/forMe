def quicksort(x):
    if len(x) <= 1:
        return x
#이렇게 해도 되낭,.? 다시봤는데 퀵정렬 아닌거 같은뎅
    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)

import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quicksort(nums))
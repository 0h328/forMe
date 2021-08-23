# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=1961&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open('input.txt')

def rotate(key):
    return list(zip(*key[::-1]))

for T in range(int(input())):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    result = [arr1, arr2, arr3]
    print('#{}'.format(T+1))

    for j in range(N):
        for i in range(3):
            print(*result[i][j], sep='', end=' ')

        print()


# #1
# 741 987 369 
# 852 654 258 
# 963 321 147 
# #2
# 872686 679398 558496 
# 952899 979157 069877 
# 317594 487722 724799 
# 997427 894586 495713 
# 778960 562998 998259 
# 694855 507496 686278 
# #3
# 0223319 0639550 5847800 
# 5851613 0762582 0170676 
# 5528111 8675252 5973763 
# 9255478 7035813 8745529 
# 3673795 4774163 1118255 
# 6760710 8197111 3161585 
# 0087485 5058139 9133220 
# #4
# 876 218 432 
# 190 397 091 
# 234 406 678 
# #5
# 958701 171819 123041 
# 176786 467775 814067 
# 873604 008368 048871 
# 178840 348677 406378 
# 760418 214080 687671 
# 140321 180461 107859 
# #6
# 894 108 971 
# 091 799 190 
# 179 914 498 
# #7
# 99451 66169 75356 
# 66720 58269 28286 
# 12842 32874 24821 
# 68282 58425 02766 
# 65357 72201 15499 
# #8
# 344 693 336 
# 968 364 869 
# 633 384 443 
# #9
# 404 344 733 
# 419 310 914 
# 337 794 404 
# #10
# 76501 93107 15669 
# 01271 60916 43803 
# 19597 68525 79591 
# 30834 53970 17210 
# 96651 14711 10567 

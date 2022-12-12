import sys
input = sys.stdin.readline


def binary(num):
    binary_list.append(num % 2)
    num = num // 2
    if num != 0:
        binary(num)


T = int(input())
for tc in range(T):
    N = int(input())
    binary_list = []
    binary(N)

    idx = 0
    while idx < len(binary_list):
        if binary_list[idx] == 1:
            print(idx, end=' ')
        idx += 1
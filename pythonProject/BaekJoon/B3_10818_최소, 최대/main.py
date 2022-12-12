import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
max_value = -1000000
min_value = 1000000
for n in num_list:
    if max_value < n:
        max_value = n
    if n < min_value:
        min_value = n
print(min_value, max_value, end=' ')
import sys
input = sys.stdin.readline


def divisor(num):
    for n in range(1, num+1):
        if num % n == 0:
            divisor_list.append(n)


N, K = map(int, input().split())
divisor_list = []
divisor(N)
if len(divisor_list) < K:
    print(0)
else:
    print(divisor_list[K-1])
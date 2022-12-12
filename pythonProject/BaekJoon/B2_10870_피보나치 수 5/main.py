import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


###################메모리 초과#################
# def fibo(a, b, n):
#     c = a + b
#     if n == N:
#         print(c)
#         return
#     fibo(b, c, n + 1)
#
#
# N = int(input())
# fibo(0, 1, 2)


N = int(input())
n = 2
fibo_list = [0, 1]
while n <= N:
    fibo_list.append(fibo_list[n-2] + fibo_list[n-1])
    n += 1

print(fibo_list[N])


##################구글링 풀이 - 재귀 함수#################
# def fibonacci(n):
# 	if n <= 1:
# 		return n
# 	return fibonacci(n-1) + fibonacci(n-2)
#
# n = int(input())
# print(fibonacci(n))


##################구글링 풀이 - for문문################
# n = int(input())
#
# fibonacci = [0, 1]
# for i in range(2, n+1):
# 	num = fibonacci[i-1] + fibonacci[i-2]
# 	fibonacci.append(num)
# print(fibonacci[n])
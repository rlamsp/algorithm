import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chars = input()
    for idx in range(30):
        if idx != 0 and idx+1 != 1 and chars[0] == chars[idx] and chars[1] == chars[idx+1]:
            if chars[:idx] == chars[idx:idx+len(chars[:idx])]:
                break
    ans = len(chars[:idx])
    print(f'#{tc} {ans}')
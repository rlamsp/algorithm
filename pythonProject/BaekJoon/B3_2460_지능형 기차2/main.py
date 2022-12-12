import sys
input = sys.stdin.readline

passengers_list = []
passengers = 0
for _ in range(10):
    out_bus, in_bus = map(int, input().split())
    passengers = passengers - out_bus + in_bus
    passengers_list.append(passengers)

print(max(passengers_list))
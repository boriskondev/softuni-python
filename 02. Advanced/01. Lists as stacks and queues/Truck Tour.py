from collections import deque

possible = False

gas_stations = int(input())

queue = deque()

for _ in range(gas_stations):
    fuel, kilometers = list(map(int, input().split()))
    station = fuel, kilometers
    queue.append(station)

current_station = 0
stations_passed = 0
current_fuel = 0
idx = 0

while True:
    fuel, kilometers = queue[idx]
    current_fuel += fuel
    if current_fuel >= kilometers:
        current_fuel -= kilometers
        stations_passed += 1
        idx += 1
        if stations_passed == len(queue):
            possible = True
            break
        if current_fuel >= 0:
            continue
    else:
        idx = 0
        current_station += 1
        current_fuel = 0
        switch_station = queue.popleft()
        queue.append(switch_station)

    if current_station == len(queue) - 1:
        break

if possible:
    print(current_station)
